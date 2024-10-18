# Music Library Genre Diversity Analysis

This repository contains Python scripts for analyzing the genre diversity of a music library managed by Beets. These tools provide insights into the distribution and variety of genres in your music collection using different diversity indices.

## Scripts

1. `shannon_diversity_index_analysis.py`: Script that uses the Shannon Diversity Index.
2. `shannon_simpson_genre_diversity_analyser.py`: An enhanced version that incorporates both Shannon and Simpson Diversity Indices.

## Features

- Calculation of diversity indices:
  - Shannon Diversity Index (both scripts)
  - Simpson Diversity Index (enhanced script only)
- Analysis of overall genre diversity (including all genre tags)
- Analysis of primary genre diversity (considering only the first genre tag)
- Explanations for diversity scores
- Display of top genres in the library
- Distribution of tracks by number of genre tags
- Implications and insights based on the diversity analysis

## Why Two Diversity Indices?

The enhanced script uses both the Shannon Diversity Index and the Simpson Diversity Index because they provide complementary information:

1. **Shannon Diversity Index:**
   - Emphasizes the richness component of diversity
   - More sensitive to rare genres in your collection
   - Assumes all genres are equally different from each other
   - Useful for detecting changes in less common genres

2. **Simpson Diversity Index:**
   - Emphasizes the evenness component of diversity
   - More sensitive to changes in the most common genres
   - Less affected by the presence of rare genres
   - Useful for understanding the dominance of certain genres in your collection

Using both indices provides a more comprehensive understanding of your library's diversity.

## Requirements

- Python 3.x
- SQLite3
- Beets music library

## Installation

1. Clone this repository
2. Ensure you have Python 3.x installed on your system.
3. No additional Python packages are required as the scripts use only built-in libraries.

## Usage

For both scripts:

1. Update the `db_path` variable to point to your Beets library database
2. Run the desired script
