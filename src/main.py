import cli

from application import SPPApi
from config import Config
from routing import DictRouteBuilder

import os


if __name__ == "__main__":
    # Create parser and get user args
    args = cli.create_parser() \
              .parse_args()

    # Load application configuration
    config = Config().load(args.configuration)

    # Start the application
    SPPApi(config, DictRouteBuilder(config.routes)).run()
