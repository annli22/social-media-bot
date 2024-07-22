# Social Media Bot

This project is a Python script that generates and posts content to Twitter and Instagram automatically. The bot uses the Eden AI API to generate text and images, and Tweepy for Twitter interactions.

## Features

- **Text Generation**: Generates short, funny stories for Twitter and Instagram posts.
- **Image Generation**: Creates images for Instagram posts.
- **Posting to Instagram**: Automatically posts generated content to Instagram.
- **Posting to Twitter**: Automatically posts generated content to Twitter.

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- Twitter Developer Account
- Facebook Developer Account (for Instagram API)

## Installation



1. **Install the required packages**:
    ```sh
    pip install tweepy
    ```
 

2. **Set up your API keys and tokens**:
   Replace the placeholder values in the script with your actual API keys and tokens:
    - `BEARER_TOKEN`
    - `CONSUMER_KEY`
    - `CONSUMER_SECRET`
    - `ACCESS_TOKEN`
    - `ACCESS_TOKEN_SECRET`
    - `INSTAGRAM_TOKEN`
    - `INSTAGRAM_ID`

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Follow the on-screen menu**:
    - Choose `Instagram` or `Twitter`.
    - Post content directly from the script.

## File Structure
Pythonproject/

│
├── main.py                # Main script for running the bot       
├── README.md              # Project documentation
└── LICENSE                # License file (optional, if you add one)




## Main Components

### Text Generation

The text generation functionality uses the Eden AI API to generate short, funny stories for social media posts. It sends a request to the API and processes the response to extract the generated text.

### Image Generation

The image generation functionality uses the Eden AI API to create images suitable for Instagram posts. It downloads the generated image and saves it locally.

### Posting to Instagram

The script includes a function to post the generated content (text and image) to Instagram using the Facebook Graph API.

### Posting to Twitter

The script uses Tweepy to post the generated text to Twitter. It includes authentication handling and tweet creation.



## Acknowledgements

- [Eden AI](https://edenai.co) for their API services.
- [Tweepy](https://www.tweepy.org/) for the Twitter API wrapper.

