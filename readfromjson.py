import json
import re
def convertToMB(size):
    ele = size.split(" ") 
    number = float(ele[0])
    unit = ele[1]
    temp = 0
    if unit == 'bytes':  
        temp = number/(1024*1024)
    
    elif unit == 'KB':
        temp = number/1024           
    
    elif unit == 'MB':   
        temp = number                                                                                            
    
    elif unit == 'GB': 
        temp = number*1024

    elif unit == 'TB':
        temp = number*1024*1024
    
    return temp


with open('temp1.json','r') as f:
    tablesandsizes= {}
    read_data = json.load(f,strict=False)
    servers = read_data.keys()
    for server in servers:
        stdout = read_data[server]["stdout"]
        pattern = re.compile("Table: (.*)") #match everything after "Table: " except new line
        tables = pattern.findall(stdout) 
        for table in tables:
            if table not in tablesandsizes.keys():
                tablesandsizes[table]=0
        pattern1 = re.compile("Space used \(total\): (.*)") #match everything after "Space used (total): " except new line
        size = pattern1.findall(stdout)
        localtablesandsizes={}
        for i in range(0,len(tables)):
            localtablesandsizes[tables[i]]= convertToMB(size[i])
        for i in localtablesandsizes.keys():
            tablesandsizes[i] = tablesandsizes[i] + localtablesandsizes[i]
    for k,v in tablesandsizes.items():
        print("{0}  {1}".format(k,v))
