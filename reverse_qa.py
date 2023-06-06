import argparse
import json
from tqdm import tqdm


def format_example(example: dict) -> dict:
    context = f"Instruction: Generate the available question about the following paragraph\n"
    context += f"Input: {example['output']}\n"
    if example.get("input"):
        context += f"FYI: {example['input']}\n"
    context += "Answer: "
    target = example["instruction"]
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
            proc_data = format_example(example)
            if proc_data is None:
                continue
            f.write(json.dumps(proc_data) + '\n')


if __name__ == "__main__":
    main()
