import requests
import os
import json

with open('data.json', 'r') as f:
    data = json.load(f)

if not os.path.exists('images'):
    os.makedirs('images')

# dl images
def download_images(num_images):
    url = 'https://thispersondoesnotexist.com/'
    for i in range(num_images):
        response = requests.get(url)
        if response.status_code == 200:
            image_name = data[i]["image"]
            image_path = os.path.join('images', image_name)
            with open(image_path, 'wb') as f:
                f.write(response.content)
                print(f"Image {i+1}/{num_images} téléchargée : {image_name}")
        else:
            print(f"Échec du téléchargement de l'image {i+1}.")

num_images = len(data)

download_images(num_images)
