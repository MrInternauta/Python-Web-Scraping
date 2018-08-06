import requests #hacer consultas
from bs4 import BeautifulSoup #Parsear el html
import urllib #Guardar las imagenes

def run():
    for i in  range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i)) #accede por get a la url
        soup = BeautifulSoup(response.content, 'html.parser') #parsea (da formato) a la informacion de la pagina
        image_container= soup.find(id='comic') #busca el id comic
        image_url = image_container.find('img')['src'] #accede a etiqueta img y al atributo src de el id
        image_name = image_url.split('/')[-1]#se llama el ultimo elemento despues de la diagonal
        print('Descargando la imagen {}'.format(image_name))
        urllib.urlretrieve('https:{}'.format(image_url), image_name)
if __name__ == '__main__':
    run()
