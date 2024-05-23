import requests, json
import pandas as pd
from io import StringIO

def requestSmardData(
        modulIDs, timestamp_from_in_milliseconds, timestamp_to_in_milliseconds,
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
    # I really wished I could've used jayvee for the dataframe manipulation but pandas' dataframe are just too handy to not use
    df = pd.read_csv(StringIO(data.text), sep=';')
    df.rename(columns={'Datum von': 'Time'}, inplace=True)
    df.drop(columns=['Datum bis'], inplace=True)
    df = culminate_data(df)
    df = convert_time_to_my_format(df)
    df.to_csv("project/electric_generation.csv", encoding='utf-8', index=False)

def culminate_data(df):
    #first make strings to doubles:
    columns_to_convert = [
        'Biomasse [MWh] Berechnete Auflösungen', 'Wasserkraft [MWh] Berechnete Auflösungen',
        'Wind Offshore [MWh] Berechnete Auflösungen', 'Wind Onshore [MWh] Berechnete Auflösungen',
        'Photovoltaik [MWh] Berechnete Auflösungen', 'Sonstige Erneuerbare [MWh] Berechnete Auflösungen',
        'Kernenergie [MWh] Berechnete Auflösungen', 'Braunkohle [MWh] Berechnete Auflösungen',
        'Steinkohle [MWh] Berechnete Auflösungen', 'Erdgas [MWh] Berechnete Auflösungen',
        'Pumpspeicher [MWh] Berechnete Auflösungen', 'Sonstige Konventionelle [MWh] Berechnete Auflösungen'
    ]

    for column in columns_to_convert:
        df[column] = df[column].str.replace(".", "", regex=False)
        df[column] = df[column].str.replace(",", ".", regex=False)
        df[column] = df[column].str.replace("-", "0", regex=False)


    df[columns_to_convert] = df[columns_to_convert].astype(float)

    df['Erneuerbare Energie [MWh]'] = df[['Biomasse [MWh] Berechnete Auflösungen', 'Wasserkraft [MWh] Berechnete Auflösungen', 'Wind Offshore [MWh] Berechnete Auflösungen', 'Wind Onshore [MWh] Berechnete Auflösungen', 'Photovoltaik [MWh] Berechnete Auflösungen', 'Sonstige Erneuerbare [MWh] Berechnete Auflösungen']].sum(axis=1)
    df['Konventionelle Energie [MWh]'] = df[['Kernenergie [MWh] Berechnete Auflösungen', 'Braunkohle [MWh] Berechnete Auflösungen', 'Steinkohle [MWh] Berechnete Auflösungen', 'Erdgas [MWh] Berechnete Auflösungen', 'Pumpspeicher [MWh] Berechnete Auflösungen', 'Sonstige Konventionelle [MWh] Berechnete Auflösungen']].sum(axis=1)
    df['Total [MWh]'] = df[['Erneuerbare Energie [MWh]', 'Konventionelle Energie [MWh]']].sum(axis=1)
    df.drop(columns=columns_to_convert, inplace=True)
    return df

def convert_time_to_my_format(df):
    df['Time'] = pd.to_datetime(df['Time'], format='%d.%m.%Y %H:%M')
    df['Time'] = df['Time'].dt.strftime('%Y%m%d%H')
    return df

if __name__ == "__main__":
    modules = [1001224, 1004066, 1004067, 1004068, 1001223, 1004069, 1004071, 1004070, 1001226, 1001228, 1001227,
               1001225] # got that from inspecting the post request; essentially each number is one power generation type


    requestSmardData(modulIDs=modules, timestamp_from_in_milliseconds=1420066800000, timestamp_to_in_milliseconds=1715724000000)
