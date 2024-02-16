import json

from ..encoders.json_enconders import MovingAverageEncoder

def is_json_file(file_path):
    """
    Check if a given file path points to a JSON file.

    Parameters:
    file_path (string): file path to check.

    Returns:
    bool: True if file_path points to a JSON file, False otherwise.
    """

    return file_path.endswith('json')

def read_input_file(file_path):
    """
    Read the contents from a JSON file.
    This function receives a file_path, checks if it points to a JSON
    file and if so reads its contents.

    Parameters:
    file_paht (string): path of the JSON file to read the content from.

    Returns:
    list: If the provided file path is valid and points to a JSON file, returns its content.
    """

    # File Path Validation
    # ================ 
    if is_json_file(file_path):
        try:

            # File Content Reading
            # ================ 
            with open(file_path, 'r') as file:
                input_data = json.load(file)

            return input_data
        
    # Error Processing
    # ================     
        except FileNotFoundError:
            print("File not found!")
            return
    else:
        print("Please provide a JSON file.")
        return

def write_output_file(moving_averages):
    """
    Produce a JSON file at /io_files with the moving averages calculated
    by the program.

    Parameters:
    moving_averages (list): The list of MovingAverage's produced by the program.

    Returns:
    This function has no return but it does produce a JSON file at /io_files with
    the moving averages calculated by the program.
    """
    
    with open("io_files/moving_averages.json", "w") as json_file:
        json.dump(moving_averages, json_file, cls=MovingAverageEncoder)