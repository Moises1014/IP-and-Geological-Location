from ipstack import GeoLookup

# Create the GeoLookup object using your API key.
geo_lookup = GeoLookup("Your acess key for the Api here")

# Create and get the ip or website neede
Ip_or_Website=input('please enter a website(ex google.com) or Ip address to get the location it came from: ')


def get_lacation_of(Ip_or_Website):
  try:
    # Retrieve the location information for 
    # any website by using it's hostname.
    # or by IP adrees
    # This function will work with hostnames
    # or IP addresses.

    location = geo_lookup.get_location(Ip_or_Website)

    # If we are unable to retrieve the location information
    # for an IP address, null will be returned.
    if location is None:
        print("Failed to find location.")
    else:
        # Print the Location dictionary.
        for keys,values in location.items():
          print(keys+':')
          print(values)    
  except Exception as e:
    print(e)

#calls the function to run
get_lacation_of(Ip_or_Website)