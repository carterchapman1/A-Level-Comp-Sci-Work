import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc 

store = ""

class MainWindow(qtw.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Text Editor")

        layout = qtw.QVBoxLayout()

        self.textbox = qtw.QTextEdit()
        self.savebtn = qtw.QPushButton('Save')
        self.closebtn = qtw.QPushButton('Close')

        self.savebtn.clicked.connect(self.save_btn_click)
        self.closebtn.clicked.connect(self.close_btn_click)
        self.textbox.TextChanged.connect(self.collect_content)

        layout.addWidget(self.textbox)
        layout.addWidget(self.savebtn)
        layout.addWidget(self.closebtn)
        

        layout.addWidget
        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def collect_content(self,text):
        store = text
        return store

    def save_btn_click(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        with open (filename, "w") as FILE:
            FILE.write(store)
    
    def close_btn_click(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        with open (filename, "r") as FILE:
            store = FILE.readlines()






app = qtw.QApplication([])

window = MainWindow(app)
window.show()

app.exec()
