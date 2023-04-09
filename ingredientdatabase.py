import sqlite3


class IngredientDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("ingredients.db")
        self.cursor = self.conn.cursor()
        self.exchanger = VolumeExchanger()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients
                            (id INTEGER PRIMARY KEY, name TEXT, price REAL, volume REAL)''')
        self.conn.commit()

    def create_ingredient(self, name, price, volume, measurement):
        volume = self.exchanger.exchange(volume, measurement)
        self.cursor.execute("INSERT INTO ingredients (name, price, volume) VALUES (?, ?, ?)", (name, price, volume))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_ingredient(self, id):
        self.cursor.execute("SELECT * FROM ingredients WHERE id=?", (id,))
        return self.cursor.fetchone()

    def get_all_ingredients(self):
        self.cursor.execute("SELECT * FROM ingredients")
        return self.cursor.fetchall()

    def update_ingredient(self, id, name, price, volume):
        self.cursor.execute("UPDATE ingredients SET name=?, price=?, volume=? WHERE id=?", (name, price, volume, id))
        self.conn.commit()

    def delete_ingredient(self, id):
        self.cursor.execute("DELETE FROM ingredients WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class VolumeExchanger:
    def __init__(self):
        self.volume_dictionary = {
            "tsp": 1,
            "tbsp": 3,
            "fl oz": 6,
            "cup": 48,
            "pint": 96,
            "quart": 192,
            "gallon": 768,
            "ml": 0.202884,
            "liter": 202.884,
            "dl": 20.2884,
            "egg": 1
        }

    def exchange(self, volume, measurement):
        if measurement not in self.volume_dictionary.keys():
            return f"Measurement selection: {measurement} not found in measurement library: " \
                   f"{[key for key in self.volume_dictionary.keys()]}"
        return volume * self.volume_dictionary[measurement]






