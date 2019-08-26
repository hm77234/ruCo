# ruCo
### runtastic json 2 gpx converter with some searchfilter

## Motivation: 
i am not a coder, i am a frustrated runtastic user. I do not like 
the mass export and i have to convert every week all files from rt.
There are a lot of good converting tools ther for converting rt data,
but non of these have filter for selecting or/and searing the dataset. 
so i wrote a filter for searching, selecting, converting and
copying for rt sport sessions export.



### current version: 1.2

converts sport-sessions with gps and heart data to gpx.

depends on python3, glob, uuid, json, os, datetime, time, sys, shutil, geopy

### Usage:

#### export runtastic data
export your data from runtastic.com, usally a export-date.zip file.
extract it in the input folder.
#### check config.json
check the config.json file for your used  sport types and add (if necessary) your types.
You will find a list of some sport types in this file. If you ar not sure about your sport
type id, check the json files in Sport-session folder, the id is the last element in this
files.
Config example:
   
       {
         "inputFolder":"input/",                #ruCo dir
         "outputFolder":"output/",              #ruCo dir
         "workFolder":"workDir/",               #ruCo dir
         "basicFolder":"Sport-sessions/",       #runtastic export structure begin
         "gpsFolder":"GPS-data/",
         "heartFolder":"Heart-rate-data/",
         "elevationFolder":"Elevation-data/",
         "userFolder":"User/",
         "weightFolder":"Weight/",
         "purchaseFolder":"Purchases/",
         "subscriptionFolder":"Subscriptions/", #runtastic export structure end
         "sportTypes":{
           "1":"Running",
           "2":"Nordic Walking",
           "3":"Bikeing",
           "4":"Mountain Bikeing",
           "7":"Hikeing","8":"cross_country_skiing",
           "22":"race_cycling",
           "34":"Weight Training"},
         "gpsDateFormat":"%Y-%m-%d %H:%M:%S %z",
         "outputFormat":"gpx",
         "inputSuffix":".json",
         "getGeoInfo":1}                        #activate gps geo info 1..activate, 0..deactivate
 
#### edit search.json
now edit the search.json file for your needs.

Filter:

    all:

    {
      "searchFilter":"2017-04-01",
      "searchMethod":"all",
      "ignoreGPSCheck":1
    }

    search filter is ignored, will find all session with gps data

    exact:

    {
      "searchFilter":"2017-04-01",
      "searchMethod":"exact",
      "ignoreGPSCheck":1
     }
    will find all files on searchfilter date (format: yyyy-mm-dd)

    from:

    {
      "searchFilter":"2017-04-01",
      "searchMethod":"from",
      "ignoreGPSCheck":1
     }
    will find all files from searchfilter date to now (format: yyyy-mm-dd)

    sid: 

    {
      "searchFilter":"2",
      "searchMethod":"sid",
      "ignoreGPSCheck":1
     }
    will find all files on sid (Sports Type Id)
    
    between:
    {
      "searchFilter":"2016-08-24:2016-09-04",
      "searchMethod":"between",
      "ignoreGPSCheck":1
    }
    wille find betwenn the dates beginn at 00:00 end at 23:59:59
    split char is ':'

!!!!!!  
"ignoreGPSCheck":1 means, that all sport sessions will be collected, 0 means, that
only sport sessions with existing gps data will be collected.

#### run ruCo_startSearch.py
or python3 ruCo_startSearch.py.py for collecting your filterted 
sessionfiles. The collection is stored in the workDir directory.

#### run ruCo_convert.py <session-id>
for converting your sessions (shown on the output fo findSportSession.py) :
python3 ruCo_convert.py.py session-id or ./ruCo_convert.py.py session-id

!!! sport sessions without gps data will be ignored by ruCo_convert !!!

!!! the session-id is not the rt file id !!!

#### run ruCo_copy.py <session-id>
if you want to copy your filtered data in the same structure as the
rt export.
copys User, Weight and Purchases as it is an copys only the selected
sport sessions with heart, elevation and gps, if exists. 
Also sessions without gps data !! 


#### check gpx files in output Folder
you will find your gpx files in the output container.

Your used files are in the workdir as file with the session-id as name.

## Sporttypes:

      run: '1',
      nordic_walking: '2',
      ride: '3',
      mountain_biking: '4',
      other: '5',
      skating: '6',
      hiking: '7',
      cross_country_skiing: '8',
      skiing: '9',
      snow_boarding: '10',
      motorbiking: '11',
      driving: '12',
      snowshoeing: '13',
      indoor_run: '14',
      indoor_ride: '15',
      elliptical: '16',
      rowing: '17',
      swimming: '18',
      walk: '19',
      riding: '20',
      golfing: '21',
      race_cycling: '22',
      tennis: '23',
      badminton: '24',
      sailing: '29',
      windsurfing: '30',
      pilates: '31',
      climbing: '32',
      frisbee: '33',
      weight_training: '34',
      volleyball: '35',
      handbike: '36',
      cross_skating: '37',
      soccer: '38',
      smovey_walking: '39',
      nordic_cross_skating: '41',
      surfing: '42',
      kite_surfing: '43',
      kayaking: '44',
      basketball: '45',
      paragliding: '47',
      wake_boarding: '48',
      freecrossen: '49',
      diving: '50',
      back_country_skiing: '53',
      ice_skating: '54',
      sledding: '55',
      snowman_building: '56',
      snowball_fight: '57',
      curling: '58',
      ice_stock: '59',
      biathlon: '60',
      kite_skiing: '61',
      speed_skiing: '62',
      baseball: '68',
      crossfit: '69',
      ice_hockey: '71',
      skateboarding: '72',
      rugby: '75',
      standup_paddling: '76'

### History

version 1.2
add geolocation to gpx desc metadata

version 1.1
copy selected sportsession to a new runtastic directory structure,
only containing the search results
ignore GPS Check during search (! not working in ruCo_convert)
renaming scripts


version 1.0
import of gpx files tested with gpxsee (https://gpxsee.org)
and bergfex (https://bergfex.at)

version 0.3
add between filter

version 0.2
add sport_type_id filter (sid) and test data

version 0.1
initial commit