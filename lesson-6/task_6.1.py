# PEP-8
import time


class TrafficLight:
    __color = None

    def running(self, __color="red"):
        while True:
            if __color == "red":
                print("red")
                time.sleep(7)
                __color = "yellow"
            else:
                if __color == "yellow":
                    print("yellow")
                    time.sleep(2)
                    __color = "green"
                else:
                    print("green")
                    time.sleep(5)
                    __color = "red"


tl = TrafficLight()
tl.running()
