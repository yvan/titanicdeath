# titanicdeath
an online web app that that will tell you whether you would have died on the titanic or not.


# phase 1:

i completed the webapp with a basic logistic regression model. i wanted to get the web app stuff out of the way first so i could then play around with which model to use.

from the original titanic dataset many of the variables i just set to 0 for now. some variables are hard to ask a user about like 'port of embarkation.' having several of the varibles set to 0 it is obvious that the logisitic regression defaults to 3 variables age, geneder, and class, with a stong emphasis on gender, you can see this also representend in this coefficient chart:

< chart here >

which shows the overwhelming strong relationship of gender and suvival compared to weaker effects for other variables. here the bigger the coefficent for gender the more it incentivezes female survival.

i want to make the app interesting so for the port embarkation variable i will randomly generate a variable for each user that is guaruanteed to match the underlying distribution of embarkation ports. that will get that variable squared away. this isnt even that odd of an assumption to make as often you buy a ticket fora boat or plane and leave from the nearest embarkation port. the fact that more people will live near one port or another will be reprsented in the distribution and by mirroring it and doling them out randomly we are actually simulating something close to real life. when you are making synthetic data it is important to understand 1 - how that data is similar or different from real life 2 - how the data you intriduce may or may not distort your training/predictions