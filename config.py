import configparser

from PySide6 import QtWidgets
def mijnfunctie():
    config["title"]["title"]= edit_title.toPlainText
def buttonclick():
    print("hey")

config = configparser.ConfigParser()
config.read("config.ini")

app = QtWidgets.QApplication()

wid = QtWidgets.QWidget()
wid.setWindowTitle('De titel')
wid.show()
layout = QtWidgets.QFormLayout(wid)

label = QtWidgets.QLabel("titel foont size:")
edit_title_size = QtWidgets.QSpinBox()
edit_title_size.setMinimum(4)
edit_title_size.setMaximum(1000)
edit_title_size.setValue(config["titel"].getint("font"))
layout.addRow(label, edit_title_size)



label = QtWidgets.QLabel("naam:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit)  # Nieuw

label = QtWidgets.QLabel("email:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw

label = QtWidgets.QLabel("naam:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit)  # Nieuw

label = QtWidgets.QLabel("email:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw

label = QtWidgets.QLabel("email:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw

label = QtWidgets.QLabel("email:")
edit = QtWidgets.QTextEdit()
layout.addRow(label, edit) # Nieuw

button1 = QtWidgets.QPushButton("Save")
layout.addWidget(button1)

button2 = QtWidgets.QPushButton("Cancel")
layout.addWidget(button2)




button1.show()
button2.show()
# Nieuw
#button2.show()

app.exec_()