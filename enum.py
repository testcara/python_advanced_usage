from enum import Enum
SEASONS = Enum('SEASONS', ('Spring', 'Summer', 'Autumn', 'Winner'))


def switch(season_name):
    print(SEASONS[season_name].value)


switch('Autumn')
