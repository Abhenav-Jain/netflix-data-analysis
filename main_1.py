import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
try:
    df = pd.read_csv('netflix_project.csv')
except FileNotFoundError:
    print("The file 'netflix_project.csv' was not found.")
    exit()

# Clean the dataset
df = df.dropna(subset=['title', 'country', 'release_year', 'rating'])

# Convert 'release_year' to numeric, forcing errors to NaN
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Drop rows with NaN in 'release_year'
df = df.dropna(subset=['release_year'])

# Convert 'release_year' to integer
df['release_year'] = df['release_year'].astype(int)

# Count the number of titles released per year
title_counts = df['release_year'].value_counts().sort_index()

# Create a bar graph of the number of titles released per year
plt.figure(figsize=(12, 6))
plt.bar(title_counts.index, title_counts.values, color='skyblue', edgecolor='black', alpha=0.7, label='Number of Titles')
plt.title('Number of Titles Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.savefig('titles_per_year.png')
plt.show()

# Create a pie chart of the distribution of ratings
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140 , colors=['skyblue', 'lightcoral', 'gold', 'lightgreen', 'lightsalmon'])
plt.title('Distribution of Ratings')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.tight_layout()
plt.savefig('ratings_distribution.png' , dpi = 300 , bbox_inches='tight')
plt.show()

# Create a histogram of movies duration with thier distribution
# Filter only Movie type
movie_df = df[df['type'] == 'Movie'].copy()

# Clean and convert duration
movie_df['duration'] = movie_df['duration'].astype(str)
movie_df = movie_df[movie_df['duration'].str.contains('min')]  # filter only proper durations
movie_df['duration'] = movie_df['duration'].str.replace(' min', '', regex=False)
movie_df['duration'] = pd.to_numeric(movie_df['duration'], errors='coerce')
movie_df = movie_df.dropna(subset=['duration'])

# Final clean duration
movie_duration = movie_df['duration'].astype(int)

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(movie_duration, bins=30, color='purple', edgecolor='black', alpha=0.7)
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_durations_distribution.png')
plt.show()

# Create a Scatter plot for visualizing release years vs number of shows
release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.scatter(release_year_counts.index, release_year_counts.values, color='orange', alpha=0.6)
plt.title('Scatter Plot of Release Years vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.xticks(rotation=45)  
plt.tight_layout()
plt.savefig('release_years_scatter.png')
plt.show()

# Horizontal bar chart for top 10 countries with most shows
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_countries.index, top_countries.values, color='teal', alpha=0.7)
plt.title('Top 10 Countries with Most Shows')
plt.xlabel('Number of Shows')
plt.tight_layout()
plt.savefig('top_countries.png')
plt.show()
