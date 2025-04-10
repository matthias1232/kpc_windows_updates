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

$pshost = get-host
$pswindow = $pshost.ui.rawui

$newsize = $pswindow.buffersize
$newsize.height = 300
$newsize.width = 150
$pswindow.buffersize = $newsize
$now = Get-Date


try
{

    #Checking for Datetime when the last update was installed and Show the Update History of the last 80 Updates
    $lastupdatelist=""
    $lastupdatelistcounter=0
    $lastupdateinstalldate=""
    $updatehistorysearcherror=0
    #$lastupdateinstalldate=@{}

    
    try
    {
       #$lastupdateinstalldate=@{}
       $Session = New-Object -ComObject Microsoft.Update.Session
       $Searcher = $Session.CreateUpdateSearcher()
       #$lastupdateinstalldate = $Searcher.QueryHistory(0,1) | select -ExpandProperty Date
       $updatehistory = $Searcher.QueryHistory(0,1000)
    }
    catch
    {
        $errMsg = $_.Exception.Message
        $errItem = $_.Exception.ItemName
        $updatehistorysearcherror = "There was an error getting update history information. Maybe Windows update is not activated or System cannot get information from WSUS Server. Error Message: $errMsg"
    }

    if ($updatehistory -and $updatehistory.count -gt 0)
    {
    
        foreach ($lastupdate in $updatehistory)
        {
            if ($lastupdate.Date -and $lastupdate.Title -and $lastupdate.Title -notlike "*Intelligence[ -]Update*" -and $lastupdatelistcounter -lt 80 )
            {
                $lastupdatelist = $lastupdatelist + $lastupdate.Date.tostring("yyyy-MM-dd hh:mm:ss") + " " + $lastupdate.Title + "XXXNEWLINEXXX"
                if($lastupdateinstalldate -eq "")
                {
                    $lastupdateinstalldate = $lastupdate.Date
                }
                $lastupdatelistcounter++
            }
        }
    }

    if ($lastupdateinstalldate)
    {
        $lastupdateinstalldays = New-TimeSpan -Start $lastupdateinstalldate -End $now
        $lastupdateinstalldays = $lastupdateinstalldays.Days
        $lastupdateinstalldate = $lastupdateinstalldate.tostring("yyyy-MM-dd hh:mm:ss")
    }
    else
    {
        $lastupdateinstalldate = "No history found"
        $lastupdateinstalldays = "99999"
    }
    if ($lastupdatelist -eq "")
    {
        $lastupdatelist = "-"
    }
    $lastupdatelist = $lastupdatelist -replace "`n|`r"
    $outputlastupdateinstalldate = "<<<windows_lastupdateinstalldate_kpc:sep(9):encoding(cp437)>>>`n"
    $jobname_windows_lastupdateinstalldate_kpc = "Windows Update History"
    $outputlastupdateinstalldate = "$outputlastupdateinstalldate" + "$jobname_windows_lastupdateinstalldate_kpc" + "`t"  + "$lastupdateinstalldate" + "`t" + "$lastupdateinstalldays" + "`t" + "$updatehistorysearcherror" + "`t" + "$lastupdatelist"
    write-host "$outputlastupdateinstalldate"


    ####Check if a reboot is required and since how many days###
    $rebootrequired = Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired"
    if ($rebootrequired -eq "True")
    {
        
        $rebootrequired = "Yes"
        $rebootrequiredsince = Get-ItemProperty -path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired" -ErrorAction SilentlyContinue -WarningAction SilentlyContinue | Select-Object -ExpandProperty 'RebootRequiredSince' -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        if($rebootrequiredsince)
        {
            $rebootrequiredsince = Get-Date -Date $rebootrequiredsince 
            $rebootrequiredsince = $rebootrequiredsince.ToLocalTime()
            $rebootrequiredsinchours = New-TimeSpan -Start $rebootrequiredsince -End $now
            $rebootrequiredsinchours = $rebootrequiredsinchours.TotalHours
            $rebootrequiredsinchours = [Math]::Truncate($rebootrequiredsinchours)
            $rebootrequiredsince = $rebootrequiredsince.tostring("yyyy-MM-dd hh:mm:ss")
        }
        else
        {
            $rebootrequiredsince = "notimefound"
            $rebootrequiredsinchours = "99999"
        }
    }
    else
    {
    $rebootrequired = "No"
    $rebootrequiredsince = "0"
    $rebootrequiredsinchours = "0"
    }
    

    #Checking for available Windows Updates
    $Mandatorycount=0
    $Mandatoryupdates=""
    $important1updates=""
    $important1count=0
    $Optionalcount=0
    $Optionalupdates=""
    $Criticalcount=0
    $Criticalupdates=""
    $Importantcount=0
    $Importantupdates=""
    $Lowcount=0
    $Lowupdates=""
    $Moderatecount=0
    $Moderateupdates=""
    $Unspecifiedcount=0
    $Unspecifiedupdates=""
    $updatesearcherror=0
    try
    {
        $UpdateSession = New-Object -ComObject Microsoft.Update.Session
        $UpdateSearcher = $UpdateSession.CreateupdateSearcher()
        $Updates = @($UpdateSearcher.Search("IsHidden=0 and IsInstalled=0").Updates)

    }
    catch
    {
        $errMsg = $_.Exception.Message
        $errItem = $_.Exception.ItemName
        $updatesearcherror = "There was an error getting update information. Maybe Windows update is not activated or System cannot get information from WSUS Server. Error Message: $errMsg"
    }


    if ($Updates -and $Updates.count -gt 0)
    {
    
        foreach ($Update in $Updates)
        {
            $Updatetitle = $Update.Title
            $Updatetitle = $Updatetitle -replace "`n|`r"

            if ($Update.AutoSelectOnWebSites -eq "True" -and $Update.Title -notlike "*Intelligence[ -]Update*")
            {
                $important1updates = $important1updates + $Updatetitle + "XXXNEWLINEXXX"
                $important1count++
            }            
            if ($Update.AutoSelectOnWebSites -ne "True" -or $Update.Title -like "*Intelligence[ -]Update*")
            {
                $Optionalupdates = $Optionalupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Optionalcount++
            }
            if ($Update.IsMandatory -eq 1)
            {
                $Mandatoryupdates = $Mandatoryupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Mandatorycount++
            }
            if ($Update.MsrcSeverity -eq "Critical")
            {
                $Criticalupdates = $Criticalupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Criticalcount++
            }
            if ($Update.MsrcSeverity -eq "Important")
            {
                $Importantupdates = $Importantupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Importantcount++
            }
            if ($Update.MsrcSeverity -eq "Low")
            {
                $Lowupdates = $Lowupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Lowcount++
            }
            if ($Update.MsrcSeverity -eq "Moderate")
            {
                $Moderateupdates = $Moderateupdates + $Updatetitle  + "XXXNEWLINEXXX"
                $Moderatecount++
            }
            if ($Update.MsrcSeverity -eq $null)
            {
                $Unspecifiedupdates = $Unspecifiedupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Unspecifiedcount++
            }
        }


}

    if ($Mandatoryupdates -eq "")
    {
        $Mandatoryupdates = "-"
    }
    if ($Optionalupdates -eq "")
    {
        $Optionalupdates = "-"
    }
    if ($Criticalupdates -eq "")
    {
        $Criticalupdates = "-"
    }
    if ($Moderateupdates -eq "")
    {
        $Moderateupdates = "-"
    }
    if ($Lowupdates -eq "")
    {
        $Lowupdates = "-"
    }
    if ($Unspecifiedupdates -eq "")
    {
        $Unspecifiedupdates = "-"
    }

   
    
    $outputwindowsupdates = "<<<windows_updates_kpc:sep(9):encoding(cp437)>>>`n"
    $jobname_windows_updates_kpc = "Windows Updates"
    $outputwindowsupdates = "$outputwindowsupdates" + "$jobname_windows_updates_kpc" + "`t" + "$Mandatorycount" + "`t" + "$important1count" +  "`t" + "$Optionalcount" + "`t" + "$Criticalcount" + "`t" + "$Importantcount" + "`t" + "$Moderatecount" + "`t" + "$Lowcount" + "`t" + "$Unspecifiedcount" + "`t" + "$rebootrequired" + "`t" + "$rebootrequiredsince" + "`t" +  "$rebootrequiredsinchours" + "`t" + "$updatesearcherror" + "`t" +  "$Mandatoryupdates" + "`t" + "$important1updates" + "`t" + "$Optionalupdates" + "`t" + "$Criticalupdates" + "`t" + "$Importantupdates" + "`t" + "$Lowupdates" + "`t" + "$Moderateupdates" + "`t" + "$Unspecifiedupdates"
    $outputwindowsupdates = $outputwindowsupdates
    write-host "$outputwindowsupdates"
}
catch
{
$errMsg = $_.Exception.Message
$errItem = $_.Exception.ItemName
Write-Error "Totally unexpected and unhandled error occured:`n Item: $errItem`n Error Message: $errMsg"
Break
}
