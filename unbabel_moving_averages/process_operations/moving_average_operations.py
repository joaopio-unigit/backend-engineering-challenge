from datetime import datetime, timedelta
from collections import deque

from ..models.window_translation_event import WindowTranslationEvent
from ..models.moving_average import MovingAverage

def get_event_timestamp(translation_events, event_index):
    """
    This function receives a translation events array and an index that should not be greater than
    the length of the array and returns a datetime object that representes the translation event
    timestamp allowing the code to the timestamps comparison and other operations.

    Parameters:
    translation_events (list): An array of translation events.
    event_index (int): The index of the translation event to get the timestamp from.

    Returns:
    datetime: The datetime object that represents the timestamp of the translation event at event_index in translation_events.
    """

    return datetime.strptime(translation_events[event_index]['timestamp'], '%Y-%m-%d %H:%M:%S.%f')



def calculate_window_events_average(window_events):
    """
    This function returns the average duration of the translation events inside a moving time window.
    This is the function that calculates for each time window its moving average.

    Parameters:
    window_events (list): The list of WindowTranslationEvent's inside a time window.

    Returns:
    int: The average duration of translation events inside the given list of WindowTranslationEvent's.
    """

    if(len(window_events) == 0):
        return 0
     
    return sum(event.duration for event in window_events)/len(window_events)



def move_window_events(window_events, window_size):
    """
    This function moves the translation events window one step in time.
    The function updates all the WindowTranslationEvent's inside the event time window by incrementing their window
    time by one and removes events that have expired, i.e., their window time is equal to the window size.

    Parameters:
    window_events (list): The list of WindowTranslationEvent inside the moving time window.
    window_size (int): The size of the time window for the translation events.
    """

    expired_window_events_number = 0    #The number of events inside the window that have expired.

    # Window Events Update
    # ====================
    for window_event in window_events:
        window_event.increment_window_time()    #Increment the window time of every window event.
        if(window_event.window_time == window_size):
            expired_window_events_number += 1

    # Expired Window Events Removal
    # =============================
    for _ in range(expired_window_events_number):
        window_events.popleft()         #The expired events are always on the left of the list due to the deque FIFO policy.




def update_window_events(translation_events, window_events, current_moving_average_timestamp, current_translation_event_index):
    """
    This function is responsible for adding a new WindowTranslationEvents for each translation events to the events window
    when the current moving window timestamp is bigger than the translation event timestamp.
    The function compares the current moving window timestamp with the timestamp of the translation events and the events that are
    now older, i.e, have a smaller timestamp than the current moving window, are added to the events window.

    Parameters:
    translation_events (list): The list of translation events.
    window_events (list): The list of events inside the current time window.
    current_moving_average_timestamp (datetime): The current timestamp of the moving window.
    current_translation_event_index (int): The index of the next event to be added to the list, i.e, the oldest event that hasn't been added yet.

    Returns:
    list: The updated version of events in the moving window.
    int: The updated version of the next translation event to be added to the moving window.
    """
    
    current_translation_event_timestamp = get_event_timestamp(translation_events, current_translation_event_index)

    while(current_translation_event_timestamp < current_moving_average_timestamp):                                      # Check if the current event to be added needs to be added at the current moving window time step.
        window_events.append(WindowTranslationEvent(translation_events[current_translation_event_index]['duration']))   # Add the event.
        current_translation_event_index +=1                                                                             # Move to the next event in the translation events.
        
        if(current_translation_event_index == len(translation_events)):                                                 # Stop looking for translation events if the index is at the end of the list.
            break
        
        current_translation_event_timestamp = get_event_timestamp(translation_events, current_translation_event_index)  # Get the timestamp of the new current translation event.

    return window_events, current_translation_event_index



def calculate_moving_averages(translation_events, window_size):
    """
    This is the main function when it comes to calculating the moving average of the translation events.
    This function receives the translation events and the moving window size, initializes every variable
    it needs to start iterating over the overall time interval of the translation events and in each
    iteration inserts new translation events in the moving window if these have a timestamp that is 
    inside the moving window time interval, gets the iteration moving window average, i.e, the timestamp
    moving average, stores it and updates both the moving window time interval and all the translation
    events inside the moving window, i.e., moves these one step in time and removes the ones that now 
    fall outside the moving window.

    Parameters:
    translation_events (list): The list of translation events to get the moving average from.
    window_size (int): The size of the moving average window.

    Returns:
    list: It returns a list of MovingAverage objects that store a timestamp and its corresponding moving average.
    """

    # Variables Initialization
    # ========================
    moving_averages = []
    window_events = deque()

    first_translation_event_timestamp = get_event_timestamp(translation_events, 0)
    # Make it so that first moving window timestamp starts at the start of a minute.
    first_moving_average_timestamp = first_translation_event_timestamp.replace(second=0, microsecond=0)

    last_translation_event_timestamp = get_event_timestamp(translation_events, len(translation_events)-1)
    # Make it so that last moving window timestamp starts at the start of a minute bigger than the last translation event timestamp minute.
    last_moving_average_timestamp = (last_translation_event_timestamp + timedelta(minutes=1)).replace(second=0, microsecond=0)

    current_moving_average_timestamp = first_moving_average_timestamp
    current_translation_event_index = 0

    # Moving Average Calculation
    # ==========================
    while current_moving_average_timestamp <= last_moving_average_timestamp:
        
        # Get the current iteration step list of translation events.
        window_events, current_translation_event_index = update_window_events(translation_events, window_events, current_moving_average_timestamp, current_translation_event_index)

        # Get the current iteration step moving window average.
        current_moving_average = calculate_window_events_average(window_events)
        moving_averages.append(MovingAverage(current_moving_average_timestamp, current_moving_average))

        # Move window an its events one step foward in time.
        move_window_events(window_events, window_size)
        current_moving_average_timestamp += timedelta(minutes=1)

    return moving_averages