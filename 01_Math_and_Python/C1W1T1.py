import numpy as np
import pandas as pd
import re
from scipy.spatial import distance

file_obj = open('sentences.txt')
data_list = list(file_obj)

sentence_list = []
word_dict = {}
sentence_dict = {}

i = 0

for line in data_list:
    sentence_split = list(filter(None, re.split('[^a-z]', line.lower())))
    for word in sentence_split:
        if word not in word_dict:
            word_dict[word] = i
            i += 1
    sentence_list.append(list(filter(None, re.split('[^a-z]', line.lower()))))

# print(sentence_list,'\n')
# print(word_dict,'\n')

all_word_list = list(word_dict.keys())

mat = pd.DataFrame(np.zeros((len(sentence_list), len(word_dict))))

# print(mat, '\n')
# print(mat.shape, '\n')

for i in range(22):
    for j in range(254):
        mat[j][i] = sentence_list[i].count(all_word_list[j])

all_word_list = list(word_dict.keys())
mat.columns = all_word_list
print(mat, '\n')

cos_dist = pd.DataFrame(np.zeros((22, 2)))

for i in range(1, 22):
    cos_dist[0][i] = i + 1
    cos_dist[1][i] = distance.cosine(np.asarray(mat.iloc[0][:]), np.asarray(mat.iloc[i][:]))

cos_dist_names = list(('sent', 'dist'))
cos_dist.columns = cos_dist_names
print(cos_dist, '\n')

sorted = cos_dist.sort_values(by='dist', ascending=True)[:3]
print(sorted, '\n')

a = str(sorted['sent'][4] - 1)
b = str(sorted['sent'][6] - 1)

answer = ' '.join([a,b])
print('answer = ', answer)

submission = open('submission-1.txt', 'w')
submission.write(answer)
submission.close()