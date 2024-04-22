#Imports, GPIO is for the raspberry Pi Pins, time is for the sleep method and the QT imports are for the GUI
import RPi.GPIO as GPIO
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

#Sets up GUI window Class
class Window(QMainWindow):
    #Initialises Window Object
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(610, 340, 600, 400)
        self.setWindowTitle("GUI Window")
        self.initUi()
        
    
    #Initialises GUI
    def initUi(self): 
        #First Radio Slider
        self.labelRed = QtWidgets.QLabel(self)
        self.labelRed.setText("Red LED")
        self.labelRed.move(50,100)
        self.sRed = QtWidgets.QSlider(self)
        self.sRed.move(40, 125)
        self.sRed.setOrientation(QtCore.Qt.Horizontal)
        self.sRed.setMinimum(0)
        self.sRed.setMaximum(100)
        self.sRed.valueChanged.connect(self.pressRed)
    
        #Second Radio Slider
        self.labelBlue = QtWidgets.QLabel(self)
        self.labelBlue.setText("Blue LED")
        self.labelBlue.move(250,100)
        self.sBlue = QtWidgets.QSlider(self)
        self.sBlue.move(240, 125)
        self.sBlue.setOrientation(QtCore.Qt.Horizontal)
        self.sBlue.setMinimum(0)
        self.sBlue.setMaximum(100)
        self.sBlue.valueChanged.connect(self.pressBlue)
            
        #Third Radio Slider
        self.labelGreen = QtWidgets.QLabel(self)
        self.labelGreen.setText("Green LED")
        self.labelGreen.move(450,100)
        self.sGreen = QtWidgets.QSlider(self)
        self.sGreen.move(440, 125)
        self.sGreen.setOrientation(QtCore.Qt.Horizontal)
        self.sGreen.setMinimum(0)
        self.sGreen.setMaximum(100)
        self.sGreen.valueChanged.connect(self.pressGreen)
    
        #Exit Button
        self.bExit = QtWidgets.QPushButton(self)
        self.bExit.setText("Push To Exit")
        self.bExit.move(250, 300)
        self.bExit.clicked.connect(self.pressExit)
        
    #Reacts when the red LED slider is changed
    def pressRed(self, value):
        #Red is GPIO10
        pwmRed.ChangeDutyCycle(value)
        
    #Reacts when the blue LED slider is changed
    def pressBlue(self, value):
        #Blue is GPIO9
        pwmBlue.ChangeDutyCycle(value)
        
    #Reacts when the green LED slider is changed
    def pressGreen(self, value):
        #Green is GPIO9
        pwmGreen.ChangeDutyCycle(value)
        
    #Reacts when the exit button is pressed
    def pressExit(self):
        GPIO.output(10, GPIO.LOW)
        GPIO.output(9, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.cleanup()
        self.close()

#Method to construct a window object
def CreateWindow():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

#Sets up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

#Sets up the PWM parts of the LEDS
pwmRed = GPIO.PWM(10,50)
pwmRed.start(0)
pwmBlue = GPIO.PWM(9,50)
pwmBlue.start(0)
pwmGreen = GPIO.PWM(11,50)
pwmGreen.start(0)

#Calls Window Creation Method
CreateWindow()

