import pathlib
import os
import logging
from mockrestserver.utils import load_json

logger = logging.getLogger("interpreter")

class Loader:
    FILE_FORMAT_MAPPER = {
        (".json"): load_json
    }

    def __init__(self, path):
        self.path = path
        self.data = self._load()

    def _load(self):
        """
        This method will figure out which interpreter to use for the given file type.
        :return:
        """
        logger.info("Loading the data from the file: %s" % self.path)
        if not os.path.exists(self.path):
            raise FileNotFoundError("Invalid file path provided - {}".format(self.path))
        suffix = pathlib.Path(self.path).suffix
        for formats in self.FILE_FORMAT_MAPPER:
            if suffix.lower() in formats:
                with open(self.path, "r") as f:
                    return self.FILE_FORMAT_MAPPER[formats](f.read())

    def get_data(self):
        return self.data
