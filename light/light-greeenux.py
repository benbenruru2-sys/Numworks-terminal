import math
running = True
DEBUG = False
separator = "-"*40
def log(msg,type="DEBUG"):
    try:
        type = str(type).upper()
        msg = str(msg)
        if DEBUG:
            print(type,"> ", msg)
    except:
        print("DEBUG crashed!")
log("Debug is enabled!")
def help():
    global separator
    print(separator,"""
Commands :
-   stop : stop the program
-   msg <msg>: print a message
-   sqrt <num>: calculate the square root of a number
-   cl : show commands
-   p2 <start> <iteration>: multiply a number by 2 until it reach 1e+50
-   pyg <side1> <side2>: calculate the pythagorean theorem
-   eval <expression>: returns the result of the expression
-   pyg+ <side1> <side2> <side3>: provide 3 numbers and check if the triangle rectangular
-   conv <convtype> <num>: Used to make conversions, do 'conv help' for help
-   h <c,l,n,a> <str>: manage result history
-   cat : Silly cat
-   cl <help>: shows help menu
""",separator)
atlas={
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
    "pass":"pass"
}
helpatlas={
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
    "history":"The '<this:cmd> <str> <float>' command is used to manage result memory\nRead the built in documentation using '<this:cmd> cl' for more info\nExemple: '<this:cmd> a' (output is all the history)"
}
argatlas={
    "ha":"h a",
    "hc":"h c",
    "hl":"h l",
    "hn":"h n"
}
conversions={
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
toremove=["cmd.","cmd","()","exec.","exec","  "]
catchar = [r"    /_/\ ",r"    (0-0) ",r" _/    |",r"   ____/"]
history = [1]
def cat():
    global catchar
    for i in catchar:
        print(i)
def evalthis(input,historyidx=1):
    input = str(input)
    try:
        float(history[-1])
        input = input.replace("h",str(history[-historyidx]))
        input = input.replace("ans",str(history[-historyidx]))
    except:
        input = input.replace("h","")
        input = input.replace("ans","")
    return eval(input)
def main():
    global running
    global separator
    global toremove
    global conversions
    global history
    print(separator,"\nWelcome in Greeenux\nfor showing commands type : cl\n",separator)
    console = ""
    parameters = []
    nothing_found_count = 0
    cl_count = 0
    while running:
        console = input("\n> ").lower().strip()
        for i in argatlas:
            console = console.replace(i,argatlas[i])
        for i in toremove:
            console = console.replace(i,"")
        parameters = console.split(" ")[1:]
        console = console.split(" ")[0]
        log("Console: ",str(console))
        log("Parameters: ",str(parameters))
        if console in atlas:
            if not nothing_found_count == 0:
                nothing_found_count = nothing_found_count - 1
            log("Nothing found count: ",str(nothing_found_count))
            if atlas[console] == "stop":
                running = False
                raise Exception("Program has been stopped by user")
            elif atlas[console] == "cl":
                if parameters == []:
                    help()
                    cl_count = cl_count +1
                    log("Cl count: "+str(cl_count))
                    if cl_count == 3:
                        print(separator,"\nHey! looks like you used the cl command quite a bit!\nIf you have more questions about how this works, please contact me on discord (@greeenmatter)\n",separator)
                        cl_count = 0
                else:
                    thishelp = parameters[0]
                    if not thishelp in atlas:
                        print("No help found for this command, type 'cl' for help")
                    else:
                        backendname=atlas[thishelp]
                        if not backendname in helpatlas:
                            log("Helpatals is broken!","error")
                            raise Exception("Please fix the helpatlas")
                        helpstr = helpatlas[backendname]
                        helpstr=helpstr.replace("<this:cmd>",thishelp)
                        print(separator)
                        print(helpstr)
                        print("Backend name: ",backendname)
                        print("Atlases: ")
                        for i in atlas:
                            if atlas[i]==backendname:
                                print("-    ",i)
                        print(separator)
            elif atlas[console] == "crash":
                log("Crash for testing")
                raise Exception("Crash for testing")
            elif atlas[console] == "eval":
                if len(parameters) == 1:
                    result = evalthis(parameters[0])
                    history.append(result)
                    print("Result:",result)
                else:
                    log("Invalid amount of parameters","error")
                    raise Exception("eval command requires 1 parameter")
            elif atlas[console] == "msg":
                print(" ".join(parameters))
            elif atlas[console] == "sqrt":
                if len(parameters) == 1:
                    print("Result: ",math.sqrt(float(evalthis(parameters[0]))))
                else:
                    log("Invalid amount of parameters","error")
                    raise Exception("sqrt command requires 1 parameter")
            elif atlas[console] == "pyg":
                if len(parameters) == 2:
                    print("Result: ",math.sqrt(float(evalthis(parameters[0]))**2 + float(evalthis(parameters[1]))**2))
                else:
                    log("Invalid amount of parameters","error")
                    raise Exception("pyg command requires 2 parameters")
            elif atlas[console] == "pyg+":
                if len(parameters) == 3:
                    match1 = math.sqrt(float(evalthis(parameters[0]))**2 + float(evalthis(parameters[1]))**2)
                    match2 = parameters[2]
                    match1 = float(match1)
                    match2 = float(match2)
                    if match1 == match2:
                        print("this triangle is rectangular")
                    else:
                        print("this triangle is not rectangular")
                else:
                    log("Invalid amount of parameters","error")
                    raise Exception("pyg+ command requires 3 parameters")
            elif atlas[console] == "p2":
                if len(parameters) == 2:
                    for i in range(1,(int(evalthis(parameters[1]))+1)):
                        print("Result: ",float(evalthis(parameters[0]))*2**i)
                else:
                    log("Invalid amount of parameters","error")
                    raise Exception("p2 command requires 2 parameters")
            elif atlas[console] == "cat":
                cat()
            elif atlas[console] == "history":
                if parameters == []:
                    print("Type 'h cl' for help")
                    continue
                htype = parameters[0]
                if htype == "cl" or htype == "help":
                    print(separator,"\nHistory helper: ",end="")
                    print("""
-  c (clear): clear history
-  l <index:default:1> (last): last result
-  n <number> (new): add a result to the history
-  a (all): print all the history
-  Tip!: using 'h' inside expressions, it will automaticly replace 'h' with the last result in history""")
                    print(separator)
                    continue
                elif htype =="c":
                    history=[1]
                    print("History cleared!")
                elif htype =="l":
                    if len(parameters)==2:
                        index = int(parameters[1])
                    else:
                        index=1
                    if history == []:
                        print("No history to show")
                    else:
                        thishistory = history[-index]
                        print("History at index ",index,": ",thishistory)
                elif htype =="n":
                    parameters[1] = str(parameters[1])
                    history.append(parameters[1])
                    print("Added ",parameters[1]," to history")
                elif htype =="a":
                    print(separator,"\nAll History: ")
                    for i in history:
                        print("-    ",i)
                    print(separator)
                else:
                    print("Sub-command not found, type 'h cl' for help")
            elif atlas[console] == "conv":
                if parameters == []:
                    print("Type 'conv cl' for help")
                    continue
                cvtype=parameters[0].lower()
                if len(parameters)==1 and cvtype in conversions:
                    print("Please provide a number to convert")
                    continue
                if cvtype == "help" or cvtype == "cl":
                    print(separator,"\nConversion helper: ")
                    for i in conversions:
                        print(i,": ",conversions[i]["help"])
                    print(separator)
                elif not cvtype in conversions:
                    print("This conversion does not exist, type 'conv cl' for help")
                else:
                    if not len(parameters) == 2:
                        log("Invalid amount of parameters","error")
                        raise Exception("conv command requires 2 parameters")
                    conversion = conversions[cvtype]["ex"]
                    conversion = conversion.replace("x",str(parameters[1]))
                    conversion = eval(conversion)
                    print("With ",cvtype," : ",parameters[1]," -> ",conversion)
                    history.append(conversion)
            elif atlas[console] == "pass":
                pass
            else:
                log("Atlas is broken!","error")
                raise Exception("No definition matched!\nPlease fix the atlas!")
        else:
            try:
                result = evalthis(console)
                print("Result: ",result)
                history.append(result)
                console="pass"
            except:
                nothing_found_count = nothing_found_count + 1
                print("No matching command found!")
            if nothing_found_count == 3:
                print("To show commands type : 'cl'")
                nothing_found_count = 0
def rootmain():
    global running
    try:
        main()
    except Exception as e:
        print("\nFatal error has occurred!\n\nError: \n",e,"\n\n")
while running:
    rootmain()