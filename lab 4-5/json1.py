import json

file_path = "pp2_labs/lab 4-5/sample-data.json"
with open(file_path, "r") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50}{'Description':<15}{'Speed':<10}{'MTU'}")
print("-" * 50, "-" * 15, "-" * 10, "-" * 4)

for item in data.get("imdata", []):
    attributes = item["l1PhysIf"]["attributes"]
    print(f"{attributes['dn']:<50}{'':<15}{attributes['speed']:<10}{attributes['mtu']}")
