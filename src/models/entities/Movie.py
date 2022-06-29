from utils.dateformat import DateFormat
class Movie():

    def __init__(selft, id, title=None, duration=None, released=None) -> None:
        selft.id = id
        selft.title = title
        selft.duration = duration
        selft.released = released
    
    def to_JSON(self):
        return {
            'id':self.id,
            'title': self.title,
            'duratiton': self.duration,
            'released': DateFormat.convert_date(self.released)
        }