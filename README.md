## Setup
1. Install Raspbian  
1. Boot with a monitor and keyboard  
        [default user/pass = pi/raspberry]  
`sudo rfkill unblock 0`  
`sudo iwlist wlan0 scan`  
`sudo raspi-config`  
        [1. Change User Password] > set a non-default password  
        [2. Network Options] > set up wifi  
        [4. Localisation Options] > set timezone  
        [5. Interfacing Options] > turn on ssh server  
1. From your computer:  
`scp motion.conf pi@<IP>:.`  
1. `ssh pi@<IP>`  
`sudo apt-get update`  
`sudo apt-get dist-upgrade`  
`sudo apt-get install motion`  
`sudo apt-get install screen`  
`mkdir videos`  
`screen -S motion`  
`sudo motion -c motion.conf`  
`Ctrl-A d`  

## Debug
1. In motion.conf:  
`stream_localhost on`  
1. Restart motion  
1. Go to:  
`<IP>:8081/source`  
