"""This project helps individuals with two common challenges with nutrition. An individual can choose a follow tool:
1. A calculator that helps estimate your calorie needs to reach your weight goals.
2. A calculator that helps determine the break down for each macro nutritient you should consume.
"""
def goal():
    goal_path_check = True
    while goal_path_check = True: 
        goal_path = input('''Please enter the number of what would you like to accomplish: 
    1. Lose Weight
    2. Maintance Weight
    3. Gain Weight''')
        try: 
            goal_path = int(goal_path)
            goal_path_check = False
        except: 
            print('You have not entered a number for what your goal is. Please enter 1-3.')
        
    duration_check = True
    while duration_check == True:
        try: 
            duration = input('How many weeks would your goal in like to accomplish this by?: ')
            days = int(duration)
            duration_check = False 
        except: 
            print('The amount of weeks needs to be in numerical form')

    if goal_path == 1: 
        weight_lost_check = True 
        while weight_lost_check == True:
            try: 
                amount_to_lose = input('What is the number of Lbs would you like to lose?: ')
                lbs_to_lose = int(amount_to_lose)
                weight_lost_check = False
            except: 
                print('The amount you enter must be a number.")
        deficit = (goal*-3500)/days
        return deficit
                      
    elif goal_path == 2:
        maintenance_calories = 0
        return maintenance_claories
                      
    elif goal_path == 3:
        weight_gain_check = True 
        while weight_gain_check == True:
            try: 
                amount_to_gain = input('What is the number of Lbs would you like to lose?: ')
                lbs_to_gain = int(amount_to_lose)
                weight_gain_check = False
            except: 
                print('The amount you enter must be a number.")
        surplus = (goal*3500)/days  
        return surplus
                      
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
    additional_calories = goal()
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
