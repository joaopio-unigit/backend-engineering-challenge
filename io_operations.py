import json

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
    else:
        print("Please provide a JSON file.")

def write_output_file(moving_averages):
    for average in moving_averages:
        print('{"date": "' + average.timestamp.strftime('%Y-%m-%d %H:%M:%S') + '", "average_delivery_time": ' + str(average.average) + '}')