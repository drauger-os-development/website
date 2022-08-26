# USB drive will not boot DraugerOS live environment

Problem: After using Rufus to install DraugerOS onto a bootable usb, DraugerOS is unable to boot to the live environment

Solution: Ensure Rufus is operating in DD mode

# Nvidia Video driver issues

Problem: When running a machine with an Nvidia GPU, you notice graphical issues such as being stuck at a low resolution, failure to launch UI or slow rendering.

Solution: For any graphics card newer than the 10-series, run

```bash
sudo apt install nvidia-driver-latest
```