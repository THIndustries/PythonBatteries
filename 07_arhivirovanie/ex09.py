class TimeZone:

    def __init__(self, value, offset_hours, offset_minutes):
        self.name = value
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f'Timezone bad name - {value}')
        else:
            self._name = value.strip()



    @property
    def offset_hours(self):
        return self._offset_hours

    @offset_hours.setter
    def offset_hours(self, value):
        if isinstance(value, int):
            if value in range(-12, 15):
                self._offset_hours = value
            else:
                raise ValueError('Offset must be between -12:00 and +14:00.')
        else:
            raise ValueError('Hour offset must be an integer.')



    @property
    def offset_minutes(self):
        return self._offset_minutes

    @offset_minutes.setter
    def offset_minutes(self, value):
        if isinstance(value, int):
            if value in range(-59, 60):
                self._offset_minutes = value
            else:
                raise ValueError('Minutes offset must between -59 and 59.')
        else:
            raise ValueError('Minutes offset must be an integer.')

