import json
import os
import requests

slackurl = "SLACK_WEBHOOK_URL"
room = "DUBTRACK_ROOM"

channel = "#off-topic"
botusername = "tunesbot"
icon_emoji = ":headphones:"

# You shouldn't need to modify anything below this line, but I can't stop you.
lockfile = "/tmp/tunesbot-{0}.lock".format(room)

r = requests.get("http://api.dubtrack.fm/room/{0}".format(room))
data = r.json()

song = data['data']['currentSong']

if song is not None:
    if not os.path.isfile(lockfile):

        message = "{0} is live on dubtrack.fm! https://www.dubtrack.fm/join/{0}".format(room)
        data = { "channel": channel, "username": botusername,
                 "icon_emoji": icon_emoji, "text": message }

        requests.post(slackurl, json.dumps(data))
        open(lockfile, "a").close()
else:
    try:
        os.remove(lockfile)
    except:
        pass
