# Imports
import snscrape.modules.twitter as sntwitter
from wordcloud import WordCloud
from PIL import Image
import pandas as pd
import xlrd

# Upload excel doc with Twitter accounts and create arrays
book = xlrd.open_workbook('EnergyTwitterAccounts.xls')
sheet = book.sheet_by_name('Sheet1')
accounts1 = [sheet.cell_value(r, 0) for r in range(sheet.nrows)]
accounts2 = [sheet.cell_value(r, 1) for r in range(sheet.nrows)]


# Setting variables to be used below
maxTweets = 50
# Creating list to append tweet data to
tweets_list = []
# Using TwitterSearchScraper to scrape data and append tweets to list
for _ in range(len(accounts1)):
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + accounts1[_]).get_items()):
        if i >= maxTweets:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.user.displayname, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.tcooutlinks, accounts2[_]])
# Creating a dataframe from the tweets list above
df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Account', 'Text', 'Likes', 'Replies', 'Retweets', 'Links', 'Type'])
# Display first 5 entries from dataframe
df.head()


# From df, create array of text for all account types
string = []
for _ in range(df.shape[0]):
    string.append(df.Text.iloc[_])
wordsoup = " ".join(string).split()   # "wordsoup" contaisn ALL text. Arrays below are separated by account type

df_writers = df[df.Type == 'Writer/Podcaster'].copy()
string = []
for _ in range(df_writers.shape[0]):
    string.append(df_writers.Text.iloc[_])
wordsoup_writers = " ".join(string).split()

df_thinktanks = df[df.Type == 'Think Tank/Activism'].copy()
string = []
for _ in range(df_thinktanks.shape[0]):
    string.append(df_thinktanks.Text.iloc[_])
wordsoup_thinktanks = " ".join(string).split()

df_Fedempl = df[df.Type == 'Politician/Fed Employee'].copy()
string = []
for _ in range(df_Fedempl.shape[0]):
    string.append(df_Fedempl.Text.iloc[_])
wordsoup_Fedempl = " ".join(string).split()

df_Fedagcy = df[df.Type == 'Fed Agency'].copy()
string = []
for _ in range(df_Fedagcy.shape[0]):
    string.append(df_Fedagcy.Text.iloc[_])
wordsoup_Fedagcy = " ".join(string).split()


# Code below does nothing. Vestige of a previous manipulation that I ended up not needing to use. Too lazy to change the variables now.
final_writers = wordsoup_writers
final_thinktanks = wordsoup_thinktanks
final_Fedempl = wordsoup_Fedempl
final_Fedagcy = wordsoup_Fedagcy


# Shared words removal. Removes top 5 words common on all lists.
shared_list = ["climate", "energy", "Energy", "Climate", "change"]
final_writers = [word for word in final_writers if word not in shared_list]
final_thinktanks = [word for word in final_thinktanks if word not in shared_list]
final_Fedempl = [word for word in final_Fedempl if word not in shared_list]
final_Fedagcy = [word for word in final_Fedagcy if word not in shared_list]
# Complete 'stop words' taken from online git forum. Plus a few of my own added.
removal_list = ["https://t.co/", "http", "t", "co", "s", "https","week","amp", "GreenBiz","day", "years","year", "I","it","thank","As","poll", "United", "opportunity", "Minister", "@FERC", "virtual" "more:", "Panelists:", "join", "Symposium", "@ENERGY", "Our", "Join", "time", "support", "here:", "But", "@TIME", "US", "And", "@GreenBiz", "w/","How", "--", "If", "@amywestervelt", "Watch","New", "learn", "things", "join", "webinar", "Register","A", "&amp" ,"&amp;","I","here","|", "role", "discuss","It's", "including", "it's","today", "hear", "key","report","The","We","This", "-","Read", "What", "full", "In", "May", "For", "Thank", "—","U.S.", "–", "great", "protect", "here", "create", "latest", "lead", "It", "Learn","good", "build", "create", "a","about","above","after","again","against","ain","all","am","an","and","any","are","aren","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always","among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately","importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning","consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly","example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd","keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"]


wc_writers = " ".join(final_writers)
wc_thinktanks = " ".join(final_thinktanks)
wc_Fedempl = " ".join(final_Fedempl)
wc_Fedagcy = " ".join(final_Fedagcy)


def create_wordcloud_100(text, name, colormap):
    # mask = numpy.array(Image.open("shape.png"))   ..Ended up not useing image mask
    # create wordcloud object
    wc = WordCloud(background_color="white",
                    max_words=5000,
                    mask=mask,
                    collocation_threshold = 100,
                    colormap = colormap,
                    stopwords = removal_list)

    wc.generate(text)
    # save wordcloud
    wc.to_file(name + "_100.jpg")  # 100 reprsents the collocation threshold used.


create_wordcloud_100(wc_writers,'writers','inferno')
create_wordcloud_100(wc_thinktanks,'thinktanks','cividis')
create_wordcloud_100(wc_Fedempl,'fedempl','magma')
create_wordcloud_100(wc_Fedagcy,'fedagcy','viridis')
