import validators
from urllib.parse import urlsplit, parse_qs, unquote


def parse_url(url: str):
  if validators.url(url) is not True:
    raise ValueError("Invalid URL")

  parsed = urlsplit(url)

  url_data = {
      "raw": url,
      "protocol": parsed.scheme,
      "port": parsed.port,
      "username": parsed.username,
      "password": parsed.password,
      "hostname": parsed.hostname,
      "netloc": parsed.netloc,
      "path": unquote(parsed.path),
      "query": parse_qs(parsed.query),
      "fragment": parsed.fragment
  }

  return url_data
