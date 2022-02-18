import bme280
import smbus2
from gpiozero import CPUTemperature
from ds18b20 import DS18B20

port = 1
address = 0x76
bus= smbus2.SMBus(port)

calibration = bme280.load_calibration_params(bus,address)

bme280_data = bme280.sample(bus,address, calibration)
humidity = bme280_data.humidity
pressure = bme280_data.pressure
temperature = bme280_data.temperature

cpu = CPUTemperature()

sensor = DS18B20()
outdoor_temp = sensor.get_temperature()

print(bme280_data.id,humidity,pressure,temperature,cpu.temperature,outdoor_temp)

