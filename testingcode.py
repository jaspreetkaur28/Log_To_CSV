import csv
import itertools 

with open('logtestscript.log', 'r') as file:
     lines = file.read().splitlines()
     lines2 = [lines[x:x+3] for x in range(0, len(lines), 3)]

Noprocessid = "             "
a = ['DEBUG' and '.mxf' and 'MediaFile/']

with open('Logs.csv', 'w') as file2:

    writer = csv.writer(file2)
    writer.writerow(('Log File Name', 'Date', 'Time', 
                             'ProcessID','FileID','MediaFileId'))
    

    for line in lines:
      
        a_match = [True for match in a if match in line]
        if True in a_match:
            name = file.name
            date = line.split(',')[0].split(' ')[0]  
            time = line.split(',')[0].split(' ')[1] 
            processid = line.split(']')[0].split('[')[1]
            fileid = line.split('Prod/')[-1].split('.mxf')[0]
            mediafileid = line.split('MediaFile/')[-1].split(' ')[0]
            
            if processid != Noprocessid:
                if fileid.startswith("M"):
                     data = name, date, time, processid, fileid, mediafileid
    
                     writer.writerow(data)
                     print (data)
                else:
                    print ("doesnt start with M")


