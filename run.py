from re import findall
from winapps import list_installed
import psutil
from typing import Counter, List, Literal
from time import sleep
import shutil
import emailing
import authenticate
import gen_pdf


def listapps() -> List:
        '''Load all apps and return apps name as List'''
        apps_load = list_installed()
        #listing and converting to string
        listing_all_apps = [str(i) for i in apps_load]
        regrex = r"name=['][\w\s]*[']"
        #Slicing for getting apps name only
        apps = [
                app[6:-1].lower()
                for detail in listing_all_apps
                for app in findall(regrex, detail)
                ]
                #avoiding duplicate and return List
        return list(set(apps))

def listprocessor() -> List:
        '''Load all runing apps and return apps name as List'''
        apps_load = psutil.process_iter()
        listing_all_apps = [str(i) for i in apps_load]
        regrex = r"name=['][\w\s.]*[']"
        #Slicing for getting apps name only
        apps = [
                app[6:-5].lower()
                for detail in listing_all_apps
                for app in findall(regrex, detail)
        ]
        #avoiding duplicate and return List
        return list(set(apps))

def counting(apps: List[str], runningapps: List[str]) -> float:
        running_apps = []
        n = 0
        while True:
                [running_apps.append(i) for i in runningapps]
                n += 60
                if n == 360:
                        return Counter(running_apps)
                        break
                sleep(1)

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_available_memory():
    """available memory in linux-instance, in byte"""
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500

error_message = None

if check_cpu_usage():
    error_message = "CPU usage is over 80%"
elif not check_disk_usage('/'):
    error_message = "Available disk space is less than 20%"
elif not check_available_memory():
    error_message = "Available memory is less than 500MB"
else:
    pass





if __name__ == "__main__":

        subject = f"Error - {error_message}"
        message = emailing.generate_error_report(subject)
        emailing.send_email(message) 
        