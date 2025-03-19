import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"] if attributes["speed"] else ""
    mtu = attributes["mtu"] if attributes["mtu"] else ""
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")
