
name = str(input("Enter the name of company: "))
time = int (input("Enter the time of use in seconds: "))
rate = float(input("Enter the hourly price: "))

h = time // 3600
m = (time % 3600) // 60
s = (time % 3600) % 60

rate = (time / 3600) * rate
iva = rate * 0.16
total = iva + rate

print("=" * 40)
print( "           SERVICE INVOICE")
print("=" * 40)
print("Client: ", '"'+ name + '"')
print("Usage time: ",h, "h:",m, "m:",s, "s")

print("\nSubtotal: " "$",rate)
print("IVA (16%): " "$", iva)
print("-" * 40)
print("TOTAL TO BE PAID: " "$",total)
print("=" * 40)
