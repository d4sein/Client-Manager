import PySimpleGUI as sg
import config

head = 'Client Manager'

def Main():
    global main_win

    client_layout = [
        [sg.Text('Client\'s information')],
        [sg.Text('Name', size=(10, 1)), sg.Input(size=(65, 1), key='_NAME_')],
        [sg.Text('Number', size=(10, 1)), sg.Input(size=(65, 1), key='_NUM_')],
        [sg.Text('Email', size=(10, 1)), sg.Input(size=(65, 1), key='_EMAIL_')],
        [sg.Text('Address', size=(10, 1)), sg.Input(size=(65, 1), key='_ADDRESS_')],
        [sg.Text('Observation', size=(10, 1)), sg.Multiline(size=(65, 6), key='_OBS_')],
        [
            sg.Button('New', key='_NEW_', visible=True),
            sg.Button('Edit', key='_EDIT_', visible=True),
            sg.Button('Delete', key='_DEL_', visible=True),
            sg.Button('Clear', key='_CLEAR_', visible=True),
            sg.Button('Source', key='_SOURCE_', visible=True),
            sg.Button('Exit', key='_EXIT_', visible=True, button_color=('white', 'red'))
        ]
    ]

    search_layout = [
        [sg.Text('Search client by keyword')],
        [sg.InputText(key='_KEYWORD_', size=(53, 1)), sg.Button('Search', key='_SEARCH_'), sg.Button('Clear', key='_CLEAR_')],
        [sg.Output(size=(71, 30), key='_OUTPUT_')]
    ]

    layout = [[sg.TabGroup([[sg.Tab('Client', client_layout), sg.Tab('Search', search_layout)]])]]

    main_win = sg.Window(head, size=(580, 600)).Layout(layout)


def Edit():
    global edit_win

    edit_layout = [
        [sg.Text('Select the client\'s folder')],
        [sg.Input(key='_DIR_', size=(61, 1)), sg.FolderBrowse('Browse', key='_BROWSE_', target='_DIR_', initial_folder=config.initial_folder)],
        [sg.Button('Confirm', key='_CONFIRM_'), sg.Button('Cancel', key='_CANCEL_')]
    ]

    edit_win = sg.Window(head).Layout(edit_layout)


def Del():
    global del_win

    del_layout = [
        [sg.Text('Are you sure?')],
        [sg.Yes(key='_YES_'), sg.No(key='_NO_')]
    ]

    del_win = sg.Window(head).Layout(del_layout)

