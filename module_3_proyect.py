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
for i in range(len(threats) -1 ) :
    if threats[i] < threats[i+1] :
        threats[i], threats[i+1] = threats[i+1], threats[i]

for i in range(len(safe_trafic) -1 ) :
    if safe_trafic[i] < safe_trafic[i+1] :
        safe_trafic[i], safe_trafic[i+1] = safe_trafic[i+1], safe_trafic[i]  

if len(threats) > 3 :
    top_threats = slice(0, 3)
    print (threats[top_threats])

print (threats)
print (safe_trafic)
    