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
      "url": url,
      "url_length": len(url),
      "protocol": parsed.scheme,
      "port": parsed.port,
      "username": parsed.username,
      "password": parsed.password,
      "hostname": parsed.hostname,
      "hostname_length": len(parsed.hostname or ""),
      "subdomain": extracted_tld.subdomain,
      "subdomain_count": len(extracted_tld.subdomain.split(".")) if extracted_tld.subdomain else 0,
      "domain": extracted_tld.domain,
      "registered_domain": f"{extracted_tld.domain}.{extracted_tld.suffix}" if extracted_tld.domain and extracted_tld.suffix else extracted_tld.domain,
      "suffix": extracted_tld.suffix,
      "ipv4": extracted_tld.ipv4,
      "ipv6": extracted_tld.ipv6,
      "netloc": parsed.netloc,
      "path": unquote(parsed.path),
      "path_depth": len([part for part in parsed.path.split("/") if part]),
      "query": parse_qs(parsed.query),
      "query_count": len(parsed.query.split("&")) if parsed.query else 0,
      "fragment": parsed.fragment,
      "has_ip": bool(extracted_tld.ipv4 or extracted_tld.ipv6),
      "has_port": parsed.port is not None,
      "has_credentials": bool(parsed.username or parsed.password)
  }

  return url_data
