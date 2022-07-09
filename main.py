# from pprint import pprint
#
# import requests
#
# def super_hero_info():
#     heroes = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
#     hero_dict = {}
#     heroes_name = ['Hulk', 'Captain America', 'Thanos']
#     for hero in heroes.json():
#         name = hero['name']
#         if name in heroes_name:
#             hero_dict[name] = hero["powerstats"]["intelligence"]
#     print(max(hero_dict, key=hero_dict.get))
#
#
# if __name__ == '__main__':
#     super_hero_info()





