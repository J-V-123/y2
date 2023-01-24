class Course():

    def __init__(self, name, credits):
        self.__name = name  # string
        self.__credits = credits  # integer

    def get_credits(self):
        return self.__credits

    def get_name(self):
        return self.__name
