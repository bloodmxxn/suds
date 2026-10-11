import sys
from src.url_parser import parse_url
from src.url_score import get_score


def main():
  if len(sys.argv) < 2:
    print("Usage: python main.py <URL>")
    sys.exit(1)

  try:
    result = parse_url(sys.argv[1])
  except ValueError as err:
    print(f"Error: {err}")
    sys.exit(1)

  print(result)


if __name__ == "__main__":
  main()
