# -*- coding: utf-8 -*-
"""
Added by Sveder: A library to return how rare is a specific pokemon. For now I'm going
to manually parse https://poke-assistant.herokuapp.com/main/pokemonstats
and save it here as a dictionary with a few helper functions.
"""

# {pokemon_name: pokemon_rarity_percentage}
POKE_RARITY = {'Oddish': '1.22', 'Weezing': '0.01', 'Magikarp': '0.07', 'Jynx': '0.01', 'Paras': '2.57', 'Kadabra': '0.01', 'Growlithe': '0.92', 'Beedrill': '0.07', 'Hitmonlee': '0.01', 'Poliwrath': '0.01', 'Machamp': '0.01', 'Butterfree': '0.01', 'Raichu': '0.01', 'Omanyte': '0.01', 'Tangela': '0.01', 'Slowpoke': '0.23', 'Mew': '0.00', 'Diglett': '0.30', 'Rhydon': '0.01', 'Poliwhirl': '0.16', 'Snorlax': '0.01', 'Parasect': '0.13', 'Tentacool': '0.33', 'Magnemite': '0.30', 'Ditto': '0.01', 'Aerodactyl': '0.01', 'Koffing': '0.01', 'Shellder': '0.13', 'Magmar': '0.01', 'Mankey': '0.63', 'Dratini': '0.01', 'Raticate': '0.23', 'Charmeleon': '0.03', 'Psyduck': '0.76', 'Slowbro': '0.01', 'Sandslash': '0.03', 'Arcanine': '0.01', 'Omastar': '0.01', 'Venusaur': '0.01', 'Articuno': '0.00', 'Blastoise': '0.01', 'Golem': '0.01', 'Krabby': '0.01', 'Pinsir': '0.01', 'Cloyster': '0.01', 'Kangaskhan': '0.01', 'Tauros': '0.01', 'Fearow': '0.10', 'Bulbasaur': '1.18', 'Jigglypuff': '0.33', 'Abra': '0.36', 'Arbok': '0.10', 'Doduo': '5.49', 'Muk': '0.01', 'Marowak': '0.01', 'Wartortle': '0.03', 'Wigglytuff': '0.01', 'Porygon': '0.01', 'Graveler': '0.13', 'Chansey': '0.01', 'Geodude': '0.95', 'Pidgeotto': '1.15', 'Rattata': '13.13', 'Mewtwo': '0.00', 'Primeape': '0.01', 'Squirtle': '0.56', 'Vulpix': '0.20', 'Zapdos': '0.00', 'Bellsprout': '1.64', 'Nidoran♂': '1.58', 'Nidoran♀': '1.35', 'Jolteon': '0.01', 'Meowth': '0.39', 'Spearow': '3.78', 'Farfetch\'d': '0.01', 'Golduck': '0.03', 'Ekans': '2.47', 'Alakazam': '0.01', 'Kabutops': '0.01', 'Nidoqueen': '0.01', 'Seel': '0.01', 'Voltorb': '0.01', 'Dragonite': '0.01', 'Gyarados': '0.01', 'Vaporeon': '0.01', 'Metapod': '0.20', 'Dragonair': '0.01', 'Ponyta': '0.46', 'Lickitung': '0.01', 'Haunter': '0.01', 'Ivysaur': '0.03', 'Onix': '0.01', 'Gastly': '0.01', 'Drowzee': '0.01', 'Goldeen': '0.01', 'Pidgey': '18.68', 'Hypno': '0.01', 'Machoke': '0.01', 'Exeggutor': '0.01', 'Poliwag': '1.22', 'Eevee': '0.01', 'Sandshrew': '1.12', 'Venomoth': '0.07', 'Victreebel': '0.01', 'Nidorino': '0.03', 'Nidorina': '0.10', 'Pidgeot': '0.26', 'Tentacruel': '0.03', 'Kingler': '0.01', 'Exeggcute': '0.01', 'Weepinbell': '0.10', 'Golbat': '0.66', 'Gengar': '0.01', 'Rapidash': '0.01', 'Dugtrio': '0.01', 'Dodrio': '0.20', 'Seadra':'0.01', 'Persian': '0.03', 'Nidoking': '0.01', 'Scyther': '0.01', 'Zubat': '17.27', 'Charmander': '0.23', 'Electrode': '0.01', 'Moltres': '0.00', 'Gloom': '0.03', 'Flareon': '0.01', 'Kabuto': '0.01', 'Electabuzz': '0.01', 'Weedle': '6.61','Charizard': '0.01', 'Pikachu': '0.03', 'Machop': '0.46', 'Caterpie': '3.78', 'Kakuna': '0.56', 'Horsea': '0.01', 'Seaking': '0.01', 'Dewgong': '0.01', 'Hitmonchan': '0.01', 'Clefable': '0.01', 'Starmie': '0.01', 'Rhyhorn': '0.01', 'Ninetales': '0.01', 'Cubone': '0.01', 'Venonat': '3.26', 'Vileplume': '0.01', 'Clefairy': '1.51', 'Grimer': '0.01', 'Magneton': '0.01', 'Mr. Mime': '0.01', 'Lapras': '0.01', 'Staryu': '0.01'}
RARE_UNDER_PERCENT = 1 # Under what percentage is a pokemon considered rare.

def is_rare(pokemon_name, rare_under_percent=RARE_UNDER_PERCENT):
    try:
        return float(POKE_RARITY[pokemon_name]) < rare_under_percent
    except:
        return True


# This basically takes the data from the table in the url above and parses it to get pokemon names. For now I did it
# once and will just use the result below, but saving the code for posterity. I also manually changed nidorin and
# farfetchd to their utf equivalent.
# def generate_poke_rarity(xxx=""):
#     poke_parts = xxx.split("</tr>")
#     for part in poke_parts:
#         data = part.split("<td>")
#         poke_name = data[1].split("<")[0].strip()
#         poke_rarity = data[2].split("<")[0].replace("&lt;", "").replace("%", "").strip()
#         print poke_name, "\t\t", poke_rarity
#         POKE_RARITY[poke_name] = poke_rarity