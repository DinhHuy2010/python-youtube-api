import requests

channel_id = "UCmSp4bDxS9R0jpeZEvkut2g"
api_key = "YOUR_KEY_NERD"
base_url = "https://www.googleapis.com/youtube/v3/channels"
url = f"{base_url}?key={api_key}&part=snippet,statistics&id={channel_id}"
request_url = requests.get(url)
if request_url.status_code == 200:
    json_data = request_url.json()
else:
    print("Error occurred.")

channel_data = json_data["items"][0]
channel_properties = channel_data["snippet"]
channel_stat = channel_data["statistics"]

for property in channel_properties:
    if property == "thumbnails" or property == "localized":
        pass
    else:
        print(property + ": " +str(channel_properties[property]))

for stat in channel_stat:
    print(stat + ": " + str(channel_stat[stat]))

print("###########################")

channel_id = "UCFAiFyGs6oDiF1Nf-rRJpZA"
url = f"{base_url}?key={api_key}&part=snippet,statistics&id={channel_id}"

request_url = requests.get(url)
if request_url.status_code == 200:
    json_data_2 = request_url.json()
else:
    print("Error occurred.")

channel_data_2 = json_data_2["items"][0]
channel_properties_2 = channel_data_2["snippet"]
channel_stat_2 = channel_data_2["statistics"]

for property in channel_properties_2:
    if property == "thumbnails" or property == "localized":
        pass
    else:
        print(property + ": " +str(channel_properties_2[property]))

for stat in channel_stat_2:
    print(stat + ": " + str(channel_stat_2[stat]))

catch = list(map(int, [channel_stat["subscriberCount"], channel_stat_2["subscriberCount"]]))

total = 0
for i in catch:
    total += i

total = total / len(catch)

print("The esctimation of subscriber count is:", round(total), "subscribers")
