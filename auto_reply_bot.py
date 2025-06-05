import json

def load_responses():
    with open("responses.json", "r") as file:
        return json.load(file)

responses = load_responses()

def check_and_reply(message):
    message = message.lower()
    for keyword in responses:
        if keyword in message:
            return responses[keyword]
    return "Maaf, saya belum mengerti pesan Anda."

# Simulasi menerima pesan
print("Bot aktif. Menunggu pesan...")

while True:
    msg = input("Pesan masuk: ")
    reply = check_and_reply(msg)
    print("Balasan bot:", reply)
