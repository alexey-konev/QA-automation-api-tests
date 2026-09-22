from dotenv import load_dotenv
import os


load_dotenv()

username = os.getenv("TEST_USERNAME")
if not username:
    raise ValueError("TEST_USERNAME is not configured")

password = os.getenv("TEST_PASSWORD")
if not password:
    raise ValueError("TEST_PASSWORD is not configured")


ENVIRONMENTS = {
    "default": "https://www.saucedemo.com"
}