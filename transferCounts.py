import json

transfers = "./startfinishtransfers.txt"

transID = {}
#transInfo = []

with open (transfers, 'rt') as transfile:
    contents = transfile.readlines()

    for line in contents:
        spline = line.split(' ')
        if spline[0] in transID:
            transID[spline[0]].append(line)
        else:
            #transID[spline[0]] = spline[0]
            transID[spline[0]] = [line]
#print(len(transID))
#print(transID)

with open('GlobusTransfers.json', 'w') as fp:
    json.dump(transID, fp)
