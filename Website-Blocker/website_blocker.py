import time
from datetime import datetime as dt

hosts_temp = 'hosts'
hosts_path = '/etc/hosts'

hosts_applied = hosts_path

redirect='127.0.0.1'
website_list = ['www.facebook.com','facebook.com','mail.google.com','gmail.com']

year = dt.now().year
month = dt.now().month
day = dt.now().day

start_block = dt(year,month,day,8)
end_block = dt(year,month,day,11)

while True:
	if start_block < dt.now() < end_block:
		print("Working hours...")
		with open(hosts_applied,'r+') as f_host:
			content=f_host.read()
			for website in website_list:
				if website in content:
					pass
				else:
					f_host.write(redirect+' '+website+'\n')

	else:
		with open(hosts_applied,'r+') as f_host:
			content=f_host.readlines()
			f_host.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					f_host.write(line)
			f_host.truncate()

		print("Leisure hours...")
	time.sleep(5)