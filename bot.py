# Description: A simple bot that checks the availability of products (GPUS) on BestBuy.ca
import requests
from bs4 import BeautifulSoup
import time

# URLs for the products
GPU1 = "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-4090-24gb-gddr6-video-card/16531651"
GPU2 = "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-4080-super-16gb-gddr6x-video-card-only-at-best-buy/17664910"
GPU3 = "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-4070-super-12gb-gddr6x-video-card-only-at-best-buy/17664911"

# List of products to check
PRODUCTS = [
    # Tuple of product name and URL
    ("NVIDIA GeForce RTX 4090 24GB", GPU1),
    ("NVIDIA GeForce RTX 4080 Super 16GB", GPU2),
    ("NVIDIA GeForce RTX 4070 Super 12GB", GPU3)
]


# Function to check the availability of the product
def check_availability(url: str) -> bool:
    # Headers for the GET request
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "*/*"
    }
    # Send a GET request to the URL
    page = requests.get(url, headers=HEADERS)

    # Parse the HTML content
    soup = BeautifulSoup(page.content, "html.parser")

    # Find the availability class in the span element of the HTML content
    availability = soup.find(
        "span", {"class": "availabilityMessage_3ZSBM container_1DAvI"})

    # Check if the product is available
    return availability and "Available to ship" in availability.text


# Main function to check the availability of the products
def main() -> None:
    for product, url in PRODUCTS:
        if check_availability(url):
            print(f"{product} is available! click the link to purchase: " + url)
        else:
            print(f"{product} is not available.")


# Run the bot with a check every hour
if __name__ == "__main__":
    counter = 1  # Counter for checks
    seconds = 60 * 60  # 1 hour
    while True:
        print(f"Checking for availability, attempt #{counter}")
        main()
        counter += 1
        time.sleep(seconds)
        print("\n")
