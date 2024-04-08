import requests
import json

def get_random_dog_image():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['message']
    else:
        print('Failed to fetch random dog image')
        return None

def main():
    print("Fetching random dog image...")
    random_dog_image = get_random_dog_image()
    if random_dog_image:
        print("Random dog image URL:", random_dog_image)
        # Дополнительный код для обработки изображения, если нужно

if __name__ == "__main__":
    main()







