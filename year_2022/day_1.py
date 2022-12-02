import logging

logger = logging.getLogger(__name__)


def main(asset):
    calories_sums = []
    current_sum = 0

    for line in asset.splitlines():
        if line.strip():
            current_sum += int(line)
        else:
            calories_sums.append(current_sum)
            current_sum = 0

    sorted_calories_sums = sorted(calories_sums, reverse=True)
    logger.info('Maximum calories: %d', sorted_calories_sums[0])
    logger.info('Top 3 calories: %r', sorted_calories_sums[:3])

