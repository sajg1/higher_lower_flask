from flask import Flask
import random
app = Flask(__name__)


winning_gifs = [
    'https://media1.giphy.com/media/S9iMXx6Lqrr5mJoMxC/200.webp?cid='
    'ecf05e47zyh04elolej3vynvp8b9tesjwia9a4wc8vvbj3xl&rid=200.webp&ct=g',
    'https://media3.giphy.com/media/KYElw07kzDspaBOwf9/100.webp?cid='
    'ecf05e47zyh04elolej3vynvp8b9tesjwia9a4wc8vvbj3xl&rid=100.webp&ct=g',
    'https://media1.giphy.com/media/7OVCzBQkDSyU4tBZrA/200w.webp?cid='
    'ecf05e472awacqloi0j33fds1p7r90s1igq6z7s5nqw03omy&rid=200w.webp&ct=g'
]
random_number = random.randint(0, 9)
print("Random Number: ", random_number)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media3.giphy.com/media/KWSWC38ifoEZG/200w.webp?cid=" \
           "ecf05e472su5iyb0x17i0eis05txaidxb5ufxb5hqnzgedc5&rid=200w.webp&ct=g'/>"

@app.route('/<int:user_guess>')
def win_or_lose(user_guess):
    if user_guess == random_number:
        gif = winning_gifs[random.randint(0,2)]
        return "<h2>You Got It!!</h2>" \
               f"<img src={gif}/>"
    elif user_guess < random_number:
        return "<h2>Too Low, try again!</h2>" \
               "<img src='https://media4.giphy.com/media/PR3585ZZSvcHO9pa76/200w.webp?cid=" \
               "ecf05e471yxszab8wu37it8uwak8ij5rb8uhkufp0sc3ijuh&rid=200w.webp&ct=g'/>"
    elif user_guess > random_number:
        return "<h2>Too High, try again!</h2>" \
               "<img src='https://media0.giphy.com/media/l2YWy9pD8sZEUMF0s/200w.webp?cid=" \
               "ecf05e47hrmqc5evghq1muzplilj2ant52dd3exyyqe65vti&rid=200w.webp&ct=g/'>"




if __name__ == "__main__":
    app.run(debug=True)

