# ---------------------
# | It's Temporary :) |
# ---------------------


from src.url_parser import parse_url


def analyze_url(url: str):
  url_data = parse_url(url)

  analysis = {
      "long_url": url_data["url_length"] > 100,
      "long_hostname": url_data["hostname_length"] > 50,
      "many_subdomains": url_data["subdomain_count"] > 3,
      "uses_ip": url_data["has_ip"],
      "has_credentials": url_data["has_credentials"],
      "many_query_params": url_data["query_count"] > 5,
      "deep_path": url_data["path_depth"] > 4,
      "missing_suffix": (
          not url_data["suffix"] and not url_data["has_ip"]
      )
  }

  return {
      "url_data": url_data,
      "analysis": analysis
  }
