# Troubleshooting

## USB drive will not boot Drauger OS live environment
**Problem**: After using Rufus to install Drauger OS onto a bootable usb, Drauger OS is unable to boot to the live environment
</br></br>

**Solution**: Ensure Rufus is operating in "dd" mode
</br></br></br>



## Nvidia Video driver issues/poor performance
**Problem**: When running a machine with an Nvidia GPU, you notice graphical issues such as being stuck at a low resolution, failure to launch UI, poor game performance or slow rendering.

</br></br>
**Solution**: Install closed source Nvidia drivers per the following instructions: </br>
**Note: Do not install drivers from Nvidia's website**
</br></br>

Depending on which Nvidia card you have, follow the instructions in A, B or C.
</br></br>
A) _If you have a 10 series card or newer_, run the following command:
</br></br>
```
sudo apt install nvidia-driver-latest
```
***
</br></br>
B) _If your card is older than the 10 series_, check [Nvidia's Website](https://www.nvidia.com/Download/index.aspx?lang=en-us) to see which driver corresponds to your graphics card.  If it is the latest Nvidia driver (545 at the time of writing), run the following command
</br></br>
```
sudo apt install nvidia-driver-latest
```
</br></br>
Note: You can see what the latest Nvidia drivers packages are available in apt using the following command and looking for the highest numbered driver release
</br></br>
```
apt search nvidia-driver
```
</br></br></br>
C) _if you card is older than the 10 series and the driver listed on [Nvidia's Website](https://www.nvidia.com/Download/index.aspx?lang=en-us) is older than the latest driver_, do the following:
</br></br>
Install, through apt, the package that corresponds to your driver.  If the latest available driver is 470, run
</br></br>
```
sudo apt install nvidia-driver-470
```
</br></br>
You can use the apt search command example in section B to see which Nvidia driver packages are available.
</br></br>
Next, install the disable-nouveau package
</br></br>
```
sudo apt install disable-nouveau
```
</br></br></br>
Lastly, whether you followed the instructions in A, B or C, reboot your computer.

</br></br></br>



## Blacklisting Nouveau
**Problem**: After installing a specific Nvidia driver version and rebooting, the system is still running Nouveau
</br></br>

**Solution**: We need to blacklist Nouveau by creating installing the following package
</br></br>
```
sudo apt install disable-nouveau
```
</br></br></br>



## No graphical output after Nvidia driver install
**Problem**: After installing the Nvidia driver, there is still no graphical output.

**Solution**: If this is a fresh Drauger OS install, reinstall the OS. Then, make sure your system is up-to-date before installing the Nvidia drivers.

Otherwise, [contact support](https://draugeros.org/contact-us) so we can walk you through more complex recovery procedures.



## Steam fails to launch
**Problem**: Upon trying to launch Steam, you received the error
</br></br>
```
Fatal error: Failed to load steamui.so
```
</br></br>

**Solution**: Try running the following command
</br></br>
```
sudo apt install --reinstall libva-x11-2:i386
```
</br></br></br>

## Booting to initramfs/busybox prompt on first boot
**Problem**: After installation of Drauger OS, the computer boots only to an iniramfs and/or busybox prompt.
</br></br>

**Solution**: Reinstall Drauger OS, but ensure the "install updates during installation" and "install restricted extras" options are disabled.
</br></br></br>


## Receive "Invalid NULL filename" error upon attempting to update
**Problem**: When attempting to install a Flatpak or update the system, the computer displays an error messages that ends with "Invalid NULL Filename:
</br></br>

**Solution**: Run the following command
</br></br>
```
sudo flatpak repair
```
</br></br></br>
