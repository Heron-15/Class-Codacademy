class Menu:
    pass

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} menu is available from {start_time} to {end_time}".format(name=self.name,
                                                                                 start_time=self.start_time,
                                                                                 end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill
        if purchased_items in self.items:
            bill += 1


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Our restaurant franchise is at {address}".format(address=self.address)

    def available_menus(self, time):
        menu_objects = []
        for menu in self.menus:
            if time > menu.start_time and time < menu.end_time:
                menu_objects.append(menu)
        return menu_objects
    def available_items_in_spesific_time(self, time):
        menu_items = []
        for menu in menus:
            if time > menu.start_time and time < menu.end_time:
                menu_items.append(menu.items)
        return menu_items


brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("Brunch", brunch_items, 11, 16)

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early_bird", early_bird_items, 15, 18)

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_items, 17, 23)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("Kids", kids_items, 11, 21)

print(brunch)
order_1 = ["pancakes", "home fries", "coffee"]
print(brunch.calculate_bill(order_1))
order_2 = ["salumeria plate", "mushroom ravioli (vegan)"]
print(early_bird.calculate_bill(order_2))

menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 10, 16)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

arepas = Business("Take a' Arepa", arepas_place)
print(arepas.name)
print(flagship_store.available_items_in_spesific_time(12))
