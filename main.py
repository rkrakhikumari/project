import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Rakhi")

    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        x = str(input("Enter what you want to speak: "))
        if x == "q":
            break
        speak.Speak(x)


