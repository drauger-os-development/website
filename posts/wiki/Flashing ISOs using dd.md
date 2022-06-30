# Flashing ISOs using `dd`
Making a bootable linux USB using `dd` in Linux is actually pretty easy. The only requirements are to already have a working Linux bootable USB or at least a working Linux installation, and to have `dd` installed. Thankfully, `dd` comes by default in almost every Linux distro.

## WARNING: Using `dd` is dangerous for your files so you should only use it against drives that do not store ANY important data. **YOU HAVE BEEN WARNED.**

So, how do you flash ISOs to a USB drive using `dd`? 


1. Open a terminal. This can usually be achieved by hitting Ctrl + Alt + T

2. type `lsblk` and press enter

3. Find which block device your USB drive is, as determined by the size indicated on screen. Here's a small example:
   </br>
   </br>
   ![example lsblk output](/assets/images/dd-demo1.png)
   </br>
   </br>
   I know that is my USB because it's just 32GB. If you have other devices of an identical size, it's highly advised to unplug them, so as not to risk targeting the wrong device.

4. Take note of the "sdb" or whatever set of letters assigned to your USB drive. It could be sda, sdc, sdd, and etc. And using this would mean adding /dev/ before the set of letters. Example: /dev/sda  /dev/sdb  /dev/sdc  /dev/sdd 

5. Get the full path of your .iso file
   </br></br>
   For example, my .iso file is in `Downloads` on my Drauger OS install, and it may be there if you just downloaded it using a web browser. With that in mind, the path should be something like this:
   </br></br>
   `/home/[username]/Downloads`
   </br></br>
   or 
   </br></br>
   `$HOME/Downloads`
   </br></br>
   or
   </br></br>
   `~/Downloads`
   </br></br>
   I prefer the first format because it does not get ruined by bash autocompletion that is triggered when you press tab in the terminal. If you want to be absolutely sure that you have the right file, open another terminal, and try typing:
   </br></br>
   `cd /home/[username]/Downloads`
   </br></br>
   Then, invoke the `ls` command and see if the file is in there.
   Do note that you have to replace [username] with your user's name.
   </br></br>
   If you do not know your username, you can figure that out by running the `whoami` command.

6. Execute:
   </br></br>
   ```
   sudo dd if=(path to your ISO) of=(path to your block device) status=progress
   ```
   </br></br>
   remember to change the values above to what you actually have else you will end up writing to some random file and not your USB, BE CAREFUL.

7. Brew a cup of tea, a pot of coffee, or eat a quick snack and wait for it finish. Please be patient as this process naturally takes a while to finish.

8. Once it is done, go verify that the USB's name in file manager has changed accordingly and verify if you can open the USB to see its new contents and (if you are knowledgeable about file systems), verify that you can read the files just to be sure

9. Reboot PC and try to boot the USB by changing the boot order to it. Remember to disable Secure Boot!

If all goes well you should have a working Live USB drive that boots just fine! Have fun and happy hacking!

