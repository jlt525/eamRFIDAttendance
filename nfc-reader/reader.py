import requests
import sys
from datetime import datetime
from time import sleep
import nfc
from nfc.clf import RemoteTarget

DEBUG = True

URL = 'https://attend.cantor.local/api/register/'

ROOMID = 9305

def send_data(cardID):
    inTime = datetime.strftime(datetime.now(), '%Y-%m-%dT%XZ')

    requestData = { 'roomid': ROOMID, 'cardserial': cardID, 'timestamp': inTime }

    if DEBUG == True:
        print("request:", requestData)

    postRequest = requests.post(URL, json = requestData, verify=False)

    if postRequest.status_code == 201:
        if DEBUG == True:
            print("[DEBUG] Registered Attendance")
        return True

    else:
        if DEBUG == True:
            print("[DEBUG] Post request failed with status code:", postRequest.status_code)
        return False

def on_connect(tag):
    try:
        saneCardID = str(tag).split()[1][3:].lower()

        if DEBUG == True:
            print("[DEBUG] Serial number from card:", saneCardID)

        send_data(saneCardID)

        return(True)

    except:
        return(False)

def main():
    if DEBUG == True:
        print("DEBUG ENABLED")
        print("[DEBUG] Start of main")
        print("[DEBUG] Using server with url:", URL)

    with nfc.ContactlessFrontend('usb:072f:2200') as clf:
        if DEBUG == True:
            print("[DEBUG] Initialised clf")

        while True:
            if DEBUG == True:
                print("[DEBUG] Entered main while loop")
            try:
                if DEBUG == True:
                    print("[DEBUG] Entered try statement")

                tag = clf.connect(rdwr={'on-connect': on_connect, 'beep-on-connect': True})

                if DEBUG == True:
                    print("[DEBUG] Got card serial number and requested attendance")

                sleep(1)

            except KeyboardInterrupt:
                clf.close()
                sys.exit(f"\nKeyboardInterrupt detected.Exiting")

if __name__ == "__main__":
    main()
