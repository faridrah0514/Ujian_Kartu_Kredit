import csv
import json

ccValid=[]
ccInvalid=[]
#ketentuan
digit_awal=['4', '5', '6']
panjang=16
angka=['0','1','2','3','4','5','6','7','8','9']


file = open('ccNasabah.json', 'r')
output=json.load(file)
for i in output:
    valid=True
    no_credit_card=i["noCreditCard"]
    # print(no_credit_card)
    # print(no_credit_card)
    if no_credit_card[0] not in digit_awal or len(i["noCreditCard"].replace("-","")) != panjang:
        valid=False
    jml=''
    for number in i["noCreditCard"].replace("-",""):
        jml=number*4
        # print(i["noCreditCard"].replace("-","").count(jml))
        if number not in angka:
            valid=False
            break
        if i["noCreditCard"].replace("-","").count(jml) > 0:
            valid=False
            break
    
    if "-" in i["noCreditCard"]:
        no_credit_card1=i["noCreditCard"].split("-")
        # print(no_credit_card1)
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
    