import psutil
from datetime import datetime
from time import sleep

log_file = open('system_log.txt', 'w')
print("--- [BÀI 1] CHƯƠNG TRÌNH GIÁM SÁT ĐANG CHẠY ---")

try:
    while True:
        cpu_avg = sum(psutil.cpu_percent(interval=1, percpu=True)) / psutil.cpu_count()
        ram = psutil.virtual_memory()
        disk_pct = psutil.disk_usage('/').percent
        status = 'CRITICAL' if cpu_avg >= 70 else 'WARNING' if cpu_avg >= 30 else 'NORMAL'
        
        line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] CPU: {cpu_avg:.1f}% | RAM: {ram.used // (1024**2)}/{ram.total // (1024**2)} MB ({ram.percent}%) | Disk: {disk_pct}% | Status: {status}"
        print(line)
        log_file.write(line + '\n')
        log_file.flush()
        sleep(2)
except KeyboardInterrupt:
    print('\nDừng giám sát.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')