# Troubleshooting

## USB drive will not boot Drauger OS live environment

**Problem**: After using Rufus to install Drauge rOS onto a bootable usb, Drauger OS is unable to boot to the live environment

**Solution**: Ensure Rufus is operating in "dd" mode

## Nvidia Video driver issues

**Problem**: When running a machine with an Nvidia GPU, you notice graphical issues such as being stuck at a low resolution, failure to launch UI or slow rendering.

**Solution**: For any graphics card newer than the 10-series, run

```bash
sudo apt install nvidia-driver-latest
```

## Blacklisting Nouveau

**Problem**: After installing a specific Nvidia driver version and rebooting, the system is still running Nouveau

**Solution**: We need to blacklist Nouveau by creating installing the following package

```bash
sudo apt install disable-nouveau
```

## Steam fails to launch

**Problem**: Upon trying to launch Steam, you received the error
```text
Fatal error: Failed to load steamui.so
```

**Solution**: Try running the following command
```bash
sudo apt install --reinstall libva-x11-2:i386
```

## Booting to initramfs/busybox prompt on first boot

**Problem**: After installation of Drauger OS, the computer boots only to an iniramfs and/or busybox prompt.

**Solution**: Reinstall Drauger OS, but ensure the "install updates during installation" and "install restricted extras" options are disabled.
