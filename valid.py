import json

ccValid=[]
ccInvalid=[]
angka=['0','1','2','3','4','5','6','7','8','9']

file = open('ccNasabah.json', 'r')
output=json.load(file)
for i in output:
    valid=True
    if i["noCreditCard"][0] not in ['4','5','6'] or len(i["noCreditCard"].replace("-","")) != 16:
        valid=False

    for number in i["noCreditCard"].replace("-",""):
        jml=number*4
        if number not in angka:
            valid=False
            break
        if i["noCreditCard"].replace("-","").count(jml) > 0:
            valid=False
            break
    
    if "-" in i["noCreditCard"]:
        for k in i["noCreditCard"].split("-"):
            if len(k) > 4:
                valid=False
                break

    if valid == True:
        ccValid.append(i)
    else:
        ccInvalid.append(i)

ccValidFile=open('ccValid.json', 'w')
json.dump(ccValid, ccValidFile)

ccInvalidFile=open('ccInvalid.json', 'w')
json.dump(ccInvalid, ccInvalidFile)
    