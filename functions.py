import json
import os
import datetime
import time
import shutil
from geopy.geocoders import Nominatim

__VERSION__="V 1.2.5"

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


def cpData(rootFolder,destFolder,srcFolder,subFolder,sid,test,singleFile):
    if test == 0:
        src_files = os.listdir(rootFolder + "/" + subFolder)
    elif test == 1:
        src_files = []
        src_files.append(singleFile)
    else:
        print("not a vaild test")
        exit(3)

    for file_name in src_files:
        full_file_name = os.path.join(rootFolder + "/" + subFolder, file_name)
        #print(full_file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, "./" + destFolder + "dir_" + str(sid)
                        + "/" + subFolder)

    return

def getGeoLocation(lon,lat):
    geolocator = Nominatim(user_agent="ruCo")
    timerCount = 0
    #seconds
    sleepTime = 10
    while timerCount < 5:
        try:
            location = geolocator.reverse(str(lat) + "," + str(lon))
            suburb,state,country = location.raw.get("address").get("suburb","Unknown"),location.raw.get("address").get("state","Unknown"),location.raw.get("address").get("country","Unknown")
            timerCount = 100
        except:
            print("some  error")
            suburb,state,country = "unknown_","unknown_","unknown_"
            timerCount = timerCount + 1
            time.sleep(timerCount * sleepTime)
    return suburb,state,country
