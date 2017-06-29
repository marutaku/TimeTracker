from DbController import DbController
import settings
from datetime import datetime


class CommandController:
    dbController = DbController()

    def __init__(self, command_array):
        self.command = command_array[0]
        self.categoly = command_array[1]
        self.command_chk()

    def command_chk(self):
        try:
            if self.command == False:
                raise ValueError('Command does not selected')

            command_list = self.dbController.getAllCommand()
            for cmd in command_list:
                cmd = str(cmd).split("'")[1]
                if self.command == str(cmd):
                    self.command_execute()
                    break
            # raise ValueError('Command not fuond')
        except ValueError as e:
            print(e)


    def command_execute(self):
        if self.command == "start":
            time = str(datetime.now())
            if self.categoly == False:
                raise ValueError('Categoly does not selected')
            self.dbController.start_task(self.categoly, time)
            print("========task start========")

        if self.command == "finish":
            task_array = self.dbController.get_continue_task(self.categoly)
            for task in task_array:
                task_id = task[0]
                start_time = task[1]
                finish_time = datetime.now()
                self.dbController.finish_task(str(task_id), str(finish_time).split(".")[0])
                task_time = finish_time - start_time
                task_time = str(task_time).split(".")[0]
                print(task_time)






