# Monthly sum of the rain data
dataPath = r"C:\Users\Michele\Desktop\my-repo\data\01_exe_rain_data_1year.txt"

#read data into a lines list
with open(dataPath,"r")as file:
    lines = file.readlines()

#print the first 5 lines
date2ValuesListMap = {}
for line in lines[:5]:
    line = line.strip()#remove spaces 
    # clean lines with # or empty
    if line.startswith("#") or len(line) == 0:
        continue
    
    #parse each line to extract the date(string) and value(num)
    lineSplit = line.split(",")
    date = lineSplit[0]
    value = float(lineSplit[1])
    #print(date, ":", value)

    #extract the year-month from the date. The key mus be unique 
    month = date[:-2]
    #print(month, ":", value)

    #aggregate the values by month (key), i.e. colllect all values
    # for each date in a list
    values = date2ValuesListMap.get(month, [])
    values.append(value)
    date2ValuesListMap[month] = values
    
    #print(date2ValuesListMap)

for month, values in date2ValuesListMap.items():
    print(month, values)#each year-month has its rain amount
    cumRain = sum(values)
    print(f"Cumulated rain for month {month} is {cumRain}")
    #after this I can remove the limit of 5 or 50 data and get all the data. If I get negative data for rain, it is probably an error (negative rain is impossible!) so I would need to filter these out
    