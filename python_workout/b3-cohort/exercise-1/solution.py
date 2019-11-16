import csv
import json
import pickle
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
            fieldnames = ["title", "author", "price"]
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
        # with open(file_path, "w") as xmlfile:
        tree = ElementTree()
        book_element = ET.Element("book")
        title_element = ET.SubElement(book_element, "title")
        author_element = ET.SubElement(book_element, "author")
        price_element = ET.SubElement(book_element, "price")

        title_element.text = self.title
        author_element.text = self.author
        price_element.text = str(self.price)

        book_element.write(file_path)


    def load(self, file_path):
        # with open(file_path, "r") as xmlfile:
        import pdb; pdb.set_trace()
        tree = ET.parse(file_path)
        root = tree.getroot()
        for child in root:
            print(child.tag, child.attrib)

