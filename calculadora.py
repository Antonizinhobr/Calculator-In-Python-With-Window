import PySimpleGUI as sg

#Autor: Anthonny Michael, estudante de programaçao Front e Back End, Python, C++ e hacker ético(Pentester)#

while True:
    layout1 = [
        [sg.Text('Primeiro Número', size=(15, 1)), sg.InputText(key='número1', size=(15, 1))],
        [sg.Text('Segundo Número', size=(15, 1),), sg.InputText(key='número2', size=(15, 1))],
        [sg.Button('Salvar Números')]
    ]

    window = sg.Window('Calculadora Python', layout1)
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        window.close()
        break

    if event == 'Salvar Números':
        número1 = values['número1']
        número2 = values['número2']
        window.hide()
        layout2 = [
            [sg.Text('Escolha uma opção', size=(15, 1))],
            [sg.Button('Soma'), sg.Button('Subtração'), sg.Button('Multiplicação'), sg.Button('Divisão')]
        ]

        window2 = sg.Window('Calculadora Python', layout2)
        event2, values2 = window2.read()

        if event2 == sg.WINDOW_CLOSED:
            window.close()
            break

        if event2 == 'Soma':
            window.close()
            window2.close()

            resultado = float(número1)+float(número2)
            layout_soma = [
                [sg.Text('Soma', size=(15, 1))],
                [sg.Text(resultado, size=(15, 1))]
            ]

            window_soma = sg.Window('Calculadora Python', layout_soma)

            event_soma, valores_soma = window_soma.read()

        if event2 == 'Subtração':
            window2.close()
            resultado_subtração = float(número1) - float(número2)
            layout_subtração = [
                [sg.Text('Subtração', size=(15, 1))],
                [sg.Text(resultado_subtração, size=(15, 1))]
            ]

            window_subtração = sg.Window('Calculadora Python', layout_subtração)

            event_subtração, valores_subtração  = window_subtração.read()

        if event2 == 'Multiplicação':
            window2.close()
            resultado_multiplicação = float(número1) * float(número2)
            layout_multiplicação = [
                [sg.Text('Multiplicação', size=(15, 1))],
                [sg.Text(resultado_multiplicação, size=(15, 1))]
            ]

            window_multiplicação = sg.Window('Calculadora Python', layout_multiplicação)

            events_multiplicação, valores_multiplicação = window_multiplicação.read()

        if event2 == 'Divisão':
            window2.close()
            resultado_divisão = float(número1) / float(número2)
            layout_divisão = [
                [sg.Text('Divisão', size=(15, 1))],
                [sg.Text(resultado_divisão, size=(15, 1))]
            ]

            window_divisão = sg.Window('Calculadora Python', layout_divisão)

            events_divisão, valores_divisão = window_divisão.read()