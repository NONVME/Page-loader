import argparse
import os

from page_loader.engine import download


def get_args_parser():
    parser = argparse.ArgumentParser(
        description='Web scrapper',
        prog='page-loader',
    )
    parser.add_argument('url', type=str)
    parser.add_argument('-o',
                        '--output',
                        help='\n set output full-path',
                        default=os.getcwd(),
                        type=str,
                        )
    return parser


def main():
    """Select format selection."""
    args = get_args_parser().parse_args()
    print(download(args.url, args.output))


if __name__ == '__main__':
    main()
