import pandas as pd
import json
from bs4 import BeautifulSoup
import yaml
from yaml.loader  import SafeLoader

path = "../../me"
#Read CSV 
data = pd.read_csv(path + ".csv")
print("\nCSV")
print(data)

# Read Json 
with open(path + ".json") as f:
    data = json.load(f)

print("\nJson")
print(data)

# Normal Text 

with open(path + ".txt") as f: 
    data = f.readlines()
print("\nNoraml Text")
print(data)

#Read xaml
print("\nxml")
with open(path + ".xml") as f:
    data = f.read()

print(data)

Bs_data = BeautifulSoup(data,"xml")


#Yaml

with open(path + ".yaml") as f: 
    data = yaml.load(f,Loader=SafeLoader)
print("\nYaml")
print(data)


