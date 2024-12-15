import os 
import json
import re

input_folder = ""       # input folder path
output_folder = ""      # output folder path

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        url = data["url"].replace("\n", "")
        vi_content = data["vi"].replace("\n", "")
        eng_content = data["en"].replace("\n", "")
        
        vi_content = re.sub(r'\d{2}:\d{2}', '', vi_content)
        eng_content = re.sub(r'\d{2}:\d{2}', '', eng_content)
        
        data["url"] = url
        data["vi"] = vi_content
        data["en"] = eng_content
        
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

print("Done")