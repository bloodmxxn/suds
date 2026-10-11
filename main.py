import sys
from src.url_analyzer import analyze_url


def main():
  if len(sys.argv) < 2:
    print("Usage: python main.py <URL>")
    sys.exit(1)

  try:
    result = analyze_url(sys.argv[1])
  except ValueError as err:
    print(f"Error: {err}")
    sys.exit(1)

  print(result)


if __name__ == "__main__":
  main()
