import json
import xml.etree.ElementTree as ET

from tabulate import tabulate

id2sent = {"-1": "negative", "0": "neutral", "1": "positive"}


def rest14(mode="train"):
    data_dir = f"dataset/new_data/Rest14/{mode}_en.xml"
    out_dir = f"dataset/json/ACSA/rest14_{mode}_en.json"
    sentiments = "positive, negative, conflict, and neutral"
    categories = "food, service, price, ambience, and miscellaneous"
    instruct = f"Summarize categories and classify sentiments. Categories include {categories}. Sentiments include {sentiments}. The sentence may has none, one, or multiple categories."
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for sentence in root.findall("sentence"):
        output = []
        aspectCategories = sentence.find("aspectCategories")
        text = sentence.find("text").text
        if aspectCategories is None:
            # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
            non_num += 1
            continue
        for aspectCategory in aspectCategories.findall("aspectCategory"):
            label = aspectCategory.get("polarity").strip()
            category = aspectCategory.get("category")
            if category == "anecdotes/miscellaneous":
                category = "miscellaneous"
            output.append({"category":category, "sentiment":label})
            if label == "positive":
                pos_num += 1
            elif label == "negative":
                neg_num += 1
            elif label == "neutral":
                neu_num += 1
            elif label == "conflict":
                con_num += 1
        if len(output) > 0:
            out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})

    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]

def lap15(mode="train"):
    data_dir = f"dataset/new_data/Lap15/{mode}_en.xml"
    out_dir = f"dataset/json/ACSA/lap15_{mode}_en.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "LAPTOP, DISPLAY, CPU, MOTHERBOARD, HARD_DISC, MEMORY, BATTERY, POWER_SUPPLY, KEYBOARD, MOUSE, FANS_COOLING, OPTICAL_DRIVES, PORTS, GRAPHICS, MULTIMEDIA_DEVICES, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
    attributes = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, PORTABILITY, CONNECTIVITY, and MISCELLANEOUS"
    instruct = f"Summarize categories and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Sentiments include {sentiments}. The sentence may has none, one, or multiple categories."
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for review in root.findall("Review"):
        for sentences in review.findall("sentences"):
            for sentence in sentences.findall("sentence"):
                output = []
                text = sentence.find("text").text
                if not sentence.findall("Opinions"):
                    # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
                    non_num += 1
                    continue
                for opinions in sentence.findall("Opinions"):
                    for opinion in opinions.findall("Opinion"):
                        category = opinion.get("category")
                        if category is None:
                            continue
                        label = opinion.get("polarity").strip()
                        output.append({"category":category.lower(), "sentiment":label})
                        if label == "positive":
                            pos_num += 1
                        elif label == "negative":
                            neg_num += 1
                        elif label == "neutral":
                            neu_num += 1
                        elif label == "conflict":
                            con_num += 1
                if len(output) > 0:
                    out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})

    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]

def lap16(mode="train"):
    data_dir = f"dataset/new_data/Lap16/{mode}_en.xml"
    out_dir = f"dataset/json/ACSA/lap16_{mode}_en.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "LAPTOP, DISPLAY, CPU, MOTHERBOARD, HARD_DISC, MEMORY, BATTERY, POWER_SUPPLY, KEYBOARD, MOUSE, FANS_COOLING, OPTICAL_DRIVES, PORTS, GRAPHICS, MULTIMEDIA_DEVICES, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
    attributes = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, PORTABILITY, CONNECTIVITY, and MISCELLANEOUS"
    instruct = f"Summarize categories and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Sentiments include {sentiments}. The sentence may has none, one, or multiple categories."
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for review in root.findall("Review"):
        for sentences in review.findall("sentences"):
            for sentence in sentences.findall("sentence"):
                output = []
                text = sentence.find("text").text
                if not sentence.findall("Opinions"):
                    # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
                    non_num += 1
                    continue
                for opinions in sentence.findall("Opinions"):
                    for opinion in opinions.findall("Opinion"):
                        category = opinion.get("category")
                        if category is None:
                            continue
                        label = opinion.get("polarity").strip()
                        output.append({"category":category.lower(), "sentiment":label})
                        if label == "positive":
                            pos_num += 1
                        elif label == "negative":
                            neg_num += 1
                        elif label == "neutral":
                            neu_num += 1
                        elif label == "conflict":
                            con_num += 1
                if len(output) > 0:
                    out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})

    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]

def phone16(mode="train", lang="zh"):
    data_dir = f"dataset/new_data/Phone16/{mode}_{lang}.xml"
    out_dir = f"dataset/json/ACSA/phone16_{mode}_{lang}.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "PHONE, DISPLAY, BATTERY, CPU, MEMORY, HARD_DISC, POWER_SUPPLY, KEYBOARD, MULTIMEDIA_DEVICES, PORTS, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
    attributes = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, CONNECTIVITY, and MISCELLANEOUS"
    instruct = f"Summarize categories and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Sentiments include {sentiments}. The sentence may has none, one, or multiple categories."
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for review in root.findall("Review"):
        for sentences in review.findall("sentences"):
            for sentence in sentences.findall("sentence"):
                output = []
                text = sentence.find("text").text
                if not sentence.findall("Opinions"):
                    # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
                    non_num += 1
                    continue
                for opinions in sentence.findall("Opinions"):
                    for opinion in opinions.findall("Opinion"):
                        category = opinion.get("category")
                        if category is None:
                            continue
                        label = opinion.get("polarity").strip()
                        output.append({"category":category.lower(), "sentiment":label})
                        if label == "positive":
                            pos_num += 1
                        elif label == "negative":
                            neg_num += 1
                        elif label == "neutral":
                            neu_num += 1
                        elif label == "conflict":
                            con_num += 1
                if len(output) > 0:
                    out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})

    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]

def came16(mode="train"):
    data_dir = f"dataset/new_data/Came16/{mode}_zh.xml"
    out_dir = f"dataset/json/ACSA/came16_{mode}_zh.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "CAMERA, LENS, PHOTO, FOCUS, DISPLAY, CPU, MEMORY, BATTERY, POWER_SUPPLY, KEYBOARD, PORTS, MULTIMEDIA_DEVICES, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
    attributes = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, PORTABILITY, CONNECTIVITY, and MISCELLANEOUS"
    instruct = f"Summarize categories and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Sentiments include {sentiments}. The sentence may has none, one, or multiple categories."
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for review in root.findall("Review"):
        for sentences in review.findall("sentences"):
            for sentence in sentences.findall("sentence"):
                output = []
                text = sentence.find("text").text
                if not sentence.findall("Opinions"):
                    # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
                    non_num += 1
                    continue
                for opinions in sentence.findall("Opinions"):
                    for opinion in opinions.findall("Opinion"):
                        category = opinion.get("category")
                        if category is None:
                            continue
                        label = opinion.get("polarity").strip()
                        output.append({"category":category.lower(), "sentiment":label})
                        if label == "positive":
                            pos_num += 1
                        elif label == "negative":
                            neg_num += 1
                        elif label == "neutral":
                            neu_num += 1
                        elif label == "conflict":
                            con_num += 1
                if len(output) > 0:
                    out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
            
    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]

def mams(mode):
    data_dir = f"dataset/new_data/MAMS-ACSA/{mode}_en.xml"
    out_dir = f"dataset/json/ACSA/mams_{mode}_en.json"
    
    sentiments = "positive, negative, conflict, and neutral"
    categories = "food, service, price, ambience, staff, menu, place, and miscellaneous"
    instruct = f"Summarize categories and classify sentiments. Categories include {categories}. Sentiments include {sentiments}. The sentence may has none, one, or multiple categories."
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    sentences = tree.getroot()
    for sentence in sentences:
        output = []
        text = sentence.find("text")
        if text is None:
            continue
        text = text.text
        aspectCategories = sentence.find("aspectCategories")
        if aspectCategories is None:
            continue
        for aspectCategory in aspectCategories:
            category = aspectCategory.get("category")
            label = aspectCategory.get("polarity")
            output.append({"category":category.lower(), "sentiment":label})
            if label == "positive":
                pos_num += 1
            elif label == "negative":
                neg_num += 1
            elif label == "neutral":
                neu_num += 1
            elif label == "conflict":
                con_num += 1     
        if len(output) > 0:
            out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})


    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]



if __name__ == "__main__":
    table = [["dataset", "Total", "Non", "Pos", "Neg", "Con", "Neu"]]

    for mode in ["train", "test"]:
        table.append(rest14(mode))

    for mode in ["train", "test"]:
        table.append(lap15(mode))

    for mode in ["train", "test"]:
        table.append(lap16(mode))

    for lang in ["zh", "nl"]:
        for mode in ["train", "test"]:
            table.append(phone16(mode, lang))
    
    for mode in ["train", "test"]:
        table.append(came16(mode))

    for mode in ["train", "val", "test"]:
        table.append(mams(mode))

    print(tabulate(table, headers="firstrow", tablefmt="simple_grid"))
