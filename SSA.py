import json

datasets = [
    "norec",
    "multibooked_ca",
    "multibooked_eu",
    "opener_en",
    "opener_es",
    "mpqa",
    "darmstadt_unis",
]

modes = ["train", "dev", "test"]

for dataset in datasets:
    for mode in modes:
        out_data = []
        with open(f"dataset/jsonl/SSA/{dataset}/{mode}.jsonl", "r") as jsonl_file:
            lines = jsonl_file.readlines()
            for line in lines:
                data = json.loads(line.strip())
                if len(data["opinions"]):
                    output = ""
                    for opinion in data["opinions"]:
                        holder = opinion["holder"]
                        # if holder == "":
                        #     holder = "NULL"
                        target = opinion["target"]
                        # if target == "":
                        #     target = "NULL"
                        expression = opinion["expression"]
                        sentiment = opinion["sentiment"].lower()
                        
                        output += f"Holder: {holder}\nTarget: {target}\nExpression: {expression}\nSentiment: {sentiment}\n\n"
                    output = output.strip()
                        
                    out_data.append({"instruction": "Extract the holders, targets, expressions from the sentence and predict their sentiment as positive, neutral or negative.",
                                    "input": data["text"],
                                    "output": output})

        with open(f"dataset/json/SSA/{dataset}_{mode}.json", "w") as json_file:
            for item in out_data:
                json_file.write(json.dumps(item, ensure_ascii=False) + '\n')