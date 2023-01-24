from dog import Dog  # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from food import Food  # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from herd import Herd  # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from dogexceptions import ObjectIsNotDogObjectError, \
    FeedingDogError  # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK


def add_dog(herd, dog):

    try:
        herd.add_member(dog)
    except ObjectIsNotDogObjectError as err:
        print(err)


def feed_dog(dog, food):

    try:
        dog.feed(food)
    except FeedingDogError as err:
        print(err)


def main():
    sausages = Food("sausages")  # Creating two correctly formed Food objects
    cookies = Food("cookies")

    dog1 = Dog("Skye", [cookies, sausages])  # Creating one correctly formed Dog object
    dog2 = Dog("Chase", "food")  # Creating a Dog object without a list
    dog3 = Dog("Marshall", [cookies, "sausages"])  # Creating a Dog object with a list with incorrect elements
    dog4 = "Peter"

    dogs = [dog1, dog2, dog3, dog4]

    my_herd = Herd("P. P.")

    for dog in dogs:  # Adding the dog objects to the herd
        add_dog(my_herd, dog)

    dog1.feed(cookies)  # This one should work correctly, without throwing errors

    '''
    The below three lines demonstrate the three cases that can cause a FeedingDogError.
    When you have not yet implemented the error handling of feed_dog in main.py, they
    should all crash the program and throw an error with a different error message
    '''

    dog1.feed("carrot")                     # This one should cause a FeedingDogError
    dog2.feed(cookies)                      # This one should cause a FeedingDogError
    dog3.feed(sausages)                     # This one should cause a FeedingDogError

    '''
    To handle the exception, fix the feed_dog function above. Here we call it three
    times with the same parameters as above. Once you have implemented the exception
    class in dogexceptions.py and raised it in dog.py, erase the comment inside the
    foor-loop (line number) and the pass command. After that add your custom 
    modifications to the function feed_dog
    '''

    dogs = [dog1, dog2, dog3]
    foods = ["carrot", cookies, sausages]

    for i in range(3):
        feed_dog(dogs[i], foods[i])
        pass


if __name__ == "__main__":
    main()
