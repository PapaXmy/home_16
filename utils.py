import json

def load_users():
    with open("./data/users.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def load_orders():
    with open("./data/orders.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def load_offers():
    with open("./data/offers.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
