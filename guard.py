#!/bin/bash
clear
sleep 2
echo "Tunggu lagi di respon"
sleep 3
clear
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'
clear
echo -b "
    📌ᏔᎬᏞᏟϴᎷᎬ📌
     ©PP  GUARD®
█║▌│█│║▌║│█║║▌│█║│█
  🛠️ J4CKOP TOOLS 🛠️

echo "";
figlet TOOLS GUARD PP | lolcat

echo -b " CODED BY J4CKOP $green " |lolcat
echo -b " FIND ME ON FB : Azis Wirahadi $green " |lolcat
figlet TOOLS GUARD PP | lolcat

###################################################
# CTRL + C                                        #
###################################################

trap ctrl_c INT
ctrl_c() {
clear
echo -b $green"[#]> (Ctrl + C ) Detected, Trying To Exit ... " |lolcat
echo -b $green"[#]> MAKASIH UDH PAKE TOOLS GUE " |lolcat
sleep 1
echo ""
echo -b $green"[#]> J4CKOP WAS HERE" |lolcat

echo -b $green"[#]> See you Again :)..." |lolcat
sleep 1
exit
}

lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo -e $b "1. PP GUARD${enda}";
echo -e $b "2. JADWAL SHOLAT${enda}";
echo -e $b "00. Exit${enda}";
echo -e "╭─\h[PILIH AJA NOMERNYA]" | lolcat
read -p "╰─#" pil;

case $pil in

1) echo "J4CKOP TOOLS-PP GUARD" | lolcat
    		pkg install php
    		pkg install git
    		git clone https://github.com/Noxturnix/guardn
    		cd guardn
    		python2 guardn.py

    		;;
2) echo "J4CKOP TOOLS JADWAL SHOLAT" | lolcat
    		pkg install php
    		pkg install git
    		git clone https://github.com/siputra12/sholatoy
    		cd sholatoy
        php run.php

    		;;
        
        00) echo "BYE BYE PARA HEKER,INCARLAH SESUATU YG MUSTAHIL" | lolcat
exit
;;

*) echo "Sorry, Your choices it's not already [SHT]"
esac
done
done
