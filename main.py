from youtube_statistics import YTstats

API_KEY = "AIzaSyBwYqcsx6JLho35YqiKIrfDoXiMpOFrPXA"
channel_id = "UCbXgNpp0jedKWcQiULLbDTA"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
# yt.get_channel_video_data()