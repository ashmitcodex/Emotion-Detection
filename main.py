sad_wrds = [ 'sad','unhappy','heartbroken','depressed','miserable','sorry','bad','melancholy','upset','worried','sorrowful','disappointed','mournful','uneasy','hopeless']
happy_wrds = ["delighted",'happy', "pleased", "glad", "satisfied", "thankful", "joyful", "joyous", "blissful", "cheerful", "thrilled", "gratified", "chuffed", "hopeful", "ecstatic", "smiling", "merry", "tickled", "cheery", "jolly", "optimistic", "laughing", "upbeat", "gleeful", "jovial", "lighthearted", "buoyant", "euphoric", "sunny", "mirthful", "jubilant", "rapturous", "exuberant", "enraptured", "elated", "blithe", "exultant", "beatific", "intoxicated", "gladsome", "exhilarated", "rhapsodic", "jocund", "blithesome", "rosy", "beaming", "gay", "rejoicing", "rhapsodical", "rapt", "sanguine"]
not_wrds = ["not", "no", "never", "none", "neither", "nor", "nothing", "nowhere", "nobody", "hardly", "scarcely", "barely", "without", "cannot", "can't", "don't", "doesn't", "didn't", "won't", "wouldn't", "shouldn't", "isn't", "aren't", "wasn't", "weren't", "hasn't", "haven't", "hadn't", "ain't"]

user_inp = input("Enter String : ")
data = 0
no_of_sadwords = 0
no_of_happywrds = 0
if any(i in user_inp and j in user_inp for i in sad_wrds for j in not_wrds): 
    print('happy')
elif any(i in user_inp and j in user_inp for i in happy_wrds for j in not_wrds):
 print('sad')
elif any(i in user_inp for i in sad_wrds):
 print('sad1')
elif any(k in user_inp for k in happy_wrds):
 print('happy1')
