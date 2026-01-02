import math

def get_weight():
    while True:
        weight = input("enter a your weight in kg: ")
        if weight.isdigit():
            weight = int(weight)
            if weight > 0:
                break
            else: 
                print ("Your weight must be greater than 0: ")
        else:
            print("Please enter a number")
    return weight    

def get_height():
    while True:
        height = input("\nenter a your height in cm: ")
        if height.isdigit():
            height = int(height)
            if height > 0:
                break
            else: 
                print ("Your height must be greater than 0: ")
        else:
            print("Please enter a number")
    return height
    

def BMI_calculator(weight, height):
    BMI = ((weight)/pow(height, 2))*100**2
    return BMI



def main():
    weight_value = get_weight()
    height_value = get_height()
    score = BMI_calculator(weight_value, height_value)
    print(f"\nYour BMI score is {score:.2f}\n")

    if score < 18.5:
        print("You are underweight.")
    elif score < 25:
        print("You have a healthy weight.")
    elif score < 30:
        print("You are overweight.")
    else:
        print("You are in the obese range.")
    
    


if __name__=="__main__":
    main()