from datetime import datetime
import requests


def make_trace(log_path):

    def _make_trace(old_function):

        def new_function(*args, **kwargs):
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.now()} '
                        'вызвана функция {old_function.__name__}\n')
                f.write(f'аргумены функции {args} {kwargs}\n')
                result = old_function(*args, **kwargs)
                f.write(f'возвращен результат {result}\n')
            return result

        return new_function

    return _make_trace


@make_trace('C:\hw5.log')
def get_hero_intel(*names):
    site = 'https://superheroapi.com/api/2619421814940190/'
    intel_dict = {}
    for name in names:
        try:
            hero_search = requests.get(site + '/search/' + name).json()
        except requests.exceptions.RequestException as e:
            return e
        if hero_search['response'] == 'error':
            return hero_search['error']
        for hero in hero_search['results']:
            if hero['name'] == name:
                intel_dict[name] = int(hero['powerstats']['intelligence'])
    return max(intel_dict, key=intel_dict.get)


if __name__ == "__main__":
    print(get_hero_intel('Hulk', 'Captain America', 'Thanos'))
