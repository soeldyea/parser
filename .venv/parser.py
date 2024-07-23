from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def delete_div(code, tag, arg):
    for div in code.find_all(tag, arg):
        div.decompose()
def clear_code(url):
    inner_html_code = str(urlopen(url).read(), 'utf-8')
    inner_soup = bs(inner_html_code, 'html.parser')
    inner_soup = inner_soup.find('div', {'class': 'article-content'})

    delete_div(inner_soup, 'div', {'class':'lazyblock-titry-Z23QzIj wp-block-lazyblock-titry'})
    for i in range(1000):
        delete_div(inner_soup, 'div', {'class':f'wp-block-lazyblock-banner{i}'})
    delete_div(inner_soup, 'div', {'class':'accordion'})
    delete_div(inner_soup, 'div', {'class':'wp-block-lazyblock-link-aside'})
    delete_div(inner_soup, 'pre', '')
    delete_div(inner_soup, 'code', '')

    return inner_soup.get_text()

def get_all_url(data_title):
    html_code = str(urlopen('https://thecode.media/all/').read(), 'utf-8')
    soup = bs(html_code, 'html.parser')

    s = soup.find(attrs={'data-title':data_title})
    url = []
    for tag in s.select('li:has(a)'):
        url.append(tag.find('a')['href'])

    content_file_name = data_title + '_content.txt'
    file = open(content_file_name, 'w')
    for x in url:
        file.write(clear_code(x)+'/n')

    file.close()

division = ['Ахах','Не стыдно','Это баг','Это как']
for el in division:
    get_all_url(el)
print(clear_code('https://thecode.media/parsing/'))




