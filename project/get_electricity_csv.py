import requests, json, time
import pandas as pd
from io import StringIO

def requestSmardData(
        modulIDs=[8004169],
        timestamp_from_in_milliseconds=(int(time.time()) * 1000) - (3 * 3600) * 1000,
        timestamp_to_in_milliseconds=(int(time.time()) * 1000),
        region="DE",
        resolution="hour",
        language="de",
        type="discrete"
):
    # http request content
    url = "https://www.smard.de/nip-download-manager/nip/download/market-data"
    body = json.dumps({
        "request_form": [
            {
                "format": "CSV",
                "moduleIds": modulIDs,
                "region": region,
                "resolution": resolution,
                "timestamp_from": timestamp_from_in_milliseconds,
                "timestamp_to": timestamp_to_in_milliseconds,
                "type": type,
                "language": language
            }]})

    # http response
    data = requests.post(url, body)

    # create pandas dataframe out of response string (csv)
    df = pd.read_csv(StringIO(data.text), sep=';')
    df.to_csv("electric_generation.csv", encoding='utf-8', index=False)

# power generation
REALIZED_POWER_GENERATION = [1001224, 1004066, 1004067, 1004068, 1001223, 1004069, 1004071, 1004070, 1001226, 1001228,
                             1001227, 1001225]

if __name__ == "__main__":
    modules = REALIZED_POWER_GENERATION

    requestSmardData(modulIDs=modules, timestamp_from_in_milliseconds=1420066800000, timestamp_to_in_milliseconds=1715724000000)
