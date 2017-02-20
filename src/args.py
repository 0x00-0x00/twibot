import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help="Help command for subparser.")

    post = subparser.add_parser("post", help="Status to post.")
    post.add_argument("-m", "--message", help="Message to post", required=True)

    return parser.parse_args()

