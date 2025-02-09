import os
import requests

def save_images(image_elements, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for lista in image_elements:
        for idx, img in enumerate(lista):
            try:
                img_url = img.get_attribute("src")
            except Exception as e:
                print("Error getting image URL:", e)
                continue
            img_data = requests.get(img_url).content
            img_name = os.path.join(output_folder, f"image_{idx}.jpg")
            with open(img_name, "wb") as f:
                f.write(img_data)
            print(f"Saved: {img_name}")
