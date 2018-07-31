import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
for country in countries:
    print( "%-50s  %s" % (country['name'], country['capital']))



