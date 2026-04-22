import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sensor_sim import SimUltrasonic, SimPotentiometer
from time import sleep

us = SimUltrasonic(echo=24, trigger=23, base_distance=50.0)
pot = SimPotentiometer(initial_value=0.4)
span = pot.value * 100

distances = []
for i in range(50):
    d = us.distance
    distances.append(d)
    print(f'Mẫu {i+1}/50: {d:.1f} cm')
    sleep(0.1)

fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(distances))
ax.plot(x, distances, 'b-', label='Khoảng cách (cm)')
ax.axhline(y=span, color='r', linestyle='--', label=f'Span = {span:.0f} cm')
ax.fill_between(x, 0, [min(d, span) for d in distances], alpha=0.2, color='red')
ax.legend()
plt.savefig('sensor_chart.png', dpi=150)
print('Saved: sensor_chart.png')