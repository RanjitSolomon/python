# {
#   key: [List],
#    key2: {Dict},
# }

travel = {
    "France" : ["Paris", "Lille"],
    "Germany": ["Berlin", "Hamburg"]
}

travel_log_visited = {
    "France" : { "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visit": 12},
    "Germany" : { "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visit": 5},
}

travel_log = [
    {
        "country": "France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visit": 12
    },
    {
        "country": "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visit": 5
    },
]

def add_new_country(cntry, visits, list_of_cities):
    travel_log.append({"country": cntry, "cities_visited" : list_of_cities, "total_visit": visits})



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
for country in travel_log:
    print(country)




