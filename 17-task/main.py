import argparse
import json
import requests
import logging

def get_user_ids(url, destination, verbose=False):
    if verbose:
        logging.basicConfig(level=logging.INFO)

    try:
        response = requests.get(url)

        if verbose:
            logging.info(f"Response from {url}: {response.status_code}")

        if response.status_code == 200:
            data = response.json()

            user_ids = {f"User {entry['userId']}": str(entry['userId']) for entry in data}

            with open(destination, 'w') as file:
                json.dump(user_ids, file, indent=2)

            if verbose:
                logging.info(f"User ids successfully written to {destination}")
        else:
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get user ids from a specified URL and write them to a file.")
    parser.add_argument("url", help="URL of the web site")
    parser.add_argument("destination", help="Destination file for writing user ids")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    get_user_ids(args.url, args.destination, args.verbose)
