#!/usr/bin/python3
import threading
import time
import time
import serial

# from uart_example import _Getch

def run_yolov5():
    while True:
        # 这里是运行yolov5的代码
        print("Running yolov5...\n")
        #time.sleep(1)  # 模拟yolov5运行

def uart_send():
    while True:
        print("串口发送...\n")
        #time.sleep(1)  # 模拟yolov5运行

if __name__ == "__main__":
    t1 = threading.Thread(target=run_yolov5)
    t2 = threading.Thread(target=uart_send)

    t1.start()
    t2.start()

    t1.join()
    t2.join()