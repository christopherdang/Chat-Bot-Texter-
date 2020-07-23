# Import modules

import xmltodict, json, glob, xml.etree.ElementTree as ET, gzip
from zipfile import ZipFile

# List of file types

file_type = ["xml", "gz", "zip", "xmltv"]

for type in file_type:
    if type == "xml":
        for f in glob.glob("Files/*.{}".format(type)):
            tree = ET.parse(f)
            root = tree.getroot()
            data = xmltodict.parse(ET.tostring(root))
            with open(f.replace(type, "json"), "w", encoding="utf-8") as out_file:
                json.dump(data, out_file, ensure_ascii=False)