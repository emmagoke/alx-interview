#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""
import sys


def print_data(file_size: int, status_code: dict) -> None:
    """
    This is an helper function that prints the file size and status codes
    """
    print(f"File size: {file_size}")
    for key in sorted(status_code.keys()):
        print(f"{key}: {status_code[key]}")


def stat() -> None:
    """
    This function handles the Log Parsing
    """

    # stdin = sys.stdin.read()
    count = 0
    total_size = 0
    status_code = {}
    try:
        # stdin = input()
        for line in sys.stdin:
            # while stdin:
            # print(len(stdin.split()))
            l_stdin = line.split()
            # l_stdin = stdin.split()
            count += 1
            try:
                total_size += int(l_stdin[-1])
                if l_stdin[-2] in status_code:
                    status_code[l_stdin[-2]] += 1
                else:
                    status_code[l_stdin[-2]] = 1
            except BaseException:
                pass

            if count % 10 == 0:
                print_data(total_size, status_code)

            # stdin = input()
    except KeyboardInterrupt:
        print_data(total_size, status_code)


if __name__ == '__main__':
    stat()
