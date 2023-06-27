my_name = 'nico'
my_age = 12
print(f"Hello I'm {my_name}, I'm {my_age} years old.")

def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)