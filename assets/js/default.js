            function AboutSubMenu() {
                var menuBox = document.getElementById('desktopAbout');
                if (menuBox.style.top == "3.5em") {
                    menuBox.style.top = "-7em";
                } else {
                    menuBox.style.top = "3.5em";
                }
            }
            function ContributingSubMenu() {
                var menuBox = document.getElementById('desktopContributing');
                if (menuBox.style.top == "3.5em") {
                    menuBox.style.top = "-50em";
                } else {
                    menuBox.style.top = "3.5em";
                }
            }
            function CommunitySubMenu() {
                var menuBox = document.getElementById('desktopCommunity');
                if (menuBox.style.top == "3.5em") {
                    menuBox.style.top = "-50em";
                } else {
                    menuBox.style.top = "3.5em";
                }
            }
/* - Mobile Navbar below - */
            function mobileSettings() {
             var menuBox = document.getElementById('mobile-options');
             if (menuBox.style.left == "0em") {
                 menuBox.style.left = "-50em";
              } else {
                  menuBox.style.left = "0em";
              }
            }
            function MobileAboutSubMenu() {
                var menuBox = document.getElementById('mobileAbout');
                var mobileOptions = document.getElementById('mobile-options');
                if (mobileOptions.style.left == '0em') {
                    mobileOptions.style.left = '-50em';
                } 
                if (menuBox.style.left == "0em") {
                    menuBox.style.left = "-50em";
                } else {
                    menuBox.style.left = "0em";
                }
            }
            function MobileContributingSubMenu() {
                var menuBox = document.getElementById('mobileContributing');
                var mobileOptions = document.getElementById('mobile-options');
                if (mobileOptions.style.left == '0em') {
                    mobileOptions.style.left = '-50em';
                } 
                if (menuBox.style.left == "0em") {
                    menuBox.style.left = "-50em";
                } else {
                    menuBox.style.left = "0em";
                }
            }
            function MobileCommunitySubMenu() {
                var menuBox = document.getElementById('mobileCommunity');
                var mobileOptions = document.getElementById('mobile-options');
                if (mobileOptions.style.left == '0em') {
                    mobileOptions.style.left = '-50em';
                } 

                if (menuBox.style.left == "0em") {
                    menuBox.style.left = "-50em";
                } else {
                    menuBox.style.left = "0em";
                }
            }
            function backToDefault() {
                var menuBox = document.getElementById('mobile-options');
                if (menuBox.style.left == '-50em') {
                    menuBox.style.left = '0em';
                } else {
                    return;
                }
            }
    // Below is the script to automatically hide open elements when scrolled away from the top of the screen (Mobile Nav)
    function hideDesktopElements() {
                const elementIDs = ["desktopAbout", "desktopContributing", "desktopCommunity"];
                changeTopValue(elementIDs);
             }
            window.addEventListener("scroll", hideDesktopElements);
            function handleClickOutsideDesktopNav(event) {
                const navbar = document.getElementById('topnav');
                if (!navbar.contains(event.target)) {
                    const elementIDs = ["desktopAbout", "desktopContributing", "desktopCommunity"];
                    changeTopValue(elementIDs);
                }
            }
            document.addEventListener('click', handleClickOutsideDesktopNav);
            function handleClickOutsideMobileNav(event) {
                const mobileNav = document.getElementById('mobile-options');
                if (!mobileNav.contains(event.target)) {
                    const elementIDs = ["mobileAbout", "mobileContributing", "mobileCommunity"];
                    changeLeftValue(elementIDs);
                }
            }
            function onlyDesktopAbout() {
                        const contrib = document.getElementById('desktopContributing')
                        const community = document.getElementById('desktopCommunity');
                        if (contrib.style.top == '3.5em') {
                            contrib.style.top = '-50em';
                        }
                        if (community.style.top == '3.5em') {
                            community.style.top = '-50em';
                        } else {
                            return
                        }
                    }
    function onlyDesktopContrib() {
                        const about = document.getElementById('desktopAbout')
                        const community = document.getElementById('desktopCommunity');
                        if (about.style.top == '3.5em') {
                            about.style.top = '-7em';
                        }
                        if (community.style.top == '3.5em') {
                            community.style.top = '-50em';
                        } else {
                            return
                        }
                    }
    function onlyDesktopCommunity() {
                        const about = document.getElementById('desktopAbout')
                        const contrib = document.getElementById('desktopContributing');
                        if (about.style.top == '3.5em') {
                            about.style.top = '-7em';
                        }
                        if (contrib.style.top == '3.5em') {
                            contrib.style.top = '-50em';
                        } else {
                            return
                        }
                    }
            function changeLeftValue(ids) {
                ids.forEach(id => {
                    const element = document.getElementById(id);
                if (element) {
                    element.style.left = "-50em";
                } else {
                    console.error("Element with ID", id, "not found.");
                }
                });
            }
             function hideMobileElements() {
                const elementIDs = ["mobile-options", "mobileAbout","mobileContributing", "mobileCommunity"];
                changeLeftValue(elementIDs);
             }
             window.addEventListener("scroll", hideMobileElements);
            function changeTopValue(ids) {
                ids.forEach(id => {
                    const element = document.getElementById(id);
                if (element) {
                    element.style.top = "-50em";
                } else {
                    console.error("Element with ID", id, "not found.");
                }
                });
            }
            document.addEventListener('click', handleClickOutsideMobileNav);
            function onlyAbout() {
                const menuBox = document.getElementById('mobileAbout')
                const contrib = document.getElementById('mobileContributing')
                const community = document.getElementById('mobileCommunity');
                if (menuBox.style.left == '-50em') {
                    menuBox.style.left = '15em'
                }
                if (contrib.style.left == '15em') {
                    contrib.style.left = '-50em';
                }
                if (community.style.left == '15em') {
                    community.style.left = '-50em';
                } else {
                    return
                }
            }
            function onlyContrib() {
                const contrib = document.getElementById('mobileAbout')
                const community = document.getElementById('mobileCommunity');
                if (contrib.style.left == '15em') {
                    contrib.style.left = '-50em';
                }
                if (community.style.left == '15em') {
                    community.style.left = '-50em';
                } else {
                    return
                }
            }
            function onlyCommunity() {
                const contrib = document.getElementById('mobileAbout')
                const community = document.getElementById('mobileContributing');
                if (contrib.style.left == '15em') {
                    contrib.style.left = '-50em';
                }
                if (community.style.left == '15em') {
                    community.style.left = '-50em';
                } else {
                    return
                }
            }
