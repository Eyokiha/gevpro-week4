#!/usr/bin/env python
#Hennie Veldthuis

import json
from collections import namedtuple

def main():
    with open('blood-die.json') as b_d_json:
        blood_die = json.load(b_d_json)
        b_d_json.close()
        
    list_blood_die = []
    country_tuple = namedtuple('country_tuple', 'language, classification')
    
    for el in blood_die:
        blood = el[2].split()
        die   = el[3].split()
        [list_blood_die.append(country_tuple(el[0], el[1])) for word_blood in blood if word_blood in die]
        
    [print(el) for el in list_blood_die]


if __name__ == '__main__':
    main()
