import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")

        layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel('Widget Demo')
        self.label1 = qtw.QComboBox()
        self.label1.addItems(['Six', 'No'])
        self.label2 = qtw.QCheckBox("Choose this")
        self.label3 = qtw.QCheckBox("or this")
        self.label4 = qtw.QLineEdit("Type Here")
        self.label5 = qtw.QRadioButton('This one?')
        self.label6 = qtw.QRadioButton('or this one?')
        self.label7 = qtw.QSlider(qtc.Qt.Orientation.Horizontal)
        self.label8 = qtw.QPushButton('Ok')
        self.label9 = qtw.QPushButton('Cancel')      
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.label5)
        layout.addWidget(self.label6)
        layout.addWidget(self.label7)
        layout.addWidget(self.label8)
        layout.addWidget(self.label9)





        
        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


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
