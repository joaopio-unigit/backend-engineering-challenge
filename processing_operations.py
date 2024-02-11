from datetime import datetime, timedelta
from window_translation_event import WindowTranslationEvent
from moving_average import MovingAverage

def get_event_timestamp(translation_events, event_index):
    return datetime.strptime(translation_events[event_index]['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

def get_window_events_average(window_events):
    if(len(window_events) == 0):
        return 0
    
    window_events_total_durantion = 0
    for event in window_events:
        window_events_total_durantion += event.duration
    
    return window_events_total_durantion/len(window_events)

def calculate_moving_averages(translation_events, window_size):
    moving_averages = []
    window_events = []

    first_translation_event_timestamp = get_event_timestamp(translation_events, 0)
    first_moving_average_event_timestamp = first_translation_event_timestamp.replace(second=0, microsecond=0)

    last_translation_event_timestamp = get_event_timestamp(translation_events, len(translation_events)-1)
    last_moving_average_event_timestamp = (last_translation_event_timestamp + timedelta(minutes=1)).replace(second=0, microsecond=0)

    current_moving_average_event_timestamp = first_moving_average_event_timestamp
    current_translation_event_index = 0

    while current_moving_average_event_timestamp <= last_moving_average_event_timestamp:
        current_translation_event_timestamp = get_event_timestamp(translation_events, current_translation_event_index)
        
        if(current_translation_event_timestamp < current_moving_average_event_timestamp):
            window_events.append(WindowTranslationEvent(translation_events[current_translation_event_index]['duration'])) 
            current_translation_event_index +=1

        
        current_moving_average = get_window_events_average(window_events)
        moving_averages.append(MovingAverage(current_moving_average_event_timestamp, current_moving_average))

        for window_event in window_events:
            window_event.increment_window_time()
            if(window_event.window_time == window_size):
                window_events.pop(0)

        current_moving_average_event_timestamp += timedelta(minutes=1)

    
    return moving_averages