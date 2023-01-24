from food import Food  # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK

'''
Todo: Implement the Exception classes ObjectIsNotDogObjectError and FeedingDogError.

ObjectIsNotDogObjectError should get the incorrect 'member'
tried to add. It needs to check which type it is, and tell the type in the message.

FeedingDogError should get the food tried to add, current element in the food list and the food list as parameters.
It should check, which of them caused the error and tell that in the message.
'''

'''
Check the definitons of the classes from the exercise on A+
'''


class ObjectIsNotDogObjectError(Exception):
    # hint: use str(type())
    def __init__(self, member):
        self.member = member

    def __str__(self):
        exc_str = "****** Exception: The object ({:s}) you tried adding in the herd " \
                  "is not a dog object, but an object of {:s}".format(str(self.member), str(type(self.member)))
        return exc_str


class FeedingDogError(Exception):
    # hint: use isinstance()
    def __init__(self, food, food_in_list, food_list):
        self.food = food
        self.food_in_list = food_in_list
        self.food_list = food_list

    def __str__(self):
        if not isinstance(self.food_list, list):
            return "****** Exception: Dog object does not have a list of foods"
        if not isinstance(self.food, Food):
            return "****** Exception: The object with which the dog is tried to be fed is not a food object"
        if not isinstance(self.food_in_list, Food):
            return "****** Exception: An object in dog's foodlist is not a food object"



