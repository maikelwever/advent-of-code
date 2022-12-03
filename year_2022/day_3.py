import logging

logger = logging.getLogger(__name__)


def character_to_priority(char):
    ascii_position = ord(char)
    if ascii_position > 96:
        return ascii_position - 96

    return ascii_position - (65 - 27)


def main(data):
    sum = 0

    for line in data.splitlines():
        middle = len(line) // 2
        first_compartment, second_compartment = line[:middle], line[middle:]
        duplicate_items = set(first_compartment).intersection(set(second_compartment))
        logger.debug('Duplicates for %s: %r', line, duplicate_items)

        for duplicate in duplicate_items:
            priority = character_to_priority(duplicate)
            sum += priority

    logger.info("Sum of the priorities of the duplicated items: %d", sum)


def main_2(data):
    sum = 0

    all_lines = data.splitlines()
    for i in range(0, len(all_lines), 3):
        three_lines = all_lines[i : i + 3]
        duplicate_items = set(three_lines[0]).intersection(three_lines[1]).intersection(three_lines[2])
        logger.debug('Duplicates for %r: %r', three_lines, duplicate_items)

        for duplicate in duplicate_items:
            priority = character_to_priority(duplicate)
            sum += priority

    logger.info("Sum of the priorities of the duplicated items: %d", sum)
