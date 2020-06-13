# Potential Privescs
## a script is running every 5 minutes as root 
	- */5  *    * * * root    /home/user4/Desktop/autoscript.sh
## interally SQL is running with creds root : root

## Sudo version 1.8.21p2 is vulnerable to privesc

## /home/user3/shell have suid bit set

## /home/user5/script have suide bit set 

## /home/user5 nfs share 

## 

[-] Sudoers configuration (condensed):Defaults	env_reset
Defaults	mail_badpass
Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
root	ALL=(ALL:ALL) ALL
user1   ALL=(ALL:ALL) ALL
user2   ALL=(user1) ALL
user8   ALL=(root) NOPASSWD: /usr/bin/vi
%admin ALL=(ALL) ALL
%sudo	ALL=(ALL:ALL) ALL



