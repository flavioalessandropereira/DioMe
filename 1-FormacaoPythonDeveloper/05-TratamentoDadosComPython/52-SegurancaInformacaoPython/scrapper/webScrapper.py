from bs4 import BeautifulSoup

import requests

#objeto site recebendo o conteudo da requisicao http do site...
site = requests.get("https://www.climatempo.com.br/").content


#objeto soup baixnado do site o html
soup = BeautifulSoup(site, 'html.parser')

#transforma html em string e o print vai exibir o html da página
print(soup.prettify())

temperatura = soup.find("span", class_ = "_block _marginb-5 -gray")

# print(temperatura.string)

print(soup.title.string)
print(soup.a)
print(soup.p)
print(soup.find('admin'))