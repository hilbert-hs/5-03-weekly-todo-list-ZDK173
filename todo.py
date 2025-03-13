# 5.03 Weekly ToDo List

todos = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': [] 
}

def add(todos_list, day, task):
    todos_list[day].append(task)

    
def get(todos_list, day):
    if day in todos_list:
        tasklist = ""
        for i in range(len(todos_list[day])-1):
            tasklist = tasklist + todos_list[day][i] + ", "
        tasklist += ("and " + todos_list[day][-1])
        print(f"On {day} you need to {tasklist}.")

ans = ""
while ans != "quit":
    ans = input("What would you like to do? (add/get/quit) ").split(" ")
    if ans != "quit":
        action = ans[0]
        Day = ans[1]
        Task = " ".join(ans[2:])

    if action == "add":
        add(todos, Day, Task)
    
    if action == "get":
        get(todos, Day)

    # if ans == "add":
    #     Day = input("What day would you like to add to? ")
    #     Task = input("What task would you like to add? ")
    #     add(Day, Task)
    
    # if ans == "get":
    #     Day = input("What day would you like to get? ")
    #     (get(Day))


