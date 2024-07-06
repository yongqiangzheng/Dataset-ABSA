import json
import os

def merge_save():
    merged_data = []
    for root, dirs, files in os.walk("dataset/json"):
        for file in files:
            if "train" in file and "mams" not in file:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(file_path, len(data))
                    merged_data.extend(data)  
    print(len(merged_data))
    with open("dataset/json/LLM/absa.json", "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(merged_data, indent=4, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    merge_save()
