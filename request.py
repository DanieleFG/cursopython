import requests 

# def baixar_arquivo(url, endereco):
#     resposta = requests.get(url)
#     if resposta.status_code == requests.codes.OK:
#         with open(endereco, 'wb') as novo_arquivo:
#                 novo_arquivo.write(resposta.content)
#         print("Download finalizado. Arquivo salvo em: {}".format(endereco))
#     else:
#         resposta.raise_for_status()

def baixar_arquivo(url, endereco):
    resposta = requests.get(url, stream=True) #AQUI
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                for parte in resposta.iter_content(chunk_size=256): #AQUI TBM
                    novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

url = 'https://bot.empauta.com/scrapy/miles/get/db/list'
endereco = '/list' 
baixar_arquivo(url, endereco);