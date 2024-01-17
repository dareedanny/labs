
import json

def task() -> float:
    with open('input.json', 'r') as file1:
        json_data = json.load(file1)
        total = sum(item["score"]*item["weight"] for item in json_data)
        return(f"{total:.3f}")

print(task())