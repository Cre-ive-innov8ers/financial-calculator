#myModule
import random

def rand_quote():
    my_rand = ["The stock market is filled with individuals who know the price of everything, but the value of nothing.","In investing, what is comfortable is rarely profitable.",

    "It's not whether you're right or wrong that's important, but how much money you make when you're right and how much you lose when you're wrong.",

    "The four most dangerous words in investing are: 'This time it's different.",

    "The goal of a successful trader is to make the best trades. Money is secondary.",

    "Risk comes from not knowing what you're doing.",

    "The stock market is a device for transferring money from the impatient to the patient.",

    "Price is what you pay. Value is what you get.",

    "The best investment you can make is in yourself.",

    "Investing should be more like watching paint dry or watching grass grow. If you want excitement, take $800 and go to Las Vegas.",

    "The time of maximum pessimism is the best time to buy, and the time of maximum optimism is the best time to sell.",

    "The most important quality for an investor is temperament, not intellect. You need a temperament that neither derives great pleasure from being with the crowd or against the crowd.",

    "Do not be embarrassed by your failures; learn from them and start again.",

    "Opportunities come infrequently. When it rains gold, put out the bucket, not the thimble.",

    "It's not whether you're right or wrong that's important, but how much money you make when you're right and how much you lose when you're wrong.",

    "I will tell you the secret to getting rich on Wall Street. You try to be greedy when others are fearful. And you try to be fearful when others are greedy.",

    "The first rule of investment is don't lose money; the second rule is don't forget the first rule."]
    y = len(my_rand)
    x =  random.randint(0, y)
    quote = my_rand[x]
    print(quote)
