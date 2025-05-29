---
layout: post
title: "Technology Business Decision - C++ or Java"
date: 2007-01-15 18:55:40 -0500
categories: rVibe Technology
tags: ['wordpress-import']
---

When building client side software that interfaces directly with the internet (as we are), it's very tempting to write in Java. You get the nice benefit of a cross-platform runtime where you can pretty much drop in code and you're ready to go. It's got great firewall tunnelling support and it's easy and fast to develop. Unfortunately performance is very slow, the memory footprint is large, it requires additional client side installs and when you want to move outside there runtime environment it gets ugly. And when using it, it feel - well, like Java, which isn't so great. So we look to C++ as a language. The performance is excellent, the code environment is solid and there are lots of classes available for it, making it easy to get up and running quickly. The developers are typically more expensive and you actually have to port the code to other platforms, but what you gain is more stability and faster performance. So we choose C++ as our language of choice since performance (or at least the perception of performance) is crucial to our application. Now you run into other concerns. How do you access the CD Burner, or the Audio Player or the Networking stack? You have to write these classes, or use ones in existence. In Microsoft, that means using MFC (Microsoft Foundation Classes), which are easy to "wrap" into your code and use them. But that gets tricky, because if you don't write them yourself, you're then tied into the Microsoft platform for lots of your core functionality. I suppose that's not all bad, but we really want to have an Apple client, not just a Microsoft. However, in the interest of time, we're wrapping MFCs with C++ code. We're deal with port and any class rewrites later. Wow - you gotta love technology speak, check out that sentence - LOL!

---

*Originally published on WordPress on January 15, 2007. Migrated to this blog on May 29, 2025.*
