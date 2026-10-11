import sys
from src.url_parser import parse_url


def main():
  if len(sys.argv) < 2:
    print("Usage: python main.py <URL>")
    sys.exit(1)

  try:
    url = parse_url(sys.argv[1])
  except ValueError as err:
    print(f"Error: {err}")

  print(url)


if __name__ == "__main__":
  main()
