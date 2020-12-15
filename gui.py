#Github Repository: https://github.com/tmKammerer/CST205-Project-Color-Window/tree/gui
#Teammates: Michael Kammerer, Yessica Torrez Hernandez, Quentin Bennett, Ari Garcia
#Title: Color Window (gui.py)
#Course: CST205-01
#Date: 12/14/20
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox,
                               QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit,
                               QRadioButton)
from PySide2.QtCore import Slot
import cv2

#RGB_List with 25 names in a list with dictionaries for each color
RGB_List = [{'cName': 'Red', 'cTuple': (255, 0, 0), 'cHex': '#FF0000'},
 {'cName': 'Green', 'cTuple': (0, 128, 0), 'cHex': '#008000'}, {
                               'cName': 'Blue', 'cTuple': (0, 0, 255), 'cHex': '#0000FF'},
 {'cName': 'Yellow', 'cTuple': (255, 255, 0), 'cHex': '#FFFF00'}, {
                                'cName': 'Gold', 'cTuple': (255, 215, 0), 'cHex': '#FFD700'},
 {'cName': 'Magenta', 'cTuple': (255, 0, 255), 'cHex': '#FF00FF'}, {
                                 'cName': 'Bisque', 'cTuple': (255, 228, 196), 'cHex': '#FFE4C4'},
 {'cName': 'Indigo', 'cTuple': (75, 0, 130), 'cHex': '#4B0082'}, {
                                'cName': 'Turquoise', 'cTuple': (64, 224, 208), 'cHex': '#40E0D0'},
 {'cName': 'Chocolate', 'cTuple': (210, 105, 30), 'cHex': '#D2691E'}, {
                                   'cName': 'Olive', 'cTuple': (128, 128, 0), 'cHex': '#808000'},
 {'cName': 'Salmon', 'cTuple': (250, 128, 114), 'cHex': '#FA8072'}, {
                                'cName': 'Orange', 'cTuple': (255, 165, 0), 'cHex': '#FFA500'},
 {'cName': 'Teal', 'cTuple': (0, 128, 128), 'cHex': '#008080'}, {
                              'cName': 'Purple', 'cTuple': (128, 0, 128), 'cHex': '#800080'},
 {'cName': 'Tan', 'cTuple': (210, 180, 140), 'cHex': '#D2B48C'}, {
                             'cName': 'Lime', 'cTuple': (0, 255, 0), 'cHex': '#00FF00'},
 {'cName': 'Coral', 'cTuple': (255, 127, 80), 'cHex': '#FF7F50'}, {
                               'cName': 'Violet', 'cTuple': (238, 130, 238), 'cHex': '#EE82EE'},
 {'cName': 'Khaki', 'cTuple': (240, 230, 140), 'cHex': '#F0E68C'}, {'cName': 'Black', 'cTuple': (0, 0, 0), 'cHex': '#000000'}, 
                                                                   {'cName': 'Dark Charcoal', 'cTuple': (51, 51, 51), 'cHex': '#333333'},
  {'cName': 'Spanish Gray', 'cTuple': (153, 153, 153), 'cHex': '#999999'}, {
                                       'cName': 'Gray', 'cTuple': (128, 128, 128), 'cHex': '#808080'},
  {'cName': 'Silver', 'cTuple': (192, 192, 192), 'cHex': '#C0C0C0'}, {
                                 'cName': 'Gainsboro', 'cTuple': (220, 220, 220), 'cHex': '#DCDCDC'},
  {'cName': 'White', 'cTuple': (255, 255, 255), 'cHex': '#FFFFFF'}]

#the cv2 image that will be used for the color
img = cv2.imread('jeanne-hebuterne.jpg')


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window Title
        self.setWindowTitle("Color Calculator")

        # Need input of R,G,B in order to get number
        self.label_title = QLabel(
            'Hello! Enter your RGB value.  ')

        # Created a box layout
        vbox1 = QVBoxLayout()
        
        #Red channel entree
        self.label_r = QLabel('Input R: ')
        self.liner_edit = QLineEdit()
        #green channel entree
        self.label_g = QLabel('Input G: ')
        self.lineg_edit = QLineEdit()
        #blue channel entree
        self.label_b = QLabel('Input B: ')
        self.lineb_edit = QLineEdit()
        

        vbox1.addWidget(self.label_title)
        vbox1.addWidget(self.label_r)
        vbox1.addWidget(self.liner_edit)
        vbox1.addWidget(self.label_g)
        vbox1.addWidget(self.lineg_edit)
        vbox1.addWidget(self.label_b)
        vbox1.addWidget(self.lineb_edit)

        gbox1 = QGroupBox('Welcome to the color calculator!')
        gbox1.setLayout(vbox1)

        mbox = QVBoxLayout()
        mbox.addWidget(gbox1)

        self.my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('Resulted color info here')
        self.my_btn.clicked.connect(self.on_click)
        vbox1.addWidget(self.my_btn)
        vbox1.addWidget(self.my_lbl)
        self.setLayout(vbox1)
        self.setLayout(mbox)

        hbox = QHBoxLayout()
        gbox1.setLayout(hbox)

    @Slot()
    def on_click(self):
      #editTexts will be made into int types here
        self.redText= int(self.liner_edit.text())
        self.greenText= int(self.lineg_edit.text())
        self.blueText= int(self.lineb_edit.text())

        #new int types are put into a tuple
        self.color = (self.redText, self.greenText, self.blueText)
        for x in RGB_List:
          if self.color == x['cTuple']:
            self.my_lbl.setText(f"Tuple: {x['cTuple']}, Name: {x['cName']}, Hex: {x['cHex']}")
            self.repaint()
            #Image prints out here, I don't know why, but the red and blue channels are reversed, this is how we got it to work
            cv2.rectangle(
              img,
              (0, 0),
              (1569, 2048),
              (self.blueText, self.greenText, self.redText), -1
            )
            cv2.imshow("Who's Jeanne?", img)
            cv2.waitKey()
          else:
            self.my_lbl.setText("You wanna try again?")
            self.repaint()
        
        



#GUI is made here
app=QApplication([])
my_win=MyWindow()
my_win.show()
app.exec_()
