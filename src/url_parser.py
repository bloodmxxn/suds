import validators
from urllib.parse import urlsplit


def parse_url(url: str):
  if not isinstance(url, str):
    raise ValueError("URL must be a string")

  if not url:
    raise ValueError("URL cannot be empty")

  result = validators.url(url)
  if result is not True:
    raise ValueError("Invalid URL")
  
  return urlsplit(url)
