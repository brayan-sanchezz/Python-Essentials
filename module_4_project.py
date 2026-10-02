print("=" * 40)
print("     NETINVENTORY - Network Manager")
print("=" * 40)
print("1. Add device")
print("2. Search inventory")
print("3. Show inventory")
print("4. Exit \n")

inventory = {}

def request_integer(message):
    while True :
        try:
            result = int(input(message))
            return result
        except:
            print("[Error] Enter a valid character")

def add_device(ip, name, type, port=22):
    inventory[ip] = (name, type, port)
    return print("Device", ip, "successfully registered.")

def search_device(search) :
    if search in inventory :
        return print(inventory[search])
    else :
        return None
        
def show_inventory():
    print("-" * 3, INVENTORY, "-" * 3)
    print("IP:", ip, "Device:", name, "Type:", kind, "Port", port, sep="|")



while True :
    select = int(input("Select an option: "))

    if select == 1 :
        ip = request_integer("Enter IP: ")
        name = input("Enter name: ")
        kind = input("Enter type (Router/Switch/Firewall): ")
        port = input("Enter port: ")

        if port != "" :
            add_device(ip, name, kind, port)
        else :
            add_device(ip, name, kind)

    if select == 2 :
        search = request_integer("Enter the IP address you want to search for: ")
        search_device(search)

    if select == 3 : 
        show_inventory()

    if select == 4 :
        break
