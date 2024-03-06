import random

nama = "Vann"

while chat != "Selesai":
    chat = input(">> ")

    if chat in ["Halo", "Hai"]:
        answer = ["Halo", "Hai"]
    elif chat in ["Apa Kabar", "Bagaimana Kabarmu"]:
        answer = ["Baik", "Saya Baik, Bagaimana denganmu?"]
    elif chat in ["Saya Baik", "Saya Sehat"]:
        answer = ["Senang Mendengarkannya"]
    elif chat == nama:
        answer = ["Baik", "Ada yg bisa saya bantu?"]
    elif chat in ["Siapa namamu?", "Namamu?"]:
        answer = ["Nama saya "+nama]
    elif chat == "Selesai":
        answer = ["Terimakasih"] 
    else:
        answer = ["Saya tidak tau", "Saya tidak mengerti"]
    x = random.randint(0,len(answer)-1)
    text = answer[x]