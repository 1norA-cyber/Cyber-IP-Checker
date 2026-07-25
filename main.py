import requests

#git_ip
def get_ip ():
    user_ip =input("Please enter your ip address:")
    while user_ip == "" :  user_ip =input("Please enter your ip address:")
    return user_ip

#validation  lib:ipaddress
def valid_ip (user_ip):
    parts= user_ip.split('.')

    if len(parts) != 4:
        return False

    try:
        parts=list(map(int,parts))
    except  ValueError :
        return False
    return all(0 <= part <= 255 for part in parts)

#generate_report + requests lib
def generate_report (user_ip):
    response = requests.get(f"http://ip-api.com/json/{user_ip}")
    data = response.json()
    report = {'IP Address':user_ip, 'Country': data.get['country','Unknown'] ,
               'ISP' : data.get['isp','Unknown'] , 'City' : data.get['city','Unknown']}
    return report

#print_report
def print_report (report):
    print(report)

#Run
def main():
    user_ip = get_ip()
    if valid_ip(user_ip) : print_report(generate_report(user_ip))
    else:print("IP is not valid")


if __name__ == "__main__": main()
