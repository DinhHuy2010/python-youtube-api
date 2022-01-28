import requests

view = 0
subs = 0
videos = 0
api_key = "AIzaSyDKNpULheImRxpFuhLV-QgwIiHBUhSOl4s"
base_url = "https://www.googleapis.com/youtube/v3/channels"
channel_ids = []
f_name = "example.txt" # Change this name if you rename the file. The file store channel channel ids on the YouTube.
with open(f_name, "r") as f:
    for i in f.readlines():
        clean = i.rstrip("\n")
        channel_ids.append(clean) # Get channel id

total = {}
for channel_id in channel_ids:
    url = f"{base_url}?key={api_key}&part=snippet,statistics&id={channel_id}"
    request_url = requests.get(url)
    if request_url.status_code == 200:
        json_data = request_url.json()
    else:
        print("Error occurred.")
        raise SystemExit
    channel_data = json_data["items"][0]
    channel_properties = channel_data["snippet"]
    channel_stat = channel_data["statistics"]
    del channel_stat["hiddenSubscriberCount"]
    channel_title = channel_properties["title"]
    total_of_views = channel_stat["viewCount"]
    total_of_subscribers = channel_stat["subscriberCount"]
    total_of_videos = channel_stat["videoCount"]
    total[channel_title] = {
        "total_of_views": total_of_views,
        "total_of_subscribers": total_of_subscribers,
        "total_of_videos": total_of_videos
        }

print("Channel name:")
for channel in total:
    print(channel)
    datas = total[channel]
    view += int(datas["total_of_views"])
    subs += int(datas["total_of_subscribers"])
    videos += int(datas["total_of_videos"])

print(f"Total of {len(total)} channels views: {view}")
print(f"Total of {len(total)} channels subscribers: {subs}")
print(f"Total of {len(total)} channels videos: {videos}")
print("#" * 40)
print(f"Total of {len(total)} channels average views: {round(view / len(total))}")
print(f"Total of {len(total)} channels average subscribers: {round(subs / len(total))}")
print(f"Total of {len(total)} channels average videos: {round(videos / len(total))}")