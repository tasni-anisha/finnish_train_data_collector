print("Finnish Train Movement Data Collector")
print("Project started successfully")
import requests
url = "https://rata.digitraffic.fi/api/v1/train-locations/latest"
response = requests.get(url, timeout=15)
print("Status code: " , response.status_code)
#convert JSON into Python data
trains =response.json()
#counting the train location record
print("Number of train records: ", len(trains))
print("\n" + "=" * 45)
print("FINNISH TRAIN MOVEMENT DATA")
print("=" * 45)

print("\nPART 1: TRAIN GPS INFORMATION")
print("-" * 45)
#display the first 5 trains
for train in trains[:5]:

    train_number = train["trainNumber"]

    coordinates = train["location"]["coordinates"]

    longitude = coordinates[0]
    latitude = coordinates[1]

    speed = train.get("speed")
    timestamp = train.get("timestamp")

    print("Train:", train_number)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Speed (km/h):", speed)
    print("Location recorded at:", timestamp)
    print("--------------------")
timetable_url = "https://rata.digitraffic.fi/api/v1/live-trains/station/TKU"
timetable_response = requests.get(timetable_url, timeout=15)
print("Timetable API status: ", timetable_response.status_code)
timetable_response.raise_for_status
timetable_trains= timetable_response.json()
print("The number of timetable records: ", len(timetable_trains))
print("\nPART 2: TURKU STATION TIMETABLE DATA")
print("-" * 45)

for train in timetable_trains[:5]:

    train_number = train["trainNumber"]

    for row in train["timeTableRows"]:

        if row["stationShortCode"] == "TKU":

            delay = row.get("differenceInMinutes")

            if delay is None:
                delay_text = "Not available"
            elif delay > 0:
                delay_text = f"{delay} minutes late"
            elif delay < 0:
                delay_text = f"{abs(delay)} minutes early"
            else:
                delay_text = "On time"

            print("Train number:", train_number)
            print("Event:", row["type"])
            print("Delay:", delay_text)
            print("--------------------")