# Windows Update Check for CheckMK
<p align="center"><img src="https://user-images.githubusercontent.com/5358267/235710289-c05aa5bb-3394-4c94-8ce0-1f0ef5382d00.png"></p>
<p align="center">#Powered by K&P Computer - www.kpc.de</o>

----------------------

### Available .mkp Package Releases: ###

https://github.com/matthias1232/kpc_windows_updates/releases


----------------------

### Windows Update Checks for CheckMK ###
 
Features:
- Check for available Windows Updates (Important and Optional, intelligence updates will be shown under optional updates)
- Checking for available Windows Updates sorted by Severity
- Individual WARN/CRIT Level settings for each type of Updates (Mandatory, Critical, Important, Moderate, Low, Unspecified Severity)
- Pending Reboot Check after Update Installation with WARN/CRIT Level Settings
- CRIT Error if Update Search does not work for a while (Windows update not activated, WSUS Problem etc..)
- Showing all available Updates in Detailed Summary
- Check for Windows Update History. Shows the last time when this System installed an Windows Update and also the List of up to the last 80 installed updates in the summary details. (Intelligence Updates are excepted)
- Warn/Crit level Settings if the System did not install any update during the last X days.
- Included in Agent Rules for Agent bakery
- No VBS Scripts anymore, only Powershell will be used
- Tested with Windows 2012R2/2016/2019/2022





### Added default Agent execution Settings for the Windows Agent Plugin (Agent Bakery): ###
- Default cache interval of 3 Hours
- Default asynchronous execution
- Default execution timeout of 1 hour (long time needet for some older systems sometimes)

If you are not using the CheckMK agent bakery or if you are working with CheckMK Raw Edition, apply the following Settings to your check_cmk.user.yml

%ProgramData%\checkmk\agent\check_mk.user.yml
````
plugins:
    enabled: yes
    execution:
    - pattern     : '$CUSTOM_PLUGINS_PATH$\windows_updates_kpc.ps1'
      async       : yes
      run         : yes
      cache_age   : 3600
      timeout     : 3600
````
### Screenshots: ###
![image](https://github.com/user-attachments/assets/b975f5aa-b6de-477d-9445-d2bf5509fe26)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/fdd7d13a-c29b-4835-aa7d-9610f7b6403c)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/e098c9b3-31c9-4b01-b693-0e75c2cddd2d)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/4cefbcb2-cbbb-4708-ac9d-6c40481794c0)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/041ee4e7-39d1-4639-bdd1-0c66a38c1b35)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/8bccc33c-a0dc-48be-a43e-0ed66a04c71c)

![image](https://github.com/matthias1232/kpc_windows_updates/assets/5358267/9b979558-cc79-493b-b4b0-3f3867bd1e4a)

![image](https://github.com/user-attachments/assets/678f5be5-385a-4184-9ace-47743a4d58d4)

![image](https://github.com/user-attachments/assets/f884a80a-19ed-49dc-be54-cbc7c5e0e142)

![image](https://github.com/user-attachments/assets/2d6a9a94-c184-4670-ae95-b9fdfd4ce1c8)






