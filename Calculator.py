from modules.Set_module import My_set
from views.Interface import Display

class Disc_calculator:
    def __init__(self):
        self.display = Display()
    
    
    def interface(self):

        while True:
            self.display.main_menu()
            option = self.display.input_handler("Insert number: ")

            if option == "":
                break

            elif int(option) == 1:
                a = My_set()
                b = My_set()



                self.display.print_message("Populating a")
                self.populate_set(a)
                self.display.print_design()


                self.display.print_message("Populating b")
                self.populate_set(b)

                union = a.union(b)
                intersection = a.intersection(b)
                difference = a.difference(b)
                difference_inverse = b.difference(a)

                subset_a_b = a.is_a_subset(b)

                subset_b_a = b.is_a_subset(a)


                self.display.print_message("Union")
                self.display.show_ans(union)
                self.display.print_message("Intersection")
                self.display.show_ans(intersection)
                self.display.print_message("difference A/B")
                self.display.show_ans(difference)

                self.display.print_message("difference B/A")
                self.display.show_ans(difference_inverse)
                self.display.print_design()
                
                self.display.print_message("Boolean Logic")
                self.display.print_message("$A ⊆ B$")
                self.display.show_ans(subset_a_b)
                self.display.print_message("B ⊆ A")
                self.display.show_ans(subset_b_a)
                
          
    
    def populate_set(self,set):
        while True:
            val = self.display.input_handler(f"press enter to exit {set.get_current_set()} :")

            if val == "":
                break

            set.add_to_set(int(val))