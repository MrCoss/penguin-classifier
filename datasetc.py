import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

species_list = [
    "Adelie", "African", "Chinstrap", "Emperor", "Erect-crested", "Fiordland",
    "Galápagos", "Gentoo", "Humboldt", "King", "Little", "Macaroni",
    "Magellanic", "Northern Rockhopper", "Rockhopper", "Royal", "Snares",
    "Southern Rockhopper"
]

# Feature ranges approximated for each species
species_ranges = {
    "Adelie":               [38, 47, 17, 20, 180, 220, 2900, 4100],
    "African":              [38, 50, 17, 21, 170, 220, 3000, 4500],
    "Chinstrap":            [40, 51, 18, 21, 180, 220, 3000, 4000],
    "Emperor":              [70, 95, 25, 35, 250, 310, 25000, 40000],
    "Erect-crested":        [45, 55, 20, 25, 200, 230, 4000, 5000],
    "Fiordland":            [45, 55, 18, 21, 180, 210, 3000, 4000],
    "Galápagos":            [45, 55, 18, 22, 180, 210, 2800, 3500],
    "Gentoo":               [45, 60, 13, 17, 210, 230, 4500, 6000],
    "Humboldt":             [42, 52, 17, 21, 180, 210, 3500, 5000],
    "King":                 [90, 110, 30, 35, 300, 350, 11000, 16000],
    "Little":               [30, 42, 13, 17, 160, 190, 1000, 1500],
    "Macaroni":             [50, 60, 22, 26, 210, 230, 4200, 5500],
    "Magellanic":           [42, 55, 18, 22, 190, 220, 3000, 4300],
    "Northern Rockhopper": [45, 58, 19, 23, 200, 220, 3400, 4700],
    "Rockhopper":           [42, 55, 17, 21, 180, 210, 3000, 3900],
    "Royal":                [50, 62, 20, 25, 200, 230, 4000, 5200],
    "Snares":               [45, 55, 18, 22, 190, 220, 3000, 4300],
    "Southern Rockhopper": [43, 55, 17, 21, 180, 210, 3000, 3900]
}

# Real island associations for each species
species_islands = {
    "Adelie": ["Ross Island", "Peter I Island", "Beaufort Island"],
    "African": ["Boulders Beach"],
    "Chinstrap": ["Deception Island", "Livingston Island"],
    "Emperor": ["Cape Crozier", "Cape Washington"],
    "Erect-crested": ["Antipodes Island", "Bounty Islands"],
    "Fiordland": ["South Fiordland"],  # mainland NZ
    "Galápagos": ["Galápagos Islands"],
    "Gentoo": ["Falkland Islands", "South Georgia"],
    "Humboldt": ["Peru Coast", "Chile Coast"],
    "King": ["Macquarie Island", "Crozet Islands"],
    "Little": ["Phillip Island", "Otago Peninsula"],
    "Macaroni": ["South Georgia", "Marion Island"],
    "Magellanic": ["Patagonia Mainland", "Isla Magdalena"],
    "Northern Rockhopper": ["Tristan da Cunha", "Gough Island"],
    "Rockhopper": ["Falkland Islands"],
    "Royal": ["Macquarie Island"],
    "Snares": ["Snares Islands"],
    "Southern Rockhopper": ["Falkland Islands", "Chile Coast"]
}

def generate_sample(species):
    r = species_ranges[species]
    return {
        "Species": species,
        "Bill_Length_mm": round(np.random.uniform(r[0], r[1]), 1),
        "Bill_Depth_mm": round(np.random.uniform(r[2], r[3]), 1),
        "Flipper_Length_mm": int(np.random.uniform(r[4], r[5])),
        "Body_Mass_g": int(np.random.uniform(r[6], r[7])),
        "Sex": random.choice(["Male", "Female"]),
        "Island": random.choice(species_islands.get(species, ["Unknown"]))
    }

# Generate 100 samples per species
rows = []
for sp in species_list:
    for _ in range(100):
        rows.append(generate_sample(sp))

df = pd.DataFrame(rows)
df.to_csv("penguin_species_dataset.csv", index=False)
print("✅ Dataset created: 1800 samples with realistic islands!")
