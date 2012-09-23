from datetime import datetime
from time import mktime


class datetime(object):
    class Builder:
        def __init__(
            self,
            year,
            month,
            day,
            hour,
            minute,
            second
        ):
            self.__year = year
            self.__month = month
            self.__day = day
            self.__hour = hour
            self.__minute = minute
            self.__second = second

        def build(self):
            return datetime(year=self.__year, month=self.__month, day=self.__day, hour=self.__hour, minute=self.__minute, second=self.__second)

        def set_day(self, day):
            self.__day = day
            return self

        def set_hour(self, hour):
            self.__hour = hour
            return self

        def set_minute(self, minute):
            self.__minute = minute
            return self

        def set_month(self, month):
            self.__month = month
            return self

        def set_second(self, second):
            self.__second = second
            return self

        def set_year(self, year):
            self.__year = year
            return self

        def update(self, datetime):
            if isinstance(datetime, datetime):
                self.set_year(datetime.year)
                self.set_month(datetime.month)
                self.set_day(datetime.day)
                self.set_hour(datetime.hour)
                self.set_minute(datetime.minute)
                self.set_second(datetime.second)
            elif isinstance(datetime, dict):
                for key, value in datetime.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(datetime)
            return self

    def __init__(
        self,
        year,
        month,
        day,
        hour,
        minute,
        second
    ):
        if year is None:
            raise ValueError('year is required')
        if not isinstance(year, int):
            raise TypeError(getattr(__builtin__, 'type')(year))
        self.__year = year

        if month is None:
            raise ValueError('month is required')
        if not isinstance(month, int):
            raise TypeError(getattr(__builtin__, 'type')(month))
        self.__month = month

        if day is None:
            raise ValueError('day is required')
        if not isinstance(day, int):
            raise TypeError(getattr(__builtin__, 'type')(day))
        self.__day = day

        if hour is None:
            raise ValueError('hour is required')
        if not isinstance(hour, int):
            raise TypeError(getattr(__builtin__, 'type')(hour))
        self.__hour = hour

        if minute is None:
            raise ValueError('minute is required')
        if not isinstance(minute, int):
            raise TypeError(getattr(__builtin__, 'type')(minute))
        self.__minute = minute

        if second is None:
            raise ValueError('second is required')
        if not isinstance(second, int):
            raise TypeError(getattr(__builtin__, 'type')(second))
        self.__second = second

    def __eq__(self, other):
        if self.year != other.year:
            return False
        if self.month != other.month:
            return False
        if self.day != other.day:
            return False
        if self.hour != other.hour:
            return False
        if self.minute != other.minute:
            return False
        if self.second != other.second:
            return False
        return True

    def __hash__(self):
        return hash((self.year,self.month,self.day,self.hour,self.minute,self.second,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "DateTime(year=%s, month=%s, day=%s, hour=%s, minute=%s, second=%s)" % (self.year, self.month, self.day, self.hour, self.minute, self.second,)

    def as_dict(self):
        return {'year': self.year, 'month': self.month, 'day': self.day, 'hour': self.hour, 'minute': self.minute, 'second': self.second}

    @property
    def day(self):
        return self.__day

    @property
    def hour(self):
        return self.__hour

    @property
    def minute(self):
        return self.__minute

    @property
    def month(self):
        return self.__month

    @classmethod
    def read(cls, iprot):
        init_kwds = {}

        iprot.readStructBegin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.readFieldBegin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'year':
                init_kwds['year'] = iprot.readI16()
            elif ifield_name == 'month':
                init_kwds['month'] = iprot.readByte()
            elif ifield_name == 'day':
                init_kwds['day'] = iprot.readByte()
            elif ifield_name == 'hour':
                init_kwds['hour'] = iprot.readByte()
            elif ifield_name == 'minute':
                init_kwds['minute'] = iprot.readByte()
            elif ifield_name == 'second':
                init_kwds['second'] = iprot.readByte()
            iprot.readFieldEnd()
        iprot.readStructEnd()

        return cls(**init_kwds)

    def replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None):
        if year is None:
            year = self.year
        if month is None:
            month = self.month
        if day is None:
            day = self.day
        if hour is None:
            hour = self.hour
        if minute is None:
            minute = self.minute
        if second is None:
            second = self.second
        return self.__class__(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    @property
    def second(self):
        return self.__second

    def write(self, oprot):
        oprot.writeStructBegin('datetime')

        oprot.writeFieldBegin('year', 6, -1)
        oprot.writeI16(self.year)
        oprot.writeFieldEnd()

        oprot.writeFieldBegin('month', 3, -1)
        oprot.writeByte(self.month)
        oprot.writeFieldEnd()

        oprot.writeFieldBegin('day', 3, -1)
        oprot.writeByte(self.day)
        oprot.writeFieldEnd()

        oprot.writeFieldBegin('hour', 3, -1)
        oprot.writeByte(self.hour)
        oprot.writeFieldEnd()

        oprot.writeFieldBegin('minute', 3, -1)
        oprot.writeByte(self.minute)
        oprot.writeFieldEnd()

        oprot.writeFieldBegin('second', 3, -1)
        oprot.writeByte(self.second)
        oprot.writeFieldEnd()

        oprot.writeFieldStop()

        oprot.writeStructEnd()

    @property
    def year(self):
        return self.__year
