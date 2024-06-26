#!/bin/bash

# Get the absolute path to the script
script_dir=$(dirname "$(readlink -f "$0")")

# Check if the script is inside the 'project' folder
if [[ $script_dir == */project ]]; then
    # If inside the 'project' folder, move up to the root directory
    project_dir=$(dirname "$script_dir")
    cd "$project_dir"
fi

# Run automated_pipline.py
python3 project/test_pipeline.py

# Check if the output file exists

echo | ls data/
if [ -f data/project.sqlite ]; then
    echo "Output file exists: data/project.sqlite"
else
    echo "Output file is missing!"
    exit 1
fi

# Perform additional tests

# Test if the city and energy_production tables exist in the database
python3 -c "
import sqlite3

# Connect to the database
conn = sqlite3.connect('data/project.sqlite')
c = conn.cursor()

# Check if the 'berlin' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'berlin\'')
table_exists = c.fetchone()

if table_exists:
    print('\'berlin\' table exists in the database')
else:
    print('ERROR: \'berlin\' table does not exist in the database')

# Check if the 'frankfurt' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'frankfurt\'')
table_exists = c.fetchone()

if table_exists:
    print('\'frankfurt\' table exists in the database')
else:
    print('ERROR: \'frankfurt\' table does not exist in the database')

# Check if the 'muenchen' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'muenchen\'')
table_exists = c.fetchone()

if table_exists:
    print('\'muenchen\' table exists in the database')
else:
    print('ERROR: \'muenchen\' table does not exist in the database')

# Check if the 'duesseldorf' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'duesseldorf\'')
table_exists = c.fetchone()

if table_exists:
    print('\'duesseldorf\' table exists in the database')
else:
    print('ERROR: \'duesseldorf\' table does not exist in the database')

# Check if the 'hamburg' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'hamburg\'')
table_exists = c.fetchone()

if table_exists:
    print('\'hamburg\' table exists in the database')
else:
    print('ERROR: \'hamburg\' table does not exist in the database')

# Check if the 'nuernberg' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'nuernberg\'')
table_exists = c.fetchone()

if table_exists:
    print('\'nuernberg\' table exists in the database')
else:
    print('ERROR: \'nuernberg\' table does not exist in the database')

# Check if the 'energy_production' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'energy_production\'')
table_exists = c.fetchone()

if table_exists:
    print('\'energy_production\' table exists in the database')
else:
    print('ERROR: \'energy_production\' table does not exist in the database')

# Check if the 'hannover' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'hannover\'')
table_exists = c.fetchone()

if table_exists:
    print('\'hannover\' table exists in the database')
else:
    print('ERROR: \'hannover\' table does not exist in the database')

# Check if the 'stuttgart' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'stuttgart\'')
table_exists = c.fetchone()

if table_exists:
    print('\'stuttgart\' table exists in the database')
else:
    print('ERROR: \'stuttgart\' table does not exist in the database')

conn.close()
"


# Test if there is data in tables
python3 -c "
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data/project.sqlite')

# Read the 'berlin' table into a DataFrame
df_berlin = pd.read_sql_query('SELECT * FROM berlin', conn)

if not df_berlin.empty:
    print('\'berlin\' table contains data')
else:
    print('\'berlin\' table has no data')

# Read the 'frankfurt' table into a DataFrame
df_frankfurt = pd.read_sql_query('SELECT * FROM frankfurt', conn)

if not df_frankfurt.empty:
    print('\'frankfurt\' table contains data')
else:
    print('\'frankfurt\' table has no data')

# Read the 'muenchen' table into a DataFrame
df_muenchen = pd.read_sql_query('SELECT * FROM muenchen', conn)

if not df_muenchen.empty:
    print('\'muenchen\' table contains data')
else:
    print('\'muenchen\' table has no data')

# Read the 'duesseldorf' table into a DataFrame
df_duesseldorf = pd.read_sql_query('SELECT * FROM duesseldorf', conn)

if not df_duesseldorf.empty:
    print('\'duesseldorf\' table contains data')
else:
    print('\'duesseldorf\' table has no data')

# Read the 'hamburg' table into a DataFrame
df_hamburg = pd.read_sql_query('SELECT * FROM hamburg', conn)

if not df_hamburg.empty:
    print('\'hamburg\' table contains data')
else:
    print('\'hamburg\' table has no data')

# Read the 'nuernberg' table into a DataFrame
df_nuernberg = pd.read_sql_query('SELECT * FROM nuernberg', conn)

if not df_nuernberg.empty:
    print('\'nuernberg\' table contains data')
else:
    print('\'nuernberg\' table has no data')

# Read the 'energy_production' table into a DataFrame
df_energy_production = pd.read_sql_query('SELECT * FROM energy_production', conn)

if not df_energy_production.empty:
    print('\'energy_production\' table contains data')
else:
    print('\'energy_production\' table has no data')

# Read the 'hannover' table into a DataFrame
df_hannover = pd.read_sql_query('SELECT * FROM hannover', conn)

if not df_hannover.empty:
    print('\'hannover\' table contains data')
else:
    print('\'hannover\' table has no data')

# Read the 'stuttgart' table into a DataFrame
df_stuttgart = pd.read_sql_query('SELECT * FROM stuttgart', conn)

if not df_stuttgart.empty:
    print('\'stuttgart\' table contains data')
else:
    print('\'stuttgart\' table has no data')

conn.close()
"
