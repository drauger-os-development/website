# How to reset your password

## If you know your password
Whether you prefer the command line or a graphical interface, changing your password in Ubuntu with KDE Plasma is quick and straightforward. Here are two options:

</br>
</br>
### Option 1: Using the Terminal

1) **Open a terminal window**: Search for "Terminal" in the Applications menu or press Ctrl + Alt + T.
</br>
2) **Type the command**: Enter passwd and press Enter.
</br>
3) **Enter current password**: Type your current password and press Enter (characters won't be displayed).
</br>
4) **Set new password**: Enter your new password and press Enter (no visual feedback).
</br>
5) **Confirm new password**: Re-enter your new password and press Enter for confirmation.
</br>
6) **Success message**: You'll see "Password changed successfully" if all went well.

</br>
</br>
### Option 2: Using the Users Application

1) **Press the super (Windows) key and search for Users**.  Select the Users application from the results
</br>
2) **Choose your account**: Select the user account whose password you want to change.
</br>
3) **Change Password**: Click the "Password" button.
</br>
4) **Enter current password**: In the "Current Password" field, type your current password.
</br>
5) **Set new password**: Enter your new password in the "New Password" and "Confirm Password" fields.
</br>
6) **Confirm change**: Click the "Change" button.
</br>
7) **Success message**: A message will confirm that your password has been changed successfully.

</br>
</br>
## If you don't know your password

1) Reboot your system.
</br>
2) During boot, hold down the Shift key until the boot menu appears.
</br>
3) Select your Drauger OS installation and press "e" to edit the boot options.
</br>
4) Look for a line to appear at the bottom and add "init=/usr/bin/bash" to the end.
</br>
5) If there is an option that says `ro` change it to `rw`.
</br>
6) Press enter to boot with the modified options.
</br>
7) You'll be dropped into a root terminal prompt.
</br>
8) Type the command: `passwd username` (replace username with your actual username).
</br>
9) Enter your current password when prompted.
</br>
10) Type your new password twice and press Enter for confirmation.
</br>
11) Reboot your system: Type `reboot` and press Enter. **NOTE**: If this does not work, simply hold the power button until your computer shuts off, then turn it back on.