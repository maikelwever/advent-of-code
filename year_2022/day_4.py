import logging

logger = logging.getLogger(__name__)


def main(data):
    containment_count = 0
    overlap_count = 0

    for line in data.splitlines():
        first_elf, second_elf = line.split(',')

        first_elf_start, first_elf_end = first_elf.split('-')
        second_elf_start, second_elf_end = second_elf.split('-')

        first_elf_range = range(int(first_elf_start), int(first_elf_end) + 1)
        second_elf_range = range(int(second_elf_start), int(second_elf_end) + 1)

        first_elf_set = set(first_elf_range)
        second_elf_set = set(second_elf_range)

        if first_elf_set >= second_elf_set or second_elf_set >= first_elf_set:
            logger.debug("Containment detected in: %s", line)
            containment_count += 1

        if first_elf_set.intersection(second_elf_set):
            logger.debug("Overlap detected in: %s", line)
            overlap_count += 1

    logger.info("Containing sets: %d", containment_count)
    logger.info("Overlapping sets: %d", overlap_count)

