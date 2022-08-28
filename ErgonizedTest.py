import requests
import string
import random
import secrets
import secretkey


while True:
    mail = str(input('Enter your email: '))
    if '@' in mail and ' ' not in mail:
        break
    else:
        print('Incorrect email!')
while True:
    usname = str(input('Enter your username: '))
    if '@' not in usname and ' ' not in usname:
        break
    else:
        print('Incorrect username!')
passs = "".join([secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in
                 range(random.randint(12, 15))])
print(passs)
api_key = secretkey.API_KEY
url = f'https://2captcha.com/in.php?key={api_key}&method=hcaptcha&sitekey=4c672d35-0701-42b2-88c3-78380b0db560' \
      f'&pageurl=https://discord.com/register'
r = requests.get(url)
result = r.text
captchaId = result.replace("OK|", "")
print(captchaId)
while True:
    url2 = f'https://2captcha.com/res.php?key={api_key}&action=get&id={captchaId}'
    r2 = requests.get(url2)
    result2 = r2.text
    print("Captcha ....")
    if 'OK' in result2:
        captcha_key = result2.replace("OK|", "")
        print(captcha_key)
        register_url = 'https://discord.com/api/v9/auth/register'
        payload = {"fingerprint": "", "email": mail, "username": usname, "password": passs, "invite": "null",
                   "consent": "true", "date_of_birth": "2001-06-05", "gift_code_sku_id": "null",
                   "captcha_key": captcha_key, "promotional_email_opt_in": "false"}
        req = requests.post(register_url, json=payload)
        print(req.text)
        exit()
