import csv
import json
import pickle
from xml.etree.ElementTree import ElementTree, Element, SubElement
import xml.etree.ElementTree as ET


class Serializable:
    def dump(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(vars(self), f)


    def load(self, file_path):
        with open(file_path, "rb") as f:
            attrs = pickle.load(f)
            for attr, value in attrs.items():
                setattr(self, attr, value)


class JSONMixin:
    def dump(self, file_path):
        with open(file_path, "w") as jsonfile:
            json.dump(vars(self), jsonfile)


    def load(self, file_path):
        with open(file_path, "r") as jsonfile:
            attrs = json.load(jsonfile)
            for attr, value in attrs.items():
                setattr(self, attr, value)


class CSVMixin:
    def dump(self, file_path):
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = vars(self).keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(vars(self))


    def load(self, file_path):
        with open(file_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            attrs = next(reader)

            for attr, value in attrs.items():
                setattr(self, attr, value)


class XMLMixin:
    def dump(self, file_path):
        with open(file_path, "w") as xmlfile:
            root_element = Element("root")

            for attr, value in vars(self).items():
                sub_element = SubElement(root_element, attr)
                sub_element.text = str(value)
                root_element.append(sub_element)

            tree = ElementTree(root_element)

            tree.write(file_path)


    def load(self, file_path):
        with open(file_path, "r") as xmlfile:
            tree = ET.parse(xmlfile)
            root = tree.getroot()

            for child in iter(root):
                setattr(self, child.tag, child.text)
