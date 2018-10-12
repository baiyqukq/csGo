from datetime import datetime

##
# print string with current time at the beginning
#
def printt(s):
    print("[%s]%s" % (datetime.now().time().isoformat(), s))
