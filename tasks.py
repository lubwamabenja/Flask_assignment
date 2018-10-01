todo_list = []
task_status ={}


#this class contains all methods required for the to_do list app
class Application:
    #this method adds tasks to the todo-list
    def create_task(self,task):
        todo_list.append(task)
        task_status[task] = "pending"
        return True
    pass
    
    #this method deletes a task
    def delete_task(self,task):
        for item in todo_list:
            if item == task:
                todo_list.remove(task)
                print("Task deleted")
                return True
            else:
                return False

    #this method marks a task as finished
    def mark_as_finished(self,task):
        for item in todo_list:
            for key,value in task_status.items():
                if key == task:
                    task_status[key] = "Finished"
                    print(task_status) 
                

    #this method deletes everything from the list
    def delete_all_tasks(self):
        todo_list.clear()
        return True
    pass

    def run_tasks(self):
        print("Select Option:")
        print()
        print("     1:Creating a Task")
        print("     2:Deleting a Task")
        print("     3:Deleting all tasks")
        print("     4:Marking a Task as Finished")

        selection = int(input("selection: "))
        if selection == 1:
            task = input("Enter Task: ")
            self.create_task(task)
            print("{}  added to list".format(task))

        elif selection == 2:
            task =  (input("Enter task to delete: "))
            self.delete_task(task)
            print("{} has been deleted")

        elif  selection == 3:
            self.delete_all_tasks()
            print(todo_list)

        elif selection == 4:
            self.mark_as_finished(input("Enter Task: "))



