import logging

from copy import copy


logger = logging.getLogger(__name__)


def search_packet(stream, header_len=4):
    buffer = ''
    counter = 0

    while len(stream) > 0:
        buffer += stream[0]
        stream = stream[1:]
        counter += 1

        if len(buffer) > header_len:
            buffer = buffer[1:]

            if len(set(buffer)) == len(buffer):
                logger.info(
                    "Current buffer contains %d different characters: %s. Marker position: %d.",
                    header_len, buffer, counter
                )
                return


def main(data):
    for stream in data.splitlines():
        search_packet(stream)


def main_2(data):
    for stream in data.splitlines():
        search_packet(stream, header_len=14)

