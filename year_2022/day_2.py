import logging

logger = logging.getLogger(__name__)


score_table = {
        ('A', 'X'): 4,  # Rock : Rock -> Draw
        ('A', 'Y'): 8,  # Rock : Paper -> Win
        ('A', 'Z'): 3,  # Rock : Scissors -> Lose

        ('B', 'X'): 1,  # Paper : Rock -> Lose
        ('B', 'Y'): 5,  # Paper : Paper -> Draw
        ('B', 'Z'): 9,  # Paper : Scissors -> Win

        ('C', 'X'): 7,  # Scissors: Rock -> Win
        ('C', 'Y'): 2,  # Scissors: Paper -> Lose
        ('C', 'Z'): 6,  # Scissors: Scissors -> Draw
}


outcome_table = {
        ('A', 'X'): 3,  # Rock : Lose -> Scissors
        ('A', 'Y'): 4,  # Rock : Draw -> Rock
        ('A', 'Z'): 8,  # Rock : Win -> Paper

        ('B', 'X'): 1,  # Paper : Lose -> Rock
        ('B', 'Y'): 5,  # Paper : Draw -> Paper
        ('B', 'Z'): 9,  # Paper : Win -> Scissors

        ('C', 'X'): 2,  # Scissors: Lose -> Paper
        ('C', 'Y'): 6,  # Scissors: Draw -> Scissors
        ('C', 'Z'): 7,  # Scissors: Win -> Rock
}

def score_func(asset, table):
    total_score = 0

    for line in asset.splitlines():
        results = tuple(line.split())
        total_score += table[results]

    logger.info("Total score: %d", total_score)


def main(asset):
    return score_func(asset, score_table)


def main_2(asset):
    return score_func(asset, outcome_table)

