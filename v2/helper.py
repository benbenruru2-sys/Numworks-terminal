# This is the helper file, it provides useful functions for the main program

import config

def cat(): #Meow
    for i in config.catchar:
        print(i)
        
def evalthis(input,variables,history,historyidx=1):
    input = str(input)
    for i in variables: # This replaces the variable placeholder with the value of the variable
            input = input.replace("v,"+i,variables[i])
            input = input.replace("v:"+i,variables[i])
    try: # Yes, ik this is one of the worst metods of testing for a number
        float(history[-1]) #Try to see if it is a number
        input = input.replace("h",str(history[-historyidx]))
        input = input.replace("ans",str(history[-historyidx]))
    except: # If the last result in history in not a number, just remove the placeholder for history
        input = input.replace("h","")
        input = input.replace("ans","")
    return eval(input)

def expthis(input,exp=config.exp): # Checks for common exepressions sutch as yes (y -> yes)
    input = str(input)
    input = input.lower().strip()
    try:
        return exp[input]
    except:
        return "Error"
 
 
 # This is just used to debug stuff, not really needed
def log(msg,type="DEBUG",DEBUG=config.DEBUG):
    try:
        type = str(type).upper()
        msg = str(msg)
        if DEBUG:
            print(type,"> ", msg)
    except:
        print("DEBUG crashed!")
        
log("Debug is enabled!")

def help(separator=config.separator): # Display basic help
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

class advprint:
    
    def __init__(self,ph=[]):
        self.ph = ph # Print history
        
    def printall(self):
        for i in self.ph:
            print(i)
            
    def add(self,msg):
        self.ph.append(msg)
        
    def delete(self,ph=[]):
        self.ph = ph
        
def clean_input_and_get_params(input,quotes='"',keepquotes=0):
    input.strip()
    params = input.split(" ")
    command = params[0].lower()
    params = params[1:]
    
    fix_params = []
    quote_flip = 0
    this_i = ""
    for i in params:
        if quotes in i:
            if quote_flip == 0:
                quote_flip = 1 # Quotes open
                this_i=i
            else:
                quote_flip = 0 # Quotes are closed
                fix_params.append(this_i)
        else:
            if quote_flip == 0:
                fix_params.append(i) # Quotes are closed
            else:
                this_i = this_i+i # Quotes are open
    if quote_flip == 1:
        fix_params.append(this_i+'"') # If the quotes are never closed, then close them for the user
    if keepquotes: 
        fix_params = fix_params.replace(quotes,"")
    
    return [command,fix_params]
        
                
            
            
    

            
      