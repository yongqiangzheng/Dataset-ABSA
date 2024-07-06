import json
import xml.etree.ElementTree as ET

from tabulate import tabulate

id2sent = {"-1": "negative", "0": "neutral", "1": "positive"}


def rest15(mode="train"):
    data_dir = f"dataset/new_data/Rest15/{mode}_en.xml"
    out_dir = f"dataset/json/TASD/rest15_{mode}_en.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "RESTAURANT, FOOD, DRINKS, SERVICE, AMBIENCE, and LOCATION"
    attributes = "GENERAL, PRICES, QUALITY, STYLE_OPTIONS and MISCELLANEOUS"
    instruct = f"Summarize categories, extract targets and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Targets are words in the sentence that explicitly mention entities, or NULL when entities are implicit. Sentiments include {sentiments.lower()}. The sentence may has none, one, or multiple categories."
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
                        target = opinion.get("target")
                        start = opinion.get("from")
                        end = opinion.get("to")
                        if target != "NULL":
                            assert text[int(start):int(end)].lower() == target.lower()
                            target = text[int(start):int(end)]
                        output.append({"target": target, "category":category.lower(), "sentiment":label})
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

def rest16(mode="train", lang="en"):
    data_dir = f"dataset/new_data/Rest16/{mode}_{lang}.xml"
    out_dir = f"dataset/json/TASD/rest16_{mode}_{lang}.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "RESTAURANT, FOOD, DRINKS, SERVICE, AMBIENCE, and LOCATION"
    attributes = "GENERAL, PRICES, QUALITY, STYLE_OPTIONS and MISCELLANEOUS"
    instruct = f"Summarize categories, extract targets and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Targets are words in the sentence that explicitly mention entities, or NULL when entities are implicit. Sentiments include {sentiments.lower()}. The sentence may has none, one, or multiple categories."
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
                        target = opinion.get("target")
                        start = opinion.get("from")
                        end = opinion.get("to")
                        if target != "NULL":
                            assert text[int(start):int(end)].lower() == target.lower()
                            target = text[int(start):int(end)]
                        output.append({"target": target, "category":category.lower(), "sentiment":label})
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

def hotel15(mode="train"):
    data_dir = f"dataset/new_data/Hotel15/{mode}_en.xml"
    out_dir = f"dataset/json/TASD/hotel15_{mode}_en.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "HOTEL, ROOMS, ROOM_AMENITIES, FACILITIES, SERVICE, LOCATION, and FOOD_DRINKS"
    attributes = "GENERAL, PRICES, DESIGN_FEATURES, CLEANLINESS, COMFORT, QUALITY, STYLE_OPTIONS, and MISCELLANEOUS"
    instruct = f"Summarize categories, extract targets and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Targets are words in the sentence that explicitly mention entities, or NULL when entities are implicit. Sentiments include {sentiments.lower()}. The sentence may has none, one, or multiple categories."
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
                        target = opinion.get("target")
                        start = opinion.get("from")
                        end = opinion.get("to")
                        if target != "NULL":
                            assert text[int(start):int(end)].lower() == target.lower()
                            target = text[int(start):int(end)]
                        output.append({"target": target, "category":category.lower(), "sentiment":label})
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

def hotel16(mode="train"):
    data_dir = f"dataset/new_data/Hotel16/{mode}_ar.xml"
    out_dir = f"dataset/json/TASD/hotel16_{mode}_ar.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "HOTEL, ROOMS, ROOM_AMENITIES, FACILITIES, SERVICE, LOCATION, and FOOD_DRINKS"
    attributes = "GENERAL, PRICES, DESIGN_FEATURES, CLEANLINESS, COMFORT, QUALITY, STYLE_OPTIONS, and MISCELLANEOUS"
    instruct = f"Summarize categories, extract targets and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Targets are words in the sentence that explicitly mention entities, or NULL when entities are implicit. Sentiments include {sentiments.lower()}. The sentence may has none, one, or multiple categories."
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
                        target = opinion.get("target")
                        start = opinion.get("from")
                        end = opinion.get("to")
                        if target != "NULL":
                            assert text[int(start):int(end)].lower() == target.lower()
                            target = text[int(start):int(end)]
                        output.append({"target": target, "category":category.lower(), "sentiment":label})
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

def muse16(mode="test"):    
    data_dir = f"dataset/new_data/Muse16/{mode}_fr.xml"
    out_dir = f"dataset/json/TASD/muse16_{mode}_fr.json"
    sentiments = "positive, negative, conflict, and neutral"
    entities = "MUSEUM, SERVICE, TOURGUIDING, FACILITIES, COLLECTIONS, LOCATION"
    attributes = "GENERAL, PRICES, INTEREST, ACTIVITIES, SETUP, COMFORT, ARCHITECTURE AND MISCELLANEOUS"
    instruct = f"Summarize categories, extract targets and classify sentiments. Categories are pairs of entities and attributes. Entities include {entities.lower()}. Attributes include {attributes.lower()}. Targets are words in the sentence that explicitly mention entities, or NULL when entities are implicit. Sentiments include {sentiments.lower()}. The sentence may has none, one, or multiple categories."
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
                        target = opinion.get("target")
                        start = opinion.get("from")
                        end = opinion.get("to")
                        if target != "NULL":
                            assert text[int(start):int(end)].lower() == target.lower()
                            target = text[int(start):int(end)]
                        output.append({"target": target, "category":category.lower(), "sentiment":label})
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
            table.append(rest15(mode))
    
    for lang in ["en", "es", "fr", "nl", "ru", "tr"]:
        for mode in ["train", "test"]:
            table.append(rest16(mode, lang))

    table.append(hotel15("test"))
    
    for mode in ["train", "test"]:
        table.append(hotel16(mode))
    
    table.append(muse16("test"))

    print(tabulate(table, headers="firstrow", tablefmt="simple_grid"))
    
