import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc

class ConversionTool(qtw.QMainWindow):

    def Go_Button(self, inputmetres):
        self.On_Go(inputmetres)

    def Number_collector(self,text):
        return text
            
        
    def Feet_Calculate(self, inputmetres):
        try:
            inputmetres = float(inputmetres)
        except ValueError:
            self.metre_box.setText(str(0))
        else:
            return self.metre_box.setText(str(float(inputmetres) / 3.281))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversion Tool")
        self.currentsize = 0
        layout = qtw.QFormLayout()
        self.Go_Button = qtw.QPushButton()
        self.Feet_Box = qtw.QLineEdit(" ")
        self.Feet_Box.textChanged.connect(self.Feet_Calculate)
        self.metre_box = qtw.QLabel('')
        layout.addRow("Feet", self.Feet_Box)
        layout.addRow("Metres", self.metre_box)
        
        layout.addWidget
        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)



app = qtw.QApplication([])

window = ConversionTool()
window.show()

app.exec()
    	
