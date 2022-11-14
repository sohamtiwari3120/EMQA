import os
import json
import random
import copy
random.seed(123)
SQUAD_FILE ="./data/train-v1.1.json"
squad_dataset = json.load(open(SQUAD_FILE, "rb"))
path_template="./data/squad_{0}_google.json"
languages=["ko","id","ar","sw","ru","fi","te","bn"]
print("len before", len(squad_dataset['data']), list(squad_dataset.keys()))
for i in languages:
    ft_path=path_template.format(i)
    with open(ft_path, "rb") as f:
        in_file = json.load(f)
        sample = random.sample(in_file['data'], len(in_file['data']))
        squad_dataset['data'].extend(sample)
        print(f"Done with {ft_path}")
print("len after", len(squad_dataset['data']), list(squad_dataset.keys()))


out_path = f'./data/merged_squad_google_transltate/'
os.makedirs(out_path, exist_ok=True)
out_file_name = os.path.join(out_path, f'squad_plus_translatedSquad_.json')
with open(out_file_name, 'w', encoding='utf-8') as outfile:
    json.dump(squad_dataset, outfile)
