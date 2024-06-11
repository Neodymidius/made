import csv
import json
import zipfile
import os

import pandas as pd
import requests

import unittest


class TestCaseDataSources(unittest.TestCase):
    def test_url_valid_energy(self):
        modules = [1001224, 1004066, 1004067, 1004068, 1001223, 1004069, 1004071, 1004070, 1001226, 1001228, 1001227,
                   1001225]
        url = "https://www.smard.de/nip-download-manager/nip/download/market-data"
        body = json.dumps({
            "request_form": [
                {
                    "format": "CSV",
                    "moduleIds": modules,
                    "region": "DE",
                    "resolution": "hour",
                    "timestamp_from": 1420066800000,
                    "timestamp_to": 1420066800000,
                    "type": "discrete",
                    "language": "de"
                }]})

        # http response
        data = requests.post(url, body)
        self.assertEqual(data.status_code, 200)  # add assertion here

    def test_url_valid_weather(self):
        r = requests.get(
            "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature"
            "/historical/")
        self.assertEqual(r.status_code, 200)

    def test_data_of_weather_station(self):
        r = requests.get(
            "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature"
            "/historical/stundenwerte_TU_00003_19500401_20110331_hist.zip")

        with open("test.zip", 'wb') as file:
            for chunk in r.iter_content(chunk_size=8192):
                file.write(chunk)
        self.assertIs(os.path.isfile("test.zip"), True)
        with zipfile.ZipFile("test.zip", 'r') as zip_ref:
            last_file = zip_ref.namelist()[-1]
            with zip_ref.open(last_file) as zf, open(last_file, 'wb') as f:
                f.write(zf.read())

        with open(last_file, 'r') as txt_file:
            lines = txt_file.readlines()

        with open(os.path.abspath(".") + "/test.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')

            for line in lines:
                row = [x.strip() for x in line.split(';')]
                writer.writerow(row)
        self.assertIs(os.path.isfile("test.csv"), True)

        os.remove("test.zip")
        os.remove(last_file)

    def test_data_weather_csv(self):
        df = pd.read_csv("test.csv", sep=';')
        test = list(df.axes[1].values)
        df_test = ["STATIONS_ID,MESS_DATUM,QN_9,TT_TU,RF_TU,eor"]
        self.assertEqual(test, df_test)
        os.remove("test.csv")


if __name__ == '__main__':
    unittest.main()
