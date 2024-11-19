import os
print("Welcome to Text to Speech AI!")
names = ["Shivam", "Sakshi", "Priyanshi", "Vishal"]
for name in names:
    print(name)

while True:
    str = input("Enter Text: ")
    if str == "bye":
        break

    command = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{str}');\""
    os.system(command)