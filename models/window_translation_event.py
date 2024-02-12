class WindowTranslationEvent :

    def __init__(self, duration):
        self._duration = duration
        self._window_time = 0

    @property
    def duration(self):
        return self._duration
    
    @property
    def window_time(self):
        return self._window_time
    
    def increment_window_time(self):
        self._window_time += 1