#!/usr/bin/python3

# =============================================================================
# Imports
# =============================================================================
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt, numpy as np

import sys, os

from ui_mainwindow import Ui_MainWindow

from WorkerThreadClasses import WorkerThreadPDFExport, WorkerThreadCardSearch, WorkerThreadCardImagePull

from Utilities_Qt import show_error, show_dialog, Parameters, show_save_confirmation, \
                         open_explorer, delete_child_widgets_from_layout, report_exceptions

from YGOCardTools import CardList

# =============================================================================
# App name and Version number
# =============================================================================
APP_NAME = "YGOProxyPrinter"
VERSION = "0.1"
BUILD_DATE = "2025_07_29"

MAIN_WINDOW_TITLE = "{app_name} v{version_number} (build {build_date})".format(app_name=APP_NAME, version_number=VERSION,
                     build_date=BUILD_DATE)

if sys.platform.startswith('win'): # Windows only
    # Fix missing taskbar icon in Windows:
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_NAME)

#%%============================================================================
# Global parameters (for initialisation)
# =============================================================================
# Application icon path
LOGO_RELATIVE_PATH = "img" + os.path.sep + "logo.ico"
EXPORT_PDF_BUTTON_ICON = r"img/floppy-disk.png"

# Window size
WINDOW_SIZE = (707, 1000)

# Number of cards on the page (do not change this)
N_CARDS = 8

# Set background color and transparency for all QGroupBoxes
QGROUPBOXES_BACKGROUND_COLOR = r"QGroupBox {background: rgba(255, 255, 255, .7);}"

# Button texts
GET_IMAGES_BUTTON_TEXT = {"onStart": "STOP", "onStop": "Get images"}
EXPORT_PDF_BUTTON_TEXT = {"onStart": "STOP", "onStop": "Export PDF"}

#%%============================================================================
# Templates
# =============================================================================


#%%============================================================================
# Definitions - functions and decorators
# =============================================================================


#%%============================================================================
# Definitions - classes
# =============================================================================


#%%============================================================================
# Definition - Main Window
# =============================================================================

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(os.path.join(scriptDir, LOGO_RELATIVE_PATH)))
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setFixedSize(*WINDOW_SIZE)
        
        # Give each widget a more explicit name to make referencing easier
        self.frames = {}
        self.already_used_combos = {}
        self.search_card_edits = {}
        self.search_card_combos = {}
        self.copy_from_buttons = {}
        
        # Give each widget a number corresponding to the card number
        for n in range(N_CARDS):
            _frame = self.__getattribute__(f"frame_{n}") # get frame number n
            _frame.search_results = CardList([]) # initialise each frame with an empty search result
            _frame.image = None # initialise each frame with a None image
            _widgets = _frame.findChildren(QtWidgets.QWidget) # find all children widgets
            for _widget in _widgets:
                _widget.card_number = n # set card number to n
            # Fill the dictionaries for easier referencing
            self.frames[n] = _frame
            self.already_used_combos[n] = self.__getattribute__(f"AlreadyUsedCardsCombo_{n}")
            self.search_card_edits[n] = self.__getattribute__(f"SearchCardEdit_{n}")
            self.search_card_combos[n] = self.__getattribute__(f"SearchCardCombo_{n}")
            self.copy_from_buttons[n] = {"up":      self.__getattribute__(f"CopyUpButton_{n}"),
                                         "down":    self.__getattribute__(f"CopyDownButton_{n}"),
                                         "left":    self.__getattribute__(f"CopyLeftButton_{n}"),
                                         "right":   self.__getattribute__(f"CopyRightButton_{n}")}
        
        # Set export button icon
        self.ExportPDFButton.setIcon(QtGui.QIcon(os.path.join(scriptDir, EXPORT_PDF_BUTTON_ICON)))
        
        # Connect each widget to its function
        self.GetImagesButton.clicked.connect(lambda checked:self.pull_images()) # Note: lambda checked is ONLY for QButtons;
                                                                                # it is a workaround for Qt's system of adding
                                                                                # an extra argument when a QButton
                                                                                # (specifically) is pressed, otherwise
                                                                                # the report_exceptions decorator doesn't work!
        self.ExportPDFButton.clicked.connect(lambda checked:self.export_PDF())
        for n in range(N_CARDS):
            self.search_card_edits[n].returnPressed.connect(self.search_card_name) # editingFinished also works, includes losing focus
            self.copy_from_buttons[n]["up"].direction = "up" # set a property called "direction"
            self.copy_from_buttons[n]["up"].clicked.connect(lambda checked:self.copy_from())
            self.copy_from_buttons[n]["down"].direction = "down"
            self.copy_from_buttons[n]["down"].clicked.connect(lambda checked:self.copy_from())
            self.copy_from_buttons[n]["left"].direction = "left"
            self.copy_from_buttons[n]["left"].clicked.connect(lambda checked:self.copy_from())
            self.copy_from_buttons[n]["right"].direction = "right"
            self.copy_from_buttons[n]["right"].clicked.connect(lambda checked:self.copy_from())
        
        # Initialise worker threads
        self.worker_thread_card_search = WorkerThreadCardSearch() # this is the worker thread object
        self.worker_thread_card_search.signal.connect(self.card_search_finished) # connect the signal from the thread to the finished method
        
        self.worker_thread_card_image_pull = WorkerThreadCardImagePull() # this is the worker thread object
        self.worker_thread_card_image_pull.signal.connect(self.image_pull_finished) # connect the signal from the thread to the finished method
        
        self.worker_thread_PDF_export = WorkerThreadPDFExport() # this is the worker thread object
        self.worker_thread_PDF_export.signal.connect(self.PDF_export_finished) # connect the signal from the thread to the finished method
        
        # Set background color and transparency for all QGroupBoxes
        _widgets = self.findChildren(QtWidgets.QGroupBox)
        for widget in _widgets:
            widget.setStyleSheet(QGROUPBOXES_BACKGROUND_COLOR)
        
        # FOR NOW, disable all "already-used" group boxes #TODO: do something with this?
        _widgets = self.findChildren(QtWidgets.QGroupBox, QtCore.QRegularExpression("AlreadyUsed"))
        for widget in _widgets:
            widget.setVisible(False)
        
        # Set focus on first search card edit
        self.search_card_edits[0].setFocus()
    
    #%% Search card name thread
    @report_exceptions
    def search_card_name(self):
        # if self.worker_thread_card_search.isRunning(): # check if the thread is already running
        #     print("BALBALBLAB")
        #     self.worker_thread_card_search.stop() # stop the thread
        #     self.toggle_widgets(state="stop", stop_button=self.GetImagesButton,
        #                         stop_button_text=GET_IMAGES_BUTTON_TEXT["onStop"]) # reset the buttons
        
        # Toggle buttons and make the "Get images" button a stop button (with STOP text)
        self.toggle_widgets(state="start", stop_button=self.GetImagesButton,
                            stop_button_text=GET_IMAGES_BUTTON_TEXT["onStart"])
        
        # Get relevant properties
        sender = self.sender()
        n = sender.card_number # get card number of sender
        # Inform the worker thread of these properties
        self.worker_thread_card_search.n = n
        self.worker_thread_card_search.all_params = self.all_params
        
        # Finally start the thread
        self.worker_thread_card_search.start()
    
    @report_exceptions
    def card_search_finished(self, worker_thread_output):
        if type(worker_thread_output) is int: # just update the progress bar
            self.update_progressBar(worker_thread_output)
        elif type(worker_thread_output) is Exception:
            show_error("Something went wrong during card name search.",
                       worker_thread_output)
            self.toggle_widgets(state="stop", stop_button=self.GetImagesButton,
                                stop_button_text=GET_IMAGES_BUTTON_TEXT["onStop"])
        elif type(worker_thread_output) is dict: # This means that the thread finished!
            name_matches = worker_thread_output["name_matches"]
            n = worker_thread_output["n"]
            if len(name_matches.card_list) > 0:
                _frame = self.frames[n]
                _frame.search_results = name_matches.card_list
                _combobox = self.search_card_combos[n]
                _combobox.clear()
                _combobox.addItems(name_matches.card_list.Name) # list of all found card names
            self.toggle_widgets(state="stop", stop_button=self.GetImagesButton,
                                stop_button_text=GET_IMAGES_BUTTON_TEXT["onStop"])
    
    #%% Card image pull thread
    @report_exceptions
    def pull_images(self):
        # Toggle buttons
        self.toggle_widgets(state="start", stop_button=self.GetImagesButton,
                            stop_button_text=GET_IMAGES_BUTTON_TEXT["onStart"])
        
        # Inform the worker thread
        self.worker_thread_card_image_pull.all_params = self.all_params
        
        # Finally start the thread
        self.worker_thread_card_image_pull.start()
    
    @report_exceptions
    def image_pull_finished(self, worker_thread_output):
        if type(worker_thread_output) is int: # just update the progress bar
            self.update_progressBar(worker_thread_output)
        elif type(worker_thread_output) is Exception:
            show_error("Something went wrong while getting the images.",
                       worker_thread_output)
            self.toggle_widgets(state="stop", stop_button=self.GetImagesButton,
                                stop_button_text=GET_IMAGES_BUTTON_TEXT["onStop"])
        elif type(worker_thread_output) is dict: # This means that the thread finished!
            images = worker_thread_output["images_raw"]
            for (n, image) in images.items():
                _frame = self.frames[n]
                # Attach image to current frame
                _frame.image = image
                # Create image data from server response
                image_data = QtCore.QByteArray(image)
                # Create pixmap
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(image_data)
                # Scale the pixmap to fit the frame while preserving aspect ratio
                scaled_pixmap = pixmap.scaled(_frame.size(), 
                    QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                    QtCore.Qt.TransformationMode.SmoothTransformation
                )
                palette = _frame.palette()
                brush = QtGui.QBrush(scaled_pixmap)
                palette.setBrush(QtGui.QPalette.ColorRole.Window, brush)
                _frame.setPalette(palette)
                _frame.setAutoFillBackground(True)
                # qlabel = QtWidgets.QLabel(self.frames[n])
                # self.verticalLayout.addWidget(qlabel)
                # pixmap = QtGui.QPixmap()
                # pixmap.loadFromData(image)
                # qlabel.setPixmap(pixmap)
                #self.frames[n].setStyleSheet(f'background-image: url("{image}"); background-repeat: no-repeat;')
            self.toggle_widgets(state="stop", stop_button=self.GetImagesButton,
                                stop_button_text=GET_IMAGES_BUTTON_TEXT["onStop"])
    
    #%% Export PDF thread
    @report_exceptions
    def export_PDF(self):
        _file = self.get_save_file()
        
        # Toggle buttons
        self.toggle_widgets(state="start", stop_button=self.ExportPDFButton,
                            stop_button_text=EXPORT_PDF_BUTTON_TEXT["onStart"])
        
        # Inform the worker thread
        self.worker_thread_PDF_export.all_params = self.all_params
        self.worker_thread_PDF_export.save_file = _file
        
        # Finally start the thread
        self.worker_thread_PDF_export.start()
    
    @report_exceptions
    def PDF_export_finished(self, worker_thread_output):
        if type(worker_thread_output) is int: # just update the progress bar
            self.update_progressBar(worker_thread_output)
        elif type(worker_thread_output) is Exception:
            show_error("Something went wrong during PDF export.",
                       worker_thread_output)
            self.toggle_widgets(state="stop", stop_button=self.ExportPDFButton,
                                stop_button_text=EXPORT_PDF_BUTTON_TEXT["onStop"])
        elif type(worker_thread_output) is dict: # This means that the thread finished!
            file_saved = worker_thread_output["file_saved"]
            show_save_confirmation("File successfully saved:", file_saved,
                                   save_folder=os.path.dirname(file_saved))
            self.toggle_widgets(state="stop", stop_button=self.ExportPDFButton,
                                stop_button_text=EXPORT_PDF_BUTTON_TEXT["onStop"])
    
    #%% Other methods
    @report_exceptions
    def update_progressBar(self, p):
        self.progressBar.setValue(p)
    
    @report_exceptions
    def update_frame(self):
        sender = self.sender()
        n = sender.card_number # get card number of sender
    
    @report_exceptions
    def copy_from(self):
        pass
    
    @report_exceptions
    def show_PDF_file(self):
        params = self.all_params
        PDFFile = os.path.abspath(params.PDFFile)
        open_explorer(PDFFile, reveal=True)
    
    @property
    def all_params(self):
        res = Parameters()
        
        res.frame_contents = {}
        for n in range(N_CARDS):
            res.frame_contents[n] = {"card_search_text":    self.search_card_edits[n].text(),
                                     "search_results":      self.frames[n].search_results,
                                     "current_index":       self.search_card_combos[n].currentIndex(),
                                     "image":               self.frames[n].image}
        
        #res.all_used_cards = np.sum([v["search_results"] for v in res.frames.values()])
        
        return res
    
    @report_exceptions
    def toggle_widgets(self, state="start", stop_button=None, stop_button_text=""):
        widgets_list = list(self.frames.values()) + [self.GetImagesButton, self.ExportPDFButton] # all widgets that need to be greyed out
        if stop_button is not None:
            stop_button.setText(stop_button_text)
            if state=="start":
                stop_button.setStyleSheet("color:red;")
            else:
                stop_button.setStyleSheet("color:black;")
            widgets_list.remove(stop_button) # remove stop_button from list of widgets to toggle
        new_state = False if state=="start" else True
        for widget in widgets_list:
            widget.setEnabled(new_state)
        if state=="start":
            self.update_progressBar(0)
        else:
            self.update_progressBar(100)
    
    @report_exceptions
    def export_results(self):
        _file = self.get_save_file(default_name=self.all_params.dataset_name)
        date_str = datetime.now().strftime("%Y_%m_%d-%Hh%Mmn%Ss_")
                
        filename = os.path.basename(_file)
        dirname = os.path.dirname(_file)
        # new_filename = date_str + filename
        # full_name = os.path.join(dirname, new_filename)
        full_name = os.path.join(dirname, filename)
        
        # Save results as .txt
        with open(full_name, "w") as f:
            f.write(self.DisplayResultsTextEdit.toPlainText())
        
        # Save figures
        list_figures_saved = []
        dirname_fig = os.path.join(dirname, "img") # save figures into "img" subfolder
        safe_path_creation(dirname_fig) # make folder if non existent
        for popup in self.list_popups:
            figname = slugify(date_str + os.path.splitext(filename)[0] + "_" + popup.popup_title) + ".png"
            full_figname = os.path.join(dirname_fig, figname)
            popup.figure.figure.savefig(full_figname)
            list_figures_saved.append(full_figname)
        
        show_save_confirmation("Files were successfully saved:", "\n".join([full_name] + list_figures_saved),
                                save_folder=os.path.abspath(dirname))
    
    # Utilities
    def get_folder(self, widget):
        _datafolder_start = folder_of_the_day()
        _datafolder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", _datafolder_start))
        if len(_datafolder)>0:
            self.datafolder = _datafolder
            widget.setText(self.datafolder)
    
    def get_file(self, widget=None):
        _datafolder_start = folder_of_the_day()
        _datafile = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", _datafolder_start)[0]
        if len(_datafile)>0:
            if widget is not None: widget.setText(_datafile)
            return _datafile
        else: return None
    
    def get_save_file(self, message="Select file to save data", default_name="",
                      formats="PDF (*.pdf)"):
        #_datafolder_start = os.path.join(folder_of_the_day(), default_name)
        _exportfile, _ = QtWidgets.QFileDialog.getSaveFileName(self, message,
                                                               "",
                                                               formats)
        return _exportfile
    
    def closeEvent(self, event):
        event.accept()

#%% Main loop
# =============================================================================
# Main function
# =============================================================================

def main():
    # Run the GUI
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

# =============================================================================
# Script when executed directly
# =============================================================================

if __name__ == '__main__':
    main()
