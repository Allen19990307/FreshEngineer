def name(City,Country,population =''):
    if population:
        country = f"{City},{Country}-population {population}"
    else:
        country = f"{City},{Country}"
    return country