import webbrowser

while True:
    msg = input("Enter Message :")
    if msg == "hi":
        print("Hey...")
    elif msg == "bye":
        print("Bye..")
        break
    elif msg.startswith("open"):
        webbrowser.open("https://"+msg.split()[-1]+".com")
    else:
        print("Sorry , I didn't Understand")
