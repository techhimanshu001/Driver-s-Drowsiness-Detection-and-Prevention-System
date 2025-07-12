import time
import random
import matplotlib.pyplot as plt

class Vehicle:
    def __init__(self):
        self.speed = 0
        self.max_speed = 120
        self.min_speed = 0
        self.drowsiness_threshold = 30
        self.drowsy = False
        self.history = {'time': [], 'speed': []}

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += random.randint(5, 15)
            if self.speed > self.max_speed:
                self.speed = self.max_speed

    def decelerate(self):
        if self.speed > self.min_speed:
            self.speed -= random.randint(5, 10)
            if self.speed < self.min_speed:
                self.speed = self.min_speed

    def update_history(self, time_elapsed):
        self.history['time'].append(time_elapsed)
        self.history['speed'].append(self.speed)

    def check_drowsiness(self):
        if self.speed < self.drowsiness_threshold:
            self.drowsy = True
        else:
            self.drowsy = False

    def plot_speed(self):
        plt.plot(self.history['time'], self.history['speed'])
        plt.xlabel('Time (seconds)')
        plt.ylabel('Speed (km/h)')
        plt.title('Vehicle Speed Over Time')
        plt.show()

def main():
    vehicle = Vehicle()
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time

        vehicle.accelerate()
        vehicle.update_history(elapsed_time)
        vehicle.check_drowsiness()

        if vehicle.drowsy:
            print("Driver is drowsy!")

        if elapsed_time >= 60:
            break

        time.sleep(1)

    vehicle.plot_speed()

if __name__ == "__main__":
    main()
