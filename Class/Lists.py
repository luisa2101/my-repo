# Lists
mylist = ["merano", "Bolzano", "Trento"]
print(mylist)

#access elements in certain positions
print("The elemnets start at position 0:", mylist[0])

#add objects 
mylist.append("Potsdam")
print(mylist)

#remove, the string must be exactly the same
mylist.remove("Potsdam")
print(mylist)

#remove items by position in list
mylist.pop(0) #remove first item
print(mylist)

#show the popped item

#item contained , NB this is case sensitive, so bolzano is different form Bolzano
mylist = ["merano", "Bolzano", "Trento"]
doIHaveBolzano = "Bolzano" in mylist
print(doIHaveBolzano)

doIHavePotsdam = "Potsdam" in mylist
print(doIHavePotsdam)

# looping, prints each item
for item in mylist:
    print(item)

#put together items in the same position
colours = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
#range function,range 10 goes from 0 to 9!
for index in range(len(colours)):#from 0 to length of list color
    colour = colours[index]
    ratio = ratios[index]
    
    print(f"{colour}->{ratio}")

#have an exact copy of a list
colours2 = colours.copy()
colours.sort()
print(colours)
print(colours2)

#break a loop when I is a certain value. "break" breaks the loop. E.g. if you loop through data and look for a particular item, you break when you find it
for i in range(10):
    if i == 5:
        break
    print(f"A){i}")
print("-------")

#Continue
for i in range(10):
    if i == 5: #whenever the condition is met, this is skipped and the function continues
        continue
    print(f"B){i}")
print("-------")

# Loop over a sequence of numbers by increasing the value by 2
for i in range(0, 10, 2):
    print(f"C){i}")
print("-------")

#The inverse, from 10 to 0
for i in range(10, 0, -2):
    print(f"D){i}")
#The range object does not allow to use floats

print("-------")
# Sorting lists
mylist = ["Merano", "Bolzano", "Trento"]
print(f"My original list:{mylist}")
mylist.sort()
print(f"My sorted list:{mylist}")
mylist.sort(reverse = True)
print(f"My rev-sorted list:{mylist}")

mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(f"A mixed case list, sorted: {mylist}") #sorted according to ASCII, so before the upper and then the lower cases

mylist.sort(key = str.lower) # use as function the lower case of the string object
print(f"A mixed case list, properly sorted: {mylist}")

#Numerical sorting
numlist = ["002", "01", "3", "004"]
numlist.sort()
print(numlist)

numlist = ["002", "01", "3", "004"]
# Define a function, "string" is the name of the varibale. We convert the string into integer. Then we can use the function as a key.
def toInt(string):
    return int(string)
    
numlist.sort(key = toInt)
print(numlist)

abc = ["a", "b", "c"]
cde = ["c", "d", "e"]

newabcde = abc + cde
print(newabcde)

#remove brackets, indicating the separator I want to use. Do not use comma!
print(";".join(newabcde))

numlist = [1.0, 2.0, 3.5, 6, 11, 34, 12]
print(max(numlist))
print(min(numlist))
print(sum(numlist))

avg = sum(numlist)/len(numlist)
print(avg)

#caluclate average using for loop
somma = 0
count = 0
for item in numlist:
    somma += item #This is like writing: somma = somma + item
    count += 1 #This is like writing: count = count + 1
average = somma/count
print(average)

#calculate the variance
for item in numlist:
    squaredDiff = 0
for item in numlist:
    squaredDiff += (item - average) ** 2
variance = squaredDiff / len(numlist)
print(variance)

    
    