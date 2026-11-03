vypadnuty = []
with open("hlasovanie_vypadnuti.txt", encoding="cp1250") as fr:
    for riadok in fr:
        if riadok.strip() != "":
            vypadnuty.append(int(riadok))

pocty = [0] * 10
sms = 0

with open("hlasovanie_1.txt", encoding="cp1250") as fr:
    for riadok in fr:
        if riadok.strip() != "":
            pocty[int(riadok) - 5220] += 1
            sms += 1

print("Celkový počet SMS:", sms)

for i in range(10):
    print(5220 + i, ":", pocty[i])

min_i = 0
for i in range(10):
    if pocty[i] < pocty[min_i]:
        min_i = i
print("Najmenej hlasov:", 5220 + min_i)

min_i = -1
for i in range(10):
    if 5220 + i not in vypadnuty:
        if min_i == -1 or pocty[i] < pocty[min_i]:
            min_i = i
print("Najmenej hlasov bez vypadnutých:", 5220 + min_i)