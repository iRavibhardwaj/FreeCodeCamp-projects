def player(prev_play, opponent_history=[]):
   opponent_history.append(prev_play)
   if prev_play=='S':
        if len(opponent_history) >=3 and opponent_history[-2]=='P' and opponent_history[-3]=='R' :
            return 'P'
        if len(opponent_history) >=3 and opponent_history[-2]=='R' and opponent_history[-3]=='R':
            return 'R'
        if len(opponent_history) >=3 and opponent_history[-2]=='P' and opponent_history[-3]=='P':
            return 'P'
        return 'R'
   # R R P P S
   if prev_play == 'P':
        if len(opponent_history) >=3 and opponent_history[-2] == 'R' and opponent_history[-3] == 'S':
           return 'R'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'R' and opponent_history[-3] == 'R':
            return 'R'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'P' and opponent_history[-3] == 'R':
            return 'R'
        if len(opponent_history) >= 3 and opponent_history[-1] == 'P' and opponent_history[-2] == 'S' and opponent_history[-3]=='S':
            return 'P'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'S' and opponent_history[-3] == 'S':
            return 'S'
        return 'S'
   # R R P P S
   if prev_play == 'R':
        if len(opponent_history) >=3 and opponent_history[-2] == 'P' and opponent_history[-3] == 'R':
           return 'S'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'P' and opponent_history[-3] == 'P':
            return 'P'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'S' and opponent_history[-3] == 'P':
            return 'P'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'R' and opponent_history[-3] == 'S':
            return 'S'
        if len(opponent_history) >= 3 and opponent_history[-1] == 'R' and opponent_history[-2] == 'P' and opponent_history[-3]=='P':
            return 'R'
        if len(opponent_history) >= 3 and opponent_history[-2] == 'S' and opponent_history[-3] == 'S':
            return 'S'
        return 'P'
   if prev_play=='':
     return  "P"