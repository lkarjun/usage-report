import re
import winapps
from winapps import list_installed
import psutil
from typing import List, Literal

def listapps() -> List:
        apps_load = winapps.list_installed()
        #listing and converting to string
        listing_all_apps = [str(i) for i in apps_load]
        regrex = r"name=['][\w\s]*[']"
        apps = [
                app[6:-1]
                for detail in listing_all_apps
                for app in re.findall(regrex, detail)
                ]
        return list(set(apps))

def listprocessor() -> List:
        apps_load = psutil.process_iter()
        listing_all_apps = [str(i) for i in apps_load]
        regrex = r"name=['][\w\s.]*[']"
        apps = [
                app[6:-5]
                for detail in listing_all_apps
                for app in re.findall(regrex, detail)
        ]
        return list(set(apps))

if __name__ == "__main__":
        pass
        