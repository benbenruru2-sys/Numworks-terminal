import helper

print(helper.expect_params(["hello","world","5.0","True"],[str,str,float,bool]))