import person

print("Making an instance when the class is in an adjacent file")

# Note the Person class is accessed by module > Class
# reference is thus by dot notation
p1 = person.Person("fred", "m", 22, 186, 88)
print(p1)
