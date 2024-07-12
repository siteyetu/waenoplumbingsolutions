from mainModules.cronJobs.cronfunc import cron
from mainModules.crypto.myCertGen  import genKeys
from prints.auth.models import Tokens
from time import time as now
# from flask import session



# expires token and logs out user
def tokenexpiry():
    def change_token_status():
        for items in Tokens.objects.all():
            if now()==items.timeofexpiry or now()>items.timeofexpiry:
                items.update(status=False)
                # username=items.username
                # session.pop(username)

    cron(change_token_status, 1)

def create_daily_pair():
    ...
    # gencert=genKeys("private"+str(now()),"public"+str(now()), None)
    # cron(gencert, 86400)
        #, **args, **kwargs)






     
