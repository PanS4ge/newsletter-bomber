import requests
import colorama
import os
import sys
import re
from discord_webhook import DiscordWebhook
import json

class RegisterNewsletter:
    method = ""
    payload = {}
    headers = {}
    endpoint = ""
    
    def __init__(self, method, payload, headers, endpoint):
        self.method = method
        self.payload = payload
        self.headers = headers
        self.endpoint = endpoint
    
class Logger:
    @staticmethod
    def Success(message):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")
        
    @staticmethod
    def Mild(message):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.YELLOW}/{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")
        
    @staticmethod
    def Failed(message):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}-{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.WHITE} {message}")

email = input("Email: ")

succ = 0
fail = 0

Logger.Mild("Preping list of newsletters")
builtinnewsletters = [
    RegisterNewsletter(
        "POST",
        {
            "newsletter": "0",
            "newsletter": "1",
            "newsletter_alcohol": "0",
            "newsletter_alcohol": "1",
            "day": "4",
            "month": "5",
            "year": "1995",
            "email": email,
            "policy": "0",
            "policy": "1",
            "agree_marketing": "0",
            "agree_marketing": "1",
            "grecaptcharesponse": "03AAYGu2RPiqKR1fLEmssBtStUaqtD5h2fUCaGdFo9l2JbkdngQwfSlwPRDvm7Fs_CWYpV7i2jTqUQQS_ipIktBi2FwNMFtvx3EG9c75VxHM6lRKcXm90mQXOwhBIqJzETf_bCdpp7tEoMRZtpVC2R4iTRT5xBoAsgKq9UVVj9pLfIAsVp8FYmieVtTjTW7nGWxBozz3aC4XHcdHDKfhoO80eNw3ULWGDKVfs35_F_UWHkZCvNfieMsjSRYsdXgCe4cwZPhJM8TK6xlsKal5OM4olJnf2hLrPtCyLE4TOoGgGkl_INHrwkDrJAaH2S0pjLgsqQcdlxews1X7jhxfc3C6PJsgo1hPk5mNfXMuBIxDFUiY9iar6YtKPrGGdcmaEvprfR7Qc_jtKytazOFuYezeOMSK1z0UW8o6sXgLpgbSjbugcoj-8OcAeipZ5zlGYWusZexrxmh8cnctfN9bH_w3DU720gogakOuIEgpjLV32kwVoFq8U3yTF2Q4NXJwi04BzyRACVR-5rHUUZiHTxy2JIsdq084zSo1HhQJ60HO1OR_dQRT9F-xzIdkcDgp2nQ5L8dGMuO-d9",
            "action": "validate_captcha"
        },
        {

        },
        "https://www.biedronka.pl/front/user/registration"
    ),
    RegisterNewsletter(
        "GET",
        {
            
        },
        {
            
        },
        "https://accace.us9.list-manage.com/subscribe/post-json?u=f9e1b907f6f668b57915b45bc&id=d8dcb9e51e&c=jQuery19008258134395183847_1689793266673&EMAIL=(MAILERXDD)&b_f9e1b907f6f668b57915b45bc_d8dcb9e51e=&subscribe=Rozpocznij&_=1689793266674"
    ),
    RegisterNewsletter(
        "POST",
        {
            "email": email,
            "listid": "HkbiTvr4g,teO9yNr4x,H1BhTwrEl,wsEqCz6bW,_gMrvGzn4,wvQ0mfm5Y"
        },
        {
            
        },
        "https://vivaldi.com/wp-content/themes/vivaldicom-theme/newsletter/ajaxsubscribe.php"
    ),
    RegisterNewsletter(
        "POST",
        {
            "mailing_action": "add",
            "mailing_email": email,
            "mailing_name": "Zjeb",
            "newsletter_consent": "on",
            "iai-recaptcha-token": "03AAYGu2SQgZ76azdxD4Ybngsmr83jTggYq-jvx-Fuq4mW_DLJC4drOV68aQDa13OLESLnYcmsXVB1A32WSnES-u1MIM1G1ym_mj5oOUWWNNkSW-OCejdNnGn2LTJ2Jrg8fUsVp059Il3W163_7tf8Rt2pq7TBN3FR9KBHIjhCLLZ-vM8Mh4a8lpOxP-RcNM0VMcmzvHjwitRicNZr8X0lnwa-F2gNJe0rVGlunUuSqmLnPdpT2pDI7girngAOct6O4065H293NG9FnwLsXncrskFRFs--HcnV23TOs3BHBs37sxVZfP75nl85BboDoTUJlC866LQgsaFK1fHQg5Ilbhf1CHuLoqtcHu89aaatlc0xNYmLs3KWIleYPZLGmsaOqTLC8sJmjc1Xw6s1TWXVPz31pREPD9jwBo-mhIYwQMr-4gH7y4oOwg3krEnrWJgbyxikLElyFqR8ofoobvWf8HcN8KXQJj7qxj7ho-fm9ODcKSbiBkINX-kFXQFgxCuY2Jn_BLBBusnSta5F18y6JmRDjlQBb7GATvcw_6_vIFpKrAz8g-xqWyA"
        },
        {
            
        },
        "https://artnapi.pl/settings.php"
    ),
    RegisterNewsletter(
        "POST",
        {
            "3f746946-34b4-442c-a677-e232cdd2bc40": "Adam",
            "e1dfc514-f301-4cb2-855a-4c8fa8331207": "Normalowski",
            "7f685ebb-7c54-4cff-a1bc-772562d25c38": "nic3sw2g@gmail.com",
            "7532e8e0-8486-ed11-81ad-0022489ba642": "true",
            "submit944549e3-d0bc-95e4-814b-800b50a1a4b1": "",
            "5dc25234-a586-ed11-81ac-000d3aba7cb4": "115000017",
            "25d6260c-a586-ed11-81ac-000d3aba7cb4": "true",
            "b02552ec-a486-ed11-81ac-000d3aba7cb4": ["115000000","115000001"]
        },
        {
            
        },
        "https://72755818d25743b085a88a8c92e6a295.svc.dynamics.com/f/formpage/dbb690c4-5f87-ed11-81ac-000d3aba7cb4/correlation/pF0a_Oe4xWDXTkS8pbYzkPwwiQuzrCMN63wTwmHbJ3o"
    ),
    RegisterNewsletter(
        "POST",
        {
            "contentId": "815589",
            "formId": "580",
            "data[16566][]": email,
            "data[16567][]": "Zjeb",
            "data[adobecampaign_subscribe][]": "1",
            "token": "03AAYGu2RfMrZQhC0oXSpvqEpb_Q1huhAWgbXmwmBvLStCqkRmNyuVEMI9FPFpKDRmEE8iE15h0Viu4PZKw4tQDZm4I9zogVTzgB8hKyGpKxujxzaPRaABJ4GURJwMkFxe3ll5GTagQI7dZMSgvnvQVx_4zn8OdR2IZ5J976uKMdp24yjDxya1AM86PE0PBfUKA7ST9Ocnxj0YZkQdryzugM3nSQjssXalH7YVkqcXipYO5r-eY6aP8d_8p0Iqcx6UPInmcWFdT2btinYyhflxgB3Q4aG9whZFzxYCLpAVDTBGSCksos7K7DP8i-ruxVfVcPKrkqy7Q4N9V-5pMAcJEnVfqaA80VIAW1_68k8wYZTAem8qqHKagVz0QpFPIfECHxGqUnELc7m3RlxXD-29dhf03M3c57hyhvIvl3sU-1N2iGNfYKogExzpemiPY1HsO5d48WDU3Gue6cAOXxDcgbOsFOezm75mDvxycQApnhWrUNsRgFen4t6aD-UajUoIH6hjWwheJ3PaaaV9EuglbcPel9vmgcITeFhlZ9KRC0AqoSze6XpdsdG0enrmofWGx7nu9dOOHkmy",
            "returnUrl": "https://www.kaercher.com/pl/serwis-i-uslugi/wsparcie-i-obsluga-klienta/newsletter.html",
            "isocode": "pl-PL"
        },
        {
            
        },
        "https://www.kaercher.com/api/v3/formbuilderv2/form"
    )
]

newsletters = []

if not os.path.exists("newsletters.json"):
    dic = []
    for x in builtinnewsletters:
        te = {}
        te["method"] = x.method
        te["payload"] = x.payload
        te["headers"] = x.headers
        te["endpoint"] = x.endpoint
        dic.append(te)
    with open("newsletters.json", "w") as nl:
        nl.write(json.dumps(dic))
    newsletters = builtinnewsletters
else:
    with open("newsletters.json", "r") as nl:
        newslettersx = json.loads(nl.read())
        for x in newslettersx:
            newsletters.append(RegisterNewsletter(x.method, x.payload, x.headers, x.endpoint))

for x in newsletters:
    Logger.Mild("Registering to " + x.endpoint[:32])
    a = requests.request(x.method, x.endpoint.replace("(MAILERXDD)", email), data=x.payload, headers=x.headers)
    if str(a.status_code) == "200":
        Logger.Success("Registered!")
        succ = succ + 1
    else:
        Logger.Failed("Failed registering :( (" + str(a.status_code) + ")")
        fail = fail + 1
        
Logger.Success(f"Finished with {(succ / (succ + fail)) * 100}% success rate!")
input()
