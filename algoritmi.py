saraksts=[5,78,2,38,6,91,3]

for j in range(len(saraksts)-1):
    for i in range(len(saraksts)-1-j):
        if saraksts[i] > saraksts[i+1]:
            temp = saraksts[i]
            saraksts[i] = saraksts[i+1]
            saraksts[i+1] = temp

print(saraksts)

skaitlis = 23

def onsmfreakshi(list, num):
    for i in range(len(list)):
        if num == list[i]:
            print(num, "is the", i, "element")
            return
    print(num, "aint it")

onsmfreakshi(saraksts, 2)
onsmfreakshi(saraksts, 23)