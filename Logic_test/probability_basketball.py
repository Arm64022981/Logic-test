# ข้อที่9
def probability_basketball_not_football(total_students, football_players, basketball_players, no_sport_players):
    at_least_one = total_students - no_sport_players
    both_sports = football_players + basketball_players - at_least_one
    basketball_only = basketball_players - both_sports
    probability = basketball_only / total_students
    return probability

if __name__ == "__main__":
    total_students = 40
    football_players = 18
    basketball_players = 15
    no_sport_players = 12

    p = probability_basketball_not_football(total_students, football_players, basketball_players, no_sport_players)
    print(f"ความน่าจะเป็นที่นักเรียนเล่นบาสเกตบอลแต่ไม่เล่นฟุตบอล = {p:.2f} หรือ {p*100:.1f}%")
