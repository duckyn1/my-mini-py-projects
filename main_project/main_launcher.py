import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from launcher import Ui_MainWindow
import subprocess

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ducky's Tools")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.notes_btn.clicked.connect(self.run_notes)
        self.ui.slot_btn.clicked.connect(self.run_slot)
        self.ui.encrypt_btn.clicked.connect(self.run_encrypt)
        self.ui.calc_btn.clicked.connect(self.run_calc)
        self.ui.clock_btn.clicked.connect(self.run_clock)
        self.ui.blud_btn.clicked.connect(self.run_blud)
        self.ui.bank_btn.clicked.connect(self.run_bank)
        self.ui.exit_btn.clicked.connect(self.close)
    
    def run_notes(self):
        try:
            subprocess.Popen(["python", "notes.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Notes: \n{str(e)}")

    def run_slot(self):
        try:
            subprocess.Popen(["python", "slot.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Slots: \n{str(e)}")

    def run_encrypt(self):
        try:
            subprocess.Popen(["python", "encrypt.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Encrypt: \n{str(e)}")

    def run_calc(self):
        try:
            subprocess.Popen(["python", "calculator.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Calculator: \n{str(e)}")

    def run_clock(self):
        try:
            subprocess.Popen(["python", "clock.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Clock: \n{str(e)}")

    def run_blud(self):
        try:
            subprocess.Popen(["python", "bludgame.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Blud Game: \n{str(e)}")

    def run_bank(self):
        try:
            subprocess.Popen(["python", "bank.py"])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot open Bank: \n{str(e)}")


def main():
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
