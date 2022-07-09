# [Day Man](https://www.youtube.com/watch?v=VCvr6tzZPTU)

It's been a long, crazy off-season. Idk about you but conference realignment has got me feeling down. I figured some dumb statistical analysis would cheer me up heading into the weekend

**Is Ryan Day a better coach during the day time or night time?**
Pretty simple question. Under Ryan Day how do the Buckeyes fare during the day time vs at night?

### Data Collection
I scraped *THE* Ohio State's schedule and results from [football-reference.com](https://www.sports-reference.com/cfb/schools/ohio-state/2019-schedule.html). For some reason, the 2019 page did not include game start times, so I filled in my resulting csv file with start times listed [here](https://fbschedules.com/2019-ohio-state-football-schedule/). I classified games with a 6pm local time or later start time as "Night" and earlier start times as "Day". 

### Data
The table below shows Ryan Day's results by game type (Day/Night). In all, [he wins **93.75 %** of his day games and **82.35 %** of his night games](https://imgur.com/a/JwLZss3). [Here is a graph](https://imgur.com/a/fUNnVNX) of Ryan Days total results by game type (*Night/Day* and *Win/Loss*). The table of this information is shown below:

GameType | Loss | Win	
:--:|:--:|:--:
Day | 2 | 30
Night | 3 | 14

I was also curious to see if Day's average margin of victory changed with the time of day. Maybe the Buckeyes are morning people? Maybe those famous [tOSU mid-day study breaks](https://images.app.goo.gl/TTwCMPZEJFe5aqJWA) were tiring his team out? That graph is [here](https://imgur.com/a/BoZjYM0)

#### SoS Day vs Night
One thing that jumped out to me was whether or not tOSU simply plays more unranked opponents during the day time. Since ranked matchups typically occur in primetime, I was curious to see if he's coached against more ranked opponents at night rather than daytime. Over his tenure Day has played the following breakdown of ranked and unranked opponents:

GameType | Ranked | Unranked
:--:|:--:|:--:
Day | 12 | 10
Night | 20 | 7

In all, Ryan Day has a *ranked daytime* win percentage of **83.3%** and an *unranked daytime win %* of **100%**. Interestingly, Day is undefeated at night against ranked opponents, and has only won [**85%** of his games at night vs unranked opponents](https://images.app.goo.gl/EbARkJyPFWaQYVMr6)

### Analysis
To see if there was any statistical relationship between game start (Night vs Day), I used the built-in $\chi^2$ contingency test from [`scipy`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html). We're testing with a null hypothesis that there is not a relationship between game start time (Day vs Night). Our test sattistics can be seen below:

$\chi^2$ | $p$ | 
:--:|:--:
1.573 | 0.2096

Since $\chi^2 > p$, we cannot reject the null hypothesis, and there is not a statistically significant relationship between the time of day and Ryan Day's win pct. Turns out he's a good coach any time of the day.

### Conclusion
[The fighter of the night man](https://www.youtube.com/watch?v=VCvr6tzZPTU) tends to win football games any time of day. The Buckeyes have a [few night games already scheduled](https://www.google.com/search?client=safari&rls=en&q=ohio+state+2022+football+schedule&ie=UTF-8&oe=UTF-8&safe=active#sie=t;/m/0fjzsy;6;/m/012hfxch;mt;fp;1;;) for the coming season, so Notre Dame and Toledo aren't necessarily safe at the shoe when the sun goes down. 

Code/data I scraped for this project can be found [here](https://github.com/andrewbowen19/ryanDay). Hope you enjoyed reading and are having a better time with this dumb offseason than I am!


*tl;dr* Ryan Day coaches real good at night too.