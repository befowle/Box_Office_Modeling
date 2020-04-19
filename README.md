Determining the Relationship Between Opening Weekend Results, Critical Reviews, and Box Office Success
-

Objectives
-
- Our goal was to find some way to predict box office success using box office revenue.

- More specifically we wanted to explore the relationship between critic + viewer ratings and box office revenue. Do critically-acclaimed films achieve box office success? Or, do films rated highly by audiences perform better?

- We also looked at domestic opening weekend revenue from 2013-2018 as an indicator of what audiences are excited to see, and if high opening weekend revenue indicated that a film would perform well overall. 

- More specifically we wanted to explore the relationship between critic + viewer ratings and box office revenue. Do critically-acclaimed films achieve box office success? Or, do films rated highly by audiences perform better?

- Overall, we found that reviews are not correlated to gross revenue, but opening weekend revenue is strongly correlated to the total gross revenue. We can even use this relationship to predict the total gross revenue based on opening weekend revenue


Process
-

- We joined data from Box Office Mojo and Metacritic to compare the critic’s score to gross revenue from the year 2018.

<img src = "images/critic_revenue.png"> 

- Notice there isn’t a strong relationship between the two data sets. 

-Because of this, we would not recommend using critic scores to predict success at the box office. It’s helpful to identify this because on the surface, one might presume that more people will go out to see a movie that is critically-acclaimed.

Observations
-
- Critic Reviews vs Gross Revenue

<img src = "images/audience_revenue.png"> reviews_revenue

- Notice there isn’t a strong relationship between the two data sets. 

-Because of this, we would not recommend using critic scores to predict success at the box office. It’s helpful to identify this because on the surface, one might presume that more people will go out to see a movie that is critically-acclaimed.

- Audience Score vs Gross Revenue

<img src = "images/audience_revenue.png"> 

- We found a similar relationship between user scores and gross revenue. High audience ratings do not mean a film does well at the box office.

- We also compared audience(user) scores to critic scores, and films that were highly rated by critics tended to be also well-reviewed by audiences. So the source of the review is also not indicative of box office success.

- Gross Revenue vs Opening Weekend Revenue

<img src = "images/gross_opening.png"> 

- The data indicates there is a linear relationship between gross revenue and opening weekend revenue, which can be used to model the predicted outcomes for new movie projects
 
- Final model:
Y = 2.9432x + 1.7e+06
R2 = 0.9028

Future Work
-
- Give scores to producers and actors based on past revenues, awards, movie numbers, social media following. Explore relationship to total gross

- Duration of movie in theaters correlation to total gross

- Social media correlations

- Budget, net/gross revenue analysis
