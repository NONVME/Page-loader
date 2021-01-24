import logging
import sys

from page_loader.args import get_args_parser
from page_loader.engine import download


logger = logging.getLogger('base_error')


def main():
    """Select format selection."""
    args = get_args_parser().parse_args()
    try:
        print(download(args.url, args.output))
    except Exception:
        logger.exception("Exception occurred")
        sys.exit(1)


if __name__ == '__main__':
    main()
