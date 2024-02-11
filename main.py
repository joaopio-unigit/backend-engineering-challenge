import sys
from io_operations import read_input_file, write_output_file
from processing_operations import calculate_moving_averages

def main(input_file_path, window_size):
    events_data = read_input_file(input_file_path)
    moving_averages = calculate_moving_averages(events_data, window_size)
    write_output_file(moving_averages)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <input_file> <window_size>")
        sys.exit(1)

    input_file = sys.argv[1]
    window_size = sys.argv[2]

    main("events.json", int(window_size))
