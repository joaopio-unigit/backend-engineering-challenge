import json

from encoders.json_enconders import MovingAverageEncoder

def is_json_file(file_path):
    return file_path.endswith('json')

def read_input_file(file_path):
    if is_json_file(file_path):
        try:
            with open(file_path, 'r') as file:
                input_data = json.load(file)

            return input_data
        
        except FileNotFoundError:
            print("File not found!")
            return
    else:
        print("Please provide a JSON file.")
        return

def write_output_file(moving_averages):
    with open("io_files/moving_averages.json", "w") as json_file:
        json.dump(moving_averages, json_file, cls=MovingAverageEncoder)