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

