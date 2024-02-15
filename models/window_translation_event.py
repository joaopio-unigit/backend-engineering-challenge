class WindowTranslationEvent :
    """
    WindowTranslationEvent is a class used to represent translation events
    that exist in the current time moving window. With this class it's
    possible to know the duration of each of the translation event in the
    moving window and keep track of how much time these have been inside
    the moving window and as such know if these still add up to the
    average calculation or not.

    Attributes:
    duration (int): The attribute that stores the duration of each translation event.
    window_time (int): The attribute that stores the amount of time the translation event has existed inside the moving window.
    """

    def __init__(self, duration):
        """
        Initialize a new instance of WindowTranslationEvent with window_time set to 0.

        Parameters:
        duration (int): The duration of the WindowTranslationEvent corresponding translation event.
        """

        self._duration = duration
        self._window_time = 0

    @property
    def duration(self):
        """
        The duration of the translation event corresponding to the WindowTranslationEvent instance.

        Returns:
        int: The duration of the translation event.
        """

        return self._duration
    
    @property
    def window_time(self):
        """
        The time the WindowTranslationEvent instance has existed inside a time window.

        Returns:
        int: The time inside a time window of the WindowTranslationEvent instance.
        """

        return self._window_time
    
    def increment_window_time(self):
        """
        This function is responsible for incrementing by 1 the time a WindowTranslationEvent
        has existed inside a time window.
        """
        
        self._window_time += 1