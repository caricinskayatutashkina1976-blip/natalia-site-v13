#!/usr/bin/env python3
"""Local-only static server. No installation, build, upload or deployment."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Run the Natalia static website locally")
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent / "dist"
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print("Open http://127.0.0.1:%s/" % args.port, flush=True)
        print("Press Ctrl+C to stop. Nothing will be published.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
