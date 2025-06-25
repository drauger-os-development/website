# Why use Drauger OS?

Curious why you should bother using Drauger OS instead of some other Linux distro, like Pop!_OS, or Ubuntu? It's a fair question. Drauger OS is a small, young distro that not many people have heard about. It makes sense to be skeptical. But, despite that, Drauger OS is a fantastic choice for gamers.

## What does Drauger OS do to improve performance?

Drauger OS has a number of things up it's sleeves that it uses to help improve performance! These range from simple things that anyone can do to their Linux install, to more complex things only the more advanced will venture to do on their own.

One of the most basic things Drauger OS does in order to increase performance, with respect to game and level load times, is using a package called `preload`. `preload` learns from your usage patterns, and intelligently loads game save data, asset data, shader code, and more into memory, before it's needed. Without it, your system would only load these things into memory when they are needed. With `preload`, Drauger OS already has this data in memory, waiting for your game, when it is called upon. And, this goes beyond game data. It also loads parts of the operating system itself, and other apps into memory ahead of time. This helps parts of the OS to load faster, and be more responsive as well.

One of the more controversial things Drauger OS does to help performance is to mandate all systems must have some form of swap space. This is used by your system when your memory is full so that your computer is able to keep running and potentially prevent itself from grinding to a halt. Swap is also used if you ever put your computer into Hibernate mode, or use [Hybrid Sleep](https://askubuntu.com/questions/219141/what-is-hybrid-suspend). It can also allow your computer to more easily offload data it will need in the future to disk, that it doesn't want to re-generate (this can already be done by writing this data to a file, but a program must be written to do so. Swap allows the operating itself to perform a similar task, in a way that the application doesn't notice). Further, it helps your computer also feel more snappy.

Drauger OS goes farther than this even, and whenever choosing which desktop, window manager, or display server we use, we always try to choose the lightest weight option, or the option that improves performance the most. This is why up until Drauger OS 7.6, we used Xfce due to how lightweight it is. And, from Drauger OS 7.7 onward, we use KDE Plasma so that we can leverage Wayland, which provides many games with a small performance bump.

Drauger OS does many other things to improve performance, such as disabling unneeded `systemd` services and using `systemd-boot`, but the single change that has the biggest impact, is the fact that we compile our own kernel in-house. This kernel is the mainline kernel. No code has been changed. The compilation options are very similar to what you find with the Xanmod kernel. However, many options that are meant for industrial, embedded, data center, or server environments have disabled to reduce the size of the kernel, and reduce the amount of running code. Much of this will simply decrease kernel size, but this too can help performance with respect to boot times and how long updates take.

## What does Drauger OS do to improve the experience with getting games running?

Drauger OS comes with a number of apps to get the average gamer up and running, playing their favorite games going. For instance, Drauger OS ships with Steam pre-installed, as well as Lutris, and Heroic. While all of these are tools and normal user could easily install on their own, having them installed ahead of time can save time and effort. Gamers can focus on getting the games running, and not the launchers needed to run the games.

Starting with Drauger OS 7.7, Drauger OS also ships with ProtonUp-Qt. This app helps gamers manage versions of Proton that are available to them, thereby making it easier for them to get a specific game that may have specific needs to run for them.

## What does Drauger OS do to otherwise help gamers?

Beyond this, Drauger OS Development makes sure to foster the community around Drauger OS and the games people love to play on it. We encourage users to discuss not just Drauger OS, but non-Linux topics even within the community. We encourage users to play games together when possible, and to help each other out with getting games and Drauger OS to run.

Drauger OS Development prides itself on having a vibrant, diverse, and active community. And encourages all gamers to join us, regardless of OS. As what introduces us, may be the OS, but the games are what really brings us all together to have fun and enjoy the many worlds we all live in thanks to technology.