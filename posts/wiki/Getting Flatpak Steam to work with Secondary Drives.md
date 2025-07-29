# Getting Flatpak Steam to work with Secondary Drives 
Before we get started, make sure you have the app "Flatseal" installed. You can install it with this command, if you don't already have it:
</br></br>
```
flatpak install com.github.tchx84.Flatseal
```
</br></br>
Drauger OS 7.7 and older do not ship with Flatseal preinstalled, so please double check if you have it!
</br></br>
Secondly, please install the package `arch-install-scripts`:
</br></br>
```
sudo apt install arch-install-scripts
```
</br></br>
Finally, please make sure your games drive is formatted in a Linux-native filesystem, such as EXT4 or BTRFS, as Proton often has problems with NTFS drives, and many games cannot be stored on FAT32/exFAT drives at all.
 </br></br>
## Step 1: Setup the drive to auto-mount
### Step 1a: Make the directory
In order for this drive to work reliably with Steam, it needs to be setup to automount. To do that, first, make a folder where you would like to access this drive. Since this is for a games drive, we will put it under our home directory, in a folder named "Games":
</br></br>
```
mkdir ~/Games
```
</br></br>
### Step 1b: Mount the drive
Next, mount the drive under that directory. Here, we will assume that drive is `/dev/sdb`, and it has a single partition:
</br></br>
```
sudo mount /dev/sdb1 ~/Games
```
</br></br>
### Step 1c: Update your FSTAB
Next, we will use the `genfstab` command to update our FSTAB file. This will automatically have the drive we just mounted auto-mount at every reboot. First, test and make sure nothing is being removed that needs to be mounted:
</br></br>
```
genfstab -U / | grep -vE "loop|portal" | sed -z 's/\n\n\n//g'
```
</br></br>
Please read the output carefully, as the command provided above is automatically going to remove entries from your FSTAB that don't need to be there, as well as wasted empty lines.
</br></br>
If everything you need is there, make a backup of your old FSTAB:
</br></br>
```
sudo cp /etc/fstab /etc/fstab.bak
```
</br></br>
Then make the new one:
</br></br>
```
genfstab -U / | grep -vE "loop|portal" | sed -z 's/\n\n\n//g' | sudo tee /etc/fstab
```
</br></br>
## Step 2: Give Steam Access to the Drive in Question
With Flatseal installed, open it, and scroll down the panel on the left until you see Steam. Click on it. This will give you access to controlling all of Steam's permissions.
</br></br> 
Scroll down until you get to the "Filesystem" section. Then, click the "Add" icon (circled in red below).
</br></br> 
![button to click to add a drive to Steam](/assets/images/FlatpakSteam-1.png)
</br></br>
Then, in the empty text box that pops up (circled in yellow above), type in where you have your new drive mounted (in our case, ~/Games).
</br></br>
Once you see the Yellow triangle to the left turn in to a diamond (depending on your theme, this may be red, blue, or some other color), you can close Flatseal.
</br></br>
## Step 3: Tell Steam to use the drive in question
If you had Steam open before, close it completely, and relaunch it. Otherwise, open Steam now, and navigate to your Steam Settings:
</br></br>
![how to get to Steam Settings](/assets/images/FlatpakSteam-2.png)
</br></br>
Once Steam Settings, go to Storage, click the drop drown, the click "Add Drive" and add your drive!
</br></br>
![how to add the drive to Steam](/assets/images/FlatpakSteam-3.png)
