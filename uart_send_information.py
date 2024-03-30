#!/usr/bin/python3
import time
import serial
import subprocess

# 串口设备的路径
serial_port = "/dev/ttyTHS1"

# sudo密码
password = "robot806"

# 创建一个Popen对象
proc = subprocess.Popen(['sudo', '-S', 'chmod', '777', serial_port], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# 使用communicate方法发送密码到stdin
stdout, stderr = proc.communicate((password + '\n').encode())

# 检查是否有错误
if proc.returncode != 0:
    print(f"Error: {stderr}")
else:
    print(f"Output: {stdout}")

# 这里定义一下lab对应的数字就好
labels2number = {'person': 0, 'bicycle': 1, 'car': 2, 'motorcycle': 3, 
                 'airplane': 4, 'bus': 5, 'train': 6, 'truck': 7, 'boat': 8, 
                 'traffic light': 9, 'fire hydrant': 10, 'stop sign': 11, 
                 'parking meter': 12, 'bench': 13, 'bird': 14, 'cat': 15, 
                 'dog': 16, 'horse': 17, 'sheep': 18, 'cow': 19, 'elephant': 20, 
                 'bear': 21, 'zebra': 22, 'giraffe': 23, 'backpack': 24, 
                 'umbrella': 25, 'handbag': 26, 'tie': 27, 'suitcase': 28, 
                 'frisbee': 29, 'skis': 30, 'snowboard': 31, 'sports ball': 32, 
                 'kite': 33, 'baseball bat': 34, 'baseball glove': 35, 
                 'skateboard': 36, 'surfboard': 37, 'tennis racket': 38, 
                 'bottle': 39, 'wine glass': 40, 'cup': 41, 'fork': 42, 
                 'knife': 43, 'spoon': 44, 'bowl': 45, 'banana': 46, 'apple': 47, 
                 'sandwich': 48, 'orange': 49, 'broccoli': 50, 'carrot': 51, 
                 'hot dog': 52, 'pizza': 53, 'donut': 54, 'cake': 55, 'chair': 56,
                 'couch': 57, 'potted plant': 58, 'bed': 59, 'dining table': 60, 
                 'toilet': 61, 'tv': 62, 'laptop': 63, 'mouse': 64, 'remote': 65, 
                 'keyboard': 66, 'cell phone': 67, 'microwave': 68, 'oven': 69, 
                 'toaster': 70, 'sink': 71, 'refrigerator': 72, 'book': 73, 
                 'clock': 74, 'vase': 75, 'scissors': 76, 'teddy bear': 77, 
                 'hair drier': 78, 'toothbrush': 79}

serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)


def uart_send(lable,x,y1,y2):
    start_time = time.time()
    #期望输入的object_information是一个三元组类型 (laber,x,y)
    label_number = labels2number[lable]
    x,y1,y2 = int(x),int(y1),int(y2)
    # print(label_number,x,y)
    # 将整数转换为字节串  要不直接将整形转换为字符型然后再编码？
    # label_number = label_number.to_bytes(2, byteorder='little') 
    # x = x.to_bytes(2, byteorder='little')
    # y1 = y1.to_bytes(2, byteorder='little')
    # y2 = y2.to_bytes(2, byteorder='little')
    label_number,x,y1,y2 = str(label_number),str(x),str(y1),str(y2)
    key_space = ','
    line_space = '\n'
    #key_space_byte = key_space.encode()
    #line_space_byte = line_space.encode()
    # print(label_number,x,y)
    data = label_number+key_space+x+key_space+ y1 +key_space+ y2 + line_space
    print(data)
    serial_port.write(data.encode())
    # serial_port.write("g\r\n".encode())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The function took {execution_time} seconds to complete.")


