import geoip2.database
import os

def get_geolocation(ip, reader):
    try:
        response = reader.city(ip)
        country = response.country.name
        return country
    except geoip2.errors.AddressNotFoundError:
        return "Unknown"

def process_file(input_file, output_file, db_file):
    if not os.path.isfile(db_file):
        print(f"Database file '{db_file}' does not exist.")
        return
    reader = geoip2.database.Reader(db_file)
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            ip = line.strip()
            country = get_geolocation(ip, reader)
            outfile.write(f"{ip} ({country})\n")
    reader.close()

input_file = 'list.txt'  #input file path
output_file = 'output_geo.txt'  #output file path
db_file = 'GeoLite2-City.mmdb'  #GeoLite2 db path
process_file(input_file, output_file, db_file) 
