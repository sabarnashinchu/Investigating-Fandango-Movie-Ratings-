import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set style for plots
plt.style.use('fivethirtyeight')
sns.set_palette('deep')

# Load the data
previous = pd.read_csv('Investigating-Fandango-Movie-Ratings/fandango_score_comparison.csv')
after = pd.read_csv('Investigating-Fandango-Movie-Ratings/movie_ratings_16_17.csv')

# Create dataframes with just the relevant Fandango data
fandango_previous = previous[['FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 
                            'Fandango_votes', 'Fandango_Difference']].copy()

fandango_after = after[['movie', 'year', 'fandango']].copy()

# Extract year information from the previous dataset
fandango_previous['Year'] = fandango_previous['FILM'].str.extract(r'\((\d{4})\)')
fandango_previous['Year'] = pd.to_numeric(fandango_previous['Year'])

# Filter to only include movies from 2015
fandango_2015 = fandango_previous[fandango_previous['Year'] == 2015].copy()

# Filter to only include movies from 2016
fandango_2016 = fandango_after[fandango_after['year'] == 2016].copy()

# Print basic information about the datasets
print(f"Number of movies in 2015 dataset: {fandango_2015.shape[0]}")
print(f"Number of movies in 2016 dataset: {fandango_2016.shape[0]}")

# Descriptive statistics for both datasets
print("\nDescriptive Statistics (2015):")
print(fandango_2015['Fandango_Ratingvalue'].describe())

print("\nDescriptive Statistics (2016):")
print(fandango_2016['fandango'].describe())

# Rename columns for consistency
fandango_2015 = fandango_2015.rename(columns={'Fandango_Ratingvalue': 'fandango'})
fandango_2015 = fandango_2015[['FILM', 'fandango']]
fandango_2015 = fandango_2015.rename(columns={'FILM': 'movie'})

fandango_2016 = fandango_2016[['movie', 'fandango']]

# Add a year column to both dataframes for identification
fandango_2015['year'] = 2015
fandango_2016['year'] = 2016

# Create a combined dataframe
df = pd.concat([fandango_2015, fandango_2016], ignore_index=True)

# Create visualizations

# 1. Distribution of ratings - Kernel Density Estimate (KDE) plot
plt.figure(figsize=(12, 8))
sns.kdeplot(data=fandango_2015, x='fandango', label='2015', shade=True)
sns.kdeplot(data=fandango_2016, x='fandango', label='2016', shade=True)
plt.title('Distribution of Fandango Ratings: 2015 vs 2016', fontsize=16)
plt.xlabel('Rating', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.legend(fontsize=12)
plt.savefig('ratings_distribution.png', bbox_inches='tight')
plt.close()

# 2. Box plot comparison
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='year', y='fandango')
plt.title('Fandango Ratings: 2015 vs 2016', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Rating', fontsize=14)
plt.savefig('ratings_boxplot.png', bbox_inches='tight')
plt.close()

# 3. Histogram comparison
plt.figure(figsize=(12, 8))
plt.hist([fandango_2015['fandango'], fandango_2016['fandango']], 
         bins=np.arange(0, 5.1, 0.5), 
         label=['2015', '2016'])
plt.title('Histogram of Fandango Ratings: 2015 vs 2016', fontsize=16)
plt.xlabel('Rating', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.legend(fontsize=12)
plt.savefig('ratings_histogram.png', bbox_inches='tight')
plt.close()

# 4. Print summary statistics to see if means are different
print("\nMean Fandango Rating (2015):", fandango_2015['fandango'].mean())
print("Mean Fandango Rating (2016):", fandango_2016['fandango'].mean())
print("\nMedian Fandango Rating (2015):", fandango_2015['fandango'].median())
print("Median Fandango Rating (2016):", fandango_2016['fandango'].median())

# 5. Percentages of movies with ratings of 4.5 or higher
percentage_45_2015 = (fandango_2015['fandango'] >= 4.5).mean() * 100
percentage_45_2016 = (fandango_2016['fandango'] >= 4.5).mean() * 100

print(f"\nPercentage of movies with ratings ≥ 4.5 in 2015: {percentage_45_2015:.2f}%")
print(f"Percentage of movies with ratings ≥ 4.5 in 2016: {percentage_45_2016:.2f}%")

# 6. Count of ratings by value
print("\nCount of ratings by value (2015):")
print(fandango_2015['fandango'].value_counts().sort_index())

print("\nCount of ratings by value (2016):")
print(fandango_2016['fandango'].value_counts().sort_index())

# 7. Create bar chart of rating counts
plt.figure(figsize=(12, 8))
rating_counts_2015 = fandango_2015['fandango'].value_counts().sort_index()
rating_counts_2016 = fandango_2016['fandango'].value_counts().sort_index()

# Combine the indices to ensure we have bars for all ratings
all_ratings = sorted(set(list(rating_counts_2015.index) + list(rating_counts_2016.index)))
 
# Create a complete series for each year, filling missing values with 0
complete_counts_2015 = pd.Series([rating_counts_2015.get(r, 0) for r in all_ratings], index=all_ratings)
complete_counts_2016 = pd.Series([rating_counts_2016.get(r, 0) for r in all_ratings], index=all_ratings)

# Create a grouped bar chart
x = np.arange(len(all_ratings))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x - width/2, complete_counts_2015, width, label='2015')
ax.bar(x + width/2, complete_counts_2016, width, label='2016')

ax.set_xticks(x)
ax.set_xticklabels(all_ratings)
ax.set_xlabel('Rating', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_title('Count of Fandango Ratings: 2015 vs 2016', fontsize=16)
ax.legend(fontsize=12)

plt.savefig('ratings_count.png', bbox_inches='tight')
plt.close()

print("\nAnalysis completed. Check the generated PNG files for visualizations.") 