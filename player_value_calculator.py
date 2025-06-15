#!/usr/bin/env python3
"""
Daily Fantasy Sports Player Value Calculator
A simple tool to help evaluate if a player is a good value pick
"""

def calculate_value_score(salary, projected_points):
    """
    Calculate points per dollar - higher is better value
    
    Args:
        salary: Player's DFS salary
        projected_points: Expected fantasy points
    
    Returns:
        Value score (points per $1000)
    """
    if salary == 0:
        return 0
    return (projected_points / salary) * 1000

def main():
    print("🏈 DFS Player Value Calculator 🏈")
    print("=" * 35)
    
    # Example players with real-ish data
    players = [
        {"name": "Josh Allen", "position": "QB", "salary": 8500, "projected": 22.5},
        {"name": "Christian McCaffrey", "position": "RB", "salary": 9200, "projected": 18.8},
        {"name": "Tyreek Hill", "position": "WR", "salary": 8800, "projected": 16.2},
        {"name": "Cole Kmet", "position": "TE", "salary": 4200, "projected": 8.5},
    ]
    
    print("Player Analysis:")
    print("-" * 50)
    
    for player in players:
        value_score = calculate_value_score(player["salary"], player["projected"])
        print(f"{player['name']:<20} {player['position']:<3} "
              f"${player['salary']:<6} {player['projected']:<6.1f}pts "
              f"Value: {value_score:.2f}")
    
    print("\n" + "=" * 50)
    print("Value Score = Points per $1000 spent")
    print("Higher value score = better bang for your buck!")
    
    # Interactive part
    print("\nTry your own player:")
    try:
        name = input("Player name: ")
        salary = int(input("Salary: $"))
        projected = float(input("Projected points: "))
        
        value = calculate_value_score(salary, projected)
        print(f"\n{name}'s value score: {value:.2f}")
        
        if value > 2.5:
            print("🔥 Excellent value pick!")
        elif value > 2.0:
            print("✅ Good value")
        elif value > 1.5:
            print("⚠️  Average value")
        else:
            print("❌ Poor value - consider other options")
            
    except ValueError:
        print("Invalid input! Please enter numbers for salary and points.")

if __name__ == "__main__":
    main()