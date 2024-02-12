import sys
from io_operations.io_operations import read_input_file, write_output_file
from process_operations.moving_average_operations import calculate_moving_averages

def main(input_file_path, window_size):
    """
    This is the main function of the program.
    This function is responsible for calling other functions and
    providing these or get from these the data it needs at each
    point of execution of the program.

    Parameters:
    input_file_path (string): Path to the JSON file with the translation events data.
    window_size (int): Size of the event window the program has to monitor and produce averages.

    Returns:
    This function does not have a return object but it does produce 
    a JSON file at /io_files with the calculated averages.
    """

    # Input Processing
    # ================    
    events_data = read_input_file(input_file_path)
    
    if(events_data):

        # Moving Averages Processing
        # ==========================
        moving_averages = calculate_moving_averages(events_data, window_size)

        # Output Processing
        # =================
        write_output_file(moving_averages)

    else:

        # Input Error Processing
        # ======================
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <input_file> <window_size>")
        sys.exit(1)

    input_file = sys.argv[1]
    window_size = sys.argv[2]

    main(input_file, int(window_size))
