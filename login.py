import PySimpleGUI as sg

sg.theme('Discord')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')],
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'admin' and valores['senha'] == '1234':
            sg.popup("Admin logado!")
        
        elif valores['usuario'] == 'user' and valores['senha'] == '1234':
            sg.popup("User logado!")

        else:
            sg.popup_error('Credenciais incorretas!')