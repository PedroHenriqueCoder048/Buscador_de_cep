import requests

def return_info_cep(cep):
    url_api=f'https://viacep.com.br/ws/{cep}/json/'
    request = requests.get(url_api)
    dic=request.json()
    request.close()
    return dic