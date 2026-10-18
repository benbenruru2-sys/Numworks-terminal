# Greeenux.py

#### This custom terminal was made by `GreeenMatter` (`@greeenmatter` on discord) (mail me [here](mailto:benbenruru2@gmail.com?subject=greeenux%20terminal))
---
Notes:  
- *No AI was used to create this project*  
- *All the code has been tested on a real calculator*  
- *This project was inspired by a friend of mine*  
- *This is meant to be used on a NumWorks calculator*

---
## Get started
The [greeenux](https://github.com/benbenruru2-sys/Numworks-terminal/blob/main/greeenux.py) terminal was created to unify all the computing goodness of a traditional calculator (+some extra) in a single place.  
It is filled to the brim with useful features such as:  
- conversions
- built-in help menu
- advanced result history
- works even if exam mode is enabled (*wink wink*)  
- lots of data-driven commands
- much more to come...


---
### Help menu

The help menu can be triggered using '`help`' or '`cl`'. It will list every command with a short description.  
For more help on a specific command, you can use '`help <cmd>`'. For example, '`help  quit`' will display:  
- Detailed explanation of the command and its arguments
- A usage example
- Backend command name
- All aliases of that command

Aliases:  
A specific command has multiple aliases, for instance '`end`','`stop`','`exit`','`close`','`kill`' and '`quit`' lead to the same result (*in this case quitting the program*)

---
### Evaluating expressions  

To eval expressions, simply type them in the terminal : '`5+5`' will give you 10  
You can also use an alias of eval + the expression (example: '`eval 5+5`')

---
### History manager

The [greeenux](https://github.com/benbenruru2-sys/Numworks-terminal/blob/main/greeenux.py) is equipped with an advanced result history manager.  
Use '`h cl`' to view the built-in help in the terminal  
You can use `h` or `ans` to reuse the last result in an expression  

Usage:  
```powershell
eval 5+5 # Adds 10 to the result history
h l # Shows the last result in history (in this case 10)
eval (h+5)*10 # Will return (10+5)*10 = 15*10 = 150
# eval will ignore the history if the last item in history is not a float or an int

# You can clear the history:
h c # A cleared history has a default of 1

# You can also add values manually to the history:
h n 10 # Adds 10 to the history

# You can list the whole history:
h a # List the whole history

# For convenience, you can also do:
hl -> h l # The code replaces 'hl' with 'h l'
hc -> h c
hn -> h n
ha -> h a 
# I added that since typing on a calculator takes a long time

# Meaning of letters:
h l #History last
h c #History clear
h n #History new
h a #History all
```

---
### Conversions
The [greeenux](https://github.com/benbenruru2-sys/Numworks-terminal/blob/main/greeenux.py) has an advanced, and highly configurable conversion system.  
To see all available conversions, type '`cv cl`' (`cv` is an alias of `convert`)  
The entire conversion system is data-driven in json: 
```json
{
    "c,f":{"ex":"x*1.8+32","help":"Convert c° to f"},
    "f,c":{"ex":"(x-32)/1.8","help":"Convert f to c°"},
    "c,k":{"ex":"x+273.15","help":"Convert c° to kelvin"},
    "k,c":{"ex":"x-273.15","help":"Convert kelvin to c°"},
    "cm,in":{"ex":"x/2.54","help":"Convert cm to inches"},
    "in,cm":{"ex":"x*2.54","help":"Convert inches to cm"},
    "cm,ft":{"ex":"x/30.48","help":"Convert cm to feet"},
    "ft,cm":{"ex":"x*30.48","help":"Convert feet to cm"},
    "kg,pd":{"ex":"x*2.20462262","help":"Convert kg to pound"},
    "pd,kg":{"ex":"x/2.20462262","help":"Convert pound to kg"},
    "kg,oz":{"ex":"x*35.27396195","help":"Convert kg to ounce"},
    "oz,kg":{"ex":"x/35.27396195","help":"Convert ounce to kg"},
    "km,mi":{"ex":"x/1.609344","help":"Convert km to miles"},
    "mi,km":{"ex":"x*1.609344","help":"Convert miles to km"},
    "m,ft":{"ex":"x*3.280839895","help":"Convert meters to feet"},
    "ft,m":{"ex":"x/3.280839895","help":"Convert feet to meters"},
    "l,gal":{"ex":"x/3.785411784","help":"Convert liters to US gallons"},
    "gal,l":{"ex":"x*3.785411784","help":"Convert US gallons to liters"},
    "kmh,mph":{"ex":"x/1.609344","help":"Convert km/h to mph"},
    "mph,kmh":{"ex":"x*1.609344","help":"Convert mph to km/h"},
    "deg,rad":{"ex":"x*0.0174532925","help":"Convert degrees to radians"},
    "rad,deg":{"ex":"x*57.2957795","help":"Convert radians to degrees"}
}
```

Usage:
```powershell
cv # Tells you to use 'cv cl' for help
cv cl # Shows every available conversion
cv c,f 10 # Convert 10 c° into Fahrenheit (in this case 50)
cv f,c 50 # Convert 50 Fahrenheit into c° (in this case 10)
```

---
### Cat

```
    /_/\ 
    (0-0) 
 _/    |
   ____/
```

---
### Dev commands

'`pass`': Just continues and does nothing (used to test `helpatlas` edge cases)  
'`atlas`': Crashes (used to test `atlas` edge cases)  
'`crash`': Crashes (used to test error handling)

---
### Error handling
The [greeenux](https://github.com/benbenruru2-sys/Numworks-terminal/blob/main/greeenux.py) will automatically restart if it crashes (it will also display the reason of the crash)