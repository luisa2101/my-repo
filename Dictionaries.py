#Map = dictionary
# A key needs to be unique
townsProvincesMap = {
    "merano": "BZ",
    "bolzano": "BZ",
    "trento":"TN"
}
print(townsProvincesMap)
print(townsProvincesMap["merano"]) #NB Keys are case sensitive, so Merano is different from merano

# add element
townsProvincesMap ["potsdam"] = "BR"
print(townsProvincesMap)

# remove element
townsProvincesMap.pop("potsdam")
print(townsProvincesMap)

# chceck if key is available
if townsProvincesMap.get("Merano") is None:
    print("key doesn't exist")
else:
    print("key exists")
    
# we set a efault value in case our key is not present
print(townsProvincesMap.get("Merano", "unknown"))

# for town, province in townsProvincesMap
for key, value in townsProvincesMap.items():
    print(key, "is in the province of", value)

print(townsProvincesMap.keys())
print(townsProvincesMap.values())

#sort dictionaries by keys
#1 transform in list
keys = list(townsProvincesMap.keys())
keys.sort()
print(keys)

# loop over a dictionary, to sort by key
for key in keys:
    print(key, "is in the province of",townsProvincesMap[key])
