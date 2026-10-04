print("=" * 40)
print("     NETINVENTORY - Network Manager")
print("=" * 40)
print("\n1. Add device")
print("2. Search inventory")
print("3. Show inventory")
print("4. Exit")

inventory = {}

def request_integer(message):
    while True :
        try:
            result = int(input(message))
            return result
        except ValueError:
            print("[Error] Enter a valid character. ")

def add_device(ip, name, kind, port=22):
    inventory[ip] = (name, kind, port)
    print("\nDevice", ip, "successfully registered.")

def search_device(search) :
    if search in inventory :
        name, kind, port = inventory[search]
        print("DEVICE:", name, "| TYPE:", kind, "| PORT:", port)
    else :
        print("IP not found")
        
def show_inventory():
    print("\n--- INVENTORY ---")
    for ip, (name, kind, port) in inventory.items():
        print("IP:", ip, "| DEVICE:", name, "| TYPE:", kind, "| PORT:", port)
    print("=" * 50)


while True :

    select = request_integer("\nSelect an option (1, 2, 3, 4): ")
    if select < 1 or select > 4 :
        print("PLEASE ENTER A VALID OPCION")
            
    if select == 1 :
        ip = input("\nEnter IP: ")
        name = input("Enter name: ")
        kind = input("Enter type (Router/Switch/Firewall): ")
        port = input("Enter port: ")

        if port != "" :
            add_device(ip, name, kind, port)
        else :
            add_device(ip, name, kind)

    if select == 2 :
        search = input("\nEnter the IP address you want to search for: ")
        search_device(search)

    if select == 3 : 
        show_inventory()

    if select == 4 :
        break
    