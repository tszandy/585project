#!/usr/bin/python
data = ["absolutely","adorable","accepted","acclaimed","accomplish","accomplishment","achievement","action","active","admire","adventure","affirmative","affluent","agree","agreeable","amazing","angelic","appealing","approve","aptitude","attractive","awesome","beaming","beautiful","believe","beneficial","bliss","bountiful","bounty","brave","bravo","brilliant","bubbly","calm","celebrated","certain","champ","champion","charming","cheery","choice","classic","classical","clean","commend","composed","congratulation","constant","cool","courageous","creative","cute","dazzling","delight","delightful","distinguished","divine","earnest","easy","ecstatic","effective","effervescent","efficient","effortless","electrifying","elegant","enchanting","encouraging","endorsed","energetic","energized","engaging","enthusiastic","essential","esteemed","ethical","excellent","exciting","exquisite","F","fabulous","fair","familiar","famous","fantastic","favorable","fetching","fine","fitting","flourishing","fortunate","free","fresh","friendly","fun","funny","generous","genius","genuine","giving","glamorous","glowing","good","gorgeous","graceful","great","green","grin","growing","H","handsome","happy","harmonious","healing","healthy","hearty","heavenly","honest","honorable","honored","hug","I","idea","ideal","imaginative","imagine","impressive","independent","innovate","innovative","instant","instantaneous","instinctive","intuitive","intellectual","intelligent","inventive","J","jovial","joy","jubilant","K","keen","kind","knowing","knowledgeable","L","laugh","legendary","light","learned","lively","lovely","lucid","lucky","luminous","M","marvelous","masterful","meaningful","merit","meritorious","miraculous","motivating","moving","natural","nice","novel","now","nurturing","nutritious","O","okay","one","one-hundred percent","open","optimistic","paradise","perfect","phenomenal","pleasurable","plentiful","pleasant","poised","polished","popular","positive","powerful","prepared","pretty","principled","productive","progress","prominent","protected","proud","quality","quick","quiet","ready","reassuring","refined","refreshing","rejoice","reliable","remarkable","resounding","respected","restored","reward","rewarding","right","robust","S","safe","satisfactory","secure","seemly","simple","skilled","skillful","smile","soulful","sparkling","special","spirited","spiritual","stirring","stupendous","stunning","success","successful","sunny","super","superb","supporting","surprising","T","terrific","thorough","thrilling","thriving","tops","tranquil","transforming","transformative","trusting","truthful","U","unreal","unwavering","up","upbeat","upright","upstanding","V","valued","vibrant","victorious","victory","vigorous","virtuous","vital","vivacious","W","wealthy","welcome","well","whole","wholesome","willing","wonderful","wondrous","worthy","wow","yes","yummy","zeal","zealous"]

#pos_file = open('positive-words.txt', 'r')
#neg_file = open('negative-words', 'r')
from Turney import *

game_reviews=read_amazon_review('amazondataset/Video_Games_5.json')

pos_words = []
neg_words = []

with open('positive-words.txt', 'r') as f:
	for word in f.readlines():
		if findword(str(word[:-1]), game_reviews):
			pos_words += [word]

print pos_words
		

