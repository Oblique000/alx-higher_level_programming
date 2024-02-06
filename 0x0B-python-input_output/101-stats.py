#!/usr/bin/python3
import sys
from collections import defaultdict

def process_log_line(line, metrics):
    """Process a log line and update metrics."""
    try:
        _, _, _, status_code, file_size = line.split(" ")[-5:]
        status_code = int(status_code)
        file_size = int(file_size)

        metrics['total_size'] += file_size
        metrics['status_counts'][status_code] += 1

    except ValueError:
        pass  # Ignore lines that don't match the expected format

def print_statistics(metrics):
    """Print the computed statistics."""
    print(f"Total file size: {metrics['total_size']}")
    
    for status_code in sorted(metrics['status_counts']):
        count = metrics['status_counts'][status_code]
        print(f"{status_code}: {count}")

def main():
    metrics = {'total_size': 0, 'status_counts': defaultdict(int)}
    line_count = 0

    try:
        for line in sys.stdin:
            process_log_line(line.strip(), metrics)
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(metrics)

    except KeyboardInterrupt:
        print_statistics(metrics)

if __name__ == "__main__":
    main()
