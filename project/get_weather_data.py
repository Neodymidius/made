import requests
import re
import zipfile
import csv
import os

stuttgart = "04931 19880101 20240521 371 48.6883 9.2235 Stuttgart-Echterdingen Baden-Württemberg"
nuremberg = "03668 19510101 20240521 314 49.5030 11.0549 Nürnberg Bayern"
munich = "03379 19970701 20240521 515 48.1632 11.5429 München-Stadt Bayern"
frankfurt = "01420 19810101 20240521 100 50.0259 8.5213 Frankfurt/Main Hessen"
duesseldorf = "01078 19760301 20240521 37 51.2960 6.7686 Düsseldorf Nordrhein-Westfalen"
hannover = "02014 19490101 20240521 55 52.4644 9.6779 Hannover Niedersachsen"
hamburg = "01228 20020101 20240521 0 54.1651 6.3460 Hamburg Hamburg"
berlin = "00433 19510101 20240521 48 52.4676 13.4020 Berlin-Tempelhof Berlin"

stations = [stuttgart, nuremberg, munich, frankfurt, duesseldorf, hannover, berlin, hamburg]

def get_zip_name():
    # all stations are having the name: stundenwerte_TU_{id}_{from}_{to}_hist.zip, idea: find by id.
    dict_station_zip_name = {}
    r = requests.get("https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/")
    text = r.text
    for station in stations:
        station = station.split(" ")
        id = station[0]
        name = station[6]
        pattern = rf'href="([^"]*{id}[^"]*)"'
        dict_station_zip_name[id+name] = re.search(pattern, text).group(1)

    return dict_station_zip_name

def get_zip_file(file_name):
    url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/"
    r = requests.get(url+file_name)
    with open(file_name, 'wb') as file:
        for chunk in r.iter_content(chunk_size=8192):
            file.write(chunk)


def extract_weather_data(file_name):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        last_file = zip_ref.namelist()[-1]
        with zip_ref.open(last_file) as zf, open(last_file, 'wb') as f:
            f.write(zf.read())
    return last_file


def convert_txt_to_csv(txt_filename, csv_filename):
    # Open the text file in read mode
    with open(txt_filename, 'r') as txt_file:
        # Read all lines from the text file
        lines = txt_file.readlines()

    # Open the CSV file in write mode
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        # Write each line to the CSV file
        for line in lines:
            # Split the line by semicolon and strip any leading/trailing whitespace
            row = [x.strip() for x in line.split(';')]
            # Write the row to the CSV file
            writer.writerow(row)





if __name__ == "__main__":
    stations_file_names = get_zip_name()
    for key, file_name in stations_file_names.items():
        print(file_name)
        get_zip_file(file_name)
        last_file = extract_weather_data(file_name)
        convert_txt_to_csv(last_file, file_name[:-4]+".csv")
        os.remove(file_name)
        os.remove(last_file)