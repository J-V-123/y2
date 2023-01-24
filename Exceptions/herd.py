# DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from dog import *
from dogexceptions import ObjectIsNotDogObjectError


class Herd:
    def __init__(self, herd_name):
        self.name = herd_name
        self.members = []

    # New dogs can be added, because the herd is empty first.
    def add_member(self, member):

        if isinstance(member, Dog):
            self.members.append(member)
        else:
            raise ObjectIsNotDogObjectError(member)

    def is_member_by_name(self, name):
        for member in self.members:
            if member.get_name() == name:
                return member
        return None

    def print_dogs_status(self, number_just_for_clarifying_printouts):
        print("*", number_just_for_clarifying_printouts, "*")
        for dog in self.members:
            print(dog)
        print("****")
