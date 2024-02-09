# How to reset your password

## If you know your password
Whether you prefer the command line or a graphical interface, changing your password in Ubuntu with KDE Plasma is quick and straightforward. Here are two options:

Option 1: Using the Terminal

1) Open a terminal window: Search for "Terminal" in the Applications menu or press Ctrl + Alt + T.
2) Type the command: Enter passwd and press Enter.
3) Enter current password: Type your current password and press Enter (characters won't be displayed).
4) Set new password: Enter your new password and press Enter (no visual feedback).
5) Confirm new password: Re-enter your new password and press Enter for confirmation.
6) Success message: You'll see "Password changed successfully" if all went well.

Option 2: Using the Users Application

1) Press the super (Windows) key and search for Users.  Select the Users application from the results
3) Choose your account: Select the user account whose password you want to change.
4) Change Password: Click the "Password" button.
5) Enter current password: In the "Current Password" field, type your current password.
6) Set new password: Enter your new password in the "New Password" and "Confirm Password" fields.
7) Confirm change: Click the "Change" button.
8) Success message: A message will confirm that your password has been changed successfully.

## If you don't know your password

1) Reboot your system.
2) During boot, hold down the Shift key until the boot menu appears.
3) Select your Drauger OS installation and press "e" to edit the boot options.
4) Look a line to appear at the bottom and add "init=/usr/bin/bash" to the end.
5) If there is an ro change it to rw.
6) Press enter to boot with the modified options.
7) You'll be dropped into a root terminal prompt.
8) Type the command: passwd username (replace username with your actual username).
9) Enter your current password when prompted.
10) Type your new password twice and press Enter for confirmation.
11) Reboot your system: Type reboot and press Enter.