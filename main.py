import argparse

parser = argparse.ArgumentParser(description="A simple argparse example")
parser.add_argument("-n", "--name", type=str, help="Your name")

args = parser.parse_args()

if args.name:
    print(f"Hello, {args.name}")
else:
    print("Hello, world")


#run by typing: python main.py --name "John Smith"
