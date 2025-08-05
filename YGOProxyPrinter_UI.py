#!/usr/bin/python3

# =============================================================================
# Imports
# =============================================================================
from PyQt5 import QtWidgets, QtGui, QtCore
# from matplotlib.backends.backend_qt5agg import (
#     FigureCanvasQTAgg as FigureCanvas,
#     NavigationToolbar2QT as NavigationToolbar)
#import matplotlib.pyplot as plt, numpy as np

import sys, os, re

from ui_mainwindow import Ui_MainWindow

from WorkerThreadClasses import WorkerThreadPDFExport, WorkerThreadCardSearch, WorkerThreadCardImagePull

from Utilities_Qt import show_error, show_dialog, Parameters, show_save_confirmation, \
                         open_explorer, report_exceptions, resource_path, StopButton

from YGOCardTools import CardList

# Specifically to close the splash screen (for compiled version only)
try:
    import pyi_splash
    pyi_splash.close()
except:
    pass

# =============================================================================
# App name and Version number
# =============================================================================
APP_NAME = "YGOProxyPrinter"
VERSION = "0.3.6"
BUILD_DATE = "2025_08_06"

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
LOGO_RELATIVE_PATH = "img/logo.png"
RUN_SEARCH_ICON = "img/magnifier.png"
GET_IMAGES_BUTTON_ICON = "img/picture.png"
EXPORT_PDF_BUTTON_ICON = "img/floppy-disk.png"
DELETE_BUTTON_ICON = "img/delete.png"
UP_ARROW_ICON = "img/up-arrow.png"
DOWN_ARROW_ICON = "img/down-arrow.png"
LEFT_ARROW_ICON = "img/left-arrow.png"
RIGHT_ARROW_ICON = "img/right-arrow.png"

# # Window size
# WINDOW_SIZE = (647, 980)

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
def calculate_destination_frame_number(n, direction):
    assert(n>=0 and n<=N_CARDS)
    if direction=="up":
        return n-3
    elif direction=="down":
        return n+3
    elif direction=="left":
        return n-1
    elif direction=="right":
        return n+1
    else:
        raise NotImplementedError("`direction` must be either `up`, `down`, `left` or `right`.")

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
        #scriptDir = os.path.dirname(os.path.realpath(__file__))
        #self.setWindowIcon(QtGui.QIcon(os.path.join(scriptDir, LOGO_RELATIVE_PATH)))
        self.setWindowIcon(QtGui.QIcon(resource_path(LOGO_RELATIVE_PATH)))
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        #self.setFixedSize(*WINDOW_SIZE)
        
        # Give each widget a more explicit name to make referencing easier
        self.frames = {}
        self.search_card_edits = {}
        self.run_search_buttons = {}
        self.search_card_combos = {}
        self.copy_to_buttons = {}
        self.delete_buttons = {}
        self.artwork_combos = {}
        
        # Give each widget a number corresponding to the card number
        for n in range(N_CARDS+1):
            _frame = self.__getattribute__(f"frame_{n}") # get frame number n
            _frame.search_results = CardList([]) # initialise each frame with an empty search result
            _frame.image = None # initialise each frame with a None image
            _widgets = _frame.findChildren(QtWidgets.QWidget) # find all children widgets
            for _widget in _widgets:
                _widget.card_number = n # set card number to n
            # Fill the dictionaries for easier referencing
            self.frames[n] = _frame
            self.search_card_edits[n] = self.__getattribute__(f"SearchCardEdit_{n}")
            self.run_search_buttons[n] = self.__getattribute__(f"RunSearchToolButton_{n}")
            self.search_card_combos[n] = self.__getattribute__(f"SearchCardCombo_{n}")
            self.copy_to_buttons[n] = {"up":      self.__getattribute__(f"CopyUpButton_{n}"),
                                       "down":    self.__getattribute__(f"CopyDownButton_{n}"),
                                       "left":    self.__getattribute__(f"CopyLeftButton_{n}"),
                                       "right":   self.__getattribute__(f"CopyRightButton_{n}")}
            self.delete_buttons[n] = self.__getattribute__(f"DeleteButton_{n}")
            self.artwork_combos[n] = self.__getattribute__(f"ArtworkVersionCombo_{n}")
        
        # Set icons
        self.GetImagesButton.setIcon(QtGui.QIcon(resource_path(GET_IMAGES_BUTTON_ICON)))
        self.ExportPDFButton.setIcon(QtGui.QIcon(resource_path(EXPORT_PDF_BUTTON_ICON)))
        for n in range(N_CARDS+1):
            self.run_search_buttons[n].setIcon(QtGui.QIcon(resource_path(RUN_SEARCH_ICON)))
            self.delete_buttons[n].setIcon(QtGui.QIcon(resource_path(DELETE_BUTTON_ICON)))
            self.copy_to_buttons[n]["up"].setIcon(QtGui.QIcon(resource_path(UP_ARROW_ICON)))
            self.copy_to_buttons[n]["down"].setIcon(QtGui.QIcon(resource_path(DOWN_ARROW_ICON)))
            self.copy_to_buttons[n]["left"].setIcon(QtGui.QIcon(resource_path(LEFT_ARROW_ICON)))
            self.copy_to_buttons[n]["right"].setIcon(QtGui.QIcon(resource_path(RIGHT_ARROW_ICON)))
        
        # Connect each widget to its function
        self.GetImagesButton.clicked.connect(lambda checked:self.pull_images()) # Note: lambda checked is ONLY for QButtons;
                                                                                # it is a workaround for Qt's system of adding
                                                                                # an extra argument when a QButton
                                                                                # (specifically) is pressed, otherwise
                                                                                # the report_exceptions decorator doesn't work!
        self.ExportPDFButton.clicked.connect(lambda checked:self.export_PDF())
        for n in range(N_CARDS+1):
            self.search_card_edits[n].returnPressed.connect(self.search_card_name) # editingFinished also works, includes losing focus
            self.run_search_buttons[n].clicked.connect(lambda checked: self.search_card_name())
            self.copy_to_buttons[n]["up"].direction = "up" # set a property called "direction"
            self.copy_to_buttons[n]["up"].clicked.connect(lambda checked:self.copy_to())
            self.copy_to_buttons[n]["down"].direction = "down"
            self.copy_to_buttons[n]["down"].clicked.connect(lambda checked:self.copy_to())
            self.copy_to_buttons[n]["left"].direction = "left"
            self.copy_to_buttons[n]["left"].clicked.connect(lambda checked:self.copy_to())
            self.copy_to_buttons[n]["right"].direction = "right"
            self.copy_to_buttons[n]["right"].clicked.connect(lambda checked:self.copy_to())
            self.delete_buttons[n].clicked.connect(lambda checked: self.reset_frame())
            self.search_card_combos[n].currentIndexChanged.connect(lambda value: self.update_artwork_versions())
        
        # Which buttons will be stop buttons? (which ones will be used as buttons that can display the "STOP" message to interrupt a QThread)
        self.GetImagesStopButton = StopButton(self.GetImagesButton)
        self.ExportPDFStopButton = StopButton(self.ExportPDFButton)
        
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
        
        # Set focus on first search card edit
        self.search_card_edits[0].setFocus()
        
        # Set available languages for card names
        self.EnglishRadioButton.setText("")
        self.EnglishRadioButton.setIcon(QtGui.QIcon(resource_path("img/united-kingdom.png")))
        self.EnglishRadioButton.language_code = "en"
        self.FrenchRadioButton.setText("")
        self.FrenchRadioButton.setIcon(QtGui.QIcon(resource_path("img/france.png")))
        self.FrenchRadioButton.language_code = "fr"
        self.GermanRadioButton.setText("")
        self.GermanRadioButton.setIcon(QtGui.QIcon(resource_path("img/germany.png")))
        self.GermanRadioButton.language_code = "de"
        self.ItalianRadioButton.setText("")
        self.ItalianRadioButton.setIcon(QtGui.QIcon(resource_path("img/italy.png")))
        self.ItalianRadioButton.language_code = "it"
        self.PortugueseRadioButton.setText("")
        self.PortugueseRadioButton.setIcon(QtGui.QIcon(resource_path("img/portugal.png")))
        self.PortugueseRadioButton.language_code = "pt"
    
    #%% Search card name thread
    @report_exceptions
    def search_card_name(self):
        if not self.worker_thread_card_search.isRunning():
            # Toggle buttons and make the "Get images" button a stop button (with STOP text)
            self.toggle_widgets(state="start")
            
            # Get relevant properties
            sender = self.sender()
            n = sender.card_number # get card number of sender
            # Inform the worker thread of these properties
            self.worker_thread_card_search.n = n
            self.worker_thread_card_search.all_params = self.all_params
            
            # Finally start the thread
            self.worker_thread_card_search.start()
        else:
            self.worker_thread_card_search.stop()
    
    @report_exceptions
    def card_search_finished(self, worker_thread_output):
        if type(worker_thread_output) is int: # just update the progress bar
            self.update_progressBar(worker_thread_output)
        elif isinstance(worker_thread_output, Exception):
            show_error("Something went wrong during card name search.",
                       worker_thread_output)
            self.toggle_widgets(state="stop")
        elif type(worker_thread_output) is dict: # This means that the thread finished!
            name_matches = worker_thread_output["name_matches"]
            n = worker_thread_output["n"]
            if len(name_matches.card_list) > 0:
                _frame = self.frames[n]
                _frame.search_results = name_matches.card_list
                _combobox = self.search_card_combos[n]
                _combobox.clear()
                _combobox.addItems(name_matches.card_list.Name) # list of all found card names
            self.toggle_widgets(state="stop")
            if n<N_CARDS: self.search_card_edits[n+1].setFocus() # give focus to the next card-search text
    
    #%% Card image pull thread
    @report_exceptions
    def pull_images(self):
        if not self.worker_thread_card_image_pull.isRunning():
            # Toggle buttons
            self.toggle_widgets(state="start", stop_button=self.GetImagesStopButton)
            
            # Inform the worker thread
            self.worker_thread_card_image_pull.all_params = self.all_params
            
            # Finally start the thread
            self.worker_thread_card_image_pull.start()
        else:
            self.worker_thread_card_image_pull.stop()
            self.toggle_widgets(state="stopping", stop_button=self.GetImagesStopButton)
    
    @report_exceptions
    def image_pull_finished(self, worker_thread_output):
        if type(worker_thread_output) is int: # just update the progress bar
            self.update_progressBar(worker_thread_output)
        elif isinstance(worker_thread_output, Exception):
            show_error("Something went wrong while getting the images.",
                       worker_thread_output)
            self.toggle_widgets(state="stop", stop_button=self.GetImagesStopButton)
        elif type(worker_thread_output) is dict: # This means that the thread finished!
            images = worker_thread_output["images_raw"]
            all_params = self.all_params
            for (n, image) in images.items():
                _image = image[all_params.frame_contents[n]["artwork_version"]]
                _frame = self.frames[n]
                # Attach image to current frame
                _frame.image = _image
                # Create image data from server response
                image_data = QtCore.QByteArray(_image)
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
            self.toggle_widgets(state="stop", stop_button=self.GetImagesStopButton)
    
    #%% Export PDF thread
    @report_exceptions
    def export_PDF(self):
        if not self.worker_thread_PDF_export.isRunning():
            _file = self.get_save_file()
            
            if len(_file) == 0:
                return
            
            # Toggle buttons
            self.toggle_widgets(state="start", stop_button=self.ExportPDFStopButton)
            
            # Inform the worker thread
            self.worker_thread_PDF_export.all_params = self.all_params
            self.worker_thread_PDF_export.save_file = _file
            
            # Finally start the thread
            self.worker_thread_PDF_export.start()
        else:
            self.worker_thread_PDF_export.stop()
            self.toggle_widgets(state="stopping", stop_button=self.ExportPDFStopButton)
    
    @report_exceptions
    def PDF_export_finished(self, worker_thread_output):
        if type(worker_thread_output) is int: # just update the progress bar
            self.update_progressBar(worker_thread_output)
        elif isinstance(worker_thread_output, Exception):
            show_error("Something went wrong during PDF export.",
                       worker_thread_output)
            self.toggle_widgets(state="stop", stop_button=self.ExportPDFStopButton)
        elif type(worker_thread_output) is dict: # This means that the thread finished!
            file_saved = worker_thread_output["file_saved"]
            show_save_confirmation("File successfully saved:", file_saved,
                                   save_folder=os.path.abspath(file_saved))
            self.toggle_widgets(state="stop", stop_button=self.ExportPDFStopButton)
    
    #%% Other methods
    @report_exceptions
    def update_progressBar(self, p):
        self.progressBar.setValue(p)
    
    @report_exceptions
    def reset_frame(self):
        sender = self.sender()
        n = sender.card_number # get card number of sender
        _frame = self.frames[n]
        _frame.search_results = CardList([])
        _frame.image = None
        _frame.setPalette(QtGui.QPalette())
        self.search_card_combos[n].clear()
        self.search_card_edits[n].clear()
        self.artwork_combos[n].clear()
        self.artwork_combos[n].setEnabled(False)
    
    @report_exceptions
    def copy_to(self):
        sender = self.sender()
        n = sender.card_number # the source frame number
        direction = sender.direction # the direction pointed to by the button
        m = calculate_destination_frame_number(n, direction) # the destination frame number
        
        source_frame = self.frames[n]
        destination_frame = self.frames[m]
        
        source_combobox = self.search_card_combos[n]
        destination_combobox = self.search_card_combos[m]
        
        source_edit = self.search_card_edits[n]
        destination_edit = self.search_card_edits[m]
        
        source_artwork = self.artwork_combos[n]
        destination_artwork = self.artwork_combos[m]
        
        destination_frame.search_results = source_frame.search_results
        destination_combobox.clear()
        destination_combobox.addItems(destination_frame.search_results.Name) # list of all found card names
        destination_combobox.setCurrentIndex(source_combobox.currentIndex())
        destination_edit.setText(source_edit.text())
        destination_artwork.setCurrentIndex(source_artwork.currentIndex())
    
    @report_exceptions
    def update_artwork_versions(self):
        sender = self.sender()
        n = sender.card_number
        all_params = self.all_params
        combobox_index = all_params.frame_contents[n]["current_index"]
        search_results = all_params.frame_contents[n]["search_results"]
        if len(search_results)==0: return
        current_card = search_results[combobox_index] # Card object
        artworks = current_card.get_image_URL()
        N_artworks = len(artworks) # number of artworks for the currently-selected search result
        if N_artworks==1:
            _combobox = self.artwork_combos[n]
            _combobox.clear()
            _combobox.setEnabled(False)
        elif N_artworks>1:
            _combobox = self.artwork_combos[n]
            _combobox.clear()
            _combobox.addItems(map(str, range(N_artworks)))
            _combobox.setEnabled(True)
    
    @report_exceptions
    def show_PDF_file(self):
        params = self.all_params
        PDFFile = os.path.abspath(params.PDFFile)
        open_explorer(PDFFile, reveal=True)
    
    @property
    def all_params(self):
        res = Parameters()
        
        res.frame_contents = {}
        for n in range(N_CARDS+1):
            res.frame_contents[n] = {"card_search_text":    self.search_card_edits[n].text(),
                                     "search_results":      self.frames[n].search_results,
                                     "current_index":       self.search_card_combos[n].currentIndex(),
                                     "artwork_version":     self.artwork_combos[n].currentIndex(),
                                     "image":               self.frames[n].image}
        
        res.language = self.get_search_language() # AVAILABLE_CARD_NAME_LANGUAGES[self.LanguageComboBox.currentText()] # language code
        
        #res.all_used_cards = np.sum([v["search_results"] for v in res.frames.values()])
        
        return res
    
    @report_exceptions
    def toggle_widgets(self, state="start", stop_button=None):
        new_state = (state=="stop")
        widgets_list = list(self.frames.values()) + [self.LanguageGroupBox, \
            self.GetImagesStopButton, self.ExportPDFStopButton] # all widgets that need to be greyed out
        if stop_button is not None:
            widgets_list.remove(stop_button) # remove stop_button from list of widgets to toggle
            stop_button.toggle(state)
        for widget in widgets_list:
            widget.setEnabled(new_state)
        if state=="start":
            self.update_progressBar(0)
        elif state=="stopping":
            self.update_progressBar(100)
        elif state=="stop":
            self.update_progressBar(100)
    
    @report_exceptions
    def get_search_language(self):
        for widget in self.LanguageGroupBox.findChildren(QtWidgets.QRadioButton):
            if widget.isChecked():
                return widget.language_code
        return "en"
    
    #%% Utilities
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
