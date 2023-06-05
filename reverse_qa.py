import argparse
import json
from tqdm import tqdm


def format_example(example: dict) -> dict:
    context = f"Instruction: {example['instruction']}\n"
    if example.get("input"):
        context += f"Input: Generate the available question about this paragraph - {example['output']}\n"
    context += "Answer: "
    target = example["input"]
    return {"context": context, "target": target}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="data/alpaca_data.json")
    parser.add_argument("--save_path", type=str, default="data/alpaca_data.jsonl")

    args = parser.parse_args()
    with open(args.data_path) as f:
        examples = json.load(f)

    with open(args.save_path, 'w') as f:
        for example in tqdm(examples, desc="formatting.."):
            f.write(json.dumps(format_example(example)) + '\n')


if __name__ == "__main__":
    main()
