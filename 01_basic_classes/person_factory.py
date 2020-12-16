# generate a lot of people

from person import Person
import random

# You will have to use
# random.randrange for age and weight
# random.choice for a name from the list, and a gender
# random.random to add a floating point val to weight
# for height, set the upper and lower bounds


fullnames = ["Fred Flint",
             "Mary Jones",
             "Bill Clint",
             "Bob Bullcraft",
             "Kim Karwashian",
             "Ernest Olde",
             "Eddie Socket",
             "Jim Jockstrap",
             "Annette Curtain",
             "Icy Weiner",
             "Mia Aaz"]
# make a second list for the genders. Assume there are 2 ;)
genders = ['M', 'F']


def make_people(num_people):
    """Generates and returns a list of Persons

    Args:
        num_people (int): the number of people to be created

    Returns:
        list of Person: a list of auto-generated Person objects
    """
    people = []
    for idx in range(num_people):
        # set vars for each of the attributes needed to create a Person
        # using the notes above:
        name = random.choice(fullnames)
        gender = random.choice(genders)
        age = random.randrange(18, 110)
        height = random.randrange(79, 210)
        weight = random.randrange(40, 200) + random.random()
        p = Person(name, gender, age, height, weight)
        people.append(p)
    return people


def main():
    num = input("Enter how many people you want to make: ")
    num = int(num)
    slaves = make_people(num)
    print(f"We have {len(slaves)} slaves")
    for s in slaves:
        print(f"\t{s}")

if __name__ == "__main__":
    main()
