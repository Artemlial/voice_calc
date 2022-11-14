import sounddevice as sd
from queue import Queue
import json
import vosk
import werds
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from abilities import *

q = Queue()

model=vosk.Model('small_vosk_model')

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

def callback(indata,frames,time,status):
    q.put(bytes(indata))

def recognize(data,vect,clf):
    # if not (trg := werds.TRIGGERS.intersection(data.split())):
    #     return
    # data.replace(list(trg)[0],'')

    data = data.split()
    res = []
    for i in data:
        if i in werds.phatwerds:
            continue
        else:
            text_vector = vect.transform([i]).toarray()
            ans = clf.predict([text_vector[0]])
            print(type(ans),ans,sep=' ')
            res.append(ans[0])
    exprr = calc(res)
    speaker(exprr)

            

def main():

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(werds.scenarios.keys()))

    clf = LogisticRegression()
    clf.fit(vectors,list(werds.scenarios.values()))

    with sd.RawInputStream(samplerate=samplerate,blocksize=16000,device=device[0],dtype='int16',channels=1,callback=callback):
        rec = vosk.KaldiRecognizer(model,samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                print(data)
                if data: #!= '':
                    # exprr = calc(data)
                    # data = ''
                    # speaker(exprr)
                    recognize(data,vectorizer,clf)

if __name__=='__main__':
    main()

