#!/usr/bin/env python
'''
Scrobble from JSON
Copyright 2013 Christopher Su
Scrobbles tracks from JSON data.
'''

import json
import os
import time
import pylast
import Private

def loadJSON(json_file):
    try:
        jsonFile = open(os.path.join(dir, json_file), "r")
    except IOError:
        logging.exception("Error opening %s." % json_file)
        sys.exit(1)
    jsonStr = jsonFile.read()
    jsonFile.close()
    try:
        data = json.loads(jsonStr)
    except ValueError:
        logging.exception("Error parsing %s." % json_file)
        sys.exit(1)
    return data

def main():
    json = loadJSON("top1000.json") # can use file or API to get json data

    password_hash = pylast.md5(Private.LASTFM_PASSWORD)
    network = pylast.LastFMNetwork(api_key = Private.LASTFM_API_KEY, api_secret = Private.LASTFM_API_SECRET, username = Private.LASTFM_USERNAME, password_hash = password_hash)

    now = int(time.time())
    count = 0
    for track in json["toptracks"]["track"]:
        network.scrobble(track["artist"]["name"], track["name"], now, mbid = track["mbid"])
        count += 1
        if count == 5:
            break

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    main()