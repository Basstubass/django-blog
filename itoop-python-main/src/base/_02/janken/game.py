# JankenGame クラスを定義しよう
class JankenGame:
    def play(self, left_hand: int, right_hand: int):
        result = self.judge(left_hand, right_hand)
        self.show_result(result)
    
