import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont, QIcon
import pyshorteners
import pyperclip

class URLShortenerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("CodeClause_URL Shortener")
        self.setGeometry(100, 100, 700, 300)
        self.setWindowIcon(QIcon('assets\icon.png'))  # Replace 'icon.png' with the actual path to your icon file

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Increase font size and set it to bold
        font = QFont()
        font.setPointSize(14)

        self.label = QLabel("Enter URL to be Shorten:")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.url_input = QLineEdit()
        self.url_input.setFont(font)
        layout.addWidget(self.url_input)

        self.shortened_label = QLabel("Shortened URL:")
        self.shortened_label.setFont(font)
        layout.addWidget(self.shortened_label)

        self.shortened_url = QLineEdit()
        self.shortened_url.setFont(font)
        layout.addWidget(self.shortened_url)

        self.shorten_button = QPushButton("Shorten")
        self.shorten_button.setFont(font)
        self.shorten_button.clicked.connect(self.shorten_url)
        layout.addWidget(self.shorten_button)

        # Create a "Copy" button for the shortened URL
        self.copy_button = QPushButton("Copy")
        self.copy_button.setFont(font)
        self.copy_button.clicked.connect(self.copy_shortened_url)
        layout.addWidget(self.copy_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.setFont(font)
        self.clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(self.clear_button)

        # Create an "Exit" button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(font)
        self.exit_button.clicked.connect(self.close)  # Connect the button to close the application
        layout.addWidget(self.exit_button)

        central_widget.setLayout(layout)

    def shorten_url(self):
        original_url = self.url_input.text()

        if not original_url:
            self.shortened_url.setText("Please enter a URL to shorten")
            self.shortened_url.setStyleSheet("color: red;")
            return

        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(original_url)

        self.shortened_url.setText(shortened_url)

    def copy_shortened_url(self):
        shortened_url = self.shortened_url.text()

        if shortened_url:
            pyperclip.copy(shortened_url)
            QMessageBox.information(self, "Copied", "Shortened URL copied to clipboard.")
        else:
            QMessageBox.warning(self, "Empty URL", "The shortened URL is empty.")

    def clear_fields(self):
        self.url_input.clear()
        self.shortened_url.clear()
        self.shortened_url.setStyleSheet("color: black;")  # Reset text color to black

def main():
    app = QApplication(sys.argv)
    window = URLShortenerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
