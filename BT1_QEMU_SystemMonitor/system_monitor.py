import psutil
from datetime import datetime
from time import sleep

# Mo file log
log_file = open('system_log.txt', 'w')
print("--- [BAI 1] CHUONG TRINH GIAM SAT DANG CHAY ---")

try:
    while True:
        # Tinh toan thong so
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_usage) / psutil.cpu_count()
        ram = psutil.virtual_memory()
        disk_pct = psutil.disk_usage('/').percent

        # Phan loai trang thai
        status = 'CRITICAL' if cpu_avg >= 70 else 'WARNING' if cpu_avg >= 30 else 'NORMAL'

        # Định dạng dòng log (ngat dong de khong bi qua dai)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ram_used_mb = ram.used // (1024**2)
        ram_total_mb = ram.total // (1024**2)

        line = (f"[{timestamp}] CPU: {cpu_avg:.1f}% | "
                f"RAM: {ram_used_mb}/{ram_total_mb} MB ({ram.percent}%) | "
                f"Disk: {disk_pct}% | Status: {status}")

        print(line)
        log_file.write(line + '\n')
        log_file.flush()
        sleep(2)
except KeyboardInterrupt:
    print('\nDung giam sat.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')

# Luu y: Phai co mot dong trong o cuoi cung file de flake8 khong bao loi W292