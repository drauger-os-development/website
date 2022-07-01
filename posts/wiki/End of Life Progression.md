# End of Life Progression
## How does Drauger OS progress through the stages of it's End-Of-Life?

All good things must come to an end. This is true of everything, including any given Drauger OS release. So what are the stages of End-Of-Life (EOL), and what do users need to do once a given release hits this final stage in it's life?

In this post, we're going to follow the End-Of-Life of a **hypothetical** Drauger OS release, called V1, and it's successor, V2. This will better help us understand how this process works and how different releases of Drauger OS affect one another.

### Stage 1: Dropped Support and Halted Updates

When our hypothetical Drauger OS V1 release first hits it's EOL, support for it is immediately dropped. Typically, the first day of EOL is the same as the first day a new release of Drauger OS (in this case, V2) is available.

If users have a bug in the old Drauger OS V1 release, they will receive no help, except if the bug pertains to updating to a new version of Drauger OS, such as V2. In those circumstances, users will receive support in upgrading to the new Drauger OS release.

Finally, no more updates will be issued to Drauger OS V1, in order to incentivize users to upgrade to supported software.

### Stage 2: `apt` Repository Shutdown

Normally, after about 2 weeks, an EOL Drauger OS release such as Drauger OS V1 will be removed from our `apt` repository. When this happens, users will no longer be able to download packages only available to Drauger OS users such as [`systemd-boot-manager`](https://github.com/drauger-os-development/systemd-boot-manager), [`xfce4-desktop-service`](https://github.com/drauger-os-development/xfce4-desktop-service), or [`steam-login-session`](https://github.com/drauger-os-development/steam-login-session).

Furthermore, because this will throw an error in `apt`, users will also no longer be able to update without modifying their `sources.list` file, found in `/etc/apt`.

At this point, the best way to upgrade is to download an ISO for a new Drauger OS version, such as V2, and install that over top of the End-Of-Life Drauger OS V1.

### Stage 3: ISO deletion

At this point, typically another new release of Drauger OS has been released (lets call this new one V3, as it replaces V2 (setting V2 down the EOL path), which replaced V1). Up until this point, the old Drauger OS version has been provided as a service to the community.

 1. When asked in a poll across multiple platforms, Drauger OS users requested old ISOs be made available. This is our compromise.
 </br></br>
 2. Being able to check out old ISOs lets new users see how far Drauger OS has come.
 </br></br>
 3. If a user needs a specific, older, version of Drauger OS for some reason, doing this makes that available to them.
 
However, by this point, the code in the provided ISO should be considered overwhelmingly insecure, and should not be trusted. Therefore, the old ISO for Drauger OS V1 is deleted, and no longer made available to download

### Conclusion

The above End-Of-Life process is relatively simple, albeit slow. We want to gently push Drauger OS users onto newer software after all. And forcing the change quickly isn't always a smart idea. So, slowing it down and allowing some time for users to tinker and decide what they want to do really helps make Drauger OS more user-friendly.

We're also looking into adding one-time notifications that pop-up whenever a specific Drauger OS release reaches End-Of-Life. These are meant to simply inform the user of what exactly is going on, what to expect, and potential courses of action.

We hope that this post has helped make the End-Of-Life of a given Drauger OS release a little more understandable, and predictable for you.