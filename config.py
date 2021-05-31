from PySide6 import QtWidgets
def mijnfunctie():
    config["title"]["title"]= edit_title.toPlainText
def buttonclick():
    print("hey")

app = QtWidgets.QApplication()

wid = QtWidgets.QWidget()
wid.setWindowTitle('De titel')
wid.show()

button = QtWidgets.QPushButton("save", wid)
button.clicked.connect(buttonclick)
layout = QtWidgets.QFormLayout(wid) # Nieuw Grid -> Form

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


button.show() # Nieuw
#button2.show()

app.exec_()