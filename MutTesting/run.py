import sys
import textwrap

from MutTest import mutating

PYTHON_FILE = sys.argv[1][2:]


def calculate_score(total, killed):
    return killed / total


if __name__ == '__main__':
    with open(PYTHON_FILE, 'r') as f:
        split_text = f.read().split('# Test')

    source_code = textwrap.dedent(split_text[0])

    killed_count, mutation_number = mutating.use_mutation(source_code)
    print("Mutation Score: ")
    print(calculate_score(mutation_number, killed_count))
