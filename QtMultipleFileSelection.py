# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:09:28 2015

@author: NIAP
"""

from PyQt4 import QtCore, QtGui

class FileDialog(QtGui.QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QtGui.QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QtGui.QFileDialog.ExistingFiles)

    def accept(self):
        QtGui.QDialog.accept(self)

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        dialog = FileDialog()
        print("Hej")
        print(dialog.selectedFiles())

        if dialog.exec_() == QtGui.QDialog.Accepted:
            print(dialog.selectedFiles()[0])
            print(dialog.selectedFiles()[1])
            print(dialog.selectedFiles()[2])

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    