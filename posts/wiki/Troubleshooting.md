# Troubleshooting

# USB drive will not boot DraugerOS live environment

Problem: After using Rufus to install DraugerOS onto a bootable usb, DraugerOS is unable to boot to the live environment

Solution: Ensure Rufus is operating in "dd" mode

# Nvidia Video driver issues

Problem: When running a machine with an Nvidia GPU, you notice graphical issues such as being stuck at a low resolution, failure to launch UI or slow rendering.

Solution: For any graphics card newer than the 10-series, run

```bash
sudo apt install nvidia-driver-latest
```

# Blacklisting Nouveau

Problem: After installing Nvidia drivers and rebooting, the system is still running Nouveau

Solution: We need to blacklist Nouveau by creating inputting the following into /etc/modprobe.d/blacklist-nvidia-nouveau.conf

```text
blacklist nouveau
options nouveau modeset=0
```

Here is the command to do everyting needed in one line

```bash
echo -e "blacklist nouveau\noptions nouveau modeset=0" | sudo tee /etc/modprobe.d/blacklist-nvidia-nouveau.conf
```

# Steam fails to launch

Problem: Upon trying to launch Steam, you received the error
```text
Fatal error: Failed to load steamui.so
```

Solution: Try running the following command
```bash
sudo apt install --reinstall libva-x11-2:i386
```