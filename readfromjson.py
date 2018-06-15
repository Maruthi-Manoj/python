import json
import re

with open('temp1.json','r') as f:
    total = []
    tables=[]
    read_data = json.load(f,strict=False)
    servers = read_data.keys()
    for server in servers:
        stdout = read_data[server]["stdout"]
        if len(tables) == 0:
            pattern = re.compile("Table: (.*)") #match everything after "Table: " except new line
            tables = pattern.findall(stdout) 
            print(len(tables))
        pattern1 = re.compile("Space used \(total\): (.*)") #match everything after "Space used (total): " except new line
        size = pattern1.findall(stdout)
        if len(total) == 0:
            for i in range(0, len(size)):
                total.insert(i,0)
            print(len(total))
        for i in range(0, len(size)):
            ele = size[i].split(" ")
            number = float(ele[0])
            if ele[1] == 'bytes':
               temp = number/(1024*1024)
            elif ele[1] == 'MB':
                temp = number
            elif ele[1] == 'GB':
                temp = number*1024
            total[i] = total[i]+temp

    for i in range(0,len(total)):
        print("{0}   {1}MB".format(tables[i].encode("utf-8"), total[i]))

             



            
