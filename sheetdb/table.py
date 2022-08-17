class table():
    def __init__(self, worksheet_object):
        self.worksheet_object = worksheet_object

    def set(self, position, value):
        self.worksheet_object.update(position, value)

    def get(self, position):
        return self.worksheet_object.get(position).first()