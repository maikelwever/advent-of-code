from collections import defaultdict

import logging


logger = logging.getLogger(__name__)


def logic(data, is_mover_9001=False):
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
    stack_count_start = sum(len(i) for i in stacks.values())

    for move_count, stack_pop, stack_append in moves:
        if is_mover_9001:
            neg_move_count = move_count * -1
            popped = stacks[stack_pop][neg_move_count:]
            stacks[stack_pop] = stacks[stack_pop][:neg_move_count]
            logger.debug("Popped %d from %d: %r, new stack: %r", neg_move_count, stack_pop, popped, stacks[stack_pop])
            stacks[stack_append].extend(popped)
        else:
            for _ in range(move_count):
                popped = stacks[stack_pop].pop()
                stacks[stack_append].append(popped)

    logger.debug("Re-ordered stacks: %r", stacks)

    message = ''
    for stack_id in sorted(stacks.keys()):
        message += stacks[stack_id][-1]

    stack_count_end = sum(len(i) for i in stacks.values())
    if stack_count_end != stack_count_start:
        logger.warning("Sanity check failed: started with %d crates, ended up with %d crates!", stack_count_start, stack_count_end)

    logger.info("Message to elfs: %s", message)


def main(data):
    return logic(data)


def main_2(data):
    return logic(data, is_mover_9001=True)

