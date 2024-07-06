import json
import xml.etree.ElementTree as ET

from copy import deepcopy

id2sent = {"-1": "negative", "0": "neutral", "1": "positive"}

semeval14_sentiment1 = "positive, negative, conflict, and neutral"
semeval14_sentiment2 = "positive, negative, conflict (both positive and negative sentiment), and neutral (neither positive nor negative sentiment)"

semeval1516_sentiment1 = "positive, negative, and neutral"
semeval1516_sentiment2 = "positive, negative, and neutral (neither positive nor negative sentiment)"

semeval14_categories1 = "food, service, price, ambience, and anecdotes/miscellaneous"
semeval14_categories2 = "food, service, price, ambience (sentences referring to the atmosphere and the environment of a restaurant), and anecdotes/miscellaneous (sentences that do not belong to the above four categories)"

lap15_entities1 = "LAPTOP, DISPLAY, CPU, MOTHERBOARD, HARD_DISC, MEMORY, BATTERY, POWER_SUPPLY, KEYBOARD, MOUSE, FANS_COOLING, OPTICAL_DRIVES, PORTS, GRAPHICS, MULTIMEDIA_DEVICES, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
# lap15_entities2 = "LAPTOP, DISPLAY (monitor, screen), CPU (processor), MOTHERBOARD, HARD DISC, MEMORY, BATTERY, POWER SUPPLY (charger, charger unit, power supply cord, power adapter), KEYBOARD (keys, numpad), MOUSE (mouse pad and the buttons on it), FANS&COOLING (fan, cooling system, heat sink), OPTICAL DRIVES (CD, DVD or Blue-ray players, DVD drive, disc drive, DVD burner), PORTS (USB, HDMI, VGA, card reader, Firewire, SD, DVI, Thunderbolt), GRAPHICS (graphics card, video card, graphics chip), MULTIMEDIA DEVICES (sound, audio, microphone, built-in camera, webcam, speakers, headphone), HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, COMPANY"
lap1516_attributes1 = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, PORTABILITY, CONNECTIVITY, and MISCELLANEOUS"

rest1516_entities1 = "RESTAURANT, FOOD, DRINKS, SERVICE, AMBIENCE, and LOCATION"
rest1516_attributes1 = "GENERAL, PRICES, QUALITY, STYLE_OPTIONS and MISCELLANEOUS"

htl1516_entities1 = "HOTEL, ROOMS, ROOM_AMENITIES, FACILITIES, SERVICE, LOCATION, and FOOD_DRINKS"
htl1516_categories1 = "GENERAL, PRICES, DESIGN_FEATURES, CLEANLINESS, COMFORT, QUALITY, STYLE_OPTIONS, and MISCELLANEOUS"

pho16_entities1 = "PHONE, DISPLAY, BATTERY, CPU, MEMORY, HARD_DISC, POWER_SUPPLY, KEYBOARD, MULTIMEDIA_DEVICES, PORTS, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
pho16_categories1 = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, CONNECTIVITY, and MISCELLANEOUS"

cam16_entities1 = "CAMERA, LENS, PHOTO, FOCUS, DISPLAY, CPU, MEMORY, BATTERY, POWER_SUPPLY, KEYBOARD, PORTS, MULTIMEDIA_DEVICES, HARDWARE, OS, SOFTWARE, WARRANTY, SHIPPING, SUPPORT, and COMPANY"
cam16_categories1 = "GENERAL, PRICE, QUALITY, OPERATION_PERFORMANCE, USABILITY, DESIGN_FEATURES, PORTABILITY, CONNECTIVITY, and MISCELLANEOUS"

mus_entities1 = ""
mus_categories1 = ""

_entities1 = ""
_categories1 = ""

sentiment = ""
categories = ""
entities = ""
attributes = ""

as_instruct = f"Extract aspects and classify sentiments. Aspects are words in the sentence and sentiments include {sentiment}. The sentence may has none, one, or multiple aspects."
easy_cs_instruct = f"Summarize categories and classify sentiments. Categories include {categories} and sentiments include {sentiment}. The sentence may has none, one, or multiple categories."
hard_cs_instruct = f"Summarize categories and classify sentiments. Categories are pairs of entities and attributes and sentiments include {sentiment}. Entities include {entities}. Attributes include {attributes}. The sentence may has none, one, or multiple categories."
acs_instruct = f"Summarize categories, extract targets and classify sentiments. Categories are pairs of entities and attributes and sentiments include {sentiment}. Entities include {entities}. Attributes include {attributes}. Targets are words in the sentence that explicitly mention entities, or NULL when entities are implicit. The sentence may has none, one, or multiple categories."



def lap14(mode="train"):
    data_dir = f"dataset/new_data/Lap14/{mode}_en.xml"
    out_dir = f"dataset/json/AE_lap14_{mode}_en.json"
    out_data = []
    non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for sentence in root.findall("sentence"):
        output = []
        aspectTerms = sentence.find("aspectTerms")
        text = sentence.find("text").text
        if aspectTerms is None:
            continue
        for aspectTerm in aspectTerms.findall("aspectTerm"):
            aspect = aspectTerm.get("term")
            start = aspectTerm.get("from")
            end = aspectTerm.get("to")
            assert text[int(start):int(end)].lower() == aspect.lower()
            aspect = text[int(start):int(end)]
            output.append([aspect, int(start), int(end)])

        sorted_output = sorted(output, key=lambda x:x[1])
        star_len = 0
        edit_text = deepcopy(text)
        for item in sorted_output:
            start = item[1] + star_len
            end = item[2] + star_len
            edit_text = edit_text[:start] + '**' + edit_text[start:end] + '**' + edit_text[end:]
            star_len += 4
        out_data.append({"instruction":"Extract aspects by inserting ** ** in reviews", "input": text, "output": edit_text})

    with open(out_dir, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
    dataset_name = out_dir.split("/")[-1].split(".")[0]
    total_num = len(out_data)
    return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]

# def rest14(mode="train"):
#     data_dir = f"dataset/new_data/Rest14/{mode}_en.xml"
#     out_dir = f"dataset/json/E2E-ATSA/rest14_{mode}_en.json"
#     sentiments = "positive, negative, conflict, and neutral"
#     instruct = f"Extract aspects and classify sentiments. Aspects are words in the sentence and sentiments include {sentiments}. The sentence may has none, one, or multiple aspects."
#     out_data = []
#     non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
#     tree = ET.parse(data_dir)
#     root = tree.getroot()
#     for sentence in root.findall("sentence"):
#         output = []
#         aspectTerms = sentence.find("aspectTerms")
#         text = sentence.find("text").text
#         if aspectTerms is None:
#             # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
#             non_num += 1
#             continue
#         for aspectTerm in aspectTerms.findall("aspectTerm"):
#             label = aspectTerm.get("polarity").strip()
#             aspect = aspectTerm.get("term")
#             start = aspectTerm.get("from")
#             end = aspectTerm.get("to")
#             assert text[int(start):int(end)].lower() == aspect.lower()
#             aspect = text[int(start):int(end)]
#             output.append({"aspect":aspect, "sentiment":label})
#             if label == "positive":
#                 pos_num += 1
#             elif label == "negative":
#                 neg_num += 1
#             elif label == "neutral":
#                 neu_num += 1
#             elif label == "conflict":
#                 con_num += 1
#         out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})

#     with open(out_dir, "w", encoding="utf-8") as json_file:
#         json_file.write(json.dumps(out_data, indent=4, ensure_ascii=False) + "\n")
#     dataset_name = out_dir.split("/")[-1].split(".")[0]
#     total_num = len(out_data)
#     return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]


# def mams(mode):
#     data_dir = f"dataset/new_data/MAMS-ATSA/{mode}_en.xml"
#     out_dir = f"dataset/json/E2E-ATSA/mams_{mode}_en.json"
#     sentiments = "positive, negative, conflict, and neutral"
#     instruct = f"Extract aspects and classify sentiments. Aspects are words in the sentence and sentiments include {sentiments}. The sentence may has none, one, or multiple aspects."
#     out_data = []
#     non_num, pos_num, neu_num, neg_num, con_num = 0, 0, 0, 0, 0
#     tree = ET.parse(data_dir)
#     sentences = tree.getroot()
#     for sentence in sentences:
#         output = []
#         text = sentence.find("text")
#         if text is None:
#             continue
#         text = text.text
#         aspectTerms = sentence.find("aspectTerms")
#         if aspectTerms is None:
#             # out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})
#             non_num += 1
#             continue
#         for aspectTerm in aspectTerms:
#             aspect = aspectTerm.get("term")
#             label = aspectTerm.get("polarity")
#             start = aspectTerm.get("from")
#             end = aspectTerm.get("to")
#             assert text[int(start):int(end)].lower() == aspect.lower()
#             aspect = text[int(start):int(end)]
#             output.append({"aspect":aspect, "sentiment":label})
#             if label == "negative":
#                 neg_num += 1
#             elif label == "neutral":
#                 neu_num += 1
#             elif label == "positive":
#                 pos_num += 1
#         out_data.append({"instruction":instruct, "input": text, "output": json.dumps(output, ensure_ascii=False)})

#     with open(out_dir, "w", encoding="utf-8") as json_file:
#         json_file.write(json.dumps(out_data, ensure_ascii=False) + "\n")
#     dataset_name = out_dir.split("/")[-1].split(".")[0]
#     total_num = len(out_data)
#     return [dataset_name, total_num, non_num, pos_num, neg_num, con_num, neu_num]


if __name__ == "__main__":

    for mode in ["train", "test"]:
        lap14(mode)

    # for mode in ["train", "test"]:
    #     table.append(rest14(mode))

    # for mode in ["train", "val", "test"]:
    #     table.append(mams(mode))


