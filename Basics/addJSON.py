"""
This is the sample program to work with JSON in python
"""
# Initializing dictionary
addbook = {}

# Adding Ritesh address in dictionary into JSON format
addbook["Ritesh"] = {"name":"Ritesh",
                  "address":"Bergwerkstrasse 76, Sargans, Switzerland",
                  "phone" : "9876543782"
                  }

# Adding Aditya address in dictionary into JSON format
addbook["Aditya"] = {"name":"Aditya",
                  "address":"364 D/2, Munikra, NewDelhi, India" ,
                  "phone" : "56786543782"
                  }

# Import in JSON module to work with JSON
import json

# Converting from JSON to string
s = json.dumps(addbook)

# Writing string into text file
with open("C://Ritesh//Work//R_AND_D//AI//Python//Exercise//Basics//data//addbook.txt","w") as f:
    f.write(s)
    f.close()

# Reading from text file
rfile = open("C://Ritesh//Work//R_AND_D//AI//Python//Exercise//Basics//data//addbook.txt","r")
filedata = rfile.read()
rfile.close()

# Converting string JSON data
newaddbook = json.loads(filedata)

# Reading particular item/record from JSON
riteshadd = newaddbook["Ritesh"]
print("Reading particular item/record from JSON: ",riteshadd)

# Reading particular column from item/record from JSON like phone
phone = newaddbook["Ritesh"]["phone"]
print("Reading particular column from item/record from JSON like phone: ",phone)

# Reading all the data from JSON
for person in newaddbook:
    print ("Record read from JSON dictionary: ", newaddbook[person])
