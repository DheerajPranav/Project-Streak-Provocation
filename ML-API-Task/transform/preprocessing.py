import json
import operator
import pickle


def TopicsRetrieval(input_str, input_data_set, key_set):
    data = []
    for t in input_data_set:
        if input_str in t['text'].lower():
            data.append(t['text'].lower())

    matchGroup = []
    verify = []
    for d in data:
        splitD = d.split(" ")
        matchedData = set(splitD) & set(key_set)
        c = dict.fromkeys(matchedData, 0)
        matchedList = list(set(splitD) & set(key_set))

    if len(matchedData) > 0:
        for m in matchedData:
            if m in verify:
                index1 = verify.index(m)
                matchGroup[index1]['count'] += 1
                for li in matchedList:
                    if li in matchGroup[index1]['matches']:
                        matchGroup[index1]['matches'][li] += 1

            elif m not in verify:
                hashArr = {
                    'word': m,
                    'count': 1,
                    'matches': c
                }
                matchGroup.append(hashArr)
                verify.append(m)
    newlist = sorted(matchGroup, key=lambda k: k['count'])
    newlist.reverse()
    slicedList = newlist[:81]
    finalArr = []
    for index, sort in enumerate(slicedList):
        if index <= 80:
            sorted_x = sorted(sort['matches'].items(), key=operator.itemgetter(1))
            sorted_x.reverse()
            wordArr = []
            xSlice = sorted_x[:10]
            for xS in xSlice:
                wordArr.append(xS[0])
            hash2 = {
                'word': sort['word'],
                'data': index / 2,
                'matches': wordArr
            }
            finalArr.append(hash2)
    print(finalArr)
    return finalArr



def predict_topic_model(input_str):
    with open('data/input_artifactory.json', encoding='utf-8') as f:
        input_data_set = json.load(f)

    with open('data/keywords.json') as f:
        kwrds = json.load(f)

    data = TopicsRetrieval(input_str, input_data_set, kwrds)
    return data


def train_topic_model():
    model = 'Sample-Model'
    with open('data/' + 'Trained_topic_model.pkl', 'wb') as fp:
        pickle.dump(model, fp)

    print('Trained & Dumped the model.')
