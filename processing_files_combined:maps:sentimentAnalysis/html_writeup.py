# Create the final_project.html file
with open("final_project.html", "w") as html_file:
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Final Project Analysis</title>
        <style>
            body {
                max-width: 800px;
                margin: auto;
                font-family: Arial, sans-serif;
                line-height: 1.6;
                padding: 20px;
            }
            h1 {
                font-size: 28px;
                margin-bottom: 20px;
                text-align: center;
            }
            h2 {
                font-size: 24px;
                margin-bottom: 15px;
            }
            p {
                font-size: 16px;
                margin-bottom: 15px;
            }
            iframe {
                width: 100%;
                max-width: 1000px; /* Adjust the maximum width as needed */
                height: 600px;
                margin: auto; /* Center the iframe horizontally */
                display: block;
            }
            .map-container {
                display: flex;
                justify-content: space-between;
                max-width: 1000px; /* Adjust the maximum width as needed */
                width: 100%;
                margin: 30px;
                margin-bottom: 150px;
            }

            .map {
                width: 100%; /* Adjust the width as needed */
                height: 500px;
                margin: 0;
                margin-bottom: 200px;
            }
            .image-row {
                display: flex;
                justify-content: space-between;
                margin-bottom: 20px;
            }

            .image-container {
                text-align: left;
                margin: 50px;
            }

            .image-container img {
                max-width: 120%;
                height: auto;
                margin-bottom: 5px;
                
            }
            
        </style>
    </head>
    <body>

        <h1>Analysis of Restaurant Reviews Using Yelp and TripAdvisor</h1>
        <p>Jessica Young and Allison Peng</p>
        <h2>Data Acquisition</h2>
        <p>
            <strong>Websites Used and Why:</strong> We scraped data from Yelp and TripAdvisor. Our goal of the project was to analyze the reviews from consumers and those websites are two widely used restaurant rating websites. In order to gather data from a reliable source, we aimed to use more popular rating websites. In return, each restaurant had more than 20 reviews, which was our goal amount of scraping from each restaurant. Other websites did not have reviews for some restaurants, thus we were not able to use those websites for gathering data. In addition, we wanted to scrape from multiple sources to create a combined database to better answer our questions. It allowed us to become familiar with two different html layouts, and adapt to the different css designs. </p>
      <div class="map-container">

    <!-- First Row of Maps -->
    <div class="map-row">
        <!-- Map 1: Restaurants in SF with Yelp -->
        <div class="map">
            <h2>Restaurants in SF with Yelp</h2>
            <iframe src="https://allison2368.github.io/restaurants_map_SF_yelp/" frameborder="5"></iframe>
        </div>

        <!-- Map 2: Restaurants in LA with Yelp -->
        <div class="map">
            <h2>Restaurants in LA with Yelp</h2>
            <iframe src="https://allison2368.github.io/restaurant_LA_yelp/" frameborder="0"></iframe>
        </div>
    </div>

    <!-- Second Row of Maps -->
    <div class="map-row">
        <!-- Map 3: Restaurants in SF with TripAdvisor -->
        <div class="map">
            <h2>Restaurants in SF with TripAdvisor</h2>
            <iframe src="https://allison2368.github.io/restaurants_SF_tripadvisor/" frameborder="0"></iframe>
        </div>

        <!-- Map 4: Restaurants in LA with TripAdvisor -->
        <div class="map">
            <h2>Restaurants in LA with TripAdvisor</h2>
            <iframe src="https://allison2368.github.io/test/" frameborder="0"></iframe>
        </div>
    </div>

</div>
        <h2>Methods</h2>
        <p>
            <strong>List of Methods:</strong> We first attempted to use an API from Yelp, however it limited us to 3 incomplete reviews per restaurant. Thus, we resorted to web scraping straight from the website using libraries such as BeautifulSoup and Requests. Since each restaurant’s reviews were located inside the restaurant link, we needed to loop through each link and scrape the reviews. Our attempts for each website differed because of the different website structures. From each website, we scraped 40 restaurants and 20 reviews each. </p>
        <p>
            <strong>What libraries were used and how was our data structured?:</strong> We used the libraries BeautifulSoup and Requests to scrape data from both websites. In addition, we used the selenium library to see the web scraping process. It assisted with spotting errors in the scraping process and helped us debug the code. Since the project was completed by two collaborators, there were two methods to scraping from the websites due to different IDE’s used, however the resulting data structure is the same. </p>
        <p>    
            <strong>Yelp:</strong> We wrote a function to get all the business information from each page in which we made requests for each individual business page and extracted all the necessary information. After starting with the search parameter (location), we scraped two pages and created a dictionary to store all the business information (names, links, ratings, reviews). The reviews were specifically stored in a list for each location in which we iterated through pages and scraped all reviews for each restaurant to add to the overall list. All reviews were saved in an HTML file to do further visualization and sentiment analysis.
           </p>
        <p>   <strong>TripAdvisor:</strong> We created a list of links for each restaurant by using BeautifulSoup to identify the individual links. This was stored in a list, then a for loop was written to loop through each link and gather the review for each restaurant. On a separate .py file, each business information (names, links, ratings) was stored in a dictionary. The dictionaries for each restaurant were combined into one list, which was a necessary data structure in order to later combine the information with a different website.  The reviews were written to an html file to do further visualization and sentiment analysis. </p>
        </p>

        <p> Example of Output for Business Information: We made a list of dictionaries as the best way to combine data</p>
        <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%209.21.51%20PM.png?raw=true" alt="Image 1">
            </div>
         <p> Example of Output for Reviews: We read the reviews into four html files: LA_yelp, LA_TripAdvisor, SF_yelp, SF_TripAdvisor</p>
        <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.08.28%20PM.png?raw=true" alt="Image 1">
            </div>
        

        <h2>Combining Data</h2>
        <p>
            <strong>Reviews:</strong> Since we scraped the reviews from different websites and locations separately, we ended up with 4 html files of reviews. LA_TripAdvisor, SF _TripAdvisor, LA_Yelp, SF_Yelp.

       
        In order to analyze the reviews from LA vs SF and Yelp vs TripAdvisor, we needed to combine certain datasets with each other.</p>
        
        <p>To analyze LA vs SF, we combined across different websites, thus LA = LA_TripAdvisor + LA_Yelp and SF = SF_TripAdvisor + LA_TripAdvisor</p>
        <p>To analyze Yelp vs TripAdvisor, we combined locations across the same website, thus Yelp = LA_Yelp + SF_Yelp and TripAdvisor = LA_TripAdvisor + SF_TripAdvisor</p>

        <p><strong>Business Info:</strong> We combined our individual scraping methods and wrote it into one code chunk. The output is the same as shown in the image, but with 40 restaurants for each combined dataset.


        <h2>Analysis</h2>
        <p>
            <strong>Exploratory Data Analysis:</strong> Top Businesses
        </p>
        <!-- First Row of Images -->
        <div class="image-row">
            <!-- Image 1 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.09.11%20PM.png?raw=true" alt="Image 1">
                <p>Image 1 LA - yelp: This bar plot is in the same format as the previous visualization, but it displays the top-rated businesses in Los Angeles. We can see that the distribution shapes of the plots are similar with Los Angeles showing a bit more variety. However, this could just be because of the recommended restaurants extracted from Yelp. In this plot, there are two restaurants with five-star ratings, and the other three with 4.7, 4.6, and 4.5 ratings respectively. This information was extracted similarly to how we retrieved the business information for San Francisco where we had dictionaries for all business information for both cities and extracted their corresponding business names for each rating.
</p>
            </div>

            <!-- Image 2 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.09.23%20PM.png?raw=true" alt="Image 2">
                <p>Image 2 SF - yelp: This bar plot shows the top-rated businesses in San Francisco. This information came from getting all the ratings from my previous output, but only extracting the numerical value. Then, we sorted the ratings in descending order to retrieve the top-rated restaurants and extracted their names from my dictionary of business information. As you can see, there is one restaurant with a 5-star rating, two restaurants with 4.9-star ratings, and two restaurants with 4.8-star ratings. There are more top-rated restaurants, but these restaurants are from the recommended list extracted from Yelp.
</p>
            </div>
        </div>

        <!-- Second Row of Images -->
        <div class="image-row">
            <!-- Image 3 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.09.31%20PM.png?raw=true" alt="Image 3">
                <p>Image 3 LA - TA: This bar plot displays the top-rated businesses in Los Angeles. In this plot, there are three restaurants with five-star ratings, and the other two with ratings of 4.5. This is to be expected as we are scraping the top recommended restaurants from TripAdvisor, so naturally the ratings of the restaurants should be relatively high. The plot for the top-rated businesses in San Francisco should be similar in both distribution shape and range. This information was extracted from the overall dictionaries for all business information for both cities and their corresponding business names for each rating.
</p>
            </div>

            <!-- Image 4 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.10.08%20PM.png?raw=true" alt="Image 4">
                <p>Image 4 SF - TA: This bar plot displays the top-rated businesses in San Francisco. We can see that the distribution shapes of this plot with the previous plot are similar. In this plot, there are two restaurants with five-star ratings, and the other three with ratings of 4.5. This is similar to the previous plot since all five restaurants share the same two ratings but with one restaurant differing. Since this plot has one more restaurant with a rating of 4.5, the average rating for the restaurants in San Francisco is slightly lower than the average rating for the restaurants in Los Angeles. But overall, the two bar plots for top-rated restaurants are very similar in distribution shape and range.
</p>
            </div>
        </div>
        <p>
            <strong>Exploratory Data Analysis Continued:</strong> All Business Ratings
        </p>
        <!-- First Row of Images -->
        <div class="image-row">
            <!-- Image 1 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.10.27%20PM.png?raw=true" alt="Image 1">
                <p>Image 1 LA - yelp: This histogram shows the business count by rating for all 20 recommended restaurants in Los Angeles. Unlike the San Francisco histogram, the distribution shape has a clear peak at a rating of 4.4. The average rating is 4.41 which is to be expected as there are eight restaurants with a rating of 4.4. With this histogram, there is not much of a range compared to the San Francisco histogram as there is a clear peak in the graph. This is just an example of what a histogram of business counts by ratings could look like for Los Angeles restaurants. Since the recommendations change based on user data, the histograms would also have minor changes, but the average rating should stay about the same.

            </div>

            <!-- Image 2 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.10.40%20PM.png?raw=true" alt="Image 2">
                <p>Image 2 SF - yelp: This bar plot shows the top-rated businesses in San Francisco. This information came from getting all the ratings from my previous output, but only extracting the numerical value. Then, we sorted the ratings in descending order to retrieve the top-rated restaurants and extracted their names from my dictionary of business information. As you can see, there is one restaurant with a 5-star rating, two restaurants with 4.9-star ratings, and two restaurants with 4.8-star ratings. There are more top-rated restaurants, but these restaurants are from the recommended list extracted from Yelp.
</p>
            </div>
        </div>

        <!-- Second Row of Images -->
        <div class="image-row">
            <!-- Image 3 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.10.49%20PM.png?raw=true" alt="Image 3">
                <p>Image 3 LA - TA: This histogram shows the business count by rating for all 20 recommended restaurants in Los Angeles. There is a clear peak at the 4.5 rating as 12 out of 20 restaurants have around a 4.5 rating. The average is probably higher than the graph for San Francisco below this graph because there are more restaurants with a rating higher than the average than there are restaurants with a lower rating. This value is to be expected as these restaurants are recommended by Trip Advisor when a user searches for Los Angeles restaurants.
</p>
            </div>

            <!-- Image 4 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.38.04%20PM.png?raw=true" alt="Image 4">
                <p>Image 4 SF - TA: This histogram shows the business count by rating for all 20 recommended restaurants in San Francisco. There is a clear peak at the 4.5 rating as 13 out of 20 restaurants have around a 4.5 rating. The average for this graph is probably slightly lower than the graph for Los Angeles above this graph because there are 3 restaurants with a rating higher and lower than the average summing up to 6 restaurants. There is one outlier restaurant with a lower rating, but since most restaurants have a rating of 4 or higher, this restaurant is not important or relevant to our analysis.
</p>
            </div>
        </div>
        <p>
            <strong>Combined Data Analysis:</strong> We combined the across websites and locations to answer our main questions. Now, we will go into exploring the combined data features to better answer our questions.
        </p>
        <!-- First Row of Images -->
        <div class="image-row">
            <!-- Image 1 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.11.09%20PM.png?raw=true" alt="Image 1">
                <p>Image 1 LA: This histogram shows the combined recommended Los Angeles restaurants from both Yelp and TripAdvisor. The graph is left-skewed with the majority of the restaurants on the side with the higher ratings. There is also a clear peak between the ratings of 4.25 and 4.5. This matches the other Los Angeles restaurants for Yelp and TripAdvisor individually as they all have around the same average rating. We should expect the combined recommended San Francisco restaurants histogram to look similar to this histogram but with a slightly higher average as seen from the previous individual San Francisco histograms.

            </div>

            <!-- Image 2 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.50.32%20PM.png?raw=true" alt="Image 2">
                <p>Image 2 SF: This histogram shows the combined recommended San Francisco restaurants from both Yelp and TripAdvisor. The graph is also left-skewed with the majority of the restaurants on the side with the higher ratings. There is also a clear peak between the ratings of 4.25 and 4.5. This matches the other San Francisco restaurants for Yelp and TripAdvisor individually as they all have around the same average rating. One difference is that there are more restaurants between the 4.75 and 5 ratings for this combined histogram compared to the previous one. This means that the average rating for San Francisco restaurants is higher than that of Los Angeles restaurants.
</p>
            </div>
        </div>

        <!-- Second Row of Images -->
        <div class="image-row">
            <!-- Image 3 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.11.27%20PM.png?raw=true" alt="Image 3">
                <p>Image 3 Yelp: This visualization shows the combination of all forty restaurants scraped from Yelp: twenty for San Francisco and twenty for Los Angeles. The distribution shape seems to be relatively normally distributed with a clear peak at the 4.4 rating. This makes sense because the individual business count by rating histograms for San Francisco and Los Angeles both had average ratings of around 4.4 to 4.5. This visualization matches the histogram for Los Angeles more than San Francisco due to its clear peak whereas there was not a distinct peak in the San Francisco histogram for business count by rating.
</p>
            </div>

            <!-- Image 4 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.11.37%20PM.png?raw=true" alt="Image 4">
                <p>Image 4 TripAdvisor: This visualization shows the combination of all forty restaurants scraped from TripAdvisor: twenty for San Francisco and twenty for Los Angeles. The distribution shape is less normal than the previous graph as it looks more skewed to the left. The graph peaks at a rating of around 4.5 but has an equal amount of restaurants in other rating segments from 4 to 5. Also, the range of this graph is larger since there are some outlier restaurants with lower ratings. There seems to be a higher average for recommended restaurants from TripAdvisor than the recommended restaurants from Yelp.
</p>
            </div>
        </div>
        
        <p>
            <strong>Sentiment Analysis:</strong> Now, we combined the reviews across websites and locations to analyze the reviews and directly answer our question. 
        </p>
        <p>
            <strong>Word Cloud:</strong> First, we will look at a word cloud to visualize which words were the most common for each website/location.
        </p>
        <!-- First Row of Images -->
        <div class="image-row">
            <!-- Image 1 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.11.46%20PM.png?raw=true" alt="Image 1">
                <p>Image 1 Yelp: This is the combined word cloud for all reviews scraped from the forty restaurants combining San Francisco and Los Angeles. We can see that the main words that stand out due to their size are positive words, such as food, great, service, and delicious. There are also other positive sentiment words in the word cloud, such as fantastic, nice, amazing, favorite, and love. This word cloud matches what we predicted because since we web scraped the top recommended restaurants, these restaurants should have high ratings and reviews since they are recommended by Yelp. The individual San Francisco and Los Angeles word clouds had similar positive words that stood out.

            </div>

            <!-- Image 2 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.11.56%20PM.png?raw=true" alt="Image 2">
                <p>Image 2 TripAdvisor: This is the combined word cloud for all reviews scraped from the forty restaurants combining San Francisco and Los Angeles. We can see that the main words that stand out due to their size are positive words such as food, great, and service. Other notable positive words are delicious, excellent, amazing, and best. This word cloud matches the previous word cloud for Yelp with similar positive words. We expect to see more positive words because the restaurants we are scraping from both websites are the ones that are recommended, so their reviews should be positive and their ratings should be higher.

</p>
            </div>
        </div>

        <!-- Second Row of Images -->
        <div class="image-row">
            <!-- Image 3 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.12.06%20PM.png?raw=true" alt="Image 3">
                <p>Image 3 LA: This is the word cloud for all Los Angeles reviews scraped from both Yelp and TripAdvisor. We can see that the main words that stand out due to their size are positive words such as great, good, service, and delicious. We notice that these word clouds match the previous word clouds in terms of words and their sizes. Even though the words are in different locations on each word cloud, there are still obvious similarities that make it seem like the Los Angeles restaurants are highly rated and recommended.
</p>
            </div>

            <!-- Image 4 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.12.12%20PM.png?raw=true" alt="Image 4">
                <p>Image 4 SF: This is the word cloud for all San Francisco reviews scraped from both Yelp and TripAdvisor. We can see that the main words that stand out due to their size are positive words such as good, food, great, and service. One thing we noticed is that service is the largest word which differs from the previous word clouds. This could mean that San Francisco restaurants typically have better service than other restaurants in other locations. The other positive words are similar to what was observed previously. There are very few if any negative words since all the restaurants are recommended by both websites.
</p>
            </div>
        </div>
        <p>
            <strong>Sentiment Analysis:</strong> We performed a sentiment analysis using the nltk library. This determined if the review was positive, negative, or neutral. 
        </p>
        <!-- First Row of Images -->
        <div class="image-row">
            <!-- Image 1 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.12.23%20PM.png?raw=true" alt="Image 1">
                <p>Image 1 LA: This is the pie chart for the sentiment analysis for all Los Angeles reviews across both websites. We expected to see more positive sentiments; however, there were more neutral sentiments. When using NLTK for the sentiment analysis, we retrieved data from vader_lexicon.txt which has preset words that we matched with our reviews. Some of the positive sentiment words must have been mixed in with the neutral sentiment words in the text file which led to a large percentage of neutral words.

            </div>

            <!-- Image 2 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.12.29%20PM.png?raw=true" alt="Image 2">
                <p>Image 2 SF: This is the pie chart for the sentiment analysis for all San Francisco reviews across both websites. The percentage of positive sentiments is slightly higher than the previous pie chart, which means that there are more positive reviews for restaurants in San Francisco compared to the restaurants in Los Angeles. This means that some of the positive reviews were correctly categorized as having a positive sentiment, so the positive sentiment percentage is slightly higher and the neutral sentiment percentage is slightly lower.

</p>
            </div>
        </div>

        <!-- Second Row of Images -->
        <div class="image-row">
            <!-- Image 3 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.12.39%20PM.png?raw=true" alt="Image 3">
                <p>Image 3 Yelp: This is the pie chart for the sentiment analysis for all Yelp reviews across both locations. The percentage of positive sentiments is lower than the other pie charts, which means that reviews on Yelp are not as positive as TripAdvisor. This can also be seen in the higher percentage of negative sentiments as well. We should also expect to see that the ratings for Yelp are lower than TripAdvisor due to the lower percentage of positive sentiments. However, the neutral sentiment percentage is higher, so some of the positive sentiment words could have been categorized as neutral.
</p>
            </div>

            <!-- Image 4 with Text -->
            <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%208.12.49%20PM.png?raw=true" alt="Image 4">
                <p>Image 4 TripAdvisor: This is the pie chart for the sentiment analysis for all TripAdvisor reviews across both locations. The percentage of positive sentiments is the highest compared to all other pie charts, which means that reviews on TripAdvisor are more positive than Yelp. We should also expect to see that the ratings for TripAdvisor are higher than Yelp due to the higher percentage of positive sentiments. The neutral sentiment percentage is the lowest, so this means that some of the positive sentiment words were correctly categorized as positive leading to a high positive review percentage.

</p>
            </div>
        </div>
       

        <h2>Conclusion, Challenges, and Final Remarks</h2>
        <p>
            <strong>Challenges:</strong> While conducting various analyses on the restaurants from Yelp and TripAdvisor, we came across several challenges. We were limited to only scraping 20 reviews for each restaurant due to being blocked if we scraped more. We attempted to download websites that would prevent the blocking, however they were not effective. In the future, we would attempt other methods to scrape to avoid being blocked. The main setback was that after web scraping many (40+) restaurants from Yelp, Yelp would detect this activity and block us from accessing the website in general. After being blocked, none of the code we had produced any output. To fix this issue, we lowered the number of restaurants scraped to 20 per location. Even though the code still took a long time to run, it reduced the possibility of being blocked by Yelp again. Also, we attempted to make an individual API key to access Yelp. Once the API key was created, we only had limited access to Yelp. We wrote completely new code to utilize the API key and tried to print out all 20 restaurants per location once again. However, the API key could only print a maximum of 20 restaurants including their names, URLs, rating, and review count. Once we tried to scrape all the reviews, we found that the API key limited us to only three reviews per restaurant, which led to another issue. We wanted twenty reviews per restaurant to do further analysis but we only ended up with three incomplete reviews for each restaurant. Eventually after being unblocked by Yelp, we resorted back to our original code that scraped all the information we wanted successfully. This is an example of what the API key output looked like: 
        </p>
        <div class="image-container">
                <img src="https://github.com/allison2368/YelpReviews/blob/main/images/Screen%20Shot%202023-12-15%20at%209.15.28%20PM.png?raw=true" alt="Image 4">
                
            </div>
        <p>
            <strong>Answer to Questions:</strong></p>
        <p>
            <strong>Is the sentiment of reviews different between restaurants in Northern California and Southern California?</strong></p>
  
            
        <p>We analyzed that the sentiment of reviews for Northern California, particularly in the San Francisco region, is slightly more positive than the sentiment of reviews for Southern California, particularly in the Los Angeles area. For NorCal, the average rating was closer to 4.5, and for SoCal, the average rating was closer to 4.4 when we analyzed the business count by rating. In the visualizations, we saw that some restaurant ratings in San Francisco were higher than the average rating. Also, the sentiment analysis for San Francisco has a higher positive percentage compared to the sentiment analysis for Los Angeles, further proving that the sentiment of reviews for restaurants in Northern California is slightly more positive than the sentiment of reviews for restaurants in Southern California.
        </p>
        
        <p>
        <strong>Is the sentiment of reviews different between restaurants reviewed with Yelp and TripAdvisor?</strong>
        </p>
        
            
        <p>We analyzed that the sentiment of reviews for restaurants reviewed with TripAdvisor was slightly more positive than the sentiment of reviews for restaurants reviewed with Yelp. For the business count by rating Yelp graph, there was a clear peak at the 4.4 rating for 18 restaurants. For the business count by rating TripAdvisor graph, the average rating was 4.5 for around 20 restaurants. So, the restaurants recommended by TripAdvisor generally have higher ratings which leads to a more positive sentiment. In the pie charts, we can see a big difference between TripAdvisor and Yelp reviews, especially in the percentage of positive sentiments being 30.7% for TripAdvisor and 24.4% for Yelp.
</p>
        <p>

            <strong>Conclusion:</strong> In conclusion, our project consisted of conducting a comprehensive analysis of the top recommended restaurants from Yelp and TripAdvisor. We focused on comparing the reviews from San Francisco and Los Angeles specifically to analyze whether the sentiment of reviews differed between restaurants in both locations and whether the sentiment of reviews differed between restaurants for both websites. We presented our findings by web-scraping and extracting the necessary information from both websites to form visualizations and perform sentiment and location analysis.
        </p>

    </body>
    </html>

    """
    html_file.write(html_content)

print("final_project.html created successfully.")
