# Drauger OS on Steam Deck
## Get the most out of your hand-held PC
</br>
Drauger OS isn't designed for hand-held PCs, but that doesn't mean it won't work on them! Since the Steam Deck's release, the Drauger OS Development team has been hard at work, making sure Drauger OS works on the Steam Deck just as well as Steam OS.
</br></br>

### What's working
</br>

#### Display Output
When using Wayland, Drauger OS automatically recognizes it is on a Steam Deck (and, presumably, other hand-held PCs. This is untested.) and rotates the screen to the correct orientation. Resolution scaling may be a bit wonky, but display output on both the internal display and external displays works perfectly out of the box!
</br></br>

#### Controls
Touch screen input is recognized in the correct locations, and the built-in controller works out of the box.
</br></br>
The right touch-pad works to control the mouse, with the right trigger for left click and left trigger for right click. However, if Steam or a game which uses the controller is launched, Drauger OS automatically hands over control to that program. Unfortunetly, the program doesn't always hand control back properly. Using Steam Big Picture Mode in Drauger OS helps to avoid this issue.
</br></br>

#### Wireless Connectivity
Both Wi-Fi and Bluetooth work flawlessly out of the box!
</br></br>

#### Battery Reporting and Charging
Battery charge and health reporting, as well as charging, both work out of the box!
</br></br>

#### SD Card Support
Using the SD Card as external storage has not been tested, but is presumed working as booting from the SD Card works out of the box, and is the recommended way to use Drauger OS on Steam Deck at the current time.
</br></br>

#### USB Support
The built-in USB-C port works correctly out of the box! This includes charging and display output.
</br></br>

#### GPU Acceleration
As the built-in GPU on the Steam Deck is RDNA-based, it works out of the box with no hassle or drivers required!
</br></br>

### What's NOT Working
</br>

#### Audio Output
Audio output, to the built-in speakers or headphone jack, is not working.
</br></br>
If you wish to have audio output on Drauger OS on Steam Deck, you still have a few options available to you. Audio output DOES work in the following scenarios:
</br>
<ul>
 <li>USB Audio</li>
 <li>Bluetooth Audio</li>
 <li>Audio output through HDMI or DisplayPort</li>
</ul>
</br>
The exact reason for audio output failing on the built-in speakers or headphone jack is currently unknown. However, we theorize that the problem has something to do with the internal DAC (digital-to-analog converter.) We are confident this issue can be fixed without using the same kernel as Steam OS, as other distros have reported working audio on the Steam Deck.