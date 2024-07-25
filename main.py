import os
import shutil
import xml.etree.ElementTree as ET

def check_xml_name(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall('object'):
        name = obj.find('name')
        if name is not None and name.text.strip():
            return True
    return False