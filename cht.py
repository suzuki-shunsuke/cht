#!/usr/bin/env python

import argparse
import json
import os
import select
import sys
import urllib


VERSION = "1.2.1"


def is_pipe():
    return select.select([sys.stdin], [], [], 0.0)[0]


def get_args():
    parser = argparse.ArgumentParser(
        description="Notify to slack when the previous command ends",
        prog="cht")
    parser.add_argument(
        "return_code", type=int, help="the previous command's return code",
        nargs="?", default=None)
    parser.add_argument(
        "-c", "--channel", default=os.environ.get("CHT_CHANNEL", None),
        help=("incoming webhook channel. If this option is not specified, "
              "the environment variable 'CHT_CHANNEL' is used."))
    parser.add_argument(
        "-u", "--url", default=os.environ.get("CHT_URL", None),
        help=("incoming webhook url. If this option is not specified, "
              "the environment variable 'CHT_URL' is used."))
    parser.add_argument(
        "-m", "--message",
        help="incoming webhook text.")
    parser.add_argument("-v", "--version", action="version", version=VERSION)
    return parser.parse_args()


def validate_args(args):
    if args.url is None:
        sys.exit("[cht][error] url is required")


def make_params(args, stdin_str):
    params = {}
    if stdin_str is None:
        if args.return_code is None:
            params["text"] = (
                "previous command has ended"
                if args.message is None else args.message)
        else:
            if args.message is None:
                params["attachments"] = [{
                    "text": "failure" if args.return_code else "success",
                    "color": "danger" if args.return_code else "good",
                }]
            else:
                result = "failure" if args.return_code else "success"
                params["attachments"] = [{
                    "text": "[{}] {}".format(result, args.message),
                    "color": "danger" if args.return_code else "good",
                }]
    else:
        if stdin_str:
            if args.message is None:
                params["attachments"] = [{
                    "text": stdin_str
                }]
            else:
                params["attachments"] = [{
                    "pretext": args.message,
                    "text": stdin_str
                }]
        else:
            if args.message is None:
                params["text"] = "previous command has ended"
            else:
                params["text"] = args.message
    params["username"] = "cht"
    if args.channel:
        params["channel"] = args.channel
    return params


def execute(stdin_str):
    args = get_args()
    validate_args(args)
    return webhook(args.url, **make_params(args, stdin_str))


def main():
    stdin_str = sys.stdin.read() if is_pipe() else None
    try:
        execute(stdin_str)
    except Exception as e:
        sys.stderr.write("{}\n\n".format(str(e)))
        if stdin_str:
            print "Previous command output:\n"
            print stdin_str


def webhook(url, **kwargs):
    try:
        return urllib.urlopen(url, json.dumps(kwargs))
    except IOError:
        sys.exit("[cht][error] slack's incoming webhook is failure")


if __name__ == "__main__":
    main()
