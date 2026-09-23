#!/usr/bin/env python3
#7.3
def famous_births(historical_figures):
    sorted_figures = sorted(
        historical_figures.values(),
        key=lambda person: person["date_of_birth"]
    )
    for person in sorted_figures:
        print(person["name"] + " is a great scientist born in " + person["date_of_birth"] + ".")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)