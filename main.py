def meditate(mana, max_mana, energy, energy_potions):

    while (energy != 0 or energy_potions != 0) and (mana != max_mana):
        mana = mana + 3

        if mana > max_mana:
            dif = mana - max_mana
            mana = mana - dif

        if mana != max_mana:
            if energy == 0 and energy_potions != 0:
                energy = 50
                energy_potions -= 1

        energy = energy - 1

    return mana, energy, energy_potions


