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

def move_labeled_images(source_folder, destination_folder, unlabeled_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith((".png", ".jpg")):
                image_path = os.path.join(root, file)
                xml_path = os.path.join(root, file.rsplit(".", 1)[0] + ".xml")

                if os.path.exists(xml_path):
                    if check_xml_name(xml_path):
                        # Eğer XML dosyası varsa ve name etiketi doluysa, resmi ve etiket dosyasını hedef klasöre taşı
                        destination_image_path = os.path.join(destination_folder, file)
                        destination_xml_path = os.path.join(destination_folder, file.rsplit(".", 1)[0] + ".xml")

                        shutil.move(image_path, destination_image_path)
                        shutil.move(xml_path, destination_xml_path)

                        print(f"{file} adlı resim ve etiket dosyası etiketli klasöre taşındı.")
                    else:
                        # Eğer XML dosyası var ama name etiketi boşsa, resmi ve XML'i etiketsiz klasöre taşı
                        unlabeled_image_path = os.path.join(unlabeled_folder, file)
                        unlabeled_xml_path = os.path.join(unlabeled_folder, file.rsplit(".", 1)[0] + ".xml")

                        shutil.move(image_path, unlabeled_image_path)
                        shutil.move(xml_path, unlabeled_xml_path)

                        print(f"{file} adlı resim ve etiket dosyası etiketsiz klasöre taşındı.")
                else:
                    print(f"{file} adlı resmin etiket dosyası bulunamadı.")