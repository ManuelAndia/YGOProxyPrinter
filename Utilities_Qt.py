# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 18:44:05 2025

@author: Eukerion
"""

import traceback, pickle, sys, subprocess, os
from time import strftime

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QObject, Qt

# =============================================================================
# Definitions - functions and decorators
# =============================================================================
def resource_path(relative):
    """Get absolute path to the resource -- ABSOLUTELY NEEDED for compiling
    with PyInstaller!"""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative)

def open_explorer(location, reveal=True):
    """Opens file explorer at location provided. If location is file and reveal is True,
    highlights the file in explorer (ONLY WINDOWS AND MACOS)."""
    if sys.platform.startswith('win'): # Windows only
        opener = ["explorer", "/select,"] if reveal else ["explorer"]
    elif sys.platform.startswith('lin'): # Linux only
        opener = ["xdg-open"]
    elif sys.platform.startswith('dar'): # macOS only (darwin)
        opener = ["open", "-R"] if reveal else ["open"]
    subprocess.run(opener + [location])

def timestamp_decorator(func):
    def modified_func(self, *args, **kwargs):
        timestamp = strftime("%Y_%m_%d @%H:%M:%S")
        print("\n")
        print(timestamp)
        return func(self, *args, **kwargs)
    
    return modified_func

def update_number_of_datasets_decorator(func):
    def modified_func(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
        except TypeError: # handles error due to PyQt5 sending extra arguments
            res = func(self)
        self.update_number_of_datasets()
        return res
    
    return modified_func

def update_dataset_colors_decorator(func):
    def modified_func(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
        except TypeError: # handles error due to PyQt5 sending extra arguments
            res = func(self)
        self.update_dataset_colors()
        return res
    
    return modified_func

def show_error(short_description, error_instance, window_title="Error", button_style="Warning"):
    error_msg = QtWidgets.QMessageBox()
    error_msg.setText(short_description)
    error_msg.setIcon(getattr(QtWidgets.QMessageBox, button_style))
    if isinstance(error_instance, Exception):
        long_description = traceback.format_exception(type(error_instance), value=error_instance, tb=error_instance.__traceback__)
        long_description = ''.join(long_description)
    elif isinstance(error_instance, str):
        long_description = error_instance
    error_msg.setInformativeText(long_description)
    error_msg.setWindowTitle(window_title)
    #scriptDir = os.path.dirname(os.path.realos.path(__file__))
    #error_msg.setWindowIcon(QtGui.QIcon(os.path.join(scriptDir, LOGO_RELATIVE_PATH)))
    error_msg.exec_()

def show_save_confirmation(short_description, error_instance, save_folder,
                           window_title="Save successful", button_style="Information"):
    error_msg = QtWidgets.QMessageBox()
    error_msg.setText(short_description)
    error_msg.setIcon(getattr(QtWidgets.QMessageBox, button_style))
    if isinstance(error_instance, Exception):
        long_description = traceback.format_exception(type(error_instance), value=error_instance, tb=error_instance.__traceback__)
        long_description = ''.join(long_description)
    elif isinstance(error_instance, str):
        long_description = error_instance
    error_msg.setInformativeText(long_description)
    error_msg.setWindowTitle(window_title)
    
    error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    
    def f(*args, **kwargs):
        error_msg.done(1)
        open_explorer(save_folder)
    
    explorer_button = error_msg.addButton('Show saved file(s)', QtWidgets.QMessageBox.YesRole)
    explorer_button.clicked.disconnect()
    explorer_button.clicked.connect(f)
    #scriptDir = os.path.dirname(os.path.realos.path(__file__))
    #error_msg.setWindowIcon(QtGui.QIcon(os.path.join(scriptDir, LOGO_RELATIVE_PATH)))
    error_msg.exec_()

def show_dialog(short_description, long_description, even_more_details=None, window_title="Information"):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText(short_description)
    msg.setInformativeText(long_description)
    msg.setWindowTitle(window_title)
    msg.setDetailedText(even_more_details)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    #scriptDir = os.path.dirname(os.path.realos.path(__file__))
    #msg.setWindowIcon(QtGui.QIcon(os.path.join(scriptDir, LOGO_RELATIVE_PATH)))
    res = msg.exec_()
    return True if res==QtWidgets.QMessageBox.Ok else False

def find_item_by_text(text, combobox):
    index = combobox.findText(text, Qt.MatchFixedString)
    if index >= 0:
        combobox.setCurrentIndex(index)
        return True
    return False

def delete_child_widgets_from_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
          child.widget().deleteLater()

def report_exceptions(f):
    """
    Decorator to catch errors and display a message in PyQt5.

    Parameters
    ----------
    f : function
        Wrapped function.

    Returns
    -------
    wrapped_f : function
        Wrapper function.

    """
    def wrapped_f(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as err:
            show_error("An error occurred.", err)
    return wrapped_f

# =============================================================================
# Definitions - classes
# =============================================================================
class StopButton(object):
    def __init__(self, button, stop_text="STOP", stop_stylesheet="color:red;"):
        self.button = button
        self.initial_text = button.text()
        self.initial_styleSheet = button.styleSheet()
        self.initial_state = button.isEnabled()
        self.stop_text = stop_text
        self.stop_stylesheet = stop_stylesheet
    
    @property
    def state(self):
        return self.button.isEnabled()
    
    def setEnabled(self, state):
        return self.button.setEnabled(state)
    
    def setText(self, text):
        return self.button.setText(text)
    
    def setStyleSheet(self, sheet):
        return self.button.setStyleSheet(sheet)
    
    def toggle(self, state="start"):
        if state=="start": # this means that the thread has started and the stop button should display the stop message
            self.setEnabled(True)
            self.setText(self.stop_text)
            self.setStyleSheet(self.stop_stylesheet)
        elif state=="stopping":
            self.setEnabled(False)
            self.setText(self.initial_text)
            self.setStyleSheet(self.initial_styleSheet)
        elif state=="stop":
            self.setEnabled(self.initial_state)
            self.setText(self.initial_text)
            self.setStyleSheet(self.initial_styleSheet)

class EmittingStream(QObject):

    textWritten = pyqtSignal(str)

    def write(self, text):
        final_text = str(text)
        self.textWritten.emit(final_text)

class Parameters(object):
    
    def __init__(self):
        pass
    
    def export(self, filename, **kwargs):
        kwargs["protocol"] = 0
        with open(filename, "wb") as f:
            pickle.dump(self, f, **kwargs)

class Counter:

    def __init__(self, name):
        self.name = name
        self.value = 0

    def reset_Counter(self):
        self.value=0

class MyQComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFocusPolicy(Qt.StrongFocus)

    def wheelEvent(self, *args, **kwargs):
        pass

class MyQTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def setEnabled(self, b):
        if b:
            self.setFlags(self.flags() | Qt.ItemIsEnabled)# | Qt.ItemIsSelectable)
        else:
            self.setFlags(self.flags() & (~Qt.ItemIsEnabled))# ^ Qt.ItemIsSelectable)
            #self.setFlags(self.flags() & ~Qt.ItemIsEditable)
    
    def setEditable(self, b):
        if b:
            self.setFlags(self.flags() | Qt.ItemIsEditable)# | Qt.ItemIsSelectable)
        else:
            self.setFlags(self.flags() & (~Qt.ItemIsEditable))# ^ Qt.ItemIsSelectable)
            #self.setFlags(self.flags() & ~Qt.ItemIsEditable)

class ThreadStopped(Exception):
    pass