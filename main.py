from PyQt5 import QtWidgets, QtGui
from pip._internal.exceptions import HashErrors

import design
import sys
from functions import *

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()

# Don't Forget:
# pyinstaller start.py -F //to make EXE
# pyuic5 design.ui -o design.py //to import PyQt5 form .ui to .py

# --- --- ---

# Window parameters
window.setWindowTitle('Mindustry power calculator')
window.setWindowIcon(QtGui.QIcon('icon.png'))

# Initialize values
helper = Helper()
languages = Languages()
languages.load_language('en')
languages.load_language('ru')
rounding = window.round.isChecked()

# A loooot of functions...

def show_answer(solution):
    strings = []
    if rounding:
        strings.append(languages.get(solution['reactor'])+' x'+str(round(solution["count"], 2)))
    else:
        strings.append(languages.get(solution['reactor']) + ' x' + str(solution["count"]))
    output = ''
    if "resources" in solution:
        for i in range(len(solution["resources"][0])):
            solution["resources"][0][i] = languages.get(solution["resources"][0][i])
        if rounding:
            strings.append(compile_or(solution["resources"][0])+' '+str(round(solution["resources"][1], 2))+'/'+languages.get('second'))
        else:
            strings.append(compile_or(solution["resources"][0]) + ' ' + str(solution["resources"][1]) + '/' + languages.get('second'))
    if "liquid" in solution:
        if rounding:
            strings.append(languages.get(solution["liquid"][0])+' '+str(round(solution["liquid"][1]))+'/'+languages.get('second'))
        else:
            strings.append(languages.get(solution["liquid"][0]) + ' ' + str(solution["liquid"][1]) + '/' + languages.get('second'))
    for s in strings:
        output += s + '\n'
    return output

def update():
    global rounding
    window.generators.clear()
    for generator in helper.content['power']:
        window.generators.addItem(languages.get(generator))
    window.solve.setText(languages.get('solve'))
    window.power.setPlaceholderText(languages.get('placeholder'))
    window.solution_text.setText(languages.get('solution')+':')
    window.round.setText(languages.get('round'))
    rounding = window.round.isChecked()

def solve():
        ok = False
        try:
            float(window.power.text())
            ok = True
        except:
            pass
        if window.selected_type.text() != '' and ok:
            solution = helper.solve(languages.find(window.selected_type.text()), float(window.power.text()))
            window.solution.setText(show_answer(solution))
        else:
            window.solution.setText(languages.get('ohno'))
        update()

def set_ru_language():
    languages.active_language = 'ru'
    save_language()
    update()
def set_en_language():
    languages.active_language = 'en'
    save_language()
    update()

def load_language():
    f = open('languages/LANGUAGE.txt')
    languages.active_language = f.readline().strip()
    f.close()
    update()

def save_language():
    f = open('languages/LANGUAGE.txt', 'w')
    f.write(languages.active_language)
    f.close()

def set_type():
    window.selected_type.setText(window.generators.selectedItems()[0].text())
    update()

#And another initializing...

load_language()
update()
window.solve.clicked.connect(solve)
window.ru_button.clicked.connect(set_ru_language)
window.en_button.clicked.connect(set_en_language)
window.round.clicked.connect(update)
window.generators.clicked.connect(set_type)

# So, let's start!
app.exec()