Finnish Train Movement Data Collector

A Python application that retrieves real railway data from Finland using the Digitraffic Railway API.
This project was developed to explore how Python can communicate with public APIs and process real-world transportation data.

Features

Retrieves train numbers and GPS coordinates
Displays train speeds in km/h
Shows timestamps of train location measurements
Retrieves arrival and departure information for Turku railway station
Displays timetable delay information when available
Handles missing delay values without assuming trains are on time

Technologies Used
Python 3
Requests – HTTP requests
JSON – API response processing
Digitraffic Railway API – Railway data source

How to Run

1. Clone the repository
git clone https://github.com/tasni-anisha/finnish_train_data_collector.git
2. Open the project folder
cd finnish_train_data_collector
3. Install the required dependency
python -m pip install -r requirements.txt
4. Run the program
python main.py

How It Works
The application uses two Digitraffic API endpoints. The first retrieves the latest reported train locations, including train numbers, GPS coordinates, speeds, and timestamps.
The second retrieves timetable information for Turku railway station (TKU), including arrival and departure events and reported delays when available.
Both API responses are processed in JSON format and displayed in the terminal.

Data Source
Digitraffic Railway Traffic API
https://www.digitraffic.fi/en/railway-traffic/

Project Scope
This is a data collection project. It does not predict train delays or provide automatic decision-making.
The program retrieves current information when executed; it does not continuously track trains or store historical data.
