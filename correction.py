import re
import xml.etree.ElementTree as ET


def semeval14(domain="Lap14", mode="train"):
    data_dir = f"dataset/new_data/{domain}/{mode}_en.xml"
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for sentence in root.findall("sentence"):
        aspectTerms = sentence.find("aspectTerms")
        if aspectTerms is None:
            continue
        text = sentence.find("text").text
        for aspectTerm in aspectTerms.findall("aspectTerm"):
            aspect = aspectTerm.get("term")
            error1 = re.search(r"[^a-zA-Z0-9\s]", aspect)
            if error1:
                print(aspect)
            start = aspectTerm.get("from")
            end = aspectTerm.get("to")
            assert text[int(start):int(end)].lower() == aspect.lower()
            mask_text = text[:int(start)] + "$T$" + text[int(end):]
            error2 = re.search(r"\$T\$[a-zA-Z]", mask_text)
            if error2:
                print(mask_text)


def semeval15(domain="Lap15", mode="train"):
    data_dir = f"dataset/new_data/{domain}/{mode}_en.xml"
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for review in root.findall("Review"):
        for sentences in review.findall("sentences"):
            for sentence in sentences.findall("sentence"):
                text = sentence.find("text").text
                if not sentence.findall("Opinions"):
                    continue
                for opinions in sentence.findall("Opinions"):
                    for opinion in opinions.findall("Opinion"):
                        aspect = opinion.get("target")
                        if aspect == "NULL":
                            continue
                        error1 = re.search(r"[^a-zA-Z0-9\s]", aspect)
                        if error1:
                            print(aspect)
                        start = opinion.get("from")
                        end = opinion.get("to")
                        assert text[int(start):int(end)].lower() == aspect.lower()
                        mask_text = text[:int(start)] + "$T$" + text[int(end):]
                        error2 = re.search(r"\$T\$[a-zA-Z]", mask_text)
                        if error2:
                            print(mask_text)


def semeval16(domain="Rest16", mode="train", lang="en"):
    data_dir = f"dataset/new_data/{domain}/{mode}_{lang}.xml"
    tree = ET.parse(data_dir)
    root = tree.getroot()
    for review in root.findall("Review"):
        for sentences in review.findall("sentences"):
            for sentence in sentences.findall("sentence"):
                text = sentence.find("text").text
                if not sentence.findall("Opinions"):
                    continue
                for opinions in sentence.findall("Opinions"):
                    for opinion in opinions.findall("Opinion"):
                        aspect = opinion.get("target")
                        if aspect == "NULL":
                            continue
                        error1 = re.search(r"[^a-zA-Z0-9\s]", aspect)
                        if error1:
                            print(aspect)
                        start = opinion.get("from")
                        end = opinion.get("to")
                        assert text[int(start):int(end)] == aspect
                        mask_text = text[:int(start)] + "$T$" + text[int(end):]
                        error2 = re.search(r"\$T\$[a-zA-Z]", mask_text)
                        if error2:
                            print(mask_text)


if __name__ == '__main__':
    """
    error1 checks whether there is a "," or "." at the end of aspects.
    error2 checks whether aspects are incomplete.
    """
    # semeval14("Lap14", "train")
    # semeval14("Lap14", "test")
    # semeval14("Rest14", "train")
    # semeval14("Rest14", "test")
    # semeval15("Rest15", "train")
    # semeval15("Rest15", "test")
    # semeval15("Hotel15", "test")
    # semeval16("Rest16", "train", "en")
    # semeval16("Rest16", "test", "en")
    # semeval16("Rest16", "train", "es")
    # semeval16("Rest16", "test", "es")
    # semeval16("Rest16", "train", "fr")
    # semeval16("Rest16", "test", "fr")
    semeval16("Rest16", "train", "nl")
    semeval16("Rest16", "test", "nl")
    semeval16("Rest16", "train", "ru")
    semeval16("Rest16", "test", "ru")
    semeval16("Rest16", "train", "tr")
    semeval16("Rest16", "test", "tr")
    semeval16("Hotel16", "train", "ar")
    semeval16("Hotel16", "test", "ar")
