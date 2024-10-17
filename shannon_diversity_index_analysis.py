import sqlite3
import math
from collections import Counter

# Correct database path
db_path = '/media/2nddrive/Audio/Beets/library'

def calculate_shannon_diversity(counts):
    total = sum(counts.values())
    shannon_diversity = 0
    for count in counts.values():
        p = count / total
        shannon_diversity -= p * math.log(p)
    return shannon_diversity

def explain_diversity_score(score):
    if score < 0.2:
        return "Very low diversity. The library is dominated by a few genres."
    elif score < 0.4:
        return "Low diversity. A small number of genres make up most of the library."
    elif score < 0.6:
        return "Moderate diversity. There's a mix of genres, but some dominate."
    elif score < 0.8:
        return "High diversity. The library has a good spread across many genres."
    else:
        return "Very high diversity. Genres are very evenly distributed across the library."

def analyze_diversity(counts):
    shannon_diversity = calculate_shannon_diversity(counts)
    max_diversity = math.log(len(counts))
    normalized_diversity = shannon_diversity / max_diversity if max_diversity > 0 else 0
    return shannon_diversity, normalized_diversity

def print_analysis(category_name, counts):
    total = sum(counts.values())
    shannon_diversity, normalized_diversity = analyze_diversity(counts)
    print(f"\n{category_name} Analysis:")
    print(f"Total genre entries: {total}")
    print(f"Unique genres: {len(counts)}")
    print(f"Shannon Diversity Index: {shannon_diversity:.4f}")
    print(f"Normalized Diversity Score: {normalized_diversity:.4f}")
    print(f"Explanation: {explain_diversity_score(normalized_diversity)}")
    print(f"\nTop 10 Genres:")
    for item, count in counts.most_common(10):
        print(f"{item}: {count}")

def print_implications(overall_score, primary_score, genre_count_distribution):
    print("\nImplications for Your Beets Library:")
    
    if overall_score > 0.7:
        print("1. High Overall Diversity: Your library has a wide variety of genres, offering a rich and varied musical experience.")
    elif overall_score > 0.5:
        print("1. Moderate Overall Diversity: Your library has a good mix of genres, but there's room for more variety.")
    else:
        print("1. Low Overall Diversity: Your library is dominated by a few genres. Consider exploring new musical styles.")
    
    if primary_score > 0.7:
        print("2. High Primary Genre Diversity: The main genres of your tracks are well-distributed, indicating a balanced collection.")
    elif primary_score > 0.5:
        print("2. Moderate Primary Genre Diversity: There's a good spread of main genres, but some dominate more than others.")
    else:
        print("2. Low Primary Genre Diversity: A few primary genres dominate your library. You might want to diversify your main genre categories.")
    
    multi_genre_percentage = (genre_count_distribution[2] + genre_count_distribution[3]) / sum(genre_count_distribution.values()) * 100
    if multi_genre_percentage > 80:
        print("3. Extensive Use of Multi-Genre Tagging: Most of your tracks have multiple genres, providing nuanced classification.")
    elif multi_genre_percentage > 50:
        print("3. Moderate Use of Multi-Genre Tagging: Many tracks have multiple genres, adding depth to your library's organization.")
    else:
        print("3. Limited Use of Multi-Genre Tagging: Consider using multiple genres for more tracks to enhance classification.")
    
    top_genres = set([genre for genre, _ in overall_counts.most_common(3)])
    print(f"4. Genre Focus: Your library is particularly strong in {', '.join(top_genres)}. Consider exploring related subgenres or complementary styles.")
    
    print("5. Playlist Potential: Your genre diversity allows for creating varied playlists across different musical styles.")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT genre FROM items WHERE genre IS NOT NULL AND genre != ''")
    genres = cursor.fetchall()
    
    conn.close()
    
    all_genres = []
    primary_genres = []
    for genre_tuple in genres:
        genre_list = [g.strip() for g in genre_tuple[0].split(',')]
        all_genres.extend(genre_list)
        primary_genres.append(genre_list[0])
    
    overall_counts = Counter(all_genres)
    primary_counts = Counter(primary_genres)
    
    print_analysis("Overall Genre", overall_counts)
    print("\nOverall Genre Analysis considers all genres assigned to tracks, including secondary and tertiary genres.")
    print("This provides a comprehensive view of the total genre diversity in your library.")
    
    print_analysis("Primary Genre", primary_counts)
    print("\nPrimary Genre Analysis only considers the first genre assigned to each track.")
    print("This shows the diversity of main genres in your library, which might be more representative of the overall musical style of each track.")
    
    print("\nAbout the Diversity Measures:")
    print("- Shannon Diversity Index: A measure of diversity that accounts for both the number of genres and their relative abundances.")
    print("  Higher values indicate greater diversity.")
    print("- Normalized Diversity Score: The Shannon Diversity Index normalized to a 0-1 scale, where 1 represents maximum possible diversity.")
    print("  This allows for easier interpretation and comparison between different analyses.")
    
    genre_count_distribution = Counter([len(genre_tuple[0].split(',')) for genre_tuple in genres])
    print("\nDistribution of tracks by number of genres:")
    for count, num_tracks in sorted(genre_count_distribution.items()):
        print(f"{count} genre{'s' if count > 1 else ''}: {num_tracks} tracks")
    
    overall_score = analyze_diversity(overall_counts)[1]
    primary_score = analyze_diversity(primary_counts)[1]
    print_implications(overall_score, primary_score, genre_count_distribution)

except Exception as e:
    print(f"An error occurred: {e}")
