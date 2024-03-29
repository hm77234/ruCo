import functions as fc
import glob
import uuid


configFile="config/config.json"
searchParams="config/search.json"


#searchMethods = exact (date); from (date); sportsTypeId (integer) ; all
#date=yyyy-mm-dd

configData = fc.readConfig(configFile)
searchData = fc.readConfig(searchParams)


mySession_id = uuid.uuid1()
#resultSessionPack = []


####checking for folder structure
for root, subdirs, files in fc.os.walk("./" + configData["inputFolder"]):
    for d in subdirs:
         if d == configData["basicFolder"][:-1]:
            dataPath= root + "/"  + configData["basicFolder"]
            #print("found basic Folder: " + dataPath)

sessionFiles = glob.glob(dataPath + '*' + configData["inputSuffix"])
#print(sessionFiles)
searchString =searchData["searchFilter"]
validFileCounter = 0
ignoredFileCounter = 0
output= open("./" + configData["workFolder"] + str(mySession_id),"w+")
if searchData["searchMethod"] == "exact":
    for f in range(len(sessionFiles)):
        sportsData = fc.readConfig(sessionFiles[f])
        sportTime = fc.timeConvert(sportsData["start_time"],sportsData["start_time_timezone_offset"])
        print(sportTime)
        if searchString in sportTime:
            #print ("Your searchitem was found!")
            if searchData["ignoreGPSCheck"] == 0:
                if fc.checkfile(dataPath + "/" + configData["gpsFolder"] + fc.os.path.basename(sessionFiles[f])) == 1:
                    output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                    validFileCounter = validFileCounter + 1
                else:
                    #print("file ignored -- no gps data")
                    ignoredFileCounter = ignoredFileCounter + 1
            else:
                output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                validFileCounter = validFileCounter + 1

elif searchData["searchMethod"] == "from":
    for f in range(len(sessionFiles)):
        sportsData = fc.readConfig(sessionFiles[f])
        searchTS = int(fc.datetime.datetime.strptime(searchString, "%Y-%m-%d").timestamp())*1000
        if sportsData["start_time"] >= searchTS:
            #print ("Your searchitem was found!")
            if searchData["ignoreGPSCheck"] == 0:
                if fc.checkfile(dataPath + "/" + configData["gpsFolder"] + fc.os.path.basename(sessionFiles[f])) == 1:
                    output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                    validFileCounter = validFileCounter + 1
                else:
                    #print("file ignored -- no gps data")
                    ignoredFileCounter = ignoredFileCounter + 1
            else:
                output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                validFileCounter = validFileCounter + 1

elif searchData["searchMethod"] == "between":
    #86400
    for f in range(len(sessionFiles)):
        sportsData = fc.readConfig(sessionFiles[f])
        searchStringList = searchString.split(":")
        searchTS_b = int(fc.datetime.datetime.strptime(searchStringList[0], "%Y-%m-%d").timestamp())*1000
        #86400 on day
        searchTS_e = int(fc.datetime.datetime.strptime(searchStringList[1], "%Y-%m-%d").timestamp())*1000 + 86400 *1000
        if sportsData["start_time"] >= searchTS_b and sportsData["start_time"] <= searchTS_e:
            #print ("Your searchitem was found!")
            if searchData["ignoreGPSCheck"] == 0:
                if fc.checkfile(dataPath + "/" + configData["gpsFolder"] + fc.os.path.basename(sessionFiles[f])) == 1:
                    output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                    validFileCounter = validFileCounter + 1
                else:
                    #print("file ignored -- no gps data")
                    ignoredFileCounter = ignoredFileCounter + 1
            else:
                output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                validFileCounter = validFileCounter + 1

elif searchData["searchMethod"] == "all":
    for f in range(len(sessionFiles)):
        sportsData = fc.readConfig(sessionFiles[f])
        if searchData["ignoreGPSCheck"] == 0:
            if fc.checkfile(dataPath + "/" + configData["gpsFolder"] + fc.os.path.basename(sessionFiles[f])) == 1:
                output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                validFileCounter = validFileCounter + 1
            else:
                #print("file ignored -- no gps data")
                ignoredFileCounter = ignoredFileCounter + 1
        else:
            output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
            validFileCounter = validFileCounter + 1

elif searchData["searchMethod"] == "sid":
    for f in range(len(sessionFiles)):
        sportsData = fc.readConfig(sessionFiles[f])
        if sportsData["sport_type_id"] == searchString:
            #print ("Your searchitem was found!")
            if searchData["ignoreGPSCheck"] == 0:
                if fc.checkfile(dataPath + "/" + configData["gpsFolder"] + fc.os.path.basename(sessionFiles[f])) == 1:
                    output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                    validFileCounter = validFileCounter + 1
                else:
                    #print("file ignored -- no gps data")
                    ignoredFileCounter = ignoredFileCounter + 1
            else:
                output.write(fc.os.path.basename(fc.os.path.splitext(sessionFiles[f])[0]) + "\n")
                validFileCounter = validFileCounter + 1


else:
    print("not a valid search method")
    exit(3)
output.close()
print("Version: " + fc.__VERSION__)
print("found " + str(validFileCounter) + " file(s) with gps data!!! and your filter criteria")
print("ignored " + str(ignoredFileCounter) + " file(s) -- no gps data")
print("for copying your selected dat run:")
print("python3 ruCo_copy.py " + str(mySession_id))
print("for converting your data to gpx run:")
print("python3 ruCo_convert.py " + str(mySession_id))
