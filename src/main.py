import cli
from config import Config
import application
import os

if __name__ == "__main__":
    # Create parser and get user args
    args = cli.create_parser() \
              .parse_args()
    print(os.getcwd())
    config = Config().load(args.configuration)

    ctx = application.ApplicationContext(config)
    app = application.SPPApi(ctx)

    app.run()
