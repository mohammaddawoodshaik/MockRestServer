import sys
import logging
import logging.config
from os import path
from mockrestserver.interpreter.loader import Loader
from mockrestserver.service.service import Service


class Context(object):

    def __init__(self, file_path):
        self.loader = Loader(file_path)
        self.data = self.loader.get_data()

    def app_ctx(self):
        return self.data.get("context")

    def endpoints(self):
        return self.data.get("endpoints")


def _initialize_logging():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'conf/logger.ini')
    logging.config.fileConfig(fname=log_file_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        raise ValueError("Need to provide file path!")
    file_path = args[1]
    _initialize_logging()
    context = Context(file_path)
    serv = Service(context)
    serv.run()