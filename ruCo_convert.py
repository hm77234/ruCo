import sys
import functions as fc

configFile="config/config.json"
dataPath=""
xmlHeader = """<?xml version="1.0" encoding="UTF-8"?>
<gpx creator="haumiRuntaticConverter" version="0.2"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"
    xmlns="http://www.topografix.com/GPX/1/1"
    xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1"
    xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3">
  <metadata>
  """
xmlFooter = """   </trkseg>
  </trk>
</gpx>
"""





def main(sid):
        configData = fc.readConfig(configFile)
        ##################
        try:
            with open("./" + configData["workFolder"] + str(sid)) as f:
                sessionFiles = f.readlines()
        except:
            print("no session id ?")
            exit(4)
        ##################
        for session in range(len(sessionFiles)):
                sportSessionId = sessionFiles[session][:-1] #delete \n
                sportSession = sportSessionId + configData["inputSuffix"]
                outputFile = sportSessionId + "." + configData["outputFormat"]
                ####checking for folder structure
                for root, subdirs, files in fc.os.walk("./" + configData["inputFolder"]):
                    for d in subdirs:
                        if d == configData["basicFolder"][:-1]:
                            dataPath= root + "/"  + configData["basicFolder"]
                            #print("found basic Folder: " + dataPath)
                if dataPath == "":
                    print("no basicFolder found")
                    exit(1)
                isSSession = fc.checkfile(dataPath + sportSession)
                isGSession = fc.checkfile(dataPath + "/" + configData["gpsFolder"] + sportSession)
                isHSession = fc.checkfile(dataPath + "/" + configData["heartFolder"] + sportSession)
                isESession = fc.checkfile(dataPath + "/" + configData["elevationFolder"] +sportSession)

                if isSSession == 0 :
                    print("no sports data found")
                    exit(2)
                if isGSession == 0:
                    print("no gps data found + jump to next value")
                    continue

                if isHSession == 1:
                    heartData = fc.readConfig(dataPath + "/" + configData["heartFolder"] + sportSession)
                sportsData = fc.readConfig(dataPath + sportSession)
                gpsData = fc.readConfig(dataPath + "/" + configData["gpsFolder"] + sportSession)
                try:
                    sportsType = configData["sportTypes"][str(sportsData["sport_type_id"])]
                except:
                    sportsType = "Unknown"
                #<time>2017-04-01T09:43:16+02:00</time>
                sessionDate = fc.timeConvert(sportsData["start_time"],sportsData["start_time_timezone_offset"])
                output= open("./" + configData["outputFolder"] + sportsType + "_"+ sessionDate + "_" +outputFile,"w+")
                #print(sessionDate)
                output.write(xmlHeader)
                output.write("   <time>" + sessionDate +"</time>\n")
                output.write("   <name>" + sportsType + "</name>\n")
                if configData["getGeoInfo"] == 1:
                    print(sportsData["longitude"])
                    suburb,state,country = fc.getGeoLocation(sportsData["longitude"],sportsData["latitude"])
                    output.write("   <desc>" + suburb + ", " + state + ", " + country + "</desc>\n")

                else:
                    output.write("   <desc>" + sportsType + "</desc>\n")
                output.write("  </metadata>\n")
                output.write("  <trk>\n")
                output.write("   <name>" + sportsType + "</name>\n")
                output.write("   <type>1</type>\n")
                output.write("   <trkseg>\n")


                for i in range(len(gpsData)):
                    output.write("    <trkpt lat=\"" + str(gpsData[i]["latitude"]) + "\" lon=\"" + str(gpsData[i]["longitude"]) + "\">\n")
                    output.write("      <ele>" + str(int(gpsData[i]["altitude"])) + "</ele>\n")
                    gpsTime = fc.datetime.datetime.strptime(gpsData[i]["timestamp"], configData["gpsDateFormat"]).isoformat()
                    output.write("      <time>" + gpsTime + "</time>\n")
                    if isHSession == 1:
                        for h in range(len(heartData)):
                            if gpsData[i]["timestamp"] == heartData[h]["timestamp"]:
                                output.write("      <extensions>\n")
                                output.write("       <gpxtpx:TrackPointExtension>\n")
                                output.write("        <gpxtpx:hr>" + str(heartData[h]["heart_rate"]) + "</gpxtpx:hr>\n")
                                output.write("       </gpxtpx:TrackPointExtension>\n")
                                output.write("      </extensions>\n")
                    output.write("    </trkpt>\n")
                output.write(xmlFooter)

                output.close()





if __name__ == '__main__':
    mySession_id = sys.argv[1:]
    main(mySession_id[0])



