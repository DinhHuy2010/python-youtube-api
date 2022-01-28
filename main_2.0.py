import requests

api_key = "AIzaSyDKNpULheImRxpFuhLV-QgwIiHBUhSOl4s"
base_url = "https://www.googleapis.com/youtube/v3/channels"
channel_ids = ["UCmSp4bDxS9R0jpeZEvkut2g", "UCFAiFyGs6oDiF1Nf-rRJpZA"]
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

for channel in total:
    print(channel + ":", total[channel])