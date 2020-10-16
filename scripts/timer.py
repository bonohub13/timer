#!/usr/bin/python3
import time
from termcolor import colored

class CountdownTimer:
    def __init__(self):
        self.init_time = int(input("input time to countdown [minutes]: "))
        self.init_time = self.init_time*60
        self.counter = 0

    def __timerloop(self):
        while self.counter < self.init_time:
            time.sleep(1)
            self.counter += 1
            print("time left: [ {}:{} ]\r".format((self.init_time-self.counter)//60, (self.init_time-self.counter)%60), end="")

    def run(self):
        try:
            self.__timerloop()
        except KeyboardInterrupt:
            print("\r", end="")
            print("timer halted.")

class CountupTimer:
    def __init__(self):
        self.counter = 0

    def __timerloop(self):
        while True:
            time.sleep(1)
            self.counter += 1
            seconds_tmp = self.counter%60
            seconds = seconds_tmp if seconds_tmp > 9 else "0{}".format(seconds_tmp)
            minutes_tmp = self.counter//60
            minutes = minutes_tmp if minutes_tmp > 9 else "0{}".format(minutes_tmp)
            font_color = "white" if minutes_tmp < 3 else if minutes_tmp < 5 "yellow" else "red"
            self.time = "[ {}:{} ]\r".format(minutes, seconds)
            print(colored("elapsed time: {}\r".format(self.time), font_color), end="")

    def run(self):
        try:
            self.__timerloop()
        except KeyboardInterrupt:
            print("\r", end="")
            print("timer halted at " + self.time)

if __name__ == "__main__":
    timer = CountupTimer()
    timer.run()
