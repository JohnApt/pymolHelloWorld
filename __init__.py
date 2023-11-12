#   Copyright (c)  2023  John Apt.
#   Permission is granted to copy, distribute and/or modify this document
#   under the terms of the GNU Free Documentation License, Version 1.2
#   or any later version published by the Free Software Foundation;
#   with no Invariant Sections, no Front-Cover Texts, and no Back-Cover
#   Texts.  A copy of the license is included in the section entitled "GNU
#   Free Documentation License".

# Import cmd
from pymol import cmd

# Import os
import os

def __init_plugin__(app=None):
    # add menu entry
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('Hello Hamline', run_plugin_gui)

# global reference to avoid garbage collection of our dialog
dialog = None

def run_plugin_gui():
    global dialog

    if dialog is None:
        # create a new (empty) Window
        dialog = make_dialog()
    dialog.show()

def make_dialog():
    # import helloHamline.py generated by pyuic5
    from . import helloHamline

    # create a new Window
    dialog = helloHamline.QtWidgets.QWidget()
    # convert it into a Qt object
    form = helloHamline.Ui_Form()
    # setupUi() is defined in helloHamline.py
    form.setupUi(dialog)

    # connect the button to a function
    form.pushButton.clicked.connect(printHello)

    return dialog

def printHello():
    # print a message to the PyMOL console

    print("Hello Hamline!")
    return


    
