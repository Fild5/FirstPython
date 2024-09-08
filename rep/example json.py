import json
numbers = [1, 2, 3, 4, 5, 6, 7]
json_date = json.dumps(numbers)
with open("numbers.json", "w") as f:
    f.write(json_date)