# titanicdeath
an online web app that that will tell you whether you would have died on the titanic or not.


# phase 1:

i completed the webapp with a basic logistic regression model. i wanted to get the web app stuff out of the way first so i could then play around with which model to use.

from the original titanic dataset many of the variables i just set to 0 for now. some variables are hard to ask a user about like 'port of embarkation.' having several of the varibles set to 0 it is obvious that the logisitic regression defaults to 4 variables age, gender, and class, title with a stong emphasis on gender, you can see this also representend in this coefficient chart:

Feature     Correlation
Sex         2.201527 <- gender
Title       0.398234 <- title
Age         0.287163 <- age
Embarked     0.261762
IsAlone     0.129140
Fare        -0.085150
Age*class   -0.311200
Pclass      -0.749007 <- class

which shows the overwhelming strong relationship of gender and suvival compared to weaker effects for other variables. here the bigger the coefficent for gender the more it incentivezes female survival.

currently the website takes 

i want to make the app interesting so for the port embarkation variable i will randomly generate a variable for each user that is guaruanteed to match the underlying distribution of embarkation ports. that will get that variable squared away. this isnt even that odd of an assumption to make as often you buy a ticket fora boat or plane and leave from the nearest embarkation port. the fact that more people will live near one port or another will be reprsented in the distribution and by mirroring it and doling them out randomly we are actually simulating something close to real life. when you are making synthetic data it is important to understand 1 - how that data is similar or different from real life 2 - how the data you intriduce may or may not distort your training/predictions. to match the underlying distribution ill just store the distribution and then sample from it.

for title we want to sample within each age group, so for each age group we want to make a bucket and sample based on the distrubtion for that title within that age group.

# phase 2:

ok so a few things ive noticed. 1 the logistic regression seems to basically default to 'woman' or 'man' this might seem obvious if you look at the coefficients that determine whether or not a person suvives (in table above). the problem with this is that it makes the site/product pretty damn uninteresting. basically this thing tells you whether you are a man or a woman (if only we had their gender identities as well then this could all be resolved). a fer things i might try:

1 - build two predictibe models, one for each gender. that way AMONG individuals of each gender we are more likely to see who survives.

2 - use a non linear classifier with more classes. so maybe an svm, and make the calsses (male survived, femal suvived, male died, female died) that way we can capture some non linear features that may make tho model more interesting.

the datavalidation is kinda messed up and for some reason im having trouble finiding up to date (wtih latest flask_Wtf shenanigans) docs for how to do it properly.

# phase 3

taking out 'how many parents do you have?' question. its a weird question, and we can just make it fit he distribution anyways. then isalone defaults to 1 how many siblings you have, 2 the distribution of how many parents most people in the dataset have, that is probably better.

ok so i fxed that. now we are no longer simplifying the complex feature set down to something it isnt, we are taking th ecomplex feature set, filling in the parts that we are missing from the form with values tht match the underlying distribution and producing a result. this adds from the user's perspective a little bit of randomness on variables that would be hard to measure in this product, men will not ALWAYS die now. Before without this element of randomness/distribution matching men would pretty much always die and women would pretty much alwyas live. this is a nice mix/compromise between a product and a predictive data science model. we could make it better by restrciting samples based on info we have.

1 - get the points aligned

2 - get the site up on the domain

resouces from: 

data : https://www.kaggle.com/c/titanic/data

https://gist.github.com/doobeh/4667330
https://medium.com/@amirziai/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
