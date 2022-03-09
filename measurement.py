import bme280
import smbus2
from gpiozero import CPUTemperature
from ds18b20 import DS18B20
from weather_repo import addWeather
import requests
from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration = bme280.load_calibration_params(bus, address)

bme280_data = bme280.sample(bus, address, calibration)
humidity = bme280_data.humidity
pressure = bme280_data.pressure
temperature = bme280_data.temperature

cpu = CPUTemperature()

sensor = DS18B20()
outdoor_temp = sensor.get_temperature()

addWeather(humidity, pressure, cpu.temperature, temperature, outdoor_temp)

secret = os.environ.get('SECRET')
requests.get(f"http://127.0.0.1:3000/revalidate?secret={secret}")
