# STATUS:
'''
inital code:

capitals = {
"France": "Paris",
â€œSpainâ€: Madrid,
â€œGermanyâ€: â€œBerlin,
â€œJapan'': â€œTokyoâ€,
â€œNorwayâ€: â€œOsloâ€
}

for country, city in capitals.items()
    print(fâ€The capital of {country) is {â€˜cityâ€™}.â€
'''



capitals = {
    'France': 'Paris',
    'Spain': 'Madrid',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'Norway': 'Oslo'}

for country, city in capitals.items():
    print(f"The capital of {country} is {city}")
