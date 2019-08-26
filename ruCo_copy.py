import functions as fc
import glob
import sys


configFile="config/config.json"
searchParams="config/search.json"



configData = fc.readConfig(configFile)
searchData = fc.readConfig(searchParams)
mySession_id = sys.argv[1:][0]
#mySession_id = "1721e50e-c26c-11e9-99b2-005056c00001"


###################
try:
    with open("./" + configData["workFolder"] + str(mySession_id)) as f:
        sessionFiles = f.readlines()
except:
    print("no session id ?")
    exit(4)
####checking for folder structure
for root, subdirs, files in fc.os.walk("./" + configData["inputFolder"]):
    for d in subdirs:
        if d == configData["basicFolder"][:-1]:
            dataPath= root + "/"  + configData["basicFolder"]
            myRoot = root

if not fc.os.path.exists("./" + configData["outputFolder"] + "dir_" + str(mySession_id)):
        for root, subdirs, files in fc.os.walk("./" + configData["inputFolder"]):
            for d in subdirs:
                if d == configData["basicFolder"][:-1]:
                    dataPath= root + "/"  + configData["basicFolder"]
                    #print("found basic Folder: " + dataPath)
                    myRoot = root
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id))
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id)
                       + "/" + configData["purchaseFolder"] + configData["subscriptionFolder"])
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["purchaseFolder"] + configData["subscriptionFolder"],mySession_id,0,"")
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["purchaseFolder"],mySession_id,0,"")
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id)
                       + "/" + configData["basicFolder"] + configData["gpsFolder"])
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id)
                       + "/" + configData["basicFolder"] + configData["heartFolder"])
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id)
                       + "/" + configData["basicFolder"] + configData["elevationFolder"])
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id)
                       + "/" + configData["userFolder"])
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["userFolder"],mySession_id,0,"")
        fc.os.makedirs("./" + configData["outputFolder"] + "dir_" + str(mySession_id)
                       + "/" + configData["weightFolder"])
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["weightFolder"],mySession_id,0,"")

for session in range(len(sessionFiles)):
    sportSessionId = sessionFiles[session][:-1] #delete \n
    sportSession = sportSessionId + configData["inputSuffix"]
    isSSession = fc.checkfile(dataPath + sportSession)
    isGSession = fc.checkfile(dataPath + "/" + configData["gpsFolder"] + sportSession)
    isHSession = fc.checkfile(dataPath + "/" + configData["heartFolder"] + sportSession)
    isESession = fc.checkfile(dataPath + "/" + configData["elevationFolder"] +sportSession)

    if isSSession == 1:
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["basicFolder"],mySession_id,1,sportSession)
    if isHSession == 1:
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["basicFolder"]  + configData["heartFolder"],mySession_id,1,sportSession)
    if isESession == 1:
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["basicFolder"]  + configData["elevationFolder"],mySession_id,1,sportSession)
    if isGSession == 1:
        fc.cpData(myRoot,configData["outputFolder"],configData["inputFolder"],configData["basicFolder"]  + configData["gpsFolder"],mySession_id,1,sportSession)
