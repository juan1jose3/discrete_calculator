class Display:
    def show_set_ans(self,result):
        print(result)

    def main_menu(self):
        self.print_design()

        print("Main Menu Options")
        print("1 Set Calculator")

        self.print_design()
        
        print()

    def print_message(self,message):
        print(message)
    
    def input_handler(self,message):
        return input(message)


    def print_design(self):
        print("-"*20)

    def show_ans(self,ans):
        print("Showing result .....")
        self.print_design()
        print(ans)
        self.print_design()

                


        
    

        
            