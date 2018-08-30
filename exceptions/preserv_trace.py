#!/usr/bin/env python

import sys
import traceback


def throws():
    raise RuntimeError('error from throws')


def cleanup():
    raise RuntimeError('error from cleanup')


def nested():
    try:
        throws()
    except Exception as e:
        try:
            cleanup()
        except Exception as e1:
            raise e1 from e


def main():
    try:
        nested()
        return 0
    except Exception as err:
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
