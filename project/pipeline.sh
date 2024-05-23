#!/bin/bash
python3 ./project/get_electricity_csv.py
python3 ./project/get_weather_data.py

jv ./project/project_pipeline.jv
jv ./project/project_pipeline2.jv
jv ./project/project_pipeline3.jv
jv ./project/project_pipeline4.jv
jv ./project/project_pipeline5.jv

rm -rf ./project/*.csv