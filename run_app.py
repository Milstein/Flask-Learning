import os

from guestbook import app

if __name__ == '__main__':
    #python run_app.py -p 5001
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-H', '--host', default='127.0.0.1')
    parser.add_argument('-p', '--port', default=5000, type=int)
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=True)

    #app.debug = True
    #host = os.environ.get('IP', '0.0.0.0')
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host=host, port=port)