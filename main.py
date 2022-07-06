# All Pokémon Data
import pypokedex

# Image
from PIL import Image, ImageTk

# Convert URL to Image
from io import BytesIO
import urllib3

# Window Display
import tkinter as tk
window = tk.Tk()
window.geometry("500x700")
window.title("Pokédex")
window.config(padx=10, pady=10)

# Windows Title
title_label = tk.Label(window, text="Pokédex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

# Pokemon Image
pokemon_img = tk.Label(window)
pokemon_img.pack(padx=10, pady=10)

# Pokemon Text Info
pokemon_info = tk.Label(window)
pokemon_info.config(font=("Arial", 20))
pokemon_info.pack(padx=10, pady=10)

# Pokemon Type
pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

# Pokemon Base Stats
pokemon_stats1 = tk.Label(window)
pokemon_stats1.config(font=("Arial", 20))
pokemon_stats1.pack(padx=10, pady=10)

pokemon_stats2 = tk.Label(window)
pokemon_stats2.config(font=("Arial", 20))
pokemon_stats2.pack(padx=10, pady=10)

pokemon_stats3 = tk.Label(window)
pokemon_stats3.config(font=("Arial", 20))
pokemon_stats3.pack(padx=10, pady=10)

# Function to load the pokémon
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))
    image = Image.open(BytesIO(response.data))

    img = ImageTk.PhotoImage(image)
    pokemon_img.config(image=img)
    pokemon_img.image = img

    pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text="/".join([t for t in pokemon.types]).title())
    pokemon_stats1.config(text=f"   HP - {pokemon.base_stats[0]}             Attack - {pokemon.base_stats[1]}".title())
    pokemon_stats2.config(text=f"Defense - {pokemon.base_stats[2]}        Sp. Atk - {pokemon.base_stats[3]}".title())
    pokemon_stats3.config(text=f"Sp. Def - {pokemon.base_stats[4]}        Speed - {pokemon.base_stats[5]}".title())

# Text above bar
label_id_name = tk.Label(window, text="ID or name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

# Bar config
text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

# Button
btn_load = tk.Button(window, text="Load Pokémon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
