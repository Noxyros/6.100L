import sys
import threading
import queue
import tkinter as tk


ITEM_DATABASE = {
    # Items in player inventory

    "golden_apple" : {
        "amount" : 1,
        "health_amount" : 40,
        "buffs" : ["strength", "night_vision", "speed", "fire_resistance", "endurance"]
    },

    "health_potion" : {
        "amount" : 3,
        "health_amount" : 70,
        "buffs" : ["health_regen"]
    },

    "mutton_stew" : {
        "amount" : 2,
        "health_amount": 20,
        "buffs": []
    }
}

player_stats = {
    "player_health" : 50,
    "current_buff" : []
}

def use_item(item_name):
    # Get item values from the database which is another dictionary with 3 entry
    print(f"\nUsing {item_name.replace('_', ' ').title()}...")

    item_properties = ITEM_DATABASE.get(item_name)
    if item_properties is None:
        print("Item Doesn't Exist!")
        return

    # Get the amount key value
    item_amount = item_properties.get('amount')

    # Get healing amount from item effects (which have 2 value, health_amount and buffs)
    if item_amount >= 1: # Check if player has sufficient item
        player_stats['player_health'] += item_properties['health_amount']
        print(f"{item_properties['health_amount']} ❤️ healed from {item_name.replace('_', ' ').title()}!\n")

        # Apply buffs
        buffs = item_properties.get('buffs', []) # Get buffs key value (a list)
        # Iterate over list element. If no element exist, stop the loop!
        for buff in buffs:
            if buff not in player_stats['current_buff']:
                player_stats['current_buff'].append(buff)
            print(f"Gained buff : {buff.replace('_', ' ').title()}!")

        # Decrease the item value
        item_properties['amount'] -= 1
        print(f"\nItem {item_name} amount: {item_properties.get('amount')}")
        if item_properties.get('amount') < 1:
            print(f"{item_name} got removed from inventory!")
            del ITEM_DATABASE[item_name]


def run_game_loop():
    while ITEM_DATABASE:
        root.after(0, update_inventory_screen)
        print(f"\nPlayer Inventory: {[(k, v.get('amount')) for k, v in ITEM_DATABASE.items()]}")
        player_input = input("\nUse Item: ")
        use_item(player_input)
        print(f"\nPlayer Status: {player_stats}")
    root.after(0, update_inventory_screen)
    print("\nNo items left in inventory!")

input_queue = queue.Queue()

class GUIConsoleRedirector:
    """Redirects all print() statements directly to the Tkinter Text Box"""
    @staticmethod
    def write(string):
        console_box.config(state=tk.NORMAL)
        console_box.insert(tk.END, string)
        console_box.see(tk.END)
        console_box.config(state=tk.DISABLED)
    def flush(self):
        pass

# Overriding Python's built-in input engine to look at our entry box
def gui_input(prompt=""):
    if prompt:
        print(prompt)
    # The background loop hits a wall here and waits until the user clicks submit
    return input_queue.get()

# Replace Python's built-in input mechanism globally
builtins = sys.modules['builtins']
builtins.input = gui_input


def handle_submit():
    """Triggered when user clicks Submit or presses Enter"""
    user_text = input_field.get()
    input_field.delete(0, tk.END)
    # Sends the text to the waiting input() function in the background
    input_queue.put(user_text)

root = tk.Tk()
root.title("Simple RPG Inventory")
root.geometry("500x500")

def update_inventory_screen():
    inventory_tuple = [(k, v.get('amount')) for k, v in ITEM_DATABASE.items()]
    inventory_label.config(text=f"Player Inventory: {inventory_tuple}")

inventory_label = tk.Label(root, text="Inventory: Loaded...", fg="cyan", bg="black", font=("Arial", 15, "bold"))
inventory_label.pack(side="top", fill="x", padx=10, pady=5)

console_box = tk.Text(root, bg="black", fg="white", font=("Courier", 13))
console_box.pack(fill="both", expand=True, padx=10, pady=10)

# Redirect standard terminal outputs to our GUI widget box
sys.stdout = GUIConsoleRedirector()
sys.stderr = GUIConsoleRedirector()

prompt_label = tk.Label(root, text="Use Item: ", fg="black", font=("Arial", 15))
prompt_label.pack(side="left", padx=(10,2))

input_field = tk.Entry(root, font=("Arial", 15))
input_field.pack(side="left", fill="x", expand=True, padx=5, pady=10)
input_field.focus()
input_field.bind("<Return>", lambda event: handle_submit())

submit_button = tk.Button(root, text="Submit", bg="blue", fg="white", command=handle_submit)
submit_button.pack(side="left", padx=(0, 19))

# Start your original logic in a separate lane so the window doesn't freeze
game_thread = threading.Thread(target=run_game_loop, daemon=True)
game_thread.start()

root.mainloop()