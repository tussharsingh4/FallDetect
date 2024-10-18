# src/data_collection.py
import smbus2
import time
import csv
import os

bus = smbus2.SMBus(1)  # I2C bus for MPU6050
address = 0x68  # MPU6050 address

# Initialize the sensor
def mpu_init():
    bus.write_byte_data(address, 0x6B, 0)

def read_mpu6050():
    acc_x = read_word_2c(0x3B)
    acc_y = read_word_2c(0x3D)
    acc_z = read_word_2c(0x3F)
    gyro_x = read_word_2c(0x43)
    gyro_y = read_word_2c(0x45)
    gyro_z = read_word_2c(0x47)
    return [acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z]

def read_word_2c(addr):
    high = bus.read_byte_data(address, addr)
    low = bus.read_byte_data(address, addr+1)
    val = (high << 8) + low
    return val - 65536 if val >= 0x8000 else val

def save_data(data):
    file_path = os.path.join('..', 'data', 'sensor_data.csv')
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Data Collection
mpu_init()
try:
    while True:
        sensor_data = read_mpu6050()
        timestamp = time.time()
        label = 0  # You can modify this manually while collecting fall vs non-fall data
        data_row = [timestamp] + sensor_data + [label]
        save_data(data_row)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Data collection stopped.")
