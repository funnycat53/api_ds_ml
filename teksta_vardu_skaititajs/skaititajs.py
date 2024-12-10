with open("teksta_vardu_skaititajs/teksts.txt", "r", encoding="UTF-8") as f:
    teksts = f.read()

vardi = teksts.split()
for i in range(len(vardi)):
    vardi[i] = vardi[i].strip(".,!-?*\'\")(").lower()

visi_vardi = {}
for vards in vardi:
    if len(vards) >= 4:
        pirmie4 = vards[:4]
        if pirmie4 in visi_vardi:
            visi_vardi[pirmie4] += 1
        else:
            visi_vardi[pirmie4] = 1

top_5_vardi = []
for _ in range(5):
    max_skaits = 0
    max_pirmie4 = ""
    
    for pirmie4, skaits in visi_vardi.items():
        if skaits > max_skaits:
            max_skaits = skaits
            max_pirmie4 = pirmie4
    
    if max_pirmie4:
        top_5_vardi.append((max_pirmie4, max_skaits))
        del visi_vardi[max_pirmie4]

for pirmie4, skaits in top_5_vardi:
    print(f"{pirmie4}*: {skaits}")