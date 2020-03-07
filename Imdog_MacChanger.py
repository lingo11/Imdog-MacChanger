import subprocess
import optparse
import re
import os
import sys


print("""\
                                                                  
                                  .       , /   .  #.                           
                             .. .              /      #                         
                             (  .                        * .%                   
                         /...                              .                    
                      ,....                                  *                  
                    ..                                        . . *             
                   . ..                                        . . .,           
                 .....  .  . .                                      .,          
                ..   .  ,..,,...   .                          .    .  .         
               .......* ,*./ *.. ..... .             .                .         
              ,..* *(/.#*%(*,/.&./ (*/./.#.,. ...( ..& *..      .* .. .         
               .,*,..,,*,(%*%(%,%,,*,,@,***//*/,#%%%&&%*,.,,,...,*..,..         
              (,,,,,,,,,,,*******/////******(/. #%&&&@@**/***,*. (**,,..        
               ,,......,,,,,,**///**,,,,..,,*//(#%%&&&/////*,*,**.*/**,*        
               .,,    ....,,,*/((**,,.....    //(%%#%%/*..,,.,,* .*****         
               ,,,.........,*/###(/*,.......,(%%%##((#. .  ... , . ,/*,         
              ,,,,,,,,...,,*/#%&&%#(/*,,,,,*//(#%%###%....  ,.*. .  ...         
             /,,,,,,,,,,,,*/#%&&&&%%#((*,,,**//((##%%*...     .   .             
            /,,,,,,,,,,,**/#%%&&&&&&%##(//*****/((##/.. ..    .. #              
            **,,,,,,,,***/(#%&@&&&&%##((((//**///(##%..,                        
           ,***,,,,,,***/#%%&%&&&@@&#((((((((//((#(#%(.*.,* .                   
            ,******,,*,.*##(,,*#&@@&(//((##((#######%/,. * ..                   
            .*******,,,....,/(#((((((((((###%###%####(,**..,,                   
             *****,,,,,,,.,*/((((####%%##%%%%%%#%%%##(/(.,../                   
              *****,,,,,,**//######%%%%&%%%%%&%%%%%%%#*. .                      
               ***,,,,,***///(/(#%%%%%&&&&&&&&&&&&%%&/(*,.*                     
               .****,,,..*....,///(%%%%&&&&&&%&&&&%&&,/*.                       
                 **,,.     ...... .,(%%%&&&&&&&&&&&&#/(                         
                 .**,,,,,****(##%##%%%%%&&&&&&&&&&&%/


                        ---IMDOG MAC CHANGER---

                    """)




#Code begins here

if os.geteuid() != 0:
    sys.exit("[-] Dei benchod pls run this with sudo")

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="add your interface card eg. eth0")
    parse_object.add_option("-m","--mac",dest="mac_address",help="insert your new mac address eg. 00:11:12:13:14:15")

    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig", user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Imdog MacChanger started!")
(user_input,arguments) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Your mac address have been succesfully been imdogged")
else:
    print("Error oh diu!!!")


