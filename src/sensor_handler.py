import time
import adafruit_dht
import board

class SensorHandler:
    def __init__(self):
        self.device = adafruit_dht.DHT11(board.D4)

    def get_sample(self):
        # Read sensor data
        return self.device

if __name__ == "__main__":

    sh = SensorHandler()

    try:
        data = sh.get_sample()
        while True:

            print(f"Temp: {data.temperature} C")
            print(f"Hum: {data.humidity} %")

            time.sleep(5)

    except KeyboardInterrupt:
        print("[Exiting]")
    except RuntimeError as e:
        print("[ERR] RunTimeError: e")