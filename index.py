import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100
        bmi = weight / (height * height)
        label_result['text'] = f'BMI: {bmi:.2f}'
        if bmi < 18.5:
            result_text = "You are underweight."
        elif 18.5 <= bmi < 24.9:
            result_text = "You have a normal weight."
        elif 25 <= bmi < 29.9:
            result_text = "You are overweight."
        else:
            result_text = "You are obese."
        messagebox.showinfo("BMI Result", result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Futuristic BMI Calculator")

# Set the size of the window
root.geometry('300x400')

# Set the background color and style
root.configure(bg='black')

# Set the title label with a futuristic style
label_title = tk.Label(root, text="BMI Calculator", font=("Helvetica", 24, 'bold'), fg="cyan", bg="black")
label_title.pack(pady=20)

# Create the entry fields for weight and height
label_weight = tk.Label(root, text="Weight (kg)", font=("Helvetica", 14), fg="white", bg="black")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root, font=("Helvetica", 14), fg="black", bg="cyan")
entry_weight.pack(pady=5)

label_height = tk.Label(root, text="Height (cm)", font=("Helvetica", 14), fg="white", bg="black")
label_height.pack(pady=5)
entry_height = tk.Entry(root, font=("Helvetica", 14), fg="black", bg="cyan")
entry_height.pack(pady=5)

# Create the calculate button with a futuristic style
button_calculate = tk.Button(root, text="Calculate", font=("Helvetica", 14, 'bold'), fg="black", bg="cyan", command=calculate_bmi)
button_calculate.pack(pady=20)

# Label to display the result
label_result = tk.Label(root, text="", font=("Helvetica", 14), fg="cyan", bg="black")
label_result.pack(pady=10)

# Set the protocol for the window close button
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main event loop
root.mainloop()
