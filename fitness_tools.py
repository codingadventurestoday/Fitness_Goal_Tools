"""This project helps individuals with two common challenges with nutrition. An individual can choose a follow tool:
1. A calculator that helps estimate your calorie needs to reach your weight goals.
2. A calculator that helps determine the break down for each macro nutritient you should consume.
"""

def weight_calculator: 
    return None 
  
def macro_calculator():
    return None 
  
  
  
# this is the homepage for the user
current_status = True 
while current_status == True: 
    tool_selection = input('''
    1. Calorie needs for your weight goals.
    2. Breakdown of Macro Nutrients for your diet.
    3. To EXIT.
    \n\n''')
    try: 
        tool_selection = int(tool_selection)
    except: 
        print('Your entry was not a numerial. Please enter the numerial of the tool you would like to use. Example: 1.')
    try: 
        if tool_selection == 1: 
            weight_calculator()
            
        elif tool_selection == 2: 
            macro_calculator()
            
        elif tool_selection == 3: 
            current_status = False
            break
