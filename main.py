from tkinter import *
import requests


def get_quote():
    """Cara One Line Solution"""
    """response = requests.get("https://api.kanye.rest").json()["quote"]"""
    
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    if len(quote) > 150:
        canvas.itemconfig(quote_text, font=("Arial", 15, "bold"))
    elif len(quote) > 120:
        canvas.itemconfig(quote_text, font=("Arial", 18, "bold"))
    elif len(quote) > 90:
        canvas.itemconfig(quote_text, font=("Arial", 21, "bold"))
    elif len(quote) > 70:
        canvas.itemconfig(quote_text, font=("Arial", 24, "bold"))
    elif len(quote) > 50:
        canvas.itemconfig(quote_text, font=("Arial", 27, "bold"))
    elif len(quote) > 30:
        canvas.itemconfig(quote_text, font=("Arial", 30, "bold"))
    elif len(quote) > 20:
        canvas.itemconfig(quote_text, font=("Arial", 33, "bold"))
    elif len(quote) > 12:
        canvas.itemconfig(quote_text, font=("Arial", 36, "bold"))
    else:
        canvas.itemconfig(quote_text, font=("Arial", 39, "bold"))
    canvas.itemconfig(quote_text, text=quote, fill="white")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()