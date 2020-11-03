# Hadoop-LVM-Setup

## Just Made The menu.py executable by writing 
"chmod +x"
and to run it 
./menu.py
And You Are Ready To Go




All you need is to set the followings

vg: <name_of_volume_group>  
pvs: <name_of_device>  
lv: <name_of_logical_volume>  
dev: <device_name>  
path: <folder_name_and_path>  
src: <device_name>  

check the name of disk or dev by 
### fdisk -l
command in linux

## FOR REDUCE AND EXTEND PLAYBOOK

#### For Extend
size is in mb 

#### For Reduce
The size you provide will be the for the new lv 
