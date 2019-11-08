import json
import pickle


class Serializable:
    def dump(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self.__dict__, f)


    def load(self, file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)


class JSONMixin:
    def dump(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.__dict__, f)


    def load(self, file_path):
        with open(file_path, "r") as f:
            return json.load(f)


class XMLMixin:
    pass


class CSVMixin:
    pass
