from dotenv import load_dotenv
import os

load_dotenv()

key: str = os.environ.get("RAPID_KEY")
url: str = os.environ.get("RAPID_HOST")

headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": url}
