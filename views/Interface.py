class Display:
    def show_set_ans(self,result):
        print(result)

    def main_menu(self):
        print(self.print_design())

        print("Main Menu Options")
        print("1 Set Calculator")

        print(self.print_design())
        
        print()

    def input_handler(self,message):
        return input(message)

    def print_set_population(self):
        print("Populating Set .... ")

    def print_design(self):
        return "-"*20

    def show_ans(self,ans):
        print("Showing result .....")
        print(ans)

                


        
    

        
            