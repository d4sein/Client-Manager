import PySimpleGUI as sg
import os
import shutil
import config
import gui


class Client:
    def __init__(self, name, number, email, address, obs):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.obs = obs


def Manage():
    if config.values['_NAME_'] == '':
        sg.Popup('Client name can\'t be empty!')
        return

    if config.values['_NAME_'] in os.listdir(config.clients):
        sg.Popup('Client already exists!')
        return

    # it removes \n from string
    config.client_data.append(config.values['_NAME_'].strip())
    config.client_data.append(config.values['_NUM_'].strip())
    config.client_data.append(config.values['_EMAIL_'].strip())
    config.client_data.append(config.values['_ADDRESS_'].strip())
    config.client_data.append(config.values['_OBS_'])

    config.client = Client(*config.client_data)
    config.client_path = config.clients + config.client.name

    if not os.path.exists(config.client_path):
        # if the _EDIT_ button was not selected
        if not config.edit:
            # it tries to create client's directory
            try:
                os.makedirs(config.clients + config.client.name + '/' + config.img)
                os.makedirs(config.clients + config.client.name + '/' + config.project)
            # if it can't, throws an exception
            except OSError:
                pass
        # if the _EDIT_ button was selected
        if config.edit:
            os.rename(config.clients + config.client_data[0], config.client_path)

    # it opens info.txt and writes the client's data
    with open(config.client_path + '/info.txt', 'w') as info:
        info.write(config.client_format.format(*config.client_data))
    info.close()

    # if the _EDIT_ button was not selected
    if not config.edit:
        sg.Popup('Client added!')
    # if the _EDIT_ button was selected
    if config.edit:
        sg.Popup('Client saved!')
        gui.main_win.FindElement('_NEW_').Update('New')
        config.edit = False

    config.client_data = []


def Edit():
    global absolute_values

    # if the user didn't select any folder
    if config.edit_values['_BROWSE_'] is None or config.edit_values['_BROWSE_'] == '':
        sg.Popup('You didn\'t select any folder or directory is invalid!')
        gui.main_win.FindElement('_NEW_').Update('New')
        gui.edit_win.Close()
        return

    address = config.edit_values['_BROWSE_']
    gui.edit_win.Close()
    address = list(address.split('/'))

    edit_values = []
    obs_values = []
    absolute_values = []

    # it tries to open the selected folder
    try:
        with open(config.clients + address[-1] + '/info.txt', 'r') as info:
            for line in info:
                line = list(line.split(': '))
                edit_values.append(line[-1])
        info.close()
    # if it can't, Popup a message
    except OSError:
        sg.Popup('You didn\'t select any folder or directory is invalid!')
        return

    # this for loop separates the observation field from the rest of the info
    for i in edit_values:
        if edit_values.index(i) >= 4:
            obs_values.append(i)
        elif edit_values.index(i) <= 3:
            absolute_values.append(i)
        else:
            pass

    obs_values = ''.join(obs_values)
    absolute_values.append(obs_values)

    # it updates all info on the screen
    gui.main_win.FindElement('_NAME_').Update(absolute_values[0])
    gui.main_win.FindElement('_NUM_').Update(absolute_values[1])
    gui.main_win.FindElement('_EMAIL_').Update(absolute_values[2])
    gui.main_win.FindElement('_ADDRESS_').Update(absolute_values[3])
    gui.main_win.FindElement('_OBS_').Update(absolute_values[4])


def Del():
    global absolute_values

    if os.path.exists(config.clients + absolute_values[0].strip()):
        shutil.rmtree(config.clients + absolute_values[0].strip(), ignore_errors=True)
        sg.Popup('{} was deleted!'.format(absolute_values[0].strip()))
    else:
        sg.Popup('{} doesn\'t exist or cannot be deleted.'.format(absolute_values[0].strip()))
        return


def Search():
    result = False
    folder = os.listdir(config.clients)
    list_of_clients = []

    # it loops through the client's info and it tries to find the keyword
    for c in folder:
        with open(config.clients + c + '/info.txt', 'r') as info:
            for line in info:
                if config.values['_KEYWORD_'].lower() in line.lower() and config.values['_KEYWORD_'].lower() != '':
                    result = True
                    with open(config.clients + c + '/info.txt', 'r') as info:
                        if c not in list_of_clients:
                            print(info.read())
                            list_of_clients.append(c)
                    info.close()
        info.close()
    # if it can't find anything, it returns a Popup message
    if not result:
        sg.Popup('Keyword not found or invalid.')


def Source():
    source = os.path.dirname(os.path.abspath(__file__))
    os.startfile(source + config.abs_clients)
