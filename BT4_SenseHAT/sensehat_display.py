from sense_emu import SenseHat
import time

sense = SenseHat()

# Hiển thị dòng chữ chào mừng với màu xanh lá
sense.show_message('Hello IoT!', text_colour=[0, 255, 0], scroll_speed=0.08)
time.sleep(1)
sense.clear()
print('Text hien thi xong tren Sense HAT Emulator.')