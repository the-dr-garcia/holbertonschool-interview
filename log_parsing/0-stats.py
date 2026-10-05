#!/usr/bin/python3
"""Reads stdin line by line and computes log metrics."""
import sys

CODES = [200, 301, 400, 401, 403, 404, 405, 500]


def print_stats(size, counts):
    """Prints total file size and line counts per status code."""
    print("File size: {}".format(size))
    for code in sorted(counts):
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))


if __name__ == "__main__":
    total_size = 0
    counts = {code: 0 for code in CODES}
    lines = 0

    try:
        for line in sys.stdin:
            sys.stderr.write("RAW: {!r}\n".format(line))
            parts = line.split()
            try:
                code = int(parts[-2])
                size = int(parts[-1])
            except (IndexError, ValueError):
                continue
            total_size += size
            if code in counts:
                counts[code] += 1
            lines += 1
            if lines % 10 == 0:
                print_stats(total_size, counts)
        if lines == 0 or lines % 10 != 0:
            print_stats(total_size, counts)
    except KeyboardInterrupt:
        print_stats(total_size, counts)
        raise
