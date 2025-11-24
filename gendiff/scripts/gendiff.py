"""Command line interface for gendiff."""

import argparse
from gendiff import generate_diff


def main():
    """Run the gendiff command line interface."""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        choices=["stylish", "plain", "json"],
        default="stylish",
    )

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == "__main__":
    main()
