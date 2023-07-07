################################################################################################################
#
# Author: K&P Computer Service- und Vertriebs-GmbH
# Author: Matthias Binder
# License: GNU General Public License
# Date: 05/2023
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


try
{
    #Checking for Datetime when the last update was installed and Show the Update History of the last 50 Updates
    $lastupdatelist=""


    $lastupdateinstalldate=@{}
    $Session = New-Object -ComObject Microsoft.Update.Session
    $Searcher = $Session.CreateUpdateSearcher()
    $lastupdateinstalldate = $Searcher.QueryHistory(1,1) | select -ExpandProperty Date
    $updatehistory = $Searcher.QueryHistory(1,500)

    if ($updatehistory -and $updatehistory.count -gt 0)
    {
    
        foreach ($lastupdate in $updatehistory)
        {
            if ($lastupdate.Date -and $lastupdate.Title)
            {
                $lastupdatelist = $lastupdatelist + $lastupdate.Date + " " + $lastupdate.Title + "XXXNEWLINEXXX"
            }
        }
    }

    if ($lastupdateinstalldate)
    {
        $lastupdateinstalldate = (New-TimeSpan -Start (Get-Date "01/01/1970") -End ($lastupdateinstalldate)).TotalSeconds
    }
    else
    {
        $lastupdateinstalldate = Get-Date "01/01/1970"
        $lastupdateinstalldate = (New-TimeSpan -Start (Get-Date "01/01/1970") -End ($lastupdateinstalldate)).TotalSeconds
    }
    $lastupdatelist = $lastupdatelist -replace "`n|`r"
    $outputlastupdateinstalldate = "<<<windows_lastupdateinstalldate_kpc:sep(9)>>>`n"
    $jobname_windows_lastupdateinstalldate_kpc = "Windows Update History"
    $outputlastupdateinstalldate = "$outputlastupdateinstalldate" + "$jobname_windows_lastupdateinstalldate_kpc" + "`t"  + "$lastupdateinstalldate" + "`t" + "$lastupdatelist"
    write-host "$outputlastupdateinstalldate"
    

    #Checking for available Windows Updates
    $Mandatorycount=0
    $Mandatoryupdates=""
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


    $UpdateSession = New-Object -ComObject Microsoft.Update.Session
    $UpdateSearcher = $UpdateSession.CreateupdateSearcher()
    $Updates = @($UpdateSearcher.Search("IsHidden=0 and IsInstalled=0").Updates)
    if ($Updates -and $Updates.count -gt 0)
    {
    
        foreach ($Update in $Updates)
        {
            $Updatetitle = $Update.Title
            $Updatetitle = $Updatetitle -replace "`n|`r"

            if ($Update.IsMandatory -eq 1)
            {
                $Mandatoryupdates = $Mandatoryupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Mandatorycount++
            }
            if ($Update.IsMandatory -eq 0)
            {
                $Optionalupdates = $Optionalupdates + $Updatetitle + "XXXNEWLINEXXX"
                $Optionalcount++
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
    $outputwindowsupdates = "<<<windows_updates_kpc:sep(9)>>>`n"
    $jobname_windows_updates_kpc = "Windows Updates"
    $outputwindowsupdates = "$outputwindowsupdates" + "$jobname_windows_updates_kpc" + "`t" + "$Mandatorycount" + "`t" + "$Optionalcount" + "`t" + "$Criticalcount" + "`t" + "$Importantcount" + "`t" + "$Lowcount" + "`t" + "$Moderatecount" + "`t" + "$Unspecifiedcount" + "`t" + "$Mandatoryupdates" + "`t" + "$Optionalupdates" + "`t" + "$Criticalupdates" + "`t" + "$Importantupdates" + "`t" + "$Lowupdates" + "`t" + "$Moderateupdates" + "`t" + "$Unspecifiedupdates"
    write-host $outputwindowsupdates
}
catch
{
$errMsg = $_.Exception.Message
$errItem = $_.Exception.ItemName
Write-Error "Totally unexpected and unhandled error occured:`n Item: $errItem`n Error Message: $errMsg"
Break
}
