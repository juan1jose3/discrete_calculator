from modules.Set_module import My_set
from views.Interface import Display

class Disc_calculator:
    def __init__(self):
        self.display = Display()
    
    
    def interface(self):

        while True:
            self.display.main_menu()
            option = self.display.input_handler("Insert number: ")

            if int(option) == 1:
                a = My_set()
                b = My_set()



                self.display.print_set_population()
                self.populate_set(a)
                self.display.print_design()

                self.display.print_set_population()
                self.populate_set(b)

                union = a.union(b)
                intersection = a.intersection(b)
                self.display.show_ans(union)
                self.display.show_ans(intersection)
                
            elif option == "":
                break
    
    def populate_set(self,set):
        while True:
            val = self.display.input_handler(f"press enter to exit {set.get_current_set()} :")

            if val == "":
                break

            set.add_to_set(int(val))