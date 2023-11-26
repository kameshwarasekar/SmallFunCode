from bs4 import BeautifulSoup
import requests
import random
import pickle


def load_data():
    anime_dict = {}
    url = 'https://www.imdb.com/list/ls033398199/'
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    table = html.find_all('div', attrs={'class': 'lister-item-content'})
    for anime in table:
        anime_title = anime.find('h3', attrs={'class':'lister-item-header'}).find('a').text
        anime_dict[anime_title] = 1
    return anime_dict


def application():
    try:
        anime_dict = pickle.load(open('anime_list.pkl', 'rb'))
    except:
        anime_dict = load_data()
    if len(anime_dict) == 0:
        print('Damn Weeb you have watched all the animes, Get a Life!')
        return;
    f2 = open('anime_list.pkl', 'wb')
    chosen_anime = random.choice(list(anime_dict.keys()))
    del anime_dict[chosen_anime]
    print('The chosen anime is: ', chosen_anime)
    pickle.dump(anime_dict, f2)
    f2.close()

application()
