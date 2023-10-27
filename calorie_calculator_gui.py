import tkinter
from tkinter import ttk
from tkinter import messagebox


def calculator():
    enter = button_in.get()

    if enter == "Calculate":

        # Information input
        try:
            bodyweight = int(weight_input.get().strip())
            height = int(height_input.get().strip())
            age = int(age_input.get().strip())
        except:
            tkinter.messagebox.showwarning(title="Error",
                                           message='Age, Height and Bodyweight fields have to contain'
                                                   ' only whole numbers !')

        gender = gender_combobox.get().strip()
        activity_level = activity_combobox.get().strip()
        goal = goal_combobox.get().strip()

        # Check match for Gender, Activity Level and Goal from drop menu.
        if gender == "Male" or gender == "Female":
            pass
        else:
            tkinter.messagebox.showwarning(title="Error",
                                           message='Gender has to be selected from drop menu !')
            raise TypeError('Gender has to be selected from drop menu !')

        if activity_level == "Little or No Exercise" or activity_level == "Exercise 1-2 Days per Week" \
                or activity_level == "Exercise 3-5 Days per Week" \
                or activity_level == "Exercise 3-5 Days per Week" \
                or activity_level == "Exercise 6-7 Days per Week" \
                or activity_level == "Exercise 6-7 Days per Week and Active Job":
            pass
        else:
            tkinter.messagebox.showwarning(title="Error",
                                           message='Activity Level has to be selected from drop menu !')
            raise TypeError('Activity Level has to be selected from drop menu !')

        if goal == "Lose" or goal == "Maintain" or goal == "Gain":
            pass
        else:
            tkinter.messagebox.showwarning(title="Error",
                                           message='Goal has to be selected from drop menu !')
            raise TypeError('Goal has to be selected from drop menu !')

        if bodyweight and height and age and gender and activity_level and goal:
            print("-----------------------------------------------------------------------------------------------")
            print(f"Your {gender} with current bodyweight of {bodyweight}kg, height {height}cm and {age} years old")
            print(f"Your activity level is {activity_level}")
            print(f"And your goal is to {goal} weight.")
        else:
            tkinter.messagebox.showwarning(title="Error",
                                           message='You have to input data in all fields !')
            raise TypeError('You have to input data in all fields !')

        """BMR (Basal Metabolic Rate) for man and woman by MIFFLIN-ST JEOR EQUATION"""
        def bmr_equation():
            global bmr
            if gender == "Male":
                bmr = 10 * bodyweight + 6.25 * height - 5 * age + 5
                print(f"Your basic calorie intake is : {bmr:.2f} Kcal")
            elif gender == "Female":
                bmr = 10 * bodyweight + 6.25 * height - 5 * age - 161
                print(f"Your basic calorie intake is : {bmr:.2f} Kcal")

        bmr_equation()

        """To determine your total daily calorie needs,
                 multiply your BMR by the appropriate activity factor - AMR(Active Metabolic Rate),
                  as follows:"""
        def amr_equation():
            global amr
            if activity_level == "Little or No Exercise":
                amr = bmr * 1.2
            elif activity_level == "Exercise 1-2 Days per Week":
                amr = bmr * 1.375
            elif activity_level == "Exercise 3-5 Days per Week":
                amr = bmr * 1.55
            elif activity_level == "Exercise 6-7 Days per Week":
                amr = bmr * 1.725
            elif activity_level == "Exercise 6-7 Days per Week and Active Job":
                amr = bmr * 1.9

        amr_equation()

        """Calculate calories depending on your goal"""
        def goal_equation():
            if goal == "Maintain":
                calories_per_day = amr
                print(f"Your daily calorie intake is calculated to {calories_per_day:.2f} Kcal")
                tkinter.messagebox.showinfo(title="Info",
                                            message=f"Your daily calorie intake is calculated to"
                                                    f" {calories_per_day:.2f} Kcal")
            elif goal == "Lose":
                calories_per_day = amr - 500  # may vary between 300-500
                print(f"Your daily calorie intake wis calculated to {calories_per_day:.2f} Kcal")
                tkinter.messagebox.showinfo(title="Info",
                                            message=f"Your daily calorie intake is calculated to"
                                                    f" {calories_per_day:.2f} Kcal")
            elif goal == "Gain":
                calories_per_day = amr + 500
                print(f"Your daily calorie intake is calculated to {calories_per_day:.2f} Kcal")
                tkinter.messagebox.showinfo(title="Info",
                                            message=f"Your daily calorie intake is calculated to"
                                                    f" {calories_per_day:.2f} Kcal")

        goal_equation()

    else:
        tkinter.messagebox.showwarning(title="Error", message='All fields are required !')


# Program window, window name, disable resizing and applying color
window = tkinter.Tk()
window.title('Calorie Calculator')
window.resizable(False, False)

frame = tkinter.Frame(window, bg="DeepSkyBlue2")
frame.pack()

# Application fields lable and format
info_frame = tkinter.LabelFrame(frame, text="Information Form", bg="DeepSkyBlue3", labelanchor='n')
info_frame.grid(row=0, column=0, padx=35, pady=30)

gender_label = tkinter.Label(info_frame, text="Gender", bg="DeepSkyBlue3")
gender_combobox = ttk.Combobox(info_frame, values=["Male", "Female"])
gender_label.grid(row=0, column=0)
gender_combobox.grid(row=1, column=0)

age_label = tkinter.Label(info_frame, text="Age", bg="DeepSkyBlue3")
age_input = tkinter.Entry(info_frame)
age_label.grid(row=0, column=1)
age_input.grid(row=1, column=1)

height_label = tkinter.Label(info_frame, text="Height (cm)", bg="DeepSkyBlue3")
height_input = tkinter.Entry(info_frame, width=23)
height_label.grid(row=2, column=0)
height_input.grid(row=3, column=0)

weight_label = tkinter.Label(info_frame, text="Weight (kg)", bg="DeepSkyBlue3")
weight_input = tkinter.Entry(info_frame)
weight_label.grid(row=2, column=1)
weight_input.grid(row=3, column=1)

activity_label = tkinter.Label(info_frame, text="Activity Level", bg="DeepSkyBlue3")
activity_combobox = ttk.Combobox(info_frame, values=["Little or No Exercise",
                                                     "Exercise 1-2 Days per Week",
                                                     "Exercise 3-5 Days per Week",
                                                     "Exercise 6-7 Days per Week",
                                                     "Exercise 6-7 Days per Week and Active Job"], width=37)
activity_label.grid(row=0, column=3)
activity_combobox.grid(row=1, column=3)

goal_label = tkinter.Label(info_frame, text="Goal", bg="DeepSkyBlue3")
goal_combobox = ttk.Combobox(info_frame, values=["Lose", "Gain", "Maintain"]
                             , width=37)
goal_label.grid(row=2, column=3)
goal_combobox.grid(row=3, column=3)

# Rearrange cells

for widget in info_frame.winfo_children():
    widget.grid_configure(padx=20, pady=5)

# Button
button_in = tkinter.StringVar(value="Calculate")
button = tkinter.Button(frame, text="Calculate", command=calculator)
button.grid(row=3, column=0, sticky="news", padx=35, pady=10)

# Keep window (program) open
window.mainloop()
