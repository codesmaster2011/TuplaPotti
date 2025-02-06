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

# Alustetaan kokonaisvoittosumma
kokonaisvoitto = 0

# Peli
def pyorita_rullat():
    return [random.choice(hedelmat) for _ in range(3)]

def tarkista_voitto(rullat):
    yhdistelma = "".join(rullat)
    return palkinnot.get(yhdistelma, 0)

def paivita_kokonaisvoitto(voitto):
    global kokonaisvoitto
    kokonaisvoitto += voitto
    kokonaisvoitto_label.config(text=f"Kokonaisvoitto: {kokonaisvoitto} euroa")

def tuplaus():
    global nykyinen_voitto
    if random.choice([True, False]):
        nykyinen_voitto *= 2
        tulos_label.config(text=tulos_label.cget("text") + f"\nTuplaus onnistui! Voitit nyt yhteensä {nykyinen_voitto} euroa!")
    else:
        nykyinen_voitto = 0
        tulos_label.config(text=tulos_label.cget("text") + "\nTuplaus epäonnistui. Menetit kaikki rahat tältä kierrokselta.")
    paivita_kokonaisvoitto(nykyinen_voitto)
    tuplaus_button.config(state="disabled")
    ei_tuplaa_button.config(state="disabled")
    pyorita_button.config(state="normal")

def ei_tuplaa():
    paivita_kokonaisvoitto(nykyinen_voitto)
    tuplaus_button.config(state="disabled")
    ei_tuplaa_button.config(state="disabled")
    pyorita_button.config(state="normal")

def pyorita():
    global nykyinen_voitto
    rullat = pyorita_rullat()
    tulos = " | ".join(rullat)
    tulos_label.config(text=tulos, font=("Helvetica", 40))
    
    nykyinen_voitto = tarkista_voitto(rullat)
    if nykyinen_voitto > 0:
        tulos_label.config(text=tulos + f"\nVoitto: {nykyinen_voitto} euroa")
        pyorita_button.config(state="disabled")
        tuplaus_button.config(state="normal")
        ei_tuplaa_button.config(state="normal")
    else:
        tulos_label.config(text=tulos + "\nEi voittoa tällä kertaa.")
        paivita_kokonaisvoitto(0)

# Luodaan graafinen käyttöliittymä
root = tk.Tk()
root.title("Tuplapotti Hedelmäpeli")
root.configure(bg="red")  # Asetetaan taustaväri punaiseksi

# Tehdään ikkunasta koko näytön kokoinen
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.quit())  # Paina ESC poistuaksesi koko näytöstä

# Palkinnot näkyviin vasempaan yläkulmaan (suurennettuna)
palkinnot_teksti = "Palkinnot:\n\n" + "\n".join([f"{k}: {v}€" for k, v in palkinnot.items()])
palkinnot_label = tk.Label(root, text=palkinnot_teksti, font=("Helvetica", 24), bg="red", fg="white")
palkinnot_label.pack(anchor='nw', padx=10, pady=10)

# Kokonaisvoitto oikeaan yläkulmaan
kokonaisvoitto_label = tk.Label(root, text=f"Kokonaisvoitto: {kokonaisvoitto} euroa", font=("Helvetica", 20), bg="red", fg="white")
kokonaisvoitto_label.pack(anchor='ne', padx=10, pady=10)

tulos_label = tk.Label(root, text="", font=("Helvetica", 40), bg="red", fg="white")
tulos_label.pack(expand=True)

# Tuplaus ja Ei Tuplaa -painikkeet, jotka ovat aluksi pois käytöstä
tuplaus_button = tk.Button(root, text="Tuplaa", command=tuplaus, font=("Helvetica", 24), state="disabled")
ei_tuplaa_button = tk.Button(root, text="Älä Tuplaa", command=ei_tuplaa, font=("Helvetica", 24), state="disabled")
tuplaus_button.pack()
ei_tuplaa_button.pack()

pyorita_button = tk.Button(root, text="Pyöritä Rullat", command=pyorita, font=("Helvetica", 24))
pyorita_button.pack()

root.mainloop()
