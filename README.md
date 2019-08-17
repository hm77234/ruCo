# ruCo
### runtastic json 2 gpx converter with some searchfilter

## Motivation: 
i am not a coder, i am a frustrated runtastic user. I do not like 
the mass export and i have to convert every week all files from rt.
There are a lot of good codes out ther for converting rt data, but
non of these have filter for selecting or/and searing the dataset. 
so i wrote a filter for searching and selecting rt sport sessions.



### version: 0.2

converts sport-sessions with gps and heart data to gpx.

depends on python3, glob, uuid, json, os, datetime, time, sys

### Usage:

#### export runtastic data
export your data from runtastic.com. Usally a export-date.zip file.
extract it in the input folder.
#### check config.json
check the config.json file for your used  sport types and add (if necessary) your types.
You will find a list of some sport types in this file. If you ar not sure about your sport
type id, check the json files in Sport-session folder, the id is the last element in this
files.
#### edit search.json
now edit the search.json file for your needs.

Filter:

    all:

    {
      "searchFilter":"2017-04-01",
      "searchMethod":"all"
    }

    search filter is ignored, will find all session with gps data

    exact:

    {
      "searchFilter":"2017-04-01",
      "searchMethod":"exact"
     }
    will find all files on searchfilter date (format: yyyy-mm-dd)

    from:

    {
      "searchFilter":"2017-04-01",
      "searchMethod":"from"
     }
    will find all files from searchfilter date to now (format: yyyy-mm-dd)

    sid: 

    {
      "searchFilter":"2",
      "searchMethod":"sid"
     }
    will find all files on sid

#### run findSportSession.py
now run ./findSportSession.py or python3 findSportSession.py
you will find your sessionfile with all valid sport-sessions in the workDir directory

#### run main.py <session-id>
then run for converting your sessions (shown on the output fo findSportSession.py) :
python3 main.py session-id or ./main.py session-id

!! the session-id is not the rt file id !!!

#### check gpx files in output Folder
you will find your gpx files in the output container.

Your used files are in the workdir as file with the session-id as name.

Sporttypes:

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

version 0.2
add sport_type_id filter (sid) and test data

version 0.1
initial commit