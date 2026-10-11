import validators
import tldextract
from urllib.parse import urlsplit, parse_qs, unquote


def parse_url(url: str):
  if not isinstance(url, str):
    raise ValueError("URL must be a string")

  if not url.strip():
    raise ValueError("URL cannot be empty")

  if validators.url(url) is not True:
    raise ValueError("Invalid URL")

  parsed = urlsplit(url)
  extracted_tld = tldextract.extract(url)

  url_data = {
      "raw": url,
      "protocol": parsed.scheme,
      "port": parsed.port,
      "username": parsed.username,
      "password": parsed.password,
      "hostname": parsed.hostname,
      "subdomain": extracted_tld.subdomain,
      "domain": extracted_tld.domain,
      "registered_domain": f"{extracted_tld.domain}.{extracted_tld.suffix}" if extracted_tld.domain and extracted_tld.suffix else extracted_tld.domain,
      "suffix": extracted_tld.suffix,
      "ipv4": extracted_tld.ipv4,
      "ipv6": extracted_tld.ipv6,
      "netloc": parsed.netloc,
      "path": unquote(parsed.path),
      "query": parse_qs(parsed.query),
      "fragment": parsed.fragment,
      "has_ip": bool(extracted_tld.ipv4 or extracted_tld.ipv6),
      "has_port": bool(parsed.port),
      "has_credentials": bool(parsed.username or parsed.password)
  }

  return url_data
