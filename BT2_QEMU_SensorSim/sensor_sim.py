import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# Thiet lap thong so mo phong
mean = 25      # Nhiet do trung binh
std_dev = 2    # Do lech chuan (Gaussian)
num_samples = 50
samples = []

print("--- [BAI 2] MO PHONG CAM BIEN GAUSSIAN ---")

try:
    for i in range(num_samples):
        # Sinh du lieu ngau nhien theo phan phoi Gaussian
        reading = np.random.normal(mean, std_dev)
        samples.append(reading)
        
        # In ket qua ra terminal (ngat dong neu can)
        print(f"Sample {i+1}/{num_samples}: {reading:.2f} C")
        sleep(0.1)

    # Ve bieu do sau khi thu thap du lieu
    plt.figure(figsize=(10, 6))
    plt.plot(samples, marker='o', linestyle='-', color='b', label='Nhiet do')
    plt.axhline(y=mean, color='r', linestyle='--', label='Trung binh')
    
    plt.title('Mo phong du lieu cam bien Nhiet do (Gaussian Distribution)')
    plt.xlabel('Mau thu')
    plt.ylabel('Gia tri (C)')
    plt.legend()
    plt.grid(True)
    
    # Luu bieu do ra file thay vi hien thi (vi chay tren QEMU/Server khong co GUI)
    plt.savefig('sensor_chart.png')
    print("--- Da luu bieu do vao file 'sensor_chart.png' ---")

except Exception as e:
    print(f"Co loi xay ra: {e}")

# Luu y quan trong: Phai co dong trong o cuoi cung file