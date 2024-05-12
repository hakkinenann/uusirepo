zero = 0
one = 1
two = 2
three = 3
four = 4

class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = zero
        self.player2_points = zero

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + one
        else:
            self.player2_points = self.player2_points + one

    def get_score(self):
        if  self.player1_points == self.player2_points:
            score = self.points_tied()
        
        elif self.player1_points >= four or self.player2_points >= four:
            point_difference = self.player1_points - self. player2_points
            score = self.advantage_or_win(point_difference)

        else: score = self.points_in_another_situations()

        return score
    
    def points_tied(self):
        if self.player1_points == zero:
            score = "Love-All"
        elif self.player1_points == one:
            score = "Fifteen-All"
        elif self.player1_points == two:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
    
    def advantage_or_win(self, point_difference):
        if point_difference == one:
                score = "Advantage player1"
        elif point_difference == -one:
                score = "Advantage player2"
        elif point_difference >= two:
                score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def points_in_another_situations(self):
        score = ""
        for i in range(one, three):
            if i == one:
                temp_score = self.player1_points
            else:
                score = score + "-"
                temp_score = self.player2_points

            if temp_score == zero:
                score = score + "Love"
            elif temp_score == one:
                score = score + "Fifteen"
            elif temp_score == two:
                score = score + "Thirty"
            elif temp_score == three:
                score = score + "Forty"
        return score
    