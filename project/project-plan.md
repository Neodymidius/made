# Project Plan

## Title
<!-- Give your project a short title. -->
Sunshine or Storms: Exploring the Weather's Influence on Stock Market Trends

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. To what degree is the weather a factor to the energy consumption and does an increase of extreme weather show any influence to the energy consumption?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
With expected rising electric energy production arises the question to what degree the daily weather 
influences the electric energy production in Germany. Therefore, the history of the electric energy production gets compared
to the weather data. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: Weather Data
* Metadata URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/TU_Stundenwerte_Beschreibung_Stationen.txt
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/stundenwerte_TU_00052_19760101_19880101_hist.zip
* Data Type: txt

Multiple URLs will be inserted here for different weather steations in Germany

### Datasource 2: Electric energy production
* Metadata URL: https://www.smard.de/home/downloadcenter/download-marktdaten/?downloadAttributes=%7B%22selectedCategory%22:1,%22selectedSubCategory%22:1,%22selectedRegion%22:%22DE%22,%22selectedFileType%22:%22CSV%22,%22from%22:1420066800000,%22to%22:1715723999999%7D
* Data URL: https://www.smard.de/home/downloadcenter/download-marktdaten/?downloadAttributes=%7B%22selectedCategory%22:1,%22selectedSubCategory%22:1,%22selectedRegion%22:%22DE%22,%22selectedFileType%22:%22CSV%22,%22from%22:1420066800000,%22to%22:1715723999999%7D
* Data Type: CSV

Only manuel data download possible for this website. But .csv is the output.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Overview Issue [#6][i1]
2. ...

[i1]: https://github.com/Neodymidius/made/issues/6