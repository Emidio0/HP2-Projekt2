# HP2-Projekt2

I detta projekt ska jag skriva ett program som läser av en temp-sensor(ds18x20) och skriver ut <unit id> <sensor id> <measurement> i terminalen. Ett exempel på hur en utskrift kan se ut är: e6614103e71d8d2e 28d6445c090000da 23.75. Programmet ska kunna se hur många temp-sensorer som är inkopplade. Det ska finnas en config.json-fil som säger vilken pin vi ska använda oss av och hur långt intervallet ska vara mellan varje utskrift. 


Detta program ska skrivas i micro Python så jag behöver använda mig av några moduler såsom onewire, machine och ds18x20. Jag skrev programmet i VS code så för att kunna köra programmet i Pico var jag tvungen att göra några saker innan jag kunde köra koden. Det första jag gjorde var att ladda ner micro Python till min pico, detta gjordes genom att hålla in BOOTSEL knappen på picon samtidigt som jag kopplade den till datorn. Jag ladda sedan ner micro Python från Google och klistrade in den i Picon. 


När jag kände mig klar med mitt program i VS code använde jag mig av Thonny för att köra programmet i Picon. 
