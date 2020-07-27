#reading Globus log files to extract which datasets were requested

import os

outputFile=open("transferErrors.txt", "a+")
#dataTransfers = []                                            # Declare an empty list named mylines.

#proceed through log files in gunzipLogs
glDir = "."
for logs in os.listdir(glDir):
    if logs.startswith("gridftp"):
        print(logs)
        logfile = open(logs, "rt")
        #with open (logs, 'rt') as myfile:     # Open log file for reading text data.
        contents = logfile.readlines()
        #print(contents)
        for line in contents:
            if 'CLIENT ERROR' in line:
                outputFile.write(line)
            '''
            if 'Starting to transfer' in line:                 # For each line, stored as myline,
                outputFile.write(line)
            if 'Finished transferring' in line:
                #dataTransfers.append(myline.rstrip('\n'))       # add its contents to mylines.
                outputFile.write(line)
            '''
        logfile.close()
#print(len(dataTransfers))
outputFile.close()
