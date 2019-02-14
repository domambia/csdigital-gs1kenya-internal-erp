from pycountry import countries 

def get_country():
    list_country = [x for x in countries]
    country_name = []
    for  y in range(len(list_country)):
        country_name.append((list_country[y].name, list_country[y].name,))

    return tuple(country_name)

def get_sectors():
    list_sectors = ['Academia', 'Agribusiness', 'Helathcare', 'Manufacturer,Trading &Financial Institutions', 'Retailer', 
                    'Transport / Communication', 'Supply  Chain,warehousing  & construction']
    sectors = []
    for sector in list_sectors:
        sectors.append((sector.capitalize(), sector ,))
    return tuple(sectors)



def get_categs():
    list_categs = ['Category A', 'Category B', 'Category B', 'Category C', 'Category D', 
                    'Category E']
    categs = []
    for categ in list_categs:
        categs.append((categ.capitalize(), categ ,))
    return tuple(categs)

