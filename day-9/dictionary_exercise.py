#!/usr/bin/python3
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
  new_input = {}
  new_input["country"] = country_visited
  new_input["visits"] = times_visited
  new_input["cities"] = cities_visited
  travel_log.append(new_input)

