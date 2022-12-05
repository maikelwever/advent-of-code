from collections import defaultdict

import logging


logger = logging.getLogger(__name__)


def main(data):
    stacks = defaultdict(list)
    moves = []
    for line in data.splitlines():
        if line.startswith('move'):
            line_parts = line.split(' ')
            moves.append((
                int(line_parts[1]),
                int(line_parts[3]),
                int(line_parts[5]),
            ))
        elif '[' in line:
            i = 0
            while line:
                token = line[:4]
                line = line[4:]
                letter = token[1]
                i += 1
                if letter != ' ':
                    stacks[i].insert(0, letter)

    logger.debug("Stacks: %r", stacks)

    for move_count, stack_pop, stack_append in moves:
        for _ in range(move_count):
            popped = stacks[stack_pop].pop()
            stacks[stack_append].append(popped)

    logger.debug("Re-ordered stacks: %r", stacks)

    message = ''
    for stack_id in sorted(stacks.keys()):
        message += stacks[stack_id][-1]

    logger.info("Message to elfs: %s", message)

