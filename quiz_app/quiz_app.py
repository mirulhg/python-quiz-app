print('welcome to my computer quiz')

playing = input('Apakah Kamu Ingin Bermain? ')

if playing.lower() != 'iya':
    quit()

print("okay ayo bermain")
score = 0

answer = input("apakah kepanjangan dari CPU? ")
if answer.lower() == "central processing unit":
    print('Benar!')
    score += 1
else:
    print("Salah!")

answer = input("apakah kepanjangan dari GPU? ")
if answer.lower() == "graphics processing unit":
    print('Benar!')
    score += 1
else:
    print("Salah!")

answer = input("apakah kepanjangan dari RAM? ")
if answer.lower() == "random access memory":
    print('benar!')
    score += 1
else:
    print("salah!")

answer = input("apakah kepanjangan dari PSU? ")
if answer.lower() == "power supply":
    print('benar!')
    score += 1
else:
    print("salah!")

print("Kamu Mendapatkan Score " + str(score) + " Pertanyaan Yang Benar!")
print("Kamu Mendapatkan Total Score " + str((score / 4) * 100) + " %.")
