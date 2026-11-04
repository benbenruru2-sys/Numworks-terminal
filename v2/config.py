# This is the python config file
# Do not edit unless you know what you are doing

DEBUG=False
separator = "-"*40

atlas={ # Atlas for all commands, thanks to this, 'help' and 'cl' will lead to the same command
    "end":"stop",
    "stop":"stop",
    "exit":"stop",
    "close":"stop",
    "kill":"stop",
    "quit":"stop",
    "help":"cl",
    "cl":"cl",
    "e":"eval",
    "eval":"eval",
    "calc":"eval",
    "crash":"crash",
    "msg":"msg",
    "print":"msg",
    "root":"sqrt",
    "sqrt":"sqrt",
    "pyg":"pyg",
    "pyg+":"pyg+",
    "p2":"p2",
    "conv":"conv",
    "cv":"conv",
    "convert":"conv",
    "conversion":"conv",
    "convertion":"conv",
    "cat":"cat",
    "meow":"cat",
    "h":"history",
    "hst":"history",
    "history":"history",
    "ans":"history",
    "atlas":"atlas",
    "pass":"pass",
    "":"pass",
    "pe":"pe",
    "pureeval":"pe",
    "pureval":"pe",
    "compile":"pe",
    "exec":"pe",
    "variables":"var",
    "variable":"var",
    "var":"var",
    "v":"var"
}

helpatlas={ # The '<this:cmd>' gets replaced by the command the user entered, so even if the backend name is 'cl', if the user used 'help', 'help' will be displayed instead of a different command that they might not know
    "stop":"The '<this:cmd>' command is used to close the calculator app",
    "cl":"The '<this:cmd> <str>'  command is used to display general help and help about specific commands\nExemple: '<this:cmd> cl' ",
    "eval":"The '<this:cmd> <str>' command is used to return the result of a expression.\n You can remplace a value with 'h' or 'ans', they will be replaced by the last result\nExemple: '<this:cmd> (5+3)*h' (output is 8 if ans=1)",
    "crash":"The '<this:cmd>' command is only meant to be used for debbuging purposes. It ensures the app crashes in a smooth way",
    "msg":"The '<this:cmd> <str>' command is used to print text to the terminal\nExemple: '<this:cmd> hello world!'",
    "sqrt":"The '<this:cmd> <float>' command returns the square root of a number\nExemple: '<this:cmd> 25' (output is 5)",
    "pyg":"The '<this:cmd> <float> <float>' command returns the last side of the triangle using the pythagore theorem\nFirst and second parameter are used to specify the lengh of two sides\nExemple: '<this:cmd> 3 4' (output is 5)",
    "pyg+":"The '<this:cmd> <float> <float> <float>' command is used to dertermine if a triangle is rectangular\nFirst and second parameter are used to specify the lengh of two short sides\nThird parameter is used to specify the lengh of the long side\nExemple: '<this:cmd> 3 4 5' (output is 'this triangle is rectangular')",
    "p2":"The '<this:cmd> <float> <int>' command is used to multiply a number by successive powers of 2\nFirst parameter is the number to multiply\nSecond parameter is how many powers of 2 to compute: it prints one result for each power from 2^1 up to 2^<int>\nExemple: '<this:cmd> 3 4' (output is 6.0, 12.0, 24.0 and 48.0, one per line)",
    "conv":"The '<this:cmd> <str> <float>' command is used to convert number betwen diferent units\nDo '<this:cmd> cl' for help on available conversions\nExemple: '<this:cmd> c,f 20' (output is 68)",
    "cat":"MEOW",
    "history":"The '<this:cmd> <str> <float>' command is used to manage result memory\nRead the built in documentation using '<this:cmd> cl' for more info\nExemple: '<this:cmd> a' (output is all the history)",
    "var":"The '<this:cmd> <str> <str> <str>' command is used to manage variables\nRead the built in documentation using '<this:cmd> cl' for more info\nExemple: '<this:cmd> a' (output is every variable)",
    "pe":"The '<this:cmd> <str>' command execute the code provided as a argument. If the argument is a known variable (sutch as '<this:cmd> atlas', it will print the 'atlas' variable)\nExample: '<this:cmd> print('hello world')' (output is 'hello world')"    
}

exp={ # Thoses are common expressions, tied to the 'expthis()' function
    "yes":"yes",
    "on":"yes",
    "y":"yes",
    "no":"no",
    "off":"no",
    "n":"no",
    "a":"all",
    "all":"all",
    "help":"cl",
    "cl":"cl",
    "c":"clear",
    "clear":"clear",
    "new":"new",
    "n":"new",
    "l":"last",
    "last":"last"
}

argatlas={ # Everything in here will be replaced, even before the creations of the arguments
    "ha":"h a",
    "hc":"h c",
    "hl":"h l",
    "hn":"h n"
}

conversions={ # All data driven conversions, in this case 'ex' is the convertion formula, and the 'x' gets replaced by the number to convert
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

toremove=["cmd.","cmd","()","exec.","  "] # Everything in here will be removed before code execution
catchar = [r"    /_/\ ",r"    (0-0) ",r" _/    |",r"   ____/"] # Hes so silly and cute