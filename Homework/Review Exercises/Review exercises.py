folder = r"C:\Users\Michele\Desktop\my-repo\data"

#Exercise 1
age = 25
name = "Mario Rossi"
activity = "skating"
job = "engineer"
print(f"Hei, I am {name}\n I am {age} and I love to go {activity}\n I work as an {job}")
print("---------------")

#Exercise 2
csvPath = f"{folder}/01_exe2_data.csv"

with open(csvPath, "r") as file:
    lines = file.readlines()
for line in lines:
    print(line)
    
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
    print(x1)
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    
    maxanalogString = lineSplit[2]
    x2 = float(maxanalogString.split(":")[1])
    
    # x2/x1 = y2/y1
    y1 = y2*x1/x2
    
    print(x1,x2,y1,y2)
print("---------------")

#Exercise 3
string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
modified_string = string.replace(',', ';')
print(modified_string)
print("---------------")

#Exercise 4
list = [ 1, 2, 3, 4, 5]
for number in list:
    print(number)
print("---------------")

#Exercise 5
for number in list:
    print(f"Number {number}")
print("---------------")

#Exercise 6
list = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
print(list[:5])
shortList = list[:5]
for item in shortList:
    print(f"Number {item}")
print("---------------")

#Exercise 7
list1 = [1, 2, 3, 4, 5]
list2 = ["first","second","third","fourth","fifth"]
for item in range(len(list1)):
    print(f"{list2[item]} is {list1[item]}")
print("---------------")

#Exercise 8
string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

#Count characters
charactersCount= len(string)
print(charactersCount)

#Count words
wordCount = len(string.split())
print(wordCount)

#Count characters without spaces
wordWithoutSpace = len(string.replace(" ","").replace("\n",""))
print(wordWithoutSpace)
print("---------------")

# Exercise 9
ReadExe9 = f"{folder}/01_exe9_data.csv"

with open(ReadExe9,"r")as file:
  lines = file.readlines()
  for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    print(line)
print("---------------")

# Exercise 10
ReadExe9 = f"{folder}/01_exe9_data.csv"

with open(ReadExe9,"r")as file:
  lines = file.readlines()
  for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    columns = line.split(",")
    column1 = columns[0]
    column2 = columns[1]
    column2 = float(columns[1])
    if column2 <= 1000:
        print(f"{column1}, {column2}")
    
# Exercise 11
ReadExe11 = f"{folder}/01_exe11_data.csv"

with open(ReadExe11,"r")as file:
  lines = file.readlines()
  for line in lines:
      line = line.strip()
      lineSplit = line.split(";")
      # print(lineSplit)
      base = lineSplit[0].split("=")[1].replace("cm", "")
      base1 = float(base)
      height = lineSplit[1].split("=")[1]
      height1 = float(height)
      # print(base)
      # print(height)
      area = (base1 * height1*100) / 2
      print(f"base * height / 2 = {base1} * {height1*100} = {area}cm2")
print("---------------")

# Exercise 12
who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
}
what = {
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
}
where = {
    44: "to town.",
    11: "in her bed.",
    201: "in the livingroom.",
    23: "up the mountain."
}
for key, value in who.items():
    activity = what[value]
    place = where[value]
    print(f"{key} {activity} {place}")
    
for key, value in who.items():
    activity = what.get(value)
    place = where.get(value)
    print(f"{key} {activity} {place}")
print("---------------")

# Exercise 12
who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
}
what = {
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
}
where = {
    "runs" : "to town.",
    "dreams" : "in her bed.",
    "plays" : "in the livingroom.",
    "walks": "up the mountain."
}
for key, value in who.items():
    activity = what[value]
    place = where[activity]
    print(f"{key} {activity} {place}")

for key, value in who.items():
    activity = what.get(value)
    place = where.get(activity)
    print(f"{key} {activity} {place}")
print("---------------")

# Exercise 13
list1 = ["a","b","c","d","e","f"]
list2 = ["c","d","e","f","g","h","a"]
list3 = ["c","d","e","f","g"]
list4 = ["c","d","e","h","a"]

lists = list1 + list2 + list3 + list4
letterCount = {}

for letter in lists:
    if letter in letterCount:
        letterCount[letter] += 1
    else:
        letterCount[letter] = 1
for letter, count in letterCount.items():
    print(f"count of {letter} = {count}")
print("---------------")

# Exercise 14
stationsPath = f"{folder}/stations.txt"

with open(stationsPath,"r")as file:
 lines = file.readlines()

for line in lines[:20]:
    print(line)
print("---------------")

# Exercise 15
stationsPath = f"{folder}/stations.txt"

with open(stationsPath,"r")as file:
 lines = file.readlines()
    
count = 0
for line in lines:
    if line.startswith("#") or len(line) == 0:
     continue
    count += 1
print(count)
print("---------------")

# Exercise 16
stationsPath = f"{folder}/stations.txt"

with open(stationsPath,"r")as file:
 lines = file.readlines()
 columns = line.split(",") #lineSplit = line.split(",")
 columnsNumber = len(columns)
 print(columnsNumber)
print("---------------")

# Exercise 17
stationsPath = f"{folder}/stations.txt"

with open(stationsPath,"r")as file:
 lines = file.readlines()
for line in lines[:20]:
    columns = line.split(",") #lineSplit = line.split(",")
    print(columns[0], columns[1])
print("---------------")

# Exercise 18
stationsPath = f"{folder}/stations.txt"

with open(stationsPath,"r")as file:
 lines = file.readlines()
 
somma = 0
count = 0

for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    columns = line.split(",")
    height = float(columns[5])
    somma += height
    count += 1

if count > 0:
    avg = somma / count
    print(f"The averae of the height of the stations is {int(avg)}")
print("---------------")

# Exercise 19
print(f"File info: stations.txt\n----------------")
print(f"Stations count: {count}")
print(f"Average value: {int(avg)}")
with open(stationsPath, "r") as file:
    line = file.readline()
    lineStrip = line.strip()
    columnNames = line.split(",")
    # print(columnNames)
    
print(f"Available fields:")
for item in columnNames:
    print(f"-> {item.strip()}")

print(f"First data lines:")
for line in lines[:6]:
    print(line)

# Exercise 20


# Exercise 21
n = 10
m = 5

for item in range(n):
    code = "*" * m
    print(code)
print("---------------")

# Exercise 22
n = 10
count = 0
for item in range(n):
    count += 1
    code2 = count * "*"
    print(code2)
print("---------------")

# Exercise 23
n = 10
count = 10
for item in range(n):
    count -= 1
    code3 = count * "*"
    print(code3)
print("---------------")

# Exercise 24
a = 10
somma = 0
for number in range(0,a):
    if number%2 == 0:
        print (number)
        somma += number
print(f"The sum of even numbers from 0 to a is {somma}")
print("---------------")

# Alternative exercise 24
a = 10
somma = 0
for number in range(0,a,2):
        print (number)
        somma += number
print(f"The sum of even numbers from 0 to a is {somma}")

print("---------------")

# Exercise 25
numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
sumEven = 0
for number in numbers:
    if number%2 == 0:
        sumEven += number
print(f"The sum of even numbers is {sumEven}")
print("---------------")

# Exercise 26
print(f"Exercise 26\n")
ReadExe261 = f"{folder}/01_exe26_dataset1.csv"
ReadExe262 = f"{folder}/01_exe26_dataset2.csv"

dict261 = {}
with open(ReadExe261, "r") as file:
    for line in file:
        line = line.strip()
        id, x, y = line.split(",")
        dict261[id] = {"x": x, "y": y}

dict262 = {}
with open(ReadExe262, "r") as file:
    for line in file:
        line = line.strip()
        id, value = line.split(",")
        dict262[id] = value

for key, value in dict261.items():
    if key in dict262:
        row = dict261[key]
        row["value"] = dict262[key]
        print(f"ID: {key}, X: {row['x']}, Y: {row['y']}, Value: {row.get('value')}")
