# OnlineNewsPopularity_QUESNAY_PADRINO
In this repository you will find :
- Our report powerpoint presentation in form of a PDF.
- A jupyter file where we clean the dataset, analyze it and apply models to it.
- The .py file of the flask
## What is the Online News Popularity dataset about?
Our dataset summarizes  a set of 61 features describing articles published on the Mashable wesbite. Mashable is an international entertainment, culture, technology, science, social  digital media platform, news website, multi-platform media and entertainment company. The objective with these features it that we would predict the popularity of an article published on the Mashable website caracterized by the number of shares of an article. Every row of our dataset corresponds to an article and its features.

Features of the dataset:
0. url: URL of the article (non-predictive)
1. timedelta: Days between the article publication and the dataset acquisition (non-predictive)
2. n_tokens_title: Number of words in the title
3. n_tokens_content: Number of words in the content
4. n_unique_tokens: Rate of unique words in the content
5. n_non_stop_words: Rate of non-stop words in the content
6. n_non_stop_unique_tokens: Rate of unique non-stop words in the content
7. num_hrefs: Number of links
8. num_self_hrefs: Number of links to other articles published by Mashable
9. num_imgs: Number of images
10. num_videos: Number of videos
11. average_token_length: Average length of the words in the content
12. num_keywords: Number of keywords in the metadata
13. data_channel_is_lifestyle: Is data channel 'Lifestyle’? 
14. data_channel_is_entertainment: Is data channel 'Entertainment'?
15. data_channel_is_bus: Is data channel 'Business'?
16. data_channel_is_socmed: Is data channel 'Social Media'?
17. data_channel_is_tech: Is data channel 'Tech'?
18. data_channel_is_world: Is data channel 'World'?
19. kw_min_min: Worst keyword (min. shares)
20. kw_max_min: Worst keyword (max. shares)
21. kw_avg_min: Worst keyword (avg. shares)
22. kw_min_max: Best keyword (min. shares)
23. kw_max_max: Best keyword (max. shares)
24. kw_avg_max: Best keyword (avg. shares)
25. kw_min_avg: Avg. keyword (min. shares)
26. kw_max_avg: Avg. keyword (max. shares)
27. kw_avg_avg: Avg. keyword (avg. shares)
28. self_reference_min_shares: Min. shares of referenced articles in Mashable, when the current article references other Mashable’s articles we look at the shares of the articles, this feature is for the minimum found.
29. self_reference_max_shares: Max. shares of referenced articles in Mashable, when the current article references other Mashable’s articles we look at the shares of the articles, this feature is for the maximum found.
30. self_reference_avg_sharess: Avg. shares of referenced articles in Mashable, when the current article references other Mashable’s articles we look at the shares of the articles, this feature is for the average found.
31. weekday_is_monday: Was the article published on a Monday?
32. weekday_is_tuesday: Was the article published on a Tuesday?
33. weekday_is_wednesday: Was the article published on a Wednesday?
34. weekday_is_thursday: Was the article published on a Thursday?
35. weekday_is_friday: Was the article published on a Friday?
36. weekday_is_saturday: Was the article published on a Saturday?
37. weekday_is_sunday: Was the article published on a Sunday?
38. is_weekend: Was the article published on the weekend?
33. weekday_is_wednesday: Was the article published on a Wednesday?
34. weekday_is_thursday: Was the article published on a Thursday?
35. weekday_is_friday: Was the article published on a Friday?
36. weekday_is_saturday: Was the article published on a Saturday?
37. weekday_is_sunday: Was the article published on a Sunday?
38. is_weekend: Was the article published on the weekend?
48. rate_positive_words: Rate of positive words among non-neutral tokens
49. rate_negative_words: Rate of negative words among non-neutral tokens
50. avg_positive_polarity: Avg. polarity of positive words
51. min_positive_polarity: Min. polarity of positive words
52. max_positive_polarity: Max. polarity of positive words
53. avg_negative_polarity: Avg. polarity of negative words
57. title_sentiment_polarity: Title polarity
58. abs_title_subjectivity: Absolute subjectivity level
59. abs_title_sentiment_polarity: Absolute polarity level

And the target
60. Shares : number of times the article was shared.








## How to use our Flask

Fisrt, run the script from the file : "project_api.py".
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_1.PNG?raw=true)

Then, copy this url in a navigator : http://127.0.0.1:5000/api/doc.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_2.PNG?raw=true)

Click on the button in green to unwind the menu.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_3.PNG?raw=true)

Click on the "Try it out" button to start editing your request.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_4.PNG?raw=true)

You need to change the text where "string" is written and answer the request you are asked.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_5.PNG?raw=true)

This is an example of how to fill the answers.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_6.PNG?raw=true)

Execute the API by using the button.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_7.PNG?raw=true)

Observe if your article would be popular or not.
![alt text](https://github.com/eva-pa/OnlineNewsPopularity_QUESNAY_PADRINO/blob/main/Images_API/Step_8.PNG?raw=true)




