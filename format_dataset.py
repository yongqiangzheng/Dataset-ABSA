import argparse
import os
import xml.etree.ElementTree as ET

from datasets import Dataset, DatasetDict

def extract_aspect_terms(xml_file):
    """从单个 XML 文件提取数据"""
    try:
        tree = ET.parse(xml_file)
    except FileNotFoundError:
        print(f"Error: File '{xml_file}' not found.")
        return []
    except ET.ParseError:
        print("Error: Invalid XML format.")
        return []
    
    root = tree.getroot()
    extracted_data = []
    text_id = 0
    
    for sentence in root.findall('sentence'):
        text_element = sentence.find('text')
        if text_element is None:
            continue
        text = text_element.text
        
        aspect_terms = sentence.find('aspectTerms')
        if aspect_terms is None:
            continue
        
        for aspect_term in aspect_terms.findall('aspectTerm'):
            term = aspect_term.get('term')
            polarity = aspect_term.get('polarity')
            from_pos = aspect_term.get('from')
            to_pos = aspect_term.get('to')
            
            if None in (term, polarity, from_pos, to_pos):
                continue
            
            try:
                from_pos = int(from_pos)
                to_pos = int(to_pos)
            except ValueError:
                print(f"Invalid position values: from={from_pos}, to={to_pos}")
                continue
            
            extracted_term = text[from_pos:to_pos]
            if extracted_term != term:
                print(f"Mismatch in text_id {text_id}: XML term='{term}', Extracted='{extracted_term}'")

            extracted_data.append({
                'text_id': text_id,
                'text': text,
                'term': term,
                'polarity': polarity,
                'from': from_pos,
                'to': to_pos
            })
        
        text_id += 1
    
    return extracted_data

def load_dataset_from_xmls(root_dir):
    """加载 train/dev/test XML 并转换为 DatasetDict"""
    xml_files = {
        "train": "train.xml",  # 假设训练集叫 train.xml
        "dev": "dev.xml",  # 验证集叫 dev.xml
        "test": "test.xml"  # 测试集叫 test.xml
    }
    
    dataset_dict = {}
    for split, xml_file in xml_files.items():
        xml_path = os.path.join(root_dir, xml_file)
        data = extract_aspect_terms(xml_path)
        dataset_dict[split] = Dataset.from_list(data)  # 转换为 Hugging Face Dataset
    
    return DatasetDict(dataset_dict)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract aspect terms and upload to Hugging Face.')
    parser.add_argument('--dataset', type=str, default="rest14_en", help='Directory containing train/dev/test XML files')
    parser.add_argument('--hf_repo', type=str, default="yqzheng/ABSA_Restaurant_2014", help='Hugging Face repository (e.g., "username/dataset-name")')
    
    args = parser.parse_args()
    
    # 1. 加载数据集
    dataset = load_dataset_from_xmls(os.path.join("dataset", args.dataset) )
    print(dataset)  # 查看数据集结构
    
    # 2. 登录 Hugging Face
    # 使用 `huggingface-cli login`
    
    # 3. 上传数据集
    dataset.push_to_hub(args.hf_repo)
    print(f"Dataset uploaded to: https://huggingface.co/datasets/{args.hf_repo}")