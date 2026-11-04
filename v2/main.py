import config
import helper

pm = helper.advprint()

def init(ph=[]):
    global pm
    helper.log("Init")
    pm.delete(ph=ph)