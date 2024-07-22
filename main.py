import tweepy
import json
import os
import requests

#Constants. Add your credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
BEARER_TOKEN= ""
INSTAGRAM_TOKEN = ' '
INSTAGRAM_ID = ''

"To run script automatically at regular intervalls: use CRON on Linux "

# Generates text for twitter/instagram
#Eden AI API headers and endpoint

EDENAI_HEADERS = {"Authorization": f"Bearer {BEARER_TOKEN}"}
TEXT_GEN_URL = "https://api.edenai.run/v2/text/generation"
IMAGE_GEN_URL = "https://api.edenai.run/v2/image/generation"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_text():
    payload = {
        #choose your chatbot
        "providers": "openai, cohere",
        #request for chatabot
        "text": "generate short,funny story for my twitter post ",
        "temperature": 0.2,
        "max_tokens": 250,

    }
    response = requests.post(TEXT_GEN_URL, json=payload, headers=EDENAI_HEADERS)
    result = json.loads(response.text)
    text = result['cohere']['generated_text']
    print(text)
    return text


def generate_image():
    payload = {
        "providers": ["replicate"],
        "text": "generate post for instagram",
        "resolution": "512x512",
    }
    response = requests.post(IMAGE_GEN_URL, json=payload, headers=EDENAI_HEADERS)
    result = response.json()
    image_url = result['replicate']['items'][0]['image_resource_url']

    # Download the image
    image_response = requests.get(image_url)
    image_path = 'generated_image.png'
    with open(image_path, 'wb') as image_file:
        image_file.write(image_response.content)

    return image_path, image_url




def post_to_instagram(image_url, caption):
    url = f'https://graph.facebook.com/v15.0/{INSTAGRAM_ID}/media'
    params = {
        'access_token': INSTAGRAM_TOKEN,
        'caption': caption,
        'image_url': image_url
    }
    response = requests.post(url, params=params)
    return response.json()



def post_to_twitter(text):
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    client.create_tweet(text=text)
def instagram_menu():
    clear_screen()
    print("Instagram Menu")
    print("1. Post on Instagram")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        #Replace the following with your Instagram credentials
        caption = generate_text()
        image_url = generate_image()
        response = post_to_instagram(image_url, caption)
        print("Posted on Instagram successfully!")
        print(response)
    elif choice == '2':
        print("Exiting Instagram Menu...")
    else:
        print("Invalid choice. Please try again.")
        instagram_menu()


def twitter_menu():
    clear_screen()
    print("Twitter Menu")
    print("1. Post on Twitter")
    print("2. Post on Twitter with Media")
    print("3. Exit")
    choice = input("Enter your choice: ")



    if choice == '1':
        text = generate_text()
        post_to_twitter(text)
        print("Posted on Twitter successfully!")
    elif choice == '2':
        print("Exiting Twitter Menu...")
    else:
        print("Invalid choice. Please try again.")
        twitter_menu()


def main_menu():
    clear_screen()
    print("Main Menu")
    print("1. Instagram")
    print("2. Twitter")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        instagram_menu()
    elif choice == '2':
        twitter_menu()
    elif choice == '3':
        print("Exiting the program...")
    else:
        print("Invalid choice. Please try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()
