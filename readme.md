`README.md` file for email bomber project:

```markdown
# Email Bomber - Educational Python Tool

> **Disclaimer**: This software is developed solely for educational purposes, specifically to demonstrate sending bulk emails via SMTP. Unauthorized or malicious use is strictly prohibited and may lead to severe legal consequences. The creator is not liable for misuse.

This tool, designed as an educational project, demonstrates email-sending automation through Python. It uses SMTP to allow sending multiple emails in bulk and provides an interactive console interface with error handling, internet connectivity checks, and customizable email settings.

## Features

- **SMTP Provider Options**: Built-in support for Gmail, Yahoo, and Outlook, with custom server configuration.
- **Internet Connection Check**: Confirms internet availability before initiating the bombing process.
- **Interactive Console**: Features colored console outputs and ASCII art.
- **Customizable Email Count**: Allows setting the number of emails to send in a session.

## Requirements

- **Python**: Version 3.6 or higher
- **SMTP Server Access**: Credentials for an email account (e.g., Gmail, Yahoo) with SMTP access.

## Dependencies

To install dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

Alternatively, manually install the required libraries:

```bash
pip install termcolor requests pyfiglet
```

### Additional Setup for Linux

If you're using a Gmail account, ensure **less secure app access** is enabled for the email account:
1. Go to your Google Account settings.
2. Navigate to **Security** > **Less secure app access**.
3. Toggle it on to allow SMTP connections.

Alternatively, generate an **App Password** for added security if you have **two-factor authentication** enabled.

## Installation & Usage (Linux)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/email-bomber.git
   cd email-bomber
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Tool**:
   Start the email bomber by executing:
   ```bash
   python3 email_bomber.py
   ```

4. **Input Details**:
   - You will be prompted for the sender email, receiver email, password, and message content.
   - Select your email provider (Gmail, Yahoo, Outlook, or custom SMTP).
   - Set the number of emails you wish to send.

### Example Run

```plaintext
$ python3 email_bomber.py
Used for education purpose Only!
Email Bomber Initializing...

Enter your email here: your-email@example.com
Enter receiver email here: target-email@example.com
Enter your password here: ********
Enter your message here: Hello from Email Bomber

Network is working... Done!
Enter service 1 for Google, 2 for Yahoo, 3 for Outlook, 4 for custom: 1

Enter number of messages sending 1 for 1000, 2 for 500, 3 for 100 and 4 for custom: 3

Starting...
Bombing count: 1
Bombing count: 2
...
```

## Code Overview

### EmailBomber Class

1. **Initialization**: Prompts for email credentials, target email, message, and displays welcome ASCII art.
2. **`is_internet_on`**: Checks internet connectivity by pinging a URL.
3. **`send_email`**: Configures the email headers and sends the email through the selected SMTP server.
4. **`service`**: Configures the SMTP server and port based on the email service selected.
5. **`startbombing`**: Manages the bulk sending process, with a count and delay between sends.
6. **`run`**: Accepts input for the total number of emails to send and initiates the process.

### Exception Handling

The script includes error handling for:
- **KeyboardInterrupt**: Allows for graceful termination if the user presses `Ctrl + C`.
- **Connection and SMTP Errors**: Displays meaningful error messages and exits.

## Legal Notice

This tool is intended solely for educational purposes and ethical demonstrations related to automated emailing and SMTP configurations. Unauthorized use for harassment, spamming, or any illegal activities is strictly prohibited. **The developer is not liable for any misuse of this tool**. Use responsibly and within legal boundaries.

---

Developed by **.ECHO** for educational purposes.
```