import pyfiglet, pyperclip

text = input("Enter text to convert to ASCII art: ")
ascii_art = pyfiglet.figlet_format(text)
pyperclip.copy(ascii_art)
print(ascii_art)

# """
#    _____     _              ____ _       _               
#   | ____|___| |__   ___    / ___(_)_ __ | |__   ___ _ __ 
#   |  _| / __| '_ \ / _ \  | |   | | '_ \| '_ \ / _ \ '__|
#  _| |__| (__| | | | (_) | | |___| | |_) | | | |  __/ |   
# (_)_____\___|_| |_|\___/   \____|_| .__/|_| |_|\___|_|   
#                                   |_|                    

# """