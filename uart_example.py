#!/usr/bin/python3
import time
import serial

encounting_barrier = True


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

#class AvoidObarrier:


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

try:
    # Send a simple header
    print("*******************获取串口通信指令*******************")
    print("*********************输入w前进**********************")
    print("*********************输入s后退**********************")
    print("*********************输入a左转**********************")
    print("*********************输入d右转**********************")
    print("*********************输入g刹车**********************")
    print("*********************输入+加速**********************")
    print("*********************输入q结束**********************")
    print("                         w                         ")
    print("                       a s d                       ")
    
    while True:
        if encounting_barrier == True:
            #直接开始避障
            #1.左转45°
            serial_port.write("a\r\n".encode())
            time.sleep(1)
            serial_port.write("g\r\n".encode())
            
            # #2.向前走1m
            serial_port.write("w\r\n".encode())
            time.sleep(1)
            serial_port.write("g\r\n".encode())

            # #3.右转45°
            serial_port.write("d\r\n".encode())
            time.sleep(1)
            serial_port.write("g\r\n".encode())

            # #4.往前走一步
            serial_port.write("w\r\n".encode())
            time.sleep(1)
            serial_port.write("g\r\n".encode())


        if serial_port.inWaiting() > 0:
            encounting_barrier = False
            getch = _Getch()
            ch = getch()
            
            if ch == 'w':  
                print("前进")
                serial_port.write("w\r\n".encode())
            elif ch == 's':
                print("后退")
                serial_port.write("s\r\n".encode())
            elif ch == 'a':
                print("左转")
                serial_port.write("a\r\n".encode())
            elif ch == 'd':
                print("右转") 
                serial_port.write("d\r\n".encode())
            elif ch == 'g':
                print("刹车") 
                serial_port.write("g\r\n".encode())
            elif ch == '+':
                print("加速") 
                serial_port.write("+\r\n".encode())
            elif(ch == 'k'):
                encounting_barrier = True
            elif(ch == 'q'):
                break
            
            
            


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
