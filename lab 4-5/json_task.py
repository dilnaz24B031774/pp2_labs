import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", "speed", " " * 10, "MTU")
print("-" * 41, "-" * 12, "-" * 13, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]: # every imdata[i] is dictionary
            print(imdata[i][j]["dn"],"\t", "\t\t\t"  , imdata[i][j]["speed"] ,"\t\t" , imdata[i][j]["mtu"])