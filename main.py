from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# - GUI - #

window = Tk()
window.title("TIME TO LEARN")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

incorrect_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0)
incorrect_button.grid(row=1, column=0)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0,)
correct_button.grid(row=1, column=1)

window.mainloop()

