---
layout: post
title: "The difficulty with syncing social data (again)"
date: 2007-02-21 18:00:30 -0500
categories: rVibe
tags: ['wordpress-import']
---

![rVibe Logo](http://meansofproduction.wordpress.com/wp-content/uploads/2007/02/rvibelogo.thumbnail.jpeg)We're headlong on development and wham hit a data issue. The trouble with social network data in our case is not just the many-many-many relationship, but also the incorporation of a rich data set within our client software. And that data in the client needs to be synced (so to speak) with the client database. This is a very tricky thing to begin with, and when you make any schema change, it gets far far far worse. We're right back to the importance of building social network and eCommerce in from the beginning - you just can't tack it on later. I really feel this strategy is a pretty substantial barrier to entry for any company developing a music product with social networking. The lastest nightly build for our release was toast. We had to refresh everything in the database (on client and server) and start over with a new build. Ugh. Not a setback, but an important event to happen anyway. Note to self - it's so much easier to have a single web database without multiple client databases. Not as much fun or value, but easier.

---

*Originally published on WordPress on February 21, 2007. Migrated to this blog on May 29, 2025.*
