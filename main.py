
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
    





def racket_cost(racket_brand):
    if racket_brand == "bullpadel":
        return 100
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "siux":
        return 200
    




def padel_balls_cost(ball_boxes):
    if ball_boxes ==1:
        return 2
    elif ball_boxes ==2:
        return 3.5
    elif ball_boxes ==3:
        return 5
    



def padel_game_cost():
    court_type = input("Enter the court type: ")
    racket_brand = input('Enter the racket brand: ')
    ball_boxes = int(input('Enter number of ball boxes: '))

    x = padel_court_cost(court_type) + racket_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return x    

result= padel_game_cost()
print(f'the genral cost {result}')

   











    
        






