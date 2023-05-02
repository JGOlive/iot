# Create a new Directory
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Can build up a dict by starting with the empty disct ()
# and storing key/value pairs into the dict like this:
# dict[key] = value-for-that-key
dict = {}
dict["a"] = "alpha"
dict["g"] = "gamma"
dict["o"] = "omega"

print(dict) #{"a": "alpha", "o":"omega", "g":"gamma"}

print(dict["a"])

dict["a"] = 6
"a" in dict
# print dict["z"]           # Throws error
if "z" in dict: print(dict["z"])
print(dict.get("z"))
# 
# 
for key in dict:print(key)
# 

#
for key in dict.keys(): print(key)

# 
print (dict.keys())

#
print(dict.values())

#
#
for key in sorted(dict.keys()):
    print(key, dict[key])

#
print(dict.items())

#
#
#
for k,v in dict.items(): print(k, ">", v)
#