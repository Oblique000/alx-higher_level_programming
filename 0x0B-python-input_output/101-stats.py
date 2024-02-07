#!/usr/bin/env python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def process_line(line, size, status_codes, valid_codes):
    """Process a line and update metrics."""
    try:
        size += int(line[-1])
    except (IndexError, ValueError):
        pass

    try:
        code = line[-2]
        if code in valid_codes:
            status_codes[code] = status_codes.get(code, 0) + 1
    except IndexError:
        pass

    return size, status_codes

def main():
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()
            size, status_codes = process_line(line, size, status_codes, valid_codes)

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

if __name__ == "__main__":
    import sys
    main()
