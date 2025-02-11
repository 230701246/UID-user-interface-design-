import speech_recognition as sr
import os

def rename_file(old_name, new_name):

    try:
        if not os.path.exists(old_name):
            print(f"Error: The file '{old_name}' does not exist.")
            return
        os.rename(old_name, new_name)
        print(f"File successfully renamed from '{old_name}' to '{new_name}'.")
    except Exception as e:
        print(f"Error renaming file: {e}")


def parse_voice_command(command):
    try:
        command = command.lower()
        if "rename" in command and "to" in command:
            words = command.split()
            old_name_index = words.index("rename") + 1
            new_name_index = words.index("to") + 1
            old_name = words[old_name_index]
            new_name = words[new_name_index]
            return old_name, new_name
        else:
            print("Invalid command format. Please use: 'Rename <old_name> to <new_name>'.")
            return None, None
    except Exception as e:
        print(f"Error parsing command: {e}")
        return None, None


def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for a command to rename a file...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=20)
        except sr.WaitTimeoutError:
            print("Listening timed out. No command detected.")
            return

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        old_name, new_name = parse_voice_command(command)
        if old_name and new_name:
            rename_file(old_name, new_name)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the command. Please try again.")
    except sr.RequestError as e:
        print(f"Could not connect to Google Speech Recognition service; {e}")


if __name__ == "__main__":
    listen_for_command()
