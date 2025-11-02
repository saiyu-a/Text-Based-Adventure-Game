import sys
import time

#Typing Effect Function - to display text one character at a time

def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
