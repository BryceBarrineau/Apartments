import numpy as np

def parse_page(soup, df):
    for item in soup.find_all('article', class_ = 'placard'):
        url = ''
        rent = ''
        contact = ''

        if item.find('a', class_ = 'property-link') is None:
            url = np.nan
        else:
            url = item.find('a', class_ = 'property-link').get('href')


        if item.find('span', class_='js-placardTitle title') is None: 
            name = np.nan
        else:
            name = item.find('span', class_ = 'js-placardTitle title').getText().strip()

        if item.find('div', class_ = 'property-address js-url') is None:
            address = np.nan
        else:
            address = item.find('div', class_ = 'property-address js-url').getText().strip()
        
        if item.find('p', class_='property-pricing') is None: 
            rent = np.nan
        else:
            rent = item.find('p', class_='property-pricing').getText().strip()

        if item.find('p', class_='property-beds') is None: 
            beds = np.nan
        else:
            beds = item.find('p', class_='property-beds').getText().strip()

        df.loc[len(df)] = [url, name, address, rent, beds]
        print(len(df), [url, name, address, rent, beds])

# Function to convert an address into latitude and longitude coordinates
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def geocode_address(address):
    # Initialize the geocoder with a user-agent name
    geolocator = Nominatim(user_agent='apartmentParser')
    try:
        # Attempt to get the geolocation data for the given address
        location = geolocator.geocode(address, timeout=10)
        
        # If a location is found, return latitude and longitude as a tuple
        if location is not None:
            return location.latitude, location.longitude
        else:
            return 'NOT FOUND'  # If the address cannot be found

    except GeocoderTimedOut:
        return 'TIMEOUT'  # Handle timeout errors to prevent crashes

    except Exception as e:
        return f'ERROR: {e}'  # Catch any other unexpected errors
    
def notAComplex(row):
    if row['Address'] is None and row['Complex Name'] and row['Complex Name'][-5:].isdigit():
        row['Address'] = row['Complex Name']
        row['Complex Name'] = None
    return row