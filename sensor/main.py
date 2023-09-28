import json
import ds18x20
import onewire
import machine
import time

# Generera ett unikt ID för Raspberry Pi Pico
pico_id = machine.unique_id()

# Läs konfigurationsdata från filen 'config.json'
with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

# Hämta pin-numret från filen config.json
pin = config_data.get("pin")
interval = config_data.get("interval")

# Skapa en Pin-instans för att kommunicera med DS18B20-sensorn
ds_pin = machine.Pin(pin)

# Initiera DS18B20-sensorn med hjälp av OneWire-protokollet
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Sök efter DS18B20-sensorer och spara deras ROM-adresser
roms = ds_sensor.scan()


while True:
    
    ds_sensor.convert_temp() # Starta temperaturmätningen
    time.sleep_ms(interval)

    for rom in roms: 
        temp = ds_sensor.read_temp(rom)# Läs temperaturen från den aktuella sensorn
        print(f"{pico_id.hex()} {rom.hex()} {temp:.2f}")  