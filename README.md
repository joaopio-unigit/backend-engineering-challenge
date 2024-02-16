# Unbabel Backend Engineering Challenge

This repository is a fork of the [Unbabel Backend Engineering Challenge](https://github.com/Unbabel/backend-engineering-challenge), which presents a coding challenge for individuals participating in their recruitment process. 

The challenge involves building a command-line application to parse a stream of events related to translation data, calculating a moving average of the translation delivery time for specified time windows. 

For more detailed information about the challenge scenario, objectives, input/output formats, and evaluation criteria, please refer to the [original repository](https://github.com/Unbabel/backend-engineering-challenge).

## Description

This repository contains my solution for the [Unbabel Backend Engineering Challenge](https://github.com/Unbabel/backend-engineering-challenge) which involved building a command-line application to parse a stream of events related to translation data and calculating a moving average of the translation delivery time for specified time windows.

For more detailed information about the challenge scenario, objectives, input/output formats, and evaluation criteria, please refer to the [original repository](https://github.com/Unbabel/backend-engineering-challenge).

## Get Started

To get started with running my solution, you `need to have Python, pip and pipenv installed` in your machine. After installing these you can follow these steps:

### 1. Clone the Repository

Clone the repository to your machine using Git:
```bash
git clone https://github.com/joaopio-unigit/backend-engineering-challenge.git
```

Navigate to the project directory:
```bash
cd backend-engineering-challenge
```

### 2. Install Dependencies

When inside the project directory, run the following command to install the project dependencies:
```bash
pipenv install
```

Then activate the project virtual environment with the following command:
```bash
pipenv shell
```

## Usage

To run this application, you can run the command `unbabel_moving_averages --input_file <events_file.json> --window_size <window_size>` and replacing `<events_file.json>` with the path to a valid JSON file containing a list of events related to translation data, and `<window_size>` with an integer representing the desired time window size for calculating the moving average.

### Example:

	unbabel_moving_averages --input_file io_files/events.json --window_size 10

The JSON input file should have a list of the translation events data like the ones at the directory `io_files` and the one below:

	[
		{
			"timestamp": "2018-12-26 18:11:08.509654",
			"translation_id": "5aa5b2f39f7254a75aa5",
			"source_language": "en",
			"target_language": "fr",
			"client_name": "airliberty",
			"event_name": "translation_delivered",
			"nr_words": 30,
			"duration": 20
		},
		{
			"timestamp": "2018-12-26 18:15:19.903159",
			"translation_id": "5aa5b2f39f7254a75aa4",
			"source_language": "en",
			"target_language": "fr",
			"client_name": "airliberty",
			"event_name": "translation_delivered",
			"nr_words": 30,
			"duration": 31
		}
	]

At the end of the execution, the program will output a JSON file to the directory `io_files` with the name `moving_averages.json`. This files will have a list moving averages corresponding to the events in the JSON file and window size input.

You can expect the `moving_averages.json`to have the format below:

	[
		{
			"date": "2018-12-26 18:11:00",
			"average_delivery_time": 0
		},
		{
			"date": "2018-12-26 18:12:00",
			"average_delivery_time": 20.0
		},
		{
			"date": "2018-12-26 18:13:00",
			"average_delivery_time": 20.0
		},
		{
			"date": "2018-12-26 18:14:00",
			"average_delivery_time": 20.0
		},
		{
			"date": "2018-12-26 18:15:00",
			"average_delivery_time": 20.0
		},
		{
			"date": "2018-12-26 18:16:00",
			"average_delivery_time": 25.5
		}
	]