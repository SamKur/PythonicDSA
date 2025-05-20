def main_welcome_method(func):
    def sub_welcome_method():
        print("Welcome to Python Advanced Section")
        func()
        print("These are imp topics")

    return sub_welcome_method()


def course_introduction():
    print("Intro...")


course_introduction()

print("#######")

main_welcome_method(course_introduction)

print("####### SAME AS #######")

@main_welcome_method  # first this method is called with
def course_introduction():
    print("Intro...")
