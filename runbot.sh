#!/bin/sh

BOTNAME=woprthings
OWNER=brian

cd /home/$OWNER/bots/$BOTNAME
. /home/$OWNER/.virtualenvs/$BOTNAME/bin/activate
./$BOTNAME.py
deactivate

