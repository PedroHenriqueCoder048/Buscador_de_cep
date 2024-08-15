import PySimpleGUI as sg 
from tkinter import *
from api.requerts import return_info_cep

layout = [
       
       [sg.Text("Digite seu cep:")],
       [sg.InputText(size=(35,10),key='inp-cep'),sg.Button('Buscar',key="btn_buscar")],
       [sg.Output(key="out-cep",size=(42,21))],
       [sg.Button('Fechar', key='btn-fechar')]
        
        ]

def get_cep(cep:str):
    return cep


def main_window():
    window = sg.Window(layout=layout,title='buscador de cep',size=(340,410))
    while True:
        event , values = window.read()
        
        dic = return_info_cep(window['inp-cep'].get())
        cep = dic['cep']
        logr =dic['logradouro']
        compl=dic['complemento']
        bairro = dic['bairro']
        local= dic['localidade']
        uf= dic['uf']
        ibge = dic['ibge']
        gia = dic['gia']
        ddd = dic['ddd']
        siafi = dic['siafi']
        
        if event == sg.WIN_CLOSED or event == 'btn-fechar':
            break
        
        
        if event == 'btn_buscar':
            window['out-cep'].update('')
            print(f'CEP: {cep}')
            print(f'LOGRADOURO: {logr}')
            print(f'COMPLEMENTO: {compl}')
            print(f'BAIRRO: {bairro}')
            print(f'LOCALIDADE: {local}')
            print(f'UF: {uf}')
            print(f'IBGE: {ibge}')
            print(f'GIA: {gia}')
            print(f'DDD: {ddd}')
            print(f'SIAFI: {siafi}')
            continue
    window.close()



def main():
    main_window()

main()
