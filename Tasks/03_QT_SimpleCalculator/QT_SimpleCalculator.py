import sys
from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout, QVBoxLayout, QPushButton, QLineEdit

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
display = QLineEdit()

# _______________|initiaze the layout |_____________________
def Simple_Calcuator_Init():
    window.setWindowTitle("Calculator")
    # ___________| Add Display field to layout|_________
    layout.addWidget(display)
    Add_Buttons_layout()


# ______________| Add clicked button text to display field|________________
def button_clicked():
    # get the text of what button clicked
    button_text=window.sender().text()
    if button_text == '=':
        try:
            # if = button pressed then take display text and perform required calcualtion and return result as string.
            result = str(eval(display.text()))
            display.setText(result)
        except:
            display.setText("Error")
    elif button_text == 'C':
        display.clear()
    else:
        # for any number or operation pressed concatinate the display text.
        display.setText(display.text() + button_text)
# ______________| Add Buttons to layout|________________
def Add_Buttons_layout():
    buttons_grid = QGridLayout()
    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', 'C', '=', '+']
    ]

    #  build buttons grid layout and asign button_clicked func.to them.
    Raw=0
    for  button_row in (buttons):
        Column=0
        for  button_text in (button_row):
            button=QPushButton(button_text)
            button.clicked.connect(button_clicked)
            buttons_grid.addWidget(button,Raw,Column)
            Column+=1
        Raw+=1
    layout.addLayout(buttons_grid)

# ______________| start function  |_______________
def Simple_Calcuator_Start():
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())


# ______________| Run the App|_______________
Simple_Calcuator_Init()
Simple_Calcuator_Start()