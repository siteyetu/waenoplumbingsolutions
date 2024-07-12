#create tasks


#Cron task 1
from apscheduler.schedulers.background import BackgroundScheduler

def cron (job, times):
	sched = BackgroundScheduler(daemon = True )
	sched.add_job(job, 'interval', seconds = times )
	#sched = BackgroundScheduler(daemon= True )
	#for items in list_of_set_job_and_time:
	#	for job, timeinseconds in items:
	#		sched.add_job(job, 'interval', seconds = timeinseconds )
	sched.start()
	# Shut down the scheduler when exiting the app
	# atexit.register( lambda : scheduler.shutdown())




def cron_in_seconds(job, times):
	...
	#shed.start()
	#shed.start()
	# Shut down the scheduler when exiting the app
	# atexit.register( lambda : scheduler.shutdown())


# #Cron task 2
# import atexit
# from apscheduler.scheduler import Scheduler

# cron = Scheduler (daemon= True )
# cron.start()
# @cron.interval_schedule(seconds= 1)
# def job_function(varfunction):
# 	varfunction
# atexit.register( lambda : cron.shutdown(wait= False))





