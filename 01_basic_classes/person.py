# class Person

class Person:
    """Emulates a person
    """
    def __init__(self, uname, gender, age, height, weight):
        """Constructor for a Person object

        Args:
            uname (str): the full name of a person
            gender (str): the gender of a person
            age (int): the age of a person
            height (float): the height of a person in cm
            weight (float): the weight of a person in Kg
        """
        self.fullname = uname  # checks? any?
        self.gender = gender  # how to check valid?
        self.age = age        # limits? type?
        self.height = height  # boundaries? type?
        self.weight = weight  # boundaries?

    def __str__(self):
        """Creates a str to represent a Person

        Returns:
            str: a str representing attr of a Person
        """
        return f"Person: {self.fullname} is {self.age}, {self.gender}, is {self.height}cm tall and weighs {self.weight}Kg"

    def life_expectancy(self):
        """Shows the life expectancy of a Person in Ireland
        based on statistics for gender

        Returns:
            float: typical life expectancy
        """
        if self.gender == "M":
            return 79.7
        elif self.gender == "F":
            return 83.4
        return 81.5

    def bmi(self):
        """Calculates the BMI for a Person

        Returns:
            float: a BMI value
        """
        return self.weight / (self.height/100) ** 2

    def bmi_category(self):
        """Calculates the BMI category based on the
        BMI value

        Returns:
            str: a description of the BMI value calculated
        """
        val = self.bmi()
        if val < 19:
            return "Skinny bone bag"
        elif val < 25:
            return "Normal"
        elif val < 30:
            return "Overweight"
        elif val < 35:
            return "Obesity Level 1"
        elif val < 40:
            return "Obesity Level 2"
        return "Obesity Level 3"

# end of class
def person_helper():
    """Gets user input to create a Person object

    Returns:
        Person: A fully formed Person object
    """
    fullname = input("Enter your name: ")
    gender = input("Enter your gender (M/F): ")
    age = input("Enter your age: ")
    age = int(age)
    height = input("Enter your height: ")
    height = float(height)
    weight = input("Enter your weight: ")
    weight = float(weight)
    p = Person(fullname, gender, age, height, weight)
    return p


def main():
    """Main function
    Loops an indefinite number of times to fill a list with
    Person objects and return the list
    """
    people = []
    print("Let's make some people!\n")
    while True:
        people.append(person_helper())
        print("\nAre you finished?")
        fin = input("Y to go again, any other key to quit :")
        if fin.lower() != 'y':
            break

    print("All people")
    for p in people:
        print(p)
    print("People and BMI + category")
    for p in people:
        print(p.fullname, p.bmi(), p.bmi_category())


if __name__ == "__main__":
    main()
