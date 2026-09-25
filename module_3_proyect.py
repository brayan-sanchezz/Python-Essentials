#variables
records = int(input("Enter the number of network records you wish to process: "))
clean_codes = []

#add status codes
for i in range(records) :
    v = int(input("Enter the status codes one by one: "))
    if v > 0 :
        clean_codes.append(v)
    else : #ignore negative numbers
        continue

new_list = [] #list without repeated numbers
#eliminate repeated numbers
for elem in clean_codes : 
    if elem not in new_list :
        new_list.append(elem)


threats = []
safe_trafic = []

#classify threats
for codes in new_list :
    if codes & 8 != 0 :
        threats.append(codes)
    else :
        safe_trafic.append(codes)

#buble sort algoritm (ordered lists)
n = len(threats)
for i in range(n) :
    for j in range(n-i-1):
         if threats[j] < threats[j+1] :
             threats[j], threats[j+1] = threats[j+1], threats[j]

k = len(safe_trafic)
for i in range(k) :
    for j in range(k-i-1) :
         if safe_trafic[j] < safe_trafic[j+1] :
            safe_trafic[j], safe_trafic[j+1] = safe_trafic[j+1], safe_trafic[j]  


#top 3 threats
if len(threats) >= 3 :
    top = threats[0:3]
   

#output
print("=" * 40)
print("         REPORTE DE SEGURIDAD")
print("=" * 40)
print("Registered Secure Traffic: ", safe_trafic)
print("Threats detected (sorted): ", threats)
print("Top three critical threats: ", top)
print("=" * 40)