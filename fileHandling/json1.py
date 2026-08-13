import json

data = {
    "name": "Aman",
    "age": 20,
    "skills": ["Python", "Django"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["name"])    


json_string = json.dumps(data)
python_obj = json.loads(json_string)
print(python_obj)


# dump → Python → JSON file
# load → JSON file → Python