from collections import namedtuple

import logging

logger = logging.getLogger(__name__)


class Folder:
    def __init__(self, parent=None):
        self.parent = parent

        self.files = dict()
        self.folders = dict()

    @property
    def total_size(self):
        files_size = sum(self.files.values())
        folders_size = sum(d.total_size for d in self.folders.values())
        #logger.debug("Files: %r, Folders: %r", files_size, folders_size)
        return files_size + folders_size

    def add_file(self, name, size):
        self.files[name] = size

    def add_folder(self, name):
        self.folders[name] = Folder(parent=self)

    def walk_sizes(self):
        for folder in self.folders.values():
            yield from folder.walk_sizes()

        yield self.total_size


def parse_shell_output(data):
    root = Folder()
    cwd = root
    running_ls = False

    for line in data.splitlines():
        if not line.strip(): continue

        if line.startswith('$'):
            command, *args = line[2:].split()
            running_ls = command == 'ls'

            if command == 'cd':
                if args[0] == '/':
                    cwd = root
                elif args[0] == '..':
                    cwd = cwd.parent
                else:
                    subfolder = cwd.folders.get(args[0])
                    if not subfolder:
                        logger.warning("Tried to enter a folder that doesnt exist: %r" , args)
                    else:
                        cwd = subfolder

        elif running_ls:
            size, name = line.split()
            if size == 'dir':
                cwd.add_folder(name)
            else:
                size = int(size)
                cwd.add_file(name, size)


    return root


def main(data):
    sum = 0
    root = parse_shell_output(data)

    for w in root.walk_sizes():
        if w < 100000:
            sum += w
            logger.debug("Folder size: %d", w)

    logger.info("Total size of folders < 100000: %d", sum)

def main_2(data):
    sum = 0
    root = parse_shell_output(data)
    total_used_space = root.total_size
    logger.debug("Size of root folder: %d", total_used_space)

    free_space = 70000000 - total_used_space
    logger.debug("Current free space: %d", free_space)

    required_extra_space = 30000000 - free_space
    logger.debug("Required extra space: %d", required_extra_space)

    candidates_for_removal = [
            w
            for w in root.walk_sizes()
            if w >= required_extra_space
    ]

    logger.debug("All candidates: %r", candidates_for_removal)
    smallest_candidate = min(candidates_for_removal)
    logger.info("The smallest folder that can be removed for the update to work is %d in size total", smallest_candidate)



