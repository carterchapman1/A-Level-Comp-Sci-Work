import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg
def cancel():
        exit()

# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File")
        self.ok_btn = qtw.QPushButton('Ok')
        self.cncl_btn = qtw.QPushButton('Cancel')
        self.cncl_btn.clicked.connect(cancel)
        layout = qtw.QVBoxLayout()
        layout2 = qtw.QHBoxLayout()
        layout3 = qtw.QFormLayout()
        layout4 = qtw.QGridLayout()    
        combobox = qtw.QComboBox()
        tickbox = qtw.QCheckBox('On or Off') 
        combobox.addItems(['One', 'Two', 'Three'])
        layout.addWidget(qtw.QLineEdit('Horizontal Layout'))
        layout2.addWidget(qtw.QPushButton('Button 1'))
        layout2.addWidget(qtw.QPushButton('Button 2'))
        layout2.addWidget(qtw.QPushButton('Button 3'))
        layout2.addWidget(qtw.QPushButton('Button 4'))
        #layout.addWidget(qtw.QLabel('Grid Layout'))
        layout4.addWidget(self.ok_btn, 5, 1)
        layout4.addWidget(self.cncl_btn, 5, 2)       
        layout4.addWidget(combobox,4,0,1,2)
        layout4.addWidget(tickbox,4,2)

        self.edit_box = qtw.QLineEdit("Type Here")
        self.edit_box.textChanged.connect(self.on_text_change)
        layout4.addWidget(self.edit_box)

        layout3.addRow("Name:", qtw.QLineEdit("Name"))
        layout3.addRow("Location:", qtw.QLineEdit("Location"))


        


        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)


        
        widget1 = qtw.QWidget()
        widget1.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget1)
    
    def on_text_change(self, text):
    	print(text)



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
