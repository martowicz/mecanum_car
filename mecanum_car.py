from machine import Pin , PWM
import network,socket
from utime import sleep

stby01 = Pin(5,Pin.OUT)
stby23 = Pin(12,Pin.OUT)

stby01.value(1)
stby23.value(1)

in10 = Pin(6,Pin.OUT)
in11 = Pin(4,Pin.OUT)
in12 = Pin(13,Pin.OUT)
in13 = Pin(11,Pin.OUT)

in20 = Pin(7,Pin.OUT)
in21 = Pin(3,Pin.OUT)
in22 = Pin(14,Pin.OUT)
in23 = Pin(10,Pin.OUT)

m0 = PWM(Pin(8))
m1 = PWM(Pin(2))
m2 = PWM(Pin(15))
m3 = PWM(Pin(9))

m0.freq(1000)
m1.freq(1000)
m2.freq(1000)
m3.freq(1000)

def StopMotors():
    in10.value(0)
    in20.value(0)
    in11.value(0)
    in21.value(0)
    in12.value(0)
    in22.value(0)
    in13.value(0)
    in23.value(0)

    
        
def Forward(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(1)
    in20.value(0)
    in11.value(1)
    in21.value(0)
    in12.value(1)
    in22.value(0)
    in13.value(1)
    in23.value(0)
    m0.duty_u16(pw)
    m1.duty_u16(pw)
    m2.duty_u16(pw)
    m3.duty_u16(pw)
    
def Backward(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(0)
    in20.value(1)
    in11.value(0)
    in21.value(1)
    in12.value(0)
    in22.value(1)
    in13.value(0)
    in23.value(1)
    m0.duty_u16(pw)
    m1.duty_u16(pw)
    m2.duty_u16(pw)
    m3.duty_u16(pw)
    
def Right(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(0)
    in20.value(1)
    in11.value(1)
    in21.value(0)
    in12.value(1)
    in22.value(0)
    in13.value(0)
    in23.value(1)
    m0.duty_u16(pw)
    m1.duty_u16(pw)
    m2.duty_u16(pw)
    m3.duty_u16(pw)

def Left(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(1)
    in20.value(0)
    in11.value(0)
    in21.value(1)
    in12.value(0)
    in22.value(1)
    in13.value(1)
    in23.value(0)
    m0.duty_u16(pw)
    m1.duty_u16(pw)
    m2.duty_u16(pw)
    m3.duty_u16(pw)
    
def Spin(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(1)
    in20.value(0)
    in11.value(0)
    in21.value(1)
    in12.value(1)
    in22.value(0)
    in13.value(0)
    in23.value(1)
    m0.duty_u16(pw)
    m1.duty_u16(pw)
    m2.duty_u16(pw)
    m3.duty_u16(pw)
    
def FrontRight(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(0)
    in20.value(0)
    in11.value(1)
    in21.value(0)
    in12.value(1)
    in22.value(0)
    in13.value(0)
    in23.value(0)
    m1.duty_u16(pw)
    m2.duty_u16(pw)
    
def FrontLeft(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(1)
    in20.value(0)
    in11.value(0)
    in21.value(0)
    in12.value(0)
    in22.value(0)
    in13.value(1)
    in23.value(0)
    m0.duty_u16(pw)
    m3.duty_u16(pw)
    
def BackRight(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(0)
    in20.value(1)
    in11.value(0)
    in21.value(0)
    in12.value(0)
    in22.value(0)
    in13.value(0)
    in23.value(1)
    m0.duty_u16(pw)
    m3.duty_u16(pw)

def BackLeft(power=100): #default=100
    #power is integer from 0 to 100
    pw = int((power*65536)/100) 
    in10.value(0)
    in20.value(0)
    in11.value(0)
    in21.value(1)
    in12.value(0)
    in22.value(1)
    in13.value(0)
    in23.value(0)
    m1.duty_u16(pw)
    m2.duty_u16(pw)

ssid='UPC26B4DE3'
password='z4zjxjVhtWa2'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>AIOTA car</title>
            </head>
            <center><b>
            
            <table>
            <!--<tr> rozpoczyna nowy wiersz w tabeli, a <td> nową komórkę w tabeli-->
                <tr>
                    <td>
                        <form action="./frontleft">
                            <input type="submit" value=" " style="height:150px; width:150px; background-color: #2b693d; font-size: 30px; border-radius: 10px;" />
                        </form>
                    </td>
                    <td>
                        <form action="./forward">
                            <input type="submit" value="FRONT" style="height:150px; width:150px; background-color: black; font-size: 30px; color: white; border-radius: 10px;" />
                        </form>
                    </td>
                    <td>
                        <form action="./frontright">
                            <input type="submit" value=" " style="height:150px; width:150px; background-color: #a61414; font-size: 30px; border-radius: 10px;" />
                        </form>
                    </td>
                </tr>
                <tr>
                    <td>
                        <form action="./left">
                            <input type="submit" value="LEFT" style="height:150px; width:150px; background-color: #2b693d; font-size: 30px; border-radius: 10px; color: white;" />
                        </form>
                    </td>
                    <td>
                        <form action="./stop">
                            <input type="submit" value="STOP" style="height:150px; width:150px; background-color: black; font-size: 30px; color: white; border-radius: 30px;" />
                        </form>
                    </td>
                    <td>
                        <form action="./right">
                            <input type="submit" value="RIGHT" style="height:150px; width:150px; background-color: #a61414; font-size: 30px; border-radius: 10px; color: white;" />
                        </form>
                    </td>
                </tr>
                <tr>
                    <td>
                        <form action="./backleft">
                            <input type="submit" value=" " style="height:150px; width:150px; background-color: #2b693d; font-size: 30px; border-radius: 10px;"  />
                        </form>
                    </td>
                    <td>
                        <form action="./backward">
                            <input type="submit" value="BACK" style="height:150px; width:150px; background-color: black; font-size: 30px; color: white; border-radius: 10px;" />
                        </form>
                    </td>
                    <td>
                        <form action="./backright">
                            <input type="submit" value=" " style="height:150px; width:150px; background-color: #a61414; font-size: 30px; border-radius: 10px;" />
                        </form>
                    </td>
                </tr>
                <tr>
                    <td>
                    </td>
                    <td>
                        <form action="./spin">
                            <input type="submit" value="SPIN" style="height:150px; width:150px; background-color: white; font-size: 30px; border-radius: 10px;" />
                        </form>
                    </td>
                    <td>
                    </td>
                </tr>
            </table>
            <h1 style="font-size: 50px; margin-top: 50px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                AIOTA Car Control
            </h1>
        </b>
        </html>
                

            """
    return str(html)

def serve(connection):
    #Start web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/forward?':
            Forward()
        elif request =='/left?':
            Left()
        elif request =='/stop?':
            StopMotors()
        elif request =='/right?':
            Right()
        elif request =='/backward?':
            Backward()
        elif request =='/backleft?':
            BackLeft()
        elif request =='/backright?':
            BackRight()
        elif request =='/frontleft?':
            FrontLeft()
        elif request =='/frontright?':
            FrontRight()
        elif request =='/spin?':
            Spin()
        html = webpage()
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()

