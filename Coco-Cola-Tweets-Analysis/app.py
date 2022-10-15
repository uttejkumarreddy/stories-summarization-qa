from flask import Flask, render_template, request
import configparser
import tweepy
import random
import pickle

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def homePage():
  if request.method == 'POST':
    # Connect to Twitter API
    parser = configparser.ConfigParser(interpolation = None)
    parser.read('configurations.ini')
    bearerToken  = parser['DEFAULT']['BEARER_TOKEN']
    client = tweepy.Client(bearer_token = bearerToken)

    # Get 10 tweets from Coca-cola page
    cocacolaID = '26787673'

    response = tweepy.Paginator(
      client.get_users_tweets,
      id = cocacolaID,
      exclude = ["retweets", "replies"],
      max_results = 10).flatten(limit = 10)

    tweets = []
    for tweet in response:
      tweets.append(tweet.text)

    # Select a random tweet
    random_number = random.randint(1, 10)
    tweet = tweets[random_number]

    # Predict the classification
    tweetArr = [tweet]
    model = pickle.load(open('model.sav', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
    input_counts = vectorizer.transform(tweetArr)
    prediction = model.predict(input_counts)

    is_advertisement = prediction[0]

    data = {'tweet': tweet, 'is_advertisement': is_advertisement}
    return render_template('home.html', data = data)
  else:
    return render_template('home.html')

if __name__ == '__main__':
  app.run(debug = True)