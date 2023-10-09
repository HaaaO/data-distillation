import mat73
import numpy as np
import pickle

data_dict_73 = mat73.loadmat('lfw_att_73.mat')
data_dict_40 = mat73.loadmat('lfw_att_40.mat')




a = {}

num = 0
for item in data_dict_40['name']:

	a['data/lfw-py/lfw_funneled/' + item.split('\\')[0] + '/' + item.split('\\')[1]] = [int(data_dict_40['label'][num][39]), int(data_dict_73['label'][num][2])]

	num += 1



with open('lfwa_young_race.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

