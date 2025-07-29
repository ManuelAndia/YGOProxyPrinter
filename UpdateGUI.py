import os

cmd = "pyside2-uic mainwindow.ui"
out = "ui_mainwindow.py"

read_from_cmd = os.popen(cmd).read()

write_to_file = read_from_cmd.replace("PySide2", "PyQt5")

## UNRESOLVED BUG::::
# QComboBox config selection:
write_to_file = write_to_file.replace("""self.ConfigSelection.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "Single Configuration", None, -1))""",
                                      """self.ConfigSelection.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Single Configuration", None, -1))""")

write_to_file = write_to_file.replace("""self.ConfigSelection.setItemText(9, QtWidgets.QApplication.translate("MainWindow", "Single Integrator", None, -1))""",
                                      """self.ConfigSelection.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Single Integrator", None, -1))""")

write_to_file = write_to_file.replace("""self.ConfigSelection.setItemText(10, QtWidgets.QApplication.translate("MainWindow", "Double Configuration", None, -1))""",
                                      """self.ConfigSelection.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Double Configuration", None, -1))""")

# QComboBox TiSa to ECDL lock sign:
write_to_file = write_to_file.replace("""self.TiSaToECDLSignCombo.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Increasing PZT voltage DECREASES beatnote frequency", None, -1))""",
                                      """self.TiSaToECDLSignCombo.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Increasing PZT voltage DECREASES beatnote frequency", None, -1))""")

write_to_file = write_to_file.replace("""self.TiSaToECDLSignCombo.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Increasing PZT voltage INCREASES beatnote frequency", None, -1))""",
                                      """self.TiSaToECDLSignCombo.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Increasing PZT voltage INCREASES beatnote frequency", None, -1))""")

# QComboBox comb monitor laser picker
write_to_file = write_to_file.replace("""self.ClientClockLaserPicker.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Hg laser", None, -1))""",
                                      """self.ClientClockLaserPicker.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Hg laser", None, -1))""")

write_to_file = write_to_file.replace("""self.ClientClockLaserPicker.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "Sr laser", None, -1))""",
                                      """self.ClientClockLaserPicker.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Sr laser", None, -1))""")

write_to_file = write_to_file.replace("""self.ClientClockLaserPicker.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "CUS laser", None, -1))""",
                                      """self.ClientClockLaserPicker.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "CUS laser", None, -1))""")

write_to_file = write_to_file.replace("""self.ClientClockLaserPicker.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "SHB laser", None, -1))""",
                                      """self.ClientClockLaserPicker.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "SHB laser", None, -1))""")

with open(out, "w") as f:
    f.write(write_to_file)