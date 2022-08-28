"""This project helps individuals with two common challenges with nutrition. An individual can choose a follow tool:
1. A calculator that helps estimate your calorie needs to reach your weight goals.
2. A calculator that helps determine the break down for each macro nutritient you should consume.
"""
def goal():
    goal_path = input('')
    duration = input('')
    try: 
        goal_path = int(goal_path)
    except: 
        print('You have not entered a number for what your goal is. Please enter 1-3.')
        goal()
        break
    if goal_path == 1: 
            
    elif goal_path == 2:
    
    elif goal_path == 3:
        
    else:
        print('The number you entered is not an option. Please enter 1-3 base off of what you would like to accomplish.')
        goal()
        break 

def determine_bmr(): 
    name = input('What is your name? : ')
    #include a loop and regex to ensure gender is male or female, age, weight, height are numbers
    gender = input(f'Hey {name}, we are going to need some information to help determine your calorie needs. What is your gender?: ')
    age = input('Alright, now that we have your gender let\'s get your age. How old are you?: ')
    weight = input('Next up. How much do you weight in Lbs?: ')
    height = input('Last part before we give you your baseline caloric needs! How tall are you in inches?: ') 
    
    if gender.lower() == 'female':
        BMR = (10*weight)+(6.25*height)-(5*age)-161
        
    elif gender.lower() == 'male':
        BMR = (10*weight)+(6.25*height)-(5*age)+5
    
    goal():
    
    
def weight_calculator(): 
    determine_bmr()
    goal()
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
