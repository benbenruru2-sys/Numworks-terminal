# This is the helper file, it provides useful functions for the main program

import config
from config import ERROR,NOTICE,LOG

def cat(catchar: list[str]=config.catchar) -> None: #Meow
    for i in catchar:
        print(i)
        
def evalthis(input: str,variables: dict[str,float|int],history: list[float|int],historyidx: int=1) -> float|int:
    input = str(input)
    for i in variables: # This replaces the variable placeholder with the value of the variable
            input = input.replace("v,"+i,str(variables[i]))
            input = input.replace("v:"+i,str(variables[i]))
    try: # Yes, ik this is one of the worst metods of testing for a number
        float(history[-1]) #Try to see if it is a number
        input = input.replace("h",str(history[-historyidx]))
        input = input.replace("ans",str(history[-historyidx]))
    except: # If the last result in history in not a number, just remove the placeholder for history
        input = input.replace("h","")
        input = input.replace("ans","")
    return eval(input)

def expthis(input: str,exp: dict[str,str]=config.exp) -> str: # Checks for common exepressions sutch as yes (y -> yes)
    input = str(input)
    input = input.lower().strip()
    try:
        return exp[input]
    except:
        return "Error"
 
 
 # This is just used to debug stuff, not really needed
 # This is not used anymore!
 # Use helper.throw("debug is on",LOG) instead
def log(msg,type="DEBUG",DEBUG=config.DEBUG):
    try:
        type = str(type).upper()
        msg = str(msg)
        if DEBUG:
            print(type,"> ", msg)
    except:
        print("DEBUG crashed!")
        
# log("Debug is enabled!")

def help(separator: str=config.separator) -> None: # Display basic help
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
    
    def __init__(self,ph: list=[]):
        self.ph = ph # Print history
        
    def printall(self):
        for i in self.ph:
            print(i)
            
    def add(self,msg: str):
        self.ph.append(msg)
        
    def delete(self,ph: list=[]):
        self.ph = ph
        
    def get_last(self) -> str:
        return self.ph[-1]
    
    def merge_last(self,index: int=2):
        if not index:
            self.ph.append(self.ph[-2]+self.ph[-1]) # appends -2+-1 to the print history
            del self.ph[-2] # Remove the 2 merged items
            del self.ph[-2] # Same line since the -3 became -2 after deleting -2
        if index:
            pass
            
            
# This is the replacement to log()
def throw(msg: str,type: str="log") -> None:
    if type.lower() in ["error","crash","err"]:
        raise Exception(msg)
    if type.lower() in ["log","debug","event"]:
        if config.DEBUG:
            print(type.upper()," > ", msg)
    if type.lower() in ["warning","notice","carful"]:
        print(type.upper(),"! : ", msg)
            
        
def process_input(input: str,toremove: list[str]=config.toremove,argatlas: dict[str,str]=config.argatlas) -> dict[str,str|list[str]]:
    input = input.strip()
    for i in toremove:
        input = input.replace(i,"")
    for i in argatlas:
        input = input.replace(i,argatlas[i])
    params: list = multi_split(input)
    command: str = params[0].lower()
    params = params[1:]
    return {"command":command,"params":params}


def multi_split(input: str,split: list[str]|str=config.split) -> list[str]:
    if isinstance(split,list):
        parts: list[str] = [input]
        for separator in split:
            split_parts: list = []
            for part in parts:
                for piece in part.split(separator):
                    split_parts.append(piece)
            parts = split_parts
        return parts
    else:
        return input.split(split)


def is_command(check: str,command: str,atlas: dict[str,str]=config.atlas) -> bool|None:
    if not check in atlas:
        return None
    if not command in atlas:
        throw("Command check could not be satisfied: command is not present in atlas",ERROR)
        return None
    if atlas[check] == atlas[command]:
        return True
    else:
        return False

def expect_params(params: list[str]|dict[str,list[str]],check: list=[str,int]) -> list: # Checks for str, int, float, bool, list, dict
    if isinstance(params,dict):
        params=params["params"]
    if isinstance(params,str):
        params=[params]
    params = list(params)
    index=0
    check = list(pad(check,len(params),"*"))
    converted = []
    for item in params:
        expected = check[index]
        if expected == "*":
            converted.append(item)
        elif expected == gettype(item):
            converted.append(item)
        else:
            throw("Expected a "+gettype_name(expected)+" type item, but instead got a "+gettype_name(gettype(item))+" item at position "+str(index)+"!",ERROR)
        index = index+1
    return converted

def pad(topad: list[str]|str,padamount: int,padwith: str=" ") -> list[str]|str:
    if len(topad) >= padamount:
        return topad
    padamount = padamount - len(topad)
    if isinstance(topad,str):
        return topad+padwith*padamount
    if isinstance(topad,list):
        for i in range(padamount):
            topad.append(padwith)
    return topad

def gettype(item: str): # Not perfect, but works good enough for now
    item = str(item).strip()
    if item in ["True","False"]:
        return bool
    elif item.isdigit():
        return int
    elif item.replace(".","",1).isdigit():
        return float
    else:
        return str
    
def gettype_name(item) -> str: # Input a bool, and instead of getting a ugly <'type':bool>, you get a nice 'bool'
    return {bool:"bool",int:"int",float:"float",list:"list",dict:"dict",str:"str"}[item]