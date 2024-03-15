import jsonlines
import argparse
from tqdm import tqdm
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True, help='Path to the LIAR dataset file')
parser.add_argument('--output', type=str, required=True, help='Path to output jsonl, i.e., liar_converted.jsonl')
args = parser.parse_args()
print('Converting LIAR dataset')
statements = list(jsonlines.open(args.input))
output = jsonlines.open(args.output, mode='w')

for statement in tqdm(statements):
    # Assume 'id', 'statement', and 'label' are available fields in the LIAR dataset.
    # Adjust field names based on the actual LIAR dataset structure.
    output.write({
        'id': statement['id'],
        'claim': statement['statement'],
        'label': statement['label'],
        # SciFact requires evidence sets, but LIAR does not provide direct evidence links.
        # We'll use an empty list to comply with the format.
        'sentences': statement['context'],
    })
