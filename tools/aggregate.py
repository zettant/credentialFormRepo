import glob
import yaml
import json

all_data = dict()


files = glob.glob("../entries/*.yaml")
for file in files:
    with open(file, "r") as f:
        cred = yaml.safe_load(f)
    all_data.update(cred)

with open("../sites.json", "w") as f:
    json.dump(all_data, f)

