from re import findall
from winapps import list_installed
from psutil import process_iter
from typing import List, Literal

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
        apps_load = process_iter()
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

if __name__ == "__main__":
        pass
        