import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mieru GUI Client")
        self.setGeometry(100, 100, 600, 400)

        # Add a label
        self.label = QLabel("Welcome to Mieru GUI Client", self)
        self.label.setGeometry(50, 50, 500, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())