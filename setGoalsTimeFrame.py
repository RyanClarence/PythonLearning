import datetime


def goal_deadline():
    goal_and_deadline = input("Enter your goal and deadline time separated by colon ")
    goal, date = goal_and_deadline.split(":")
    deadline_date = datetime.datetime.strptime(date, "%d.%m.%Y")
    current_date = datetime.datetime.today()
    print("You Have {} days to active your {} goal".format(deadline_date - current_date, goal))


if __name__ == "__main__":
    goal_deadline()
