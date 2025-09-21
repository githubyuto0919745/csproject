from datetime import datetime
import csv

KEY_INDEX =0
HEIGHT_INDEX = 0
LIGHT_INDEX=1
HEAVY_INDEX = 2

FOOD_INDEX = 0
PROTEIN_INDEX = 1

def main(): 
    birthday = get_birthday()
    age = calculate_age(birthday)
    gender = get_gender()
    weight = get_weight()
    height = get_height()
    bmi = calculate_bmi(weight,height)
    display_bmi(bmi)
    
    ideal_light_weight,ideal_heavy_weight  = read_ideal_weight('ideal_weight.csv',HEIGHT_INDEX,height)
    compare_current_ideal_weight(weight,ideal_light_weight,ideal_heavy_weight)
    
  
    RDA_age = get_RDA_age_gender(gender,age)
    RDA_weight = get_RDA_weight(weight)
    RDA = calculate_RDA(RDA_age,RDA_weight)
    display_RDA(RDA)
   

    protein_dictionary = read_protein_intake('protein.csv',FOOD_INDEX)
    food, quantity = get_food(protein_dictionary)
    
    total_protein = collect_total_intake_protein(protein_dictionary,food,quantity)
    display_protein(total_protein, RDA, protein_dictionary)


# AGE
def get_birthday():
    birthday= input('Please enter your birthday (yyyy-mm-dd): ')
    return birthday
def calculate_age(birthday):    
    today = datetime.now()
    birth = datetime.strptime(birthday,'%Y-%m-%d')
    years = today.year - birth.year
    if birth.year > today.year or birth.month == today.month and birth.day > today.day:
        years -= 1
    return years    
#Gender
def get_gender():
    return input('Please enter your gender (M/F): ').upper()

#Weight    
def get_weight():
    unite = input('Which units would you like to use? (lbs or kg)').lower()
    if unite == 'lbs':
        weight_lbs= float(input('What is your weight? (lbs)'))
        weight_kg= weight_lbs * 0.45359237
        print(f'Your weight is {weight_kg:.0f} kg.')
    else:
        weight_kg = float(input('What is your weight? (Kg)'))
        weight_lbs = weight_kg * 2.20462262
        print(f'Your weight is {weight_lbs:.0f} lbs.')
    return weight_lbs

#Height
def get_height():
    unite= input('Which units would you like to use? (feet/inches)').lower()
    if unite ==  'feet':
        height_feet= float(input('What is your height? (feet)'))
        height_inches= height_feet * 12
        print(f'Your height is {height_inches:.0f} inches.')
    else:
        height_inches = float(input('What is your height? (Inches)'))
        height_feet= height_inches* 0.08333333
        print(f'Your height is {height_feet:.0f} feet.')
    return height_inches

#bmi
def calculate_bmi(weight, height):
    middle = (weight * 703)/height
    bmi = middle/height
    return bmi
def display_bmi(bmi):
    if bmi >=19 and bmi<25:
        print(f'BMI is {bmi:.2f}. It is optimum range! (19-24) ')
    elif bmi >=25:
        print(f'BMI is {bmi:.2f}. It is overweight...optimm range is (19-24)')   

#Ideal weight
def read_ideal_weight(filename,KEY_INDEX,height):
    ideal_dictionary = {}
    with open(filename,'rt') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #blank the first line 

        for row in reader:
            key = int(row[KEY_INDEX])
            ideal_dictionary[key] = row

        height = int(height)
        
        ideal_light_weight= int(ideal_dictionary[height][LIGHT_INDEX])
        ideal_heavy_weight =int(ideal_dictionary[height][HEAVY_INDEX])
    
    return ideal_light_weight,ideal_heavy_weight
        

def compare_current_ideal_weight(weight,ideal_light_weight,ideal_heavy_weight):
    print(f'Your ideal weight is between {ideal_light_weight} to {ideal_heavy_weight} ')
    ideal_light_weight = int(ideal_light_weight)
    ideal_heavy_weight = int(ideal_heavy_weight)

    if ideal_light_weight <= weight and weight <= ideal_heavy_weight:
            print(f'So {weight:.0f} lbs is within the ideal range for your height')
    else:
        loss_fat_lbs = weight - ideal_heavy_weight   
        loss_fat_kg= loss_fat_lbs *   0.45359237
        print(f'You need to lose at least {loss_fat_lbs:.0f} lbs ({loss_fat_kg:.0f} kg) for your height.')


#RDA             
def get_RDA_age_gender(gender,age):
    RDA_age=0

    pregnant = input('Are you pregnant? (Yes/No): ').lower()
    if pregnant == 'yes':
        RDA_age = 71.0
    else:
        if gender == 'M':
            if age >=9 and age<14:
                RDA_age = 34.0
            elif age >=14 and age<19:
                RDA_age = 52.0    
            elif age>=19 and age<70:
                RDA_age = 56.0
        elif gender == 'F':
            if age >=9 and age<14:
                RDA_age = 34.0
            elif age >=14 and age<70:
                RDA_age = 46.0
            
    return RDA_age   

def get_RDA_weight(weight):
    weight_kg = weight * 0.45359237
    RDA_weight = weight_kg * 0.8
    return RDA_weight


def calculate_RDA(RDA_age,RDA_weight):
    RDA = float((RDA_age + RDA_weight)/2)
    return RDA

def display_RDA(RDA):
    print(f'Your total RDA in grams per day is {RDA:.0f}g!')  


def get_food(protein_dictionary):
    print("*Protein Dictionary*")
    for food,values in protein_dictionary.items():
        print(f'Food: {food}')
        print(f'Protein: {values[PROTEIN_INDEX]}')
   
    while True:
        food = input('What did you eat? ').strip()
        quantity = input('What is the quantity')
        question = input('Is there anything else you ingested today? (Yes/No): ').lower()
        if question == 'no':
            break

    return food, quantity
    
def read_protein_intake(filename,KEY_INDEX):
    protein_dictionary = {}

    with open(filename,'rt') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #blank the first line 

        for row in reader:
            if len(row) > KEY_INDEX:
                key = row[KEY_INDEX]
                protein_dictionary[key] = row
    return protein_dictionary

def collect_total_intake_protein(protein_dictionary,food,quantity):
    total_protein = 0                

    if food.lower() in protein_dictionary:
        protein_per = float(protein_dictionary[food][PROTEIN_INDEX])
        total_protein += int(quantity) * protein_per
        print(f'Total intake protein at the moment is :{total_protein}g')

    return  total_protein  

def display_protein(total_protein,RDA,protein_dictionary):
    total_protein = float(total_protein)
    RDA = float(RDA)
    while True:
        if  total_protein < RDA:
            protein_gain = float(RDA - total_protein)
            print(f' You stil need to intake {protein_gain:.0f} grams of protein for the day!')    
           
            food, quantity = get_food(protein_dictionary)
            protein_per = float(protein_dictionary[food.lower()][PROTEIN_INDEX])
            total_protein += int(quantity) * protein_per
            print(f'Total intake protein at the moment is: {total_protein}g')
            # new_protein_intake = collect_total_intake_protein(protein_dictionary,food,quantity)
            # total_protein += new_protein_intake
        elif total_protein > RDA:
            print(f'Great job! You have reached your daily protein target!')
            break

if __name__ == '__main__':
    main()



