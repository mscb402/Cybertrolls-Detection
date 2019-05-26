
import json
import numpy as np
import os
print("Loading...")

import sys
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
import keras
sys.stderr = stderr #移除keras“Using TensorFlow backend.”的提示
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #屏蔽tf的提示

model = keras.models.load_model('model.h5')
WordIdx = json.load(open('word.json'))

#欺凌检测
def Bully(text):
    s_q = keras.preprocessing.text.text_to_word_sequence(text)
    s_v = [WordIdx.get(i,WordIdx['_UNK_']) for i in s_q]
    res = model.predict(np.asarray([s_v]))
    value = res[0][0]
    if value > 0.5:
        return ('网络暴力',value)
    else:
        return ('正常',value)

s = sys.argv[1]
print('-----------')
print(s)
print(Bully(s))

