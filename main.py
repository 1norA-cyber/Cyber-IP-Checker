import requests
from datetime import datetime


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
    report = {'IP Address':user_ip, 'Country': data.get('country','Unknown') ,
               'ISP' : data.get('isp','Unknown') , 'City' : data.get('city','Unknown'),
             'Scan Date': datetime.now().strftime('%Y-%m-%d'),'Scan time': datetime.now().strftime('%H:%M:%S')}
    return report

#print_report
def print_report (report):
    print(report)
#Save report
def save_report(report):
    filename= f"{report['IP Address']}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(f'reports/{filename}','w') as new_report:
        new_report.write("Cyber_IP_Checker\n")
        new_report.write("======================\n")
        for key, value in report.items():
            new_report.write(f"{key}: {value}\n")

        print('file save successfully')

#Run
def main():
    while True:
        user_ip = get_ip()
        if valid_ip(user_ip) :
            reports = generate_report(user_ip)
            print_report(reports)
            save_report(reports)
            break
        else:print("IP is not valid")


if __name__ == "__main__": main()
