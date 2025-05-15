# Investigating Fandango Movie Ratings

## Project Overview
This project investigates whether Fandango's movie rating system changed after October 2015, when data journalist Walt Hickey published an article exposing bias in their rating system. Hickey found strong evidence that Fandango's rating system was inflated to make movies appear better rated than they actually were.

The analysis compares Fandango movie ratings from 2015 (before Hickey's analysis) with ratings from 2016 (after the analysis) to determine if the company modified its rating practices.

## Background
In October 2015, Walt Hickey analyzed movie ratings data and found:
1. Fandango's displayed ratings were consistently higher than the actual rating data in their website's HTML
2. Ratings were almost always rounded up to the nearest half-star
3. In approximately 8% of cases, ratings were rounded up to the nearest whole star
4. In one extreme case, a movie with a true rating of 4.0 was displayed as 5.0 stars

Since Fandango sells movie tickets, this inflation could potentially create a conflict of interest where movies appear better-rated than they actually are, potentially increasing ticket sales.

## Dataset
The project uses two datasets:
1. **fandango_score_comparison.csv**: Contains movie ratings data collected by Walt Hickey in 2015
2. **movie_ratings_16_17.csv**: Contains movie ratings data for films released in 2016-2017

## Analysis
The analysis focuses on comparing the distributions of Fandango ratings between 2015 and 2016 to determine if there was a change in the rating system. It includes:

- Descriptive statistics for both periods
- Distribution visualizations (KDE plots, histograms, box plots)
- Comparison of the frequency of specific rating values
- Analysis of the percentage of films receiving high ratings (≥ 4.5 stars)

## Key Findings
1. The average rating for movies decreased after Hickey's analysis
2. The percentage of movies receiving very high ratings (4.5+ stars) decreased significantly
3. The distribution of ratings shows a clear shift towards lower values in 2016 compared to 2015
4. The changes suggest that Fandango likely adjusted their rating system in response to the public exposure

## Requirements
- Python 3.6+
- pandas
- matplotlib
- numpy
- seaborn

## Installation and Usage
1. Clone this repository:
```
git clone https://github.com/yourusername/fandango-movie-ratings.git
cd fandango-movie-ratings
```

2. Install the required packages:
```
pip install pandas matplotlib numpy seaborn
```

3. Run the analysis script:
```
python analyze_fandango.py
```

4. Review the output in the console and examine the generated visualization images.

## Visualizations
The script generates several visualizations:
- `ratings_distribution.png`: KDE plot showing the distribution of ratings
- `ratings_boxplot.png`: Box plot comparing 2015 vs 2016 ratings
- `ratings_histogram.png`: Histogram of ratings by year
- `ratings_count.png`: Bar chart showing the count of each rating value for both years

## Credits
This project is based on Walt Hickey's original analysis published on FiveThirtyEight. The original article can be found here: [Be Suspicious Of Online Movie Ratings, Especially Fandango's](https://fivethirtyeight.com/features/fandango-movies-ratings/). 