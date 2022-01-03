import re

import bs4
import requests

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}


def getHtml(url, headers):
    if url == 'outfile.html':
        with open('outfile.html', 'r', encoding='utf-8') as reader:
            r = reader.read()
        return r
    else:
        r = requests.get(url, headers=headers, verify=False)
        r.raise_for_status()
        return r.text


if __name__ == '__main__':

    headers = {
        'User-Agent':
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
         '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36')
    }
    url = 'https://habr.com'

    soup = bs4.BeautifulSoup(getHtml('outfile.html', headers),
                             features='html.parser')

    articles = soup.find_all('article')

    for article in articles:
        prev_set = set(word.lower() for word in re.split(
            "\s|(?<!\d)[,.](?!\d)",
            article.find(class_='article-formatted-body').text))
        if KEYWORDS & prev_set:
            art_time = article.time['title']
            art_name = article.find('h2',
                                    class_='tm-article-snippet__title').text
            art_link = url + article.h2.a['href']
            print(f"{art_time} - {art_name} - {art_link}")
