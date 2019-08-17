import json
import os
import datetime
import time

VERSION="V 0.2.5"

def readConfig(jsonFile):
    #Read JSON data into the datastore variable
    if jsonFile:
        with open(jsonFile, 'r') as f:
            dataStore = json.load(f)

    #Use the new datastore datastructure
    return dataStore;

def checkfile(iPath):
    if os.path.isfile(iPath):
        return 1
    else:
        return 0

def timeConvert(ts,os):
    workDate = datetime.datetime.utcfromtimestamp(int(ts)/1000 + int(os/1000))
    utc_offset = datetime.timedelta(seconds=+int(os/1000))
    workDate = workDate.replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()
    return workDate