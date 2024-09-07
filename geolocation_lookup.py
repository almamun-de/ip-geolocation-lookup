import requests

def get_geolocation(ip):
    """
    Fetches and displays the geolocation data for the provided IP address.
    
    :param ip: The IP address to look up.
    """
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success':
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ZIP: {data['zip']}")
        print(f"ISP: {data['isp']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
    else:
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    get_geolocation(ip_address)
