import argparse
import os


def get_args_parser():
    parser = argparse.ArgumentParser(description='Web scrapper',
                                     prog='page-loader')

    parser.add_argument('url', type=str)
    parser.add_argument('-o',
                        '--output',
                        help='\n set output full-path',
                        default=os.getcwd(),
                        type=str)
    return parser
