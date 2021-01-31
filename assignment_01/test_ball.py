# @Author:srattigan
# @Date:2021-01-13 11:05:57
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-20 18:59:30


# -- IMPORTS --
import operator  # see https://docs.python.org/3/library/operator.html
import random as r
from ball import Ball
from ball import rand_nums  # a tuple gen that takes a min, max and num_nums
from test_draw_ball import draw_balls  # func for drawing balls on canvas


# -- GLOBALS/CONSTANTS --
ball_bucket = []  # hold 10 instantiations
test_nums = [1, 2, 3, 5, 10]  # use for mul and div
arith_ops = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.truediv}
logical_ops = {}


# -- FUNCTIONS --
def instantiation_tests():
    """
    (list) - >bool
    Tests Instantiation and repr/str methods
    """
    global ball_bucket  # needed to mod a global not passed to a function
    print("---Instantiation and repr tests---")
    try:
        # make 10 instances of ball and add to ball_bucket
        # ensure that the last two are the same for equality test later
        print(f"\n\tAll instantiations successful\n")
        print("\n\tThese are the objs to be used in all tests\n")
        for each in ball_bucket:
            print("\t", each)
        print("\tNote: All instantiations printed using __repr__ method\n")
        return True
    except Warning("Failed Instantiation"):
        print("Something went horribly wrong")
        return False


def area_tests(ball_list):
    for b in ball_list:
        print(f"\t{b} has area {b.area()}")


def volume_tests(ball_list):
    for b in ball_list:
        print(f"\t{b} has volume {b.volume()}")


def set_pos_tests(ball_list):
    for b in ball_list:
        print(f"\tChanging pos of ball {b}")
        b.set_pos(rand_nums(20, 690, 2))  #  have you a func to gen a tup?
        print(f"\t\t\t  to {b}")


def set_color_tests(ball_list):
    print("\tNot Implemented")  # Complete the code to iterate and change color


def add_sum_tests(ball_list, ops=["+", "-"]):
    for op in ops:
        print(f"\t | Testing {op} operator |\n")
        for idx in range(len(ball_list)-1):
            try:
                result = arith_ops[op](ball_list[idx], ball_list[idx+1])
                print(f"\t{ball_list[idx]} {op}")
                print(f"\t{ball_list[idx+1]} =")
                print(f"\t{result}\n")
            except:  # just leave without Warning or Error
                calc = f"{ball_list[idx].radius} {op} {ball_list[idx+1].radius}"
                print(f"\t***Could not do {calc}***\n") 


def mul_div_tests(ball_list, num_list=test_nums, ops=["*", "/"]):
    for op in ops:
        print(f"\t | Testing {op} operator |\n")
        for b in ball_list:
            for num in test_nums:
                result = arith_ops[op](b, num)
                print(f"\t{b} with vol {b.volume()} {op}")
                print(f"\t{num} = {result} with volume {result.volume()}\n")


def logical_tests(ball_list):
    print("\tNot Implemented")


def draw_test(ball_list):
    print("\tNot Implemented")


def main(tests):
    print("\t\t TESTS FOR BALL CLASS\n")
    created = instantiation_tests()
    if created:
        for test in tests:
            print(f"\n\n-- Testing {test.__name__} method --\n")
            try:
                test(ball_bucket)
            except Warning(f"Error found in {test.__name__} method"):
                continue
    else:
        print("\tTests could not be completed- instantiation failed\n")


if __name__ == "__main__":
    test_funcs = [area_tests,
                  volume_tests,
                  set_pos_tests,
                  set_color_tests,
                  add_sum_tests,
                  mul_div_tests,
                  logical_tests,
                  draw_test
                  ]
    main(test_funcs)
