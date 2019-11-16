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
    fieldnames = ["title", "author", "price"]

    def dump(self, file_path):
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSVMixin.fieldnames)
            writer.writerow(vars(self))


    def load(self, file_path):
        with open(file_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=CSVMixin.fieldnames)
            attrs = next(reader)
            for attr, value in attrs.items():
                setattr(self, attr, value)


class XMLMixin:
    def dump(self, file_path):
        with open(file_path, "w") as xmlfile:
            book_element = Element("book")

            title_element = SubElement(book_element, "title")
            author_element = SubElement(book_element, "author")
            price_element = SubElement(book_element, "price")
            title_element.text = self.title
            author_element.text = self.author
            price_element.text = str(self.price)

            book_element.append(title_element)
            book_element.append(author_element)
            book_element.append(price_element)

            tree = ElementTree(book_element)

            tree.write(file_path)


    def load(self, file_path):
        with open(file_path, "r") as xmlfile:
            tree = ET.parse(xmlfile)
            root = tree.getroot()

            for child in iter(root):
                setattr(self, child.tag, child.text)
