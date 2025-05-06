#!/usr/bin/env python3
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the #License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU #General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Written by Matthias Binder m.binder@kpc.de, July 2023
#
################################################################################################################
#
# Author: K&P Computer Service- und Vertriebs-GmbH
# Author: Matthias Binder
# License: GNU General Public License
# License Changed to GPL: 11/2024
#
# 
# For Support and Sales Please Contact K&P Computer!
#
# E-Mail: hds@kpc.de
#
# 24/7 Helpdesk-Support:
# International: +800 4479 3300
# Germany: +49 6122 7071 330
# Austria: +43 1 525 1833
#
# Web Germany: https://www.kpc.de
# Web Austria: https://www.kpc.at
# Web International: https://www.kpc.de/en
#
################################################################################################################


#<<<windows_lastupdateinstalldate_kpc:sep(9):encoding(cp437)>>>
#Windows Update History	07/09/2023 19:11:05	1	07/09/2023 19:11:05 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.4052.0)XXXNEWLINEXXX07/08/2023 19:14:01 Security Intelligence Update for Microsoft Defender Antivirus - KB2267602 (Version 1.391.3953.0)

#support = "For Support and Sales Please Contact K&P Computer! \n \n E-Mail: hds@kpc.de \n \n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

support = ""

from cmk.agent_based.v2 import *
import pprint
from datetime import datetime, timedelta


def discover_windows_lastupdateinstalldate_kpc(section):
    for jobname_windows_lastupdateinstalldate_kpc, lastupdateinstalldate, lastupdateinstalldays, updatehistorysearcherror, lastupdatelist in section:  
        yield Service(item=jobname_windows_lastupdateinstalldate_kpc)


def check_windows_lastupdateinstalldate_kpc(item, params, section):
    if params["warning_lower"][0] == 'fixed':
        warn = params["warning_lower"][1][0]
        crit = params["warning_lower"][1][1]
    else:
        warn = 9999999
        crit = 9999999
          
    for line in section:
        if len(line) < 5:
            continue  # Skip incomplete lines

        jobname_windows_lastupdateinstalldate_kpc, lastupdateinstalldate, lastupdateinstalldays, updatehistorysearcherror, lastupdatelist = line[
            :5
        ]

        if (lastupdatelist == "-"):
            lastupdatelist = ""

        lastupdatelist = lastupdatelist .replace("XXXNEWLINEXXX", "\n")
        lastupdatelist = "\n \n" + lastupdatelist + "\n \n \n" + support
        if jobname_windows_lastupdateinstalldate_kpc != item:
            continue  # Skip not matching lines

        if int(lastupdateinstalldays) >= crit:
             state = State.CRIT
        elif int(lastupdateinstalldays) >= warn:
             state = State.WARN
        else:
             state = State.OK
        if int(lastupdateinstalldays) == 999999:
             lastupdateinstalldays = "?"
             state = State.CRIT
        if int(warn) == 9999999:
                warn = "Always OK"
        if int(crit) == 9999999:
                crit = "Always OK"
                
        summarytext= "Last installation of Windows Updates: " + lastupdateinstalldate + " (" + str(lastupdateinstalldays) + " days ago) / (warn: " + str(warn) + " / crit: " + str(crit) + ")"
        summarydetails = "Update History:" + lastupdatelist + support
       
        if (updatehistorysearcherror != "0"):
            state=State.CRIT
            summarytext= str(updatehistorysearcherror)
            summarydetails = " "
            
        yield Result(
             state=state,
             summary=f"{summarytext}",
             details = summarydetails )

check_plugin_windows_lastupdateinstalldate_kpc = CheckPlugin(
    name = "windows_lastupdateinstalldate_kpc",
    sections = [ "windows_lastupdateinstalldate_kpc" ],
    service_name = "%s",
    discovery_function = discover_windows_lastupdateinstalldate_kpc,
    check_function = check_windows_lastupdateinstalldate_kpc,
    check_default_parameters={
     "warning_lower": ('fixed', (30, 50)),
    },
    check_ruleset_name="windows_updates_kpc_windows_lastupdateinstalldate",
)