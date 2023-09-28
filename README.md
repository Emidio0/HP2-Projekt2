# HP2-Projekt2

# Temperaturmätning med Raspberry Pi Pico och DS18B20

För att använda koden behöver du:

- En Raspberry Pi Pico
- En DS18B20-temperatursensor

I detta projekt ska jag skriva ett program som läser av en temp-sensor(ds18x20) och skriver ut <unit id> <sensor id> <measurement> i terminalen. Ett exempel på hur en utskrift kan se ut är: e6614103e71d8d2e 28d6445c090000da 23.75. Programmet ska kunna se hur många temp-sensorer som är inkopplade. Det ska finnas en config.json-fil som säger vilken pin vi ska använda oss av och hur långt intervallet ska vara mellan varje utskrift. 


## Installation

För att köra koden på din Raspberry Pi Pico, följ dessa steg:

1. **Ladda ner MicroPython till Raspberry Pi Pico**
   - Håll in BOOTSEL-knappen på Picon samtidigt som du ansluter den till datorn.
   - Ladda ner MicroPython och överför den till Picon.

2. **Kör koden med Thonny**
   - Öppna koden i en lämplig IDE, t.ex. VS Code.
   - Anslut din Pico till datorn via USB.
   - Använd Thonny eller liknande för att köra koden på din Pico.

---
