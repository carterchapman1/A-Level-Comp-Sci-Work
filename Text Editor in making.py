import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc 
from PyQt6.QtGui import QTextDocument 

store = ""

class MainWindow(qtw.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Text Editor")

        layout = qtw.QVBoxLayout()

        

        self.textbox = qtw.QTextEdit("Enter text here")
        self.savebtn = qtw.QPushButton('Save')
        self.openbtn = qtw.QPushButton('Open')
        self.closebtn = qtw.QPushButton('Close')



        self.savebtn.clicked.connect(self.save_btn_click)
        self.openbtn.clicked.connect(self.open_btn_click)
        self.closebtn.clicked.connect(self.close_btn_click)

        layout.addWidget(self.textbox,0)
        layout.addWidget(self.savebtn,1)
        layout.addWidget(self.openbtn,2)
        layout.addWidget(self.closebtn,3)


        
        

        layout.addWidget
        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def getting_the_text(self):
        inputedtext = self.textbox.document()    
        text = inputedtext.toPlainText()
        return text

    def save_btn_click(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        try:
            with open (filename, "w") as FILE:
                    FILE.write(self.getting_the_text())
                    FILE.close
            self.textbox.clear()
        except FileNotFoundError:
            pass
    
    
    def open_btn_click(self):
        filename , _= qtw.QFileDialog.getOpenFileName(self)
        try:
            with open (filename, "r") as FILE:
                self.textbox.append(FILE.read())
                FILE.close
        except FileNotFoundError:
            pass
        
    def close_btn_click():
        exit()


app = qtw.QApplication([])

window = MainWindow(app)
window.show()
print('hello')
app.exec()
