# Time Complexity: O(N) where N is total competitions
# Space Complexity: O(K) where K is total teams
def tournamentWinner(competitions, results):
    # Write your code here.
    max_points = 0
    winning_team = ''
    points = {}
    for index, competition in enumerate(competitions):
        if results[index] == 0:
            winner = competition[1]
        else:
            winner = competition[0]
        points[winner] = points.get(winner, 0) + 3
        if points[winner] > max_points:
            max_points = points[winner]
            winning_team = winner
    return winning_team
