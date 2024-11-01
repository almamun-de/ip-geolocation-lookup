# IP Geolocation Lookup Script

## Description

This is a simple Python script that fetches geolocation information for a given IP address using the `ip-api.com` public API. The script displays information such as the country, region, city, ZIP code, ISP, and geographical coordinates (latitude and longitude) for the IP address.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/almamun-de/ip-geolocation-lookup.git
   cd ip-geolocation-lookup

Install the requests library if you don't have it already:
pip install requests

Run the script:
python3 geolocation_lookup.py

Example
When you run the script and enter an IP address like 8.8.8.8 (Google's public DNS), you might see output similar to this:
Enter the IP address: 8.8.8.8
IP: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ZIP: 94035
ISP: Google LLC
Latitude: 37.4056
Longitude: -122.0775
