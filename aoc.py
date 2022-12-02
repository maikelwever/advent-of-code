#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from timeit import Timer

import logging


def main():
    parser = ArgumentParser()

    parser.add_argument('-y', '--year', type=int, default=2022, help='Yearly folder to use')
    parser.add_argument('-b', '--bench', '--benchmark', action='store_true', help='Run the function 10000 times as a benchmark.')
    parser.add_argument('-q', '--quick', '--quick-bench', '--quick-benchmark', action='store_true', help='Run the function 100 times as a benchmark.')
    parser.add_argument('-d', '-v', '--debug', '--verbose', action='store_true', help='Set logging level to DEBUG')
    parser.add_argument('-t', '--two', '--main-two', action='store_true', help='Run main_2 instead of main function')
    parser.add_argument('day', type=int, help='Index of the advent to look up.')

    args = parser.parse_args()

    import_statement = f'year_{args.year}.day_{args.day}'
    day_module = __import__(import_statement, globals(), locals(), [None], 0)

    asset_path = Path(f'year_{args.year}') / 'assets' / f'day_{args.day}.txt'
    with open(asset_path) as f:
        asset_contents = f.read()

    if args.two:
        def func():
            day_module.main_2(asset_contents)
    else:
        def func():
            day_module.main(asset_contents)

    if args.bench or args.quick:
        logging.basicConfig(level=logging.WARN)

        timer = Timer(func)

        repeat = 100 if args.quick else 10000
        result = timer.timeit(number=repeat)
        print(f'Benchmark result: {result} for {repeat} runs.')

    else:
        if args.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

        func()


if __name__ == "__main__":
    main()

