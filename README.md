# Unbabel Backend Engineering Challenge

This repository is a fork of the [Unbabel Backend Engineering Challenge](https://github.com/Unbabel/backend-engineering-challenge), which presents a coding challenge for individuals participating in their recruitment process. 

The challenge involves building a command-line application to parse a stream of events related to translation data, calculating a moving average of the translation delivery time for specified time windows. 

For more detailed information about the challenge scenario, objectives, input/output formats, and evaluation criteria, please refer to the [original repository](https://github.com/Unbabel/backend-engineering-challenge).

## Description

This repository contains my solution for the [Unbabel Backend Engineering Challenge](https://github.com/Unbabel/backend-engineering-challenge) which involved building a command-line application to parse a stream of events related to translation data and calculating a moving average of the translation delivery time for specified time windows.

For more detailed information about the challenge scenario, objectives, input/output formats, and evaluation criteria, please refer to the [original repository](https://github.com/Unbabel/backend-engineering-challenge).

## Get Started

To get started with running and testing my solution you need to download or clone my repository and have Python installed in your machine.

## Usage

To run this application, you can run the command `python main.py <events_file.json> <window_size>` and replacing `<events_file.json>` with the path to a valid JSON file containing a list of events related to translation data, and `<window_size>` with an integer representing the desired time window size for calculating the moving average.

### Example:

	python main.py io_files/events.json 10

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
			"timestamp": "2018-12-26 18:11:00",
			"average": 0
		},
		{
			"timestamp": "2018-12-26 18:12:00",
			"average": 20.0
		},
		{
			"timestamp": "2018-12-26 18:13:00",
			"average": 20.0
		},
		{
			"timestamp": "2018-12-26 18:14:00",
			"average": 20.0
		},
		{
			"timestamp": "2018-12-26 18:15:00",
			"average": 20.0
		},
		{
			"timestamp": "2018-12-26 18:16:00",
			"average": 25.5
		}
	]