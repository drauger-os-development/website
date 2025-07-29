# Getting Flatpak Steam to work with Secondary Drives 
Before we get started, make sure you have the app "Flatseal" installed. You can install it with this command, if you don't already have it:
 
```
flatpak install com.github.tchx84.Flatseal
```
Drauger OS 7.7 and older do not ship with Flatseal preinstalled, so please double check if you have it!

Secondly, please install the package `arch-install-scripts`:
```
sudo apt install arch-install-scripts
```

Finally, please make sure your games drive is formatted in a Linux-native filesystem, such as EXT4 or BTRFS, as Proton often has problems with NTFS drives, and many games cannot be stored on FAT32/exFAT drives at all.
 
## Step 1: Setup the drive to auto-mount
### Step 1a: Make the directory
In order for this drive to work reliably with Steam, it needs to be setup to automount. To do that, first, make a folder where you would like to access this drive. Since this is for a games drive, we will put it under our home directory, in a folder named "Games":

```
mkdir ~/Games
```

### Step 1b: Mount the drive
Next, mount the drive under that directory. Here, we will assume that drive is `/dev/sdb`, and it has a single partition:

```
sudo mount /dev/sdb1 ~/Games
```

### Step 1c: Update your FSTAB
Next, we will use the `genfstab` command to update our FSTAB file. This will automatically have the drive we just mounted auto-mount at every reboot. First, test and make sure nothing is being removed that needs to be mounted:

```
genfstab -U / | grep -vE "loop|portal" | sed -z 's/\n\n\n//g'
```

Please read the output carefully, as the command provided above is automatically going to remove entries from your FSTAB that don't need to be there, as well as wasted empty lines.

If everything you need is there, make a backup of your old FSTAB:

```
sudo cp /etc/fstab /etc/fstab.bak
```

Then make the new one:

```
genfstab -U / | grep -vE "loop|portal" | sed -z 's/\n\n\n//g' | sudo tee /etc/fstab
```
 
## Step 2: Give Steam Access to the Drive in Question
With Flatseal installed, open it, and scroll down the panel on the left until you see Steam. Click on it. This will give you access to controlling all of Steam's permissions.
 
Scroll down until you get to the "Filesystem" section. Then, click the "Add" icon (circled in red below).
 
![button to click to add a drive to Steam](/assets/images/FlatpakSteam-1.png)

Then, in the empty text box that pops up (circled in yellow above), type in where you have your new drive mounted (in our case, ~/Games).

Once you see the Yellow triangle to the left turn in to a diamond (depending on your theme, this may be red, blue, or some other color), you can close Flatseal.

## Step 3: Tell Steam to use the drive in question
If you had Steam open before, close it completely, and relaunch it. Otherwise, open Steam now, and navigate to your Steam Settings:

![how to get to Steam Settings](/assets/images/FlatpakSteam-2.png)

Once Steam Settings, go to Storage, click the drop drown, the click "Add Drive" and add your drive!

![how to add the drive to Steam](/assets/images/FlatpakSteam-3.png)
