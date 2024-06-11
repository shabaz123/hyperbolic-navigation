

# Introduction
I often take satellite navigation systems such as GPS for granted, and it got me thinking about how dependent we are on that technology, and how on earth people managed in the past. This article documents my findings.

It covers the concept of latitude and longitude, and how navigation was performed around the 18th century using star or sun location, and measuring time. 

By the 20th century, during WW2, techniques were developed that relied on multiple ground station radio transmitters sending signals with a certain phase relationship or with a particular pulse sequence. Radio receivers on ships and aircraft would be used to measure the phase difference or pulse timing between the two signals, and using that to approach a location fix.

# Longitude and Time-keeping

In the introduction of a book called [Longitude](https://www.amazon.co.uk/Longitude-Genius-Greatest-Scientific-Problem/dp/080271529X), Neil Armstrong mentions how [Pope Alexander IV](https://en.wikipedia.org/wiki/Pope_Alexander_IV) drew a vertical line from North to South, and assigned all lands to the two top maritime powers of Europe: all lands to the west to Spain, and all to the right to Portugal. The problem was, no-one knew where the line fell!

The problem of identifying precise longitude was of high importance, because sailors would routinely perish, because of the difficulty of determining where land was.

<img width="100%" align="left" src="assets\diag-latitude.jpg">

**Latitude** (angle indicating how far up or down the globe) was not too difficult to figure out, because it could be determined in several ways; for instance you could search for particular stars (for instance the North Star, and measuring the angle of it from the horizon). A quick daytime method would be to measure the angle of the sun from your visible horizon, which is known as the sun's angle of elevation, and subtract it from 90. Then, a correction is needed because the earth tilts up to plus or minus 23.4 degrees over the course of the year; it's seasonal (about +23.4 degrees in mid-June, and -23.4 degrees in mid-December, and is close to zero mid-March and mid-September), is easy to calculate, and is called the sun's angle of declination. You'd need to subtract the magnitude of the angle of declination, to get an accurate result.

<img width="100%" align="left" src="assets\diag-lat-lon-explained.jpg">

However, **longitude** starts at an arbitrary man-made position (it happens to be in Greenwich, London). There are many stories of ships traveling the wrong distance east or west around the globe, and (if not crashing into rocks), poor longitude estimates resulted in overshooting or undershooting land, and, with depleting food, and risk of scurvy, the captain deciding to turn around, and traveling for days or weeks, only to then realize that the first direction must have been correct. Just on one voyage, two thousand sailors on four warships died for want of better navigation, and eventually, the UK government issued a reward (worth millions in today’s money) for a solution. It went unclaimed for more than half a century.

Some people believed the solution lay with correct timing. The problem was, clocks were inaccurate in the 1700’s!

The reason time is important, is that, (there are several ways, but this is the simplest to understand) by simply looking at the position of the sun (which moves across the sky at 15 degrees per hour), and knowing the time at the Greenwich Meridian, you can determine your longitude. For example, if the sun is directly above you, and the time at Greenwich is 1 pm, then you know that your longitude must be 15 degrees west of Greenwich.

There were some crackpot suggestions for the time problem, one of them being ‘the wounded dog’ method. There was a theory that a particular medicine had mystical powers of ‘healing at a distance’ if the original bandage was soaked in it. The logic went that if a dog were deliberately wounded and then placed on a ship, then someone on land could daily soak the bandage at noon, and the distant wounded dog would let out a yelp at that precise time since the medicine would sting in the wound. You’d just need to deliberately prevent the wound from fully healing, for months while out to voyage.

The person who actually solved the problem, [John Harrison](https://en.wikipedia.org/wiki/John_Harrison), was treated badly, and, for a lifetime’s work, received just a small reward with only three years of life left to enjoy it. John Harrison’s solution was an ultra-accurate timepiece (so accurate, it easily competes with modern quartz watches some 250 years later!) that could withstand operation on ships.

# Hyperbolic Radio Navigation

Fast-forward to the period approaching World War 2, and now there were requirements for accurate airborne navigation. Various radio-based ideas were considered, and it was soon very obvious that relying simply on signal strength was not very feasible because it was hard to accurately measure signal strength at a distance because it dropped off so quickly, and therefore the inaccuracies would be significant.

It was felt by some that pulse-based (RADAR was a secret at that time) and phase-based systems might hold more promise. This opened up a whole range of possibilities, collectively known as hyperbolic navigation systems. If you have two transmitters transmitting in phase, or transmitting pulses simultaneously, then if a receiver is exactly halfway between the two transmitters, then the signals arrive in phase (or pulses arrive simultaneously). If, however, the receiver is at a different location, then there will be a phase or delay difference. The difference remains the same if the receiver is at any location which traces a hyperbola. The diagram below shows why.

The concentric circles emanating from one transmitter site indicate the positions where signals arrive at fixed times. If you try to intersect those circles with those from the other transmitter location, such that the difference between the pairs of ranges always remains a fixed distance, then hyperbolae are traced out. All the hyperbolae in the diagram below, have the same fixed difference of phase or pulse, the colors are just to identify separate lines or ‘lanes’, but if the receiver is on any of these lines, the phase difference is the same. For any given delay or phase difference, it is possible to plot a set of hyperbolae.

<img width="100%" align="left" src="assets\hyperbolae-lines.jpg">


What the above means is that if you have a way of measuring the phase difference or pulse arrival delay between the two transmitters, you can place yourself on a set of hyperbolae. You won’t know which of the hyperbola lines you are on, however.

Various things can be done to try to identify the particular hyperbola out of the set. One method is for the two transmitters to sweep through phase relative to each other. That results in the hyperbola lines bending as the phase changes so that the receiver sees a time-varying signal strength, an increase in received signal when they are on a hyperbola, and a decrease when they are in between two lines. Then, timing can help identify which hyperbola you’re on. Another method is to switch to a lower frequency, so that there are fewer hyperbola lines temporarily, so that the receiver can coarsely resolve, before switching to a higher frequency.

# Pulses: Gee System (QH)

One system developed in the UK, later called the Gee system (known as ‘QH’ during WW2), relied on pulses. A master transmitter would synchronize three slave transmitters, all transmitting a pulse at the same frequency after a fixed pause from the master transmission. Together, these four transmitters are known as a **chain**.

<img width="100%" align="left" src="assets\gee-diagram2.jpg">


At the receiver end, the pulses were observed on a little display (known as an oscilloscope) that charted the pulse blips over time. The circuitry would direct the pulses onto two visual graphical traces. The master transmitter pulse was observed on both traces. The next received pulse would be sent to the top trace. The pulse after that was sent to the second trace. The final pulse was sent to both traces, but it happened to be a double pulse, so it could be distinguished. The operator would measure the distance between the pulses, and the intersecting hyperbolae would provide a position fix.

The photo here shows a Gee receiver and display unit.

<img width="100%" align="left" src="assets\gee-photo.jpg">

Image source: [Wikipedia](https://commons.wikimedia.org/wiki/File:J_M_Briscoe24_07_200713_05_14IMG2104_GEE_AIRBORNE.JPG)


There is some excellent detail (including beautiful photographs) at [radiomuseum.co.uk](https://www.radiomuseum.co.uk/rf25.html).

Since there was no trigger circuitry, the operator manually fine-tuned until the pulses sat in the correct position on the display. Best-case accuracy was about 150 meters, but at distances of several hundred miles, the error could easily be several miles.

Gee was used during WW2 for navigation around the UK.


# Phase: Decca Navigation (QM)

For Operation Overlord (Battle of Normandy), a different navigation system was used, called QM (later called the Decca Navigational System). The idea was invented by William O’Brien and Harvey Schwarz in the USA but gained significant interest in the UK and was trialed in 1941 on the Welsh coast. The system relied on phase difference, rather than measuring the time between pulses. The way it worked was that a master site and a number of slaves (two or three), together known as a chain, all transmitted signals at different frequencies, but all locked to a base frequency. The receiver would multiply pairs of received signals to a common frequency and then work out the phase difference.

In 1943, the base frequency **f** was 14 kHz, and the master and two slaves transmitted at **6f**, **8f** and **9f** respectively (i.e. 84, 112 and 126 kHz).

At the receiving end, the master and first slave received signals would be separately multiplied by 4 and 3 respectively, i.e. 84 x 4 and 112 x 3, which would result in two signals both of frequency 24f (336 kHz), but with different phase, depending on location with respect to the master and the first slave.

Similarly, the master and second slave signals would be separately multiplied by 3 and 2, resulting in two signals of frequency 18f (252 kHz), again with a phase relationship. (Later, a third slave was added, at a frequency of **5f**).

Just as shown in the earlier diagram, hyperbola lines could be drawn at any phase relationship, for instance when the signals are in phase, at zero degrees.

The lines were used as ‘**lanes**’ during Operation Overlord, creating invisible paths through the English Channel towards Normandy. Minesweepers followed those paths, allowing ships and landing craft to follow.

<img width="100%" align="left" src="assets\nav-map-oo.jpg">


The receiver didn’t use an oscilloscope but instead used a center-zero meter that would display the phase shift. The lanes were separated by several hundred meters. A tiny movement (a few feet) off one of the lanes would cause a phase shift from zero, which would move the meter needle significantly. By seeing the number of deflections, the lines could be easily counted. After WW2, further improvements to the system were made, so that lane counting became unnecessary. By the time the system was fully mature, the transmitter sites were transmitting signals at different frequencies, over a 20-second period, repeatedly, and the sequence was quite complex. A very good collection of information about the Decca system can be found at [Jerry Proc’s website](http://www.jproc.ca/hyperbolic/decca.html).

By the 1980’s or so, there were about 50 chains deployed. The diagram below shows the European chains; 25 were deployed there. The circled values are unique chain numbers. The slave transmitters within each chain had color-code identifiers (red, green, purple).

<img width="100%" align="left" src="assets\european-chains.jpg">

Image source: Philips

The Decca system was deployed in many regions, and was used commercially until about the year 2000. The receivers were made by Racal Decca, but eventually other manufacturers, particularly Philips, built them too. This model is made by Philips, despite the Racal logo.

<img width="100%" align="left" src="assets\yn-photo.jpg">


If you're curious what's inside, the photo below shows all the interesting bits in the lower half of the case (the other half just houses the LCD digit displays and keypad).

<img width="100%" align="left" src="assets\yn-parts-annotated.jpg">


There appears to be a frequency synthesizer, two simultaneous RF receivers (so that the phase between pairs of signals can be measured), and everything is co-ordinated with an 8085-based microprocessor. 

# Summary

It’s easy to take satellite-based navigation systems for granted these days, but there was a time when thousands of lives would frequently be lost due to the difficulty of determining longitude. Although that was solved in the 18th century, there were new demands during WW2.

Prior to GPS deployment, hyperbolic navigation systems were the state-of-the-art, a couple of them being QH and QM, or Gee and Decca, respectively. The Decca system relied on phase measurement to place the receiver on hyperbolic lines or lanes and, with multiple transmitters, onto a grid of lanes. After WW2, the system was adapted for commercial use and ran successfully until the year 2000. An example of a Decca navigation system receiver was examined briefly.

There were many other hyperbolic or hyperbolic-like navigation systems that are not covered here. Some systems were incrementally improved upon, and others were independently developed. 

Thanks for reading.

## Further Reading: Quick Look at Satellite-Based Navigation: How Does it Work?

Now that pre-GPS techniques have been discussed, you may be interested in how GPS and other Global Navigation Satellite Systems (GNSS) function.

There are well over a hundred satellites in orbit, which transmit signals containing timing information and satellite position. The timing information comes from an ultra-precise clock inside each satellite. The satellite position can be pictured by imagining a sphere surrounding the planet. The satellite position can be defined using two angles: the angle from one of the poles, and the angle around the sphere (a bit like longitude), which meet up at the satellite location on that sphere.

The timing information, and the satellite position information, are transmitted at a frequency of about 1.5 GHz, and, due to the distance of the satellite orbit, it takes about 10 msec to arrive on Earth.

The received signal is very weak and would be impossible to pull out of the noise, so it is sent relatively slowly (50 bits per second), with each bit of data being encoded with a special (much faster) binary pattern before it’s transmitted. The GPS receiver tries to match up the pattern. When it does that, then, mathematically, the signal can be recovered from the noise; the pattern is known as a pseudo-random sequence (although it contains the word ‘random’, it’s not random in the normal sense; it looks random to a casual viewer, but in reality it has a pattern that can be exactly replicated by the receiver), and the matching effect is known as autocorrelation. Together, it is known as Spread Spectrum communication. The signal directed toward Earth is invisible by the time it arrives (since it’s below the noise floor!) until autocorrelation is achieved by the receiving system.

Another neat trick is that many satellites can transmit simultaneously, each with a different pseudo-random sequence, and the receiver can, in parallel, perform multiple matching operations, to achieve autocorrelation for each signal.

The receiver is designed to have the ability to time things too, but not to the same accuracy as the satellites! The receiver will locally timestamp the arrival time of each message, and then compare that local timestamp with the time encoded in the satellite signals. Once there are signals from at least four satellites (the more the better!), then there is enough information to use simultaneous equations, to solve for the location of the receiver.

Today, there are more global navigation systems than just GPS out there; there is also Galileo (European), BeiDou (Chinese) and GLONASS (Russian), all operating in a similar way. There are also more geographically-specific navigation systems too. A GNSS receiver (colloquially known as a GPS receiver) can receive information from several of the navigation systems, and therefore provide more accurate location information, by selecting based on received signal quality.

In order to make use of GNSS, nowadays a single chip can be used. The chip will typically receive the RF signals, shift them to a much lower frequency, then perform the correlation operation, and then pre-programmed software inside the chip will compute the receiver location. The pre-programmed software has a model of the Earth, to try to reduce errors in altitude (height) measurement, say, above sea level. 

The altitude is interesting to briefly consider; the earth isn’t spherical, it bulges a little, i.e. it is slightly ellipsoidal, plus, on top of that, sea level depends on gravity, and gravity isn’t constant across the earth. Where the earth is denser, it attracts more water, and the mean sea level rises there. There is an internal table of heights inside the chip, and the reported altitude takes that into account, to try to provide an altitude value that is referenced off that internal table of mean sea levels at the reported location. It’s known as an orthometric height. 

## Further Reading (References)

[Longitude](https://www.amazon.co.uk/Longitude-Genius-Greatest-Scientific-Problem/dp/080271529X) book by Dava Sobel

[Early History of the Decca Navigation System](https://digital-library.theiet.org/content/journals/10.1049/jiere.1985.0069) - Powell

[Decca Yacht Navigator User Manual](https://elektrotanya.com/showresult?what=decca+yacht&kategoria=All&kat2=All)

[Decca website](http://www.jproc.ca/hyperbolic/decca.html) by Jerry Proc
