from datetime import datetime
import xml.etree.ElementTree as ET

# Generate version string
now = datetime.now()
version_string = now.strftime("%d.%m.%Y-Build%H%M%S")

# Create the file structure
root = ET.Element("root")
version = ET.SubElement(root, "version")
version.text = version_string

# Create a new XML file with the results
tree = ET.ElementTree(root)
with open("MetaData.xml", "wb") as files:
    tree.write(files, encoding='utf-8', xml_declaration=True)
