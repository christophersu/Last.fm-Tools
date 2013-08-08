#!/usr/bin/env python
'''
Scrobble Single Track
Copyright 2013 Christopher Su
Scrobbles a single track to Last.fm.
'''

import pylast
import time
import Private

def main():
    password_hash = pylast.md5(Private.LASTFM_PASSWORD)
    network = pylast.LastFMNetwork(api_key = Private.LASTFM_API_KEY, api_secret = Private.LASTFM_API_SECRET, username = Private.LASTFM_USERNAME, password_hash = password_hash)
    now = int(time.time())
    network.scrobble("Death Cab for Cutie", "I Will Follow You Into the Dark", now)

if __name__ == "__main__":
    main()