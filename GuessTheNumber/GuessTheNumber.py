import random

import tkinter as tk

from tkinter import messagebox

from PIL import Image, ImageTk

# Creating the function to handle the 'Guess' button click....
def check_guess():
    global attempts, score, current_round, total_score
    guess = entry_guess.get()

    try:
        guess = int(guess)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    attempts += 1

    if guess < secret_number:
        result_label.config(text="Too low! Try again.", fg="yellow")

    elif guess > secret_number:
        result_label.config(text="Too high! Try again.", fg="blue")

    else:
        calculate_score()
        result_label.config(text=f"Congratulations! You guessed it right in {attempts} attempts! Your score for this round: {score}", fg="green")

        entry_guess.config(state="disabled")

        guess_button.config(state="disabled")
        current_round += 1

        total_score += score

        if current_round <= 5:

            next_button.config(state="normal")

        else:
            end_game()

# Creating the function to calculate the score based on the number of attempts...

def calculate_score():
    global score

    if attempts == 1:
        score = 100

    elif attempts == 2:
        score = 90

    elif attempts == 3:
        score = 80

    elif attempts == 4:
        score = 70

    elif attempts == 5:
        score = 60

    else:
        score = 50

# Creating the function to handle the 'Next Round' button click...

def next_round():
    set_range()

# Creating function to handle the 'Restart Game' button click...

def restart_game():

    global total_score, current_round

    total_score = 0

    current_round = 1

    set_range()

# Creating function to end the game and display final score...

def end_game():
    result_label.config(text=f"Game Over! Total Score: {total_score}", fg="green")

    entry_guess.config(state="disabled")

    next_button.config(state="disabled")

    restart_button.config(state="normal")

# Creating functions to handle the 'Set Range' button click and start a new round...

def set_range():
    global secret_number, lower_bound, upper_bound, attempts, score

    attempts = 0
    score = 0

    try:
        lower_bound = int(entry_lower.get())

        upper_bound = int(entry_upper.get())

        if lower_bound >= upper_bound:
            messagebox.showerror("Error", "Upper bound must be greater than lower bound!")

            return
        secret_number = random.randint(lower_bound, upper_bound)

        label_range.config(text=f"I'm thinking of a number between {lower_bound} and {upper_bound}")

        result_label.config(text="")

        entry_guess.config(state="normal")

        guess_button.config(state="normal")

        next_button.config(state="disabled")

        restart_button.config(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for the range!")

# Initializing the  variables... DO NOT TOUCH THIS AT ANY COST.... 

lower_bound = 1

upper_bound = 100

secret_number = random.randint(lower_bound, upper_bound)

attempts = 0

score = 0

current_round = 1

total_score = 0

# Creating the main window ....

root = tk.Tk()

root.title("Guess The Number")

root.configure(bg='#27024a')  #  background color...Main...

# Loading the given  image....
logo_image = Image.open("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\GuessTheNumber\\Logo.png")

logo_image = logo_image.resize((200, 200))  # Resize the image as needed

logo_photo = ImageTk.PhotoImage(logo_image)

# Setting the application icon...

root.iconphoto(True, logo_photo)

# Increasing the width of the window and add padding...idk why this issue occured...

root.geometry("600x600")

root['padx'] = 20

root['pady'] = 20

# Creating the widgets with improved appearance...

label_intro = tk.Label(root, text="Welcome to Guess the Number Game!", bg='#27024a', fg="white", font=("Arial", 14, "bold"))
label_intro.grid(row=1, column=0, columnspan=4)


label_hint = tk.Label(root, text="Enter the range for the number to be guessed:", bg='#27024a', fg="white", font=("Arial", 12))
label_hint.grid(row=2, column=0, columnspan=4)


frame_range = tk.Frame(root, bg='#27024a')
frame_range.grid(row=3, column=0, columnspan=4, pady=10)


label_lower = tk.Label(frame_range, text="Lower Bound:", bg='#27024a', fg="white", font=("Arial", 12))
label_lower.grid(row=0, column=0, padx=5)


entry_lower = tk.Entry(frame_range, width=10, font=("Arial", 12))
entry_lower.grid(row=0, column=1)
entry_lower.insert(0, str(lower_bound))



label_upper = tk.Label(frame_range, text="Upper Bound:", bg='#27024a', fg="white", font=("Arial", 12))
label_upper.grid(row=0, column=2, padx=5)


entry_upper = tk.Entry(frame_range, width=10, font=("Arial", 12))
entry_upper.grid(row=0, column=3)
entry_upper.insert(0, str(upper_bound))



set_range_button = tk.Button(root, text="Set Range", command=set_range, bg='#89b6ad', fg="#791103", font=("Arial", 12, "bold"))
set_range_button.grid(row=4, column=0, columnspan=4, pady=10)


label_range = tk.Label(root, text=f"I'm thinking of a number between {lower_bound} and {upper_bound}", bg='#27024a', fg="white", font=("Arial", 12, "bold"))
label_range.grid(row=5, column=0, columnspan=4)


entry_guess = tk.Entry(root, width=10, state="disabled", font=("Arial", 12))
entry_guess.grid(row=6, column=0, pady=10)


guess_button = tk.Button(root, text="Guess", command=check_guess, state="disabled", bg='#95a8cc', fg="#791103", font=("Arial", 12, "bold"))
guess_button.grid(row=6, column=1, pady=10)


next_button = tk.Button(root, text="Next Round", command=next_round, state="disabled", bg='#89b6ad', fg="#791103", font=("Arial", 12, "bold"))
next_button.grid(row=6, column=2, pady=10)


restart_button = tk.Button(root, text="Restart Game", command=restart_game, state="disabled", bg='#95a8cc', fg="#791103", font=("Arial", 12, "bold"))
restart_button.grid(row=6, column=3, pady=10)


result_label = tk.Label(root, text="", bg='#27024a', fg="white", font=("Arial", 12, "bold"))
result_label.grid(row=7, column=0, columnspan=4, pady=10)


# Creating a 3D looking boundary around the result_label....
result_label.config(relief=tk.RIDGE, bd=3, highlightbackground="#f9ca38", highlightthickness=2)


# Implementing the GUI....
root.mainloop()
