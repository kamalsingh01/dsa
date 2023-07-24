class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Covention Check")
        print("Compiling")
        print("Running")
class Laptop:

    def code(self, ide):
        ide.execute()

lap1 = Laptop()
ide = PyCharm()
lap1.code(ide)
lap1.code(MyEditor()) 