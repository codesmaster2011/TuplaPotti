import random
import tkinter as tk
from tkinter import messagebox

# Hedelmäkuvakkeet
hedelmat = ["🍒", "🍋", "🍉", "🍇", "🍓", "🍊", "🍍", "🍌"]

# Palkinnot
palkinnot = {
    "🍒🍒🍒": 100,
    "🍋🍋🍋": 200,
    "🍉🍉🍉": 300,
    "🍇🍇🍇": 400,
    "🍓🍓🍓": 500,
    "🍊🍊🍊": 600,
    "🍍🍍🍍": 700,
    "🍌🍌🍌": 800,
}

# Peli
def pyorita_rullat():
    return [random.choice(hedelmat) for _ in range(3)]

def tarkista_voitto(rullat):
    yhdistelma = "".join(rullat)
    return palkinnot.get(yhdistelma, 0)

def pyorita():
    rullat = pyorita_rullat()
    tulos = " | ".join(rullat)
    tulos_label.config(text=tulos, font=("Helvetica", 40))

    voitto = tarkista_voitto(rullat)
    if voitto > 0:
        tulos_label.config(text=tulos + f"\nVoitto: {voitto} euroa")
        if messagebox.askyesno("Tuplaus", "Haluatko tuplata voiton?"):
            if random.choice([True, False]):
                voitto *= 2
                tulos_label.config(text=tulos + f"\nTuplaus onnistui! Voitit nyt yhteensä {voitto} euroa!")
            else:
                voitto = 0
                tulos_label.config(text=tulos + "\nTuplaus epäonnistui. Menetit kaikki rahat tältä kierrokselta.")
        else:
            tulos_label.config(text=tulos + f"\nVoitto: {voitto} euroa")
    else:
        tulos_label.config(text=tulos + "\nEi voittoa tällä kertaa.")

# Luodaan graafinen käyttöliittymä
root = tk.Tk()
root.title("Tuplapotti Hedelmäpeli")
root.configure(bg="red")  # Asetetaan taustaväri punaiseksi

# Tehdään ikkunasta koko näytön kokoinen
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.quit())  # Paina ESC poistuaksesi koko näytöstä

tulos_label = tk.Label(root, text="", font=("Helvetica", 40), bg="red", fg="white")
tulos_label.pack(expand=True)

voitto_label = tk.Label(root, text="", font=("Helvetica", 20), bg="red", fg="white")  # Korjattu voitto_label
voitto_label.pack()

pyorita_button = tk.Button(root, text="Pyöritä Rullat", command=pyorita, font=("Helvetica", 24))
pyorita_button.pack()

root.mainloop()
