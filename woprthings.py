#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import random
from twython import Twython

myhandle = 'woprthings'

def auth():
    with open("etc/access.json", 'r') as access:
        db = json.load(access)
    return Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])

def get_phrase():
    with open('share/dialogue.json', 'r') as dialogue_json:
        dialogue_list = json.load(dialogue_json)
        dialogue = dialogue_list['dialogphrases']
        phrase = dialogue[random.randint(0, len(dialogue) - 1)]
        return phrase

def main():
    print('[i] @{myhandle} ACTIVATE!'.format(myhandle=myhandle))
    twutt_text = get_phrase()
    print('[!] Gonna twutt: {twutt_text}'.format(twutt_text=twutt_text))
    twitter = auth()
    twitter.update_status(status=twutt_text)

if __name__ == "__main__":
    main()
