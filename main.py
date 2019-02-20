import PySimpleGUI as sg
import os
import shutil
import config # manage all the variables
import gui # manage all gui stuff
import func # manage all the functions

gui.Main()

while True:
    config.event, config.values = gui.main_win.Read()

    if config.event == '_NEW_':
        func.Manage()

    if config.event == '_EDIT_':
        gui.main_win.FindElement('_NEW_').Update('Save')
        config.edit = True
        gui.Edit()

        while True:
            config.edit_event, config.edit_values = gui.edit_win.Read()

            if config.edit_event == '_CONFIRM_':
                func.Edit()
                gui.edit_win.Close()
                break

            if config.edit_event is None or config.edit_event == '_CANCEL_':
                gui.main_win.FindElement('_NEW_').Update('New')
                gui.edit_win.Close()
                break

    if config.event == '_DEL_':
        if config.edit:
            gui.Del()

            while True:
                config.del_event, config.del_values = gui.del_win.Read()

                if config.del_event == '_YES_':
                    func.Del()
                    gui.del_win.Close()
                    break

                if config.del_event is None or config.del_event == '_NO_':
                    gui.del_win.Close()
                    break
        else:
            sg.Popup('You didn\'t select any client to delete.')

    if config.event == '_CLEAR_':
        gui.main_win.FindElement('_OUTPUT_').Update('')
        pass

    if config.event == '_SOURCE_':
        func.Source()

    if config.event == '_SEARCH_':
        func.Search()

    if config.event is None or config.event == '_EXIT_':
        gui.main_win.Close()
        break
