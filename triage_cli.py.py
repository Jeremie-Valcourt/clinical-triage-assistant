import time
import json 
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number only.")
def heart(heart_rate):
    if heart_rate <60:
        print("WARNING: Your heart rate is lower than normal (below 60 bpm).\nIf you feel dizzy, weak, or faint, please seek medical attention.\n")
        return False
    elif heart_rate >100:
        print("WARNING: Your heart rate is higher than normal (above 100 bpm)\nRest for a few minutes and consult a healthcare provider\nif it stays elevated")
        return False
    else:
        return True

def respiratory(res_rate):
    if res_rate <12:
        print("WARNING: Your breathing rate is slower than normal (below 12 breaths per minute). \nPlease speak with a healthcare professional.\n")
        return False
    elif res_rate >20:
        print("WARNING: Your breathing rate is faster than normal (above 20 breaths per minute).\n If you feel short of breath, seek medical care.")
        return False
    else:
        return True 
def systolic(sys_rate):
    if sys_rate <90:
        print("WARNING: Your systolic blood pressure is low (below 90 mmHg). \nSit or lie down if you feel lightheaded and contact a doctor.")
        return False
    elif sys_rate >120:
        print("WARNING: Your systolic blood pressure is above normal (over 120 mmHg). \nConsider rechecking after resting and consult a healthcare provider.")
        return False
    else:
        return True
try:
    with open("patients.json", "r") as file:
        patients = json.load(file)
except FileNotFoundError:
    patients = []
    
while True:
    print("1. Add Patient\n2. View All Patients\n3. Exit\n")
    choice = input("Enter your choice (1-3): ").strip()
    if choice == "1":
        print("Hello")
        name = input("What is your name?").strip().capitalize()
        heart_rate = get_integer("Enter Heart Rate: ")
        res_rate = get_integer("Enter Respiratory Rate: ")
        sys_rate = get_integer("Enter Systolic Blood Pressure: ")
    
        while True:
            print("Please confirm: ")
            print("Heart Rate:",heart_rate,
                  "\nRespiratory Rate: ",res_rate,
                  "\nSystolic Blood pressure:",sys_rate)
            confirmation = input("is this all true?").lower().strip()
            if confirmation == "yes":
                print("Okay!")
                break
            elif confirmation == "no":
                which_one = input("Which one is wrong?" "\nHeart Rate" "\nRespiratory Rate" "\nSystolic Blood Pressure\n").lower().strip()
                if which_one == "heart rate":
                    heart_rate = get_integer("Enter Heart Rate: ")
                elif which_one == "respiratory rate":
                    res_rate = get_integer("Enter Respiratory Rate: ")
                elif which_one == "systolic blood pressure":
                    sys_rate = get_integer("Enter Systolic Blood Pressure")
                else:
                    print("Type it properly, completely, you can only fix 1 at a time!")
            
        
            else:
                print("please only put yes or no!")
        

        my_dict={
            "Patient Name": name,
            "Heart Rate": heart_rate,
            "Respiratory Rate": res_rate,
            "Systolic Blood Pressure": sys_rate,
            }
        for key, value in my_dict.items():
            print(key, ":", value)

        hr_ok = heart(heart_rate)
        res_ok = respiratory(res_rate)
        sys_ok = systolic(sys_rate)
        patients.append(my_dict)

        with open("patients.json", "w") as file:
            json.dump(patients, file, indent=4)

            
        if hr_ok and res_ok and sys_ok:
            print("All your vital signs are within the normal resting adult range!")
    elif choice == "2":
        if len(patients)==0:
            print("No patients have been recored yet")
        else:
            for patient in patients:
                print("\n--- Patient Record ---")
                for key, value in patient.items():
                    print(key, ":", value)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!! Please enter 1, 2, or 3.")

