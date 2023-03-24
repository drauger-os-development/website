# Developing For Drauger OS
## Overview

Drauger OS is a Linux desktop operating system that prioritizes performance above all else. As such, there are different considerations one must take into account when writing code for Drauger OS, versus something like Ubuntu, or even Windows or MacOS. In this article, we plan to cover some of the other issues developers must take into account when developing for Drauger OS.

## Licensing
Software written for Drauger OS may be under any license. However, if you want your software to be included in the ISO file we distribute, it MUST be under an open-source license such as the GPL, the MIT license, or BSD license. If you license your code under a more closed license, then while we will gladly include it in our repositories, we will not include it in the ISO.

## Programming Languages
Under no circumstances should code for Drauger OS be written in Java. Javascript should also be avoided wherever possible, with the sole exception being the website. Both of these languages have a reputation for being slow, and indeed there are better options available.

Otherwise, developers are more than welcome to write their code in another language which supports Linux. However, we suggest the following, in no particular order:
 - Python 3.x
 - Rust
 - C
 - C++
 - UNIX Shell / BASH

### In-house code
Software written for Drauger OS by contributors is largely written in Python. This allows us to iterate quickly, skip the entire compilation step, support multiple CPU architectures, and provides us with access to the massive Python ecosystem. This is not to say, however, that code MUST be written in Python.
 
 ### Externally Contributed Code
 Externally contributed code should be written in the same language as the majority of whatever project it is contributed to, wherever  possible.
 
 If contributing an entire project or application to Drauger OS, recommended languages should be adhered  to more strictly 


## Security
While security is not the number one concern of Drauger OS, it is still an issue we take very seriously as users have the right to be safe while playing their favorite games. As such, when developing your software, it is strictly forbidden to take any shortcuts which significantly decrease security, introduce vulnerabilities, and/or backdoors into the system.

## Privacy
Privacy is of the utmost importance. Under no circumstances should data be collected on users without them providing their express consent to the data collection, and full transparency as to what data is being collected.
