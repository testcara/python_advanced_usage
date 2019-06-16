dict_season = {
    "spring": "It is Spring!",
    "autumn": "It is Autumn!",
    "summer": "It is Summer!",
    "winner": "It is Winner!"
}


def switch(seanson_name):
    print(dict_season.get(seanson_name, None))


switch('spring')
