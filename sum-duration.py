#!/usr/bin/env python
'''
Last.fm Playcount Sum from JSON
Copyright 2013 Christopher Su
Takes Last.fm API JSON output and sums playcounts.
'''

import json
import os

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
    json = loadJSON("drew.json") # can use file or API to get json data
    sum = 0
    for track in json["toptracks"]["track"]:
        if track["duration"] != '':
            sum += int(track["duration"])*int(track["playcount"])
    print sum

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    main()