import requests
from bs4 import BeautifulSoup

#
# url = 'https://pt.stackoverflow.com/questions/tagged/python'
# response = requests.get(url)
# # print(response.text)
#
# html = BeautifulSoup(response.text, 'html.parser')
# # print(html)
#
# for pergunta in html.select('.question-summary'):
#     titulo = pergunta.select_one('.question-hyperlink')
#     data = pergunta.select_one('.relativetime')
#     votos = pergunta.select_one('.vote-count-post strong')
#     print(data.text,votos.text,  titulo.text,sep='\t\t')

url = 'https://www.digikey.com/en/products/detail/yageo/RC0603JR-07300RL/726765'
response = requests.get(url)
# print(response.text)

html = BeautifulSoup(response.text, 'html.parser')
print(html)

# for atributo in html.select('.attr-col'):
#     # subcategory = pergunta.select_one('.question-hyperlink')
#     # case_code_in = pergunta.select_one('.relativetime')
#     # tolerance = pergunta.select_one('.vote-count-post strong')
#     # resistance = pergunta.select_one('.vote-count-post strong')
#
#     # print(data.text,votos.text,  titulo.text,sep='\t\t')
#     print(atributo.text, sep='\t\t')
