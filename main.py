import json
from pynput import keyboard

with open("characters.json", "r") as f:
    char2morse = json.load(f)
    morse2char = dict(zip(char2morse.values(), char2morse.keys()))

morse_code = ""

def on_press(key):
    global morse_code, morse2char
    string = "\r "

    if key == keyboard.Key.esc:
        return False
    
    if key == keyboard.Key.space:
        morse_code += " "
    else:
        try:
            k = key.char
        except:
            k = key.name

        if k in [".", "-", "/"]:
            morse_code += k

    for word in morse_code.split("/"):
        for letter in word.split(" "):
            char = morse2char.get(letter)
            if char:
                string += char
        string += " "
    print(string[:-1], end="")

# ... . .-.. .- -- / ---... -.--.-
print("Morse Code:")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

"""
# Alternative of lines 38-40
with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except Exception as e:
        print(f'{e.args[0]} was pressed')
"""