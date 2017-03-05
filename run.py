import argparse

from echobot import app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--production', dest='debug', action='store_false')
    parser.add_argument('--debug', dest='debug', action='store_false')
    parser.set_defaults(debug=True)
    parser.add_argument('--port', default='5000', type=int)

    args = parser.parse_args()

    app.run(debug=args.debug, port=args.port)
