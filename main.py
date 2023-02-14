import os
import sys
import ctypes
import utils.libs as lib

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QApplication, QListWidget


def popUp(title: str, text: str):
    ctypes.windll.user32.MessageBoxW(None, title, text, None)


class Load(QWidget):
    def __init__(self) -> None:
        super(Load, self).__init__()
        uic.loadUi("./ui/load.ui", self)

        self.setWindowTitle("Neon - PIP | load")
        self.setFixedHeight(300)
        self.setFixedWidth(400)

        self.libs = self.findChild(QListWidget, "libs_list")
        self.show_button = self.findChild(QPushButton, "show_libs")
        self.clear_button = self.findChild(QPushButton, "clear_libs")

        self.show_button.clicked.connect(self.show_libs_clicked)
        self.clear_button.clicked.connect(self.clear_libs_clicked)

    def show_libs_clicked(self):
        self.libs.addItem(lib.load_libs)

    def clear_libs_clicked(self):
        self.libs.clear()


class Manage(QWidget):
    def __init__(self) -> None:
        super(Manage, self).__init__()
        uic.loadUi("./ui/manage.ui", self)

        self.setWindowTitle("Neon - PIP | manage")
        self.setFixedHeight(198)
        self.setFixedWidth(196)

        self.lib = self.findChild(QLineEdit, "lib_name")
        self.install_button = self.findChild(QPushButton, "install_lib")
        self.uninstall_button = self.findChild(QPushButton, "uninstall_lib")

        self.install_button.clicked.connect(self.install_lib_clicked)
        self.uninstall_button.clicked.connect(self.uninstall_lib_clicked)

    def install_lib_clicked(self):
        try:
            os.system(lib.install + self.lib.text())
            popUp("installed", f"{self.lib.text()} successful installed")
        except:
            popUp("Error", f"impossible install {self.lib.text()}")

    def uninstall_lib_clicked(self):
        try:
            os.system(lib.delete + self.lib.text())
            popUp("Removed", f"{self.lib.text()} successful removed")
        except:
            popUp("Error", f"impossible remove {self.lib.text()}")


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        uic.loadUi("./ui/main.ui", self)

        self.setWindowTitle("Neon - PIP")
        self.setFixedHeight(119)
        self.setFixedWidth(226)

        self.load_button = self.findChild(QPushButton, "load_wid")
        self.manage_button = self.findChild(QPushButton, "manage_wid")

        self.load_button.clicked.connect(self.load)
        self.manage_button.clicked.connect(self.manage)

        self.show()

    def load(self):
        load.show()

    def manage(self):
        manage.show()


if __name__ == "__main__":
    os.system('')

    app = QApplication(sys.argv)

    load = Load()
    manage = Manage()
    window = Window()

    app.exec()
