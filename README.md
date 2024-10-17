"""
Beets Library Genre Diversity Analyzer

This script analyzes the genre diversity of a Beets music library using the Shannon Diversity Index.
It provides insights into both overall and primary genre distributions, calculates diversity scores,
and offers implications for library management and music exploration.

Features:
- Analyzes overall genre diversity (including all genres per track)
- Analyzes primary genre diversity (first genre per track)
- Calculates Shannon Diversity Index and Normalized Diversity Score
- Provides distribution of tracks by number of genres
- Offers insights and implications based on the analysis results

Usage:
1. Ensure you have Python 3 and the Beets library installed
2. Set the 'db_path' variable to point to your Beets database location
3. Run the script: python3 genrediversity.py

This script is designed to work with Beets libraries where genres are comma-separated,
with a maximum of three genres per track.
"""
