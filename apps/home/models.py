import pandas as pd
import numpy as np
import json

# Load some stuff
with open('apps/static/assets/ai/distance_matrix.npy','rb') as f:
    distance_mat = np.load(f)

embed_df = pd.read_csv('apps/static/assets/ai/skill_embed.csv')
init_sort = pd.read_csv('apps/static/assets/ai/initial_skill_sort.csv')

def get_id(skill):
    for i,skill_name in enumerate(embed_df['name']):
        if skill_name == skill:
            return i
    raise ValueError('skill not found')


def sort_by_total_distance(skill_list):
    distance_list = []
    id_list = []
    for skill in skill_list:
        id_list.append(get_id(skill['skill']))
    for i in range(len(distance_mat)):
        if i not in id_list:
            total_distance = 0
            for idx in id_list:
                total_distance += distance_mat[i,idx]
            distance_list.append(total_distance)
        else:
            distance_list.append(float('inf'))
    distances = np.array(distance_list)
    idx = np.argsort(distances)
    top_distances = distances[idx]
    return top_distances, idx

def initializeItems():
    names = list(init_sort['name'])
    weights = list(init_sort['weight'])
    return [{'skill': skill, 'weight': weight} for skill, weight in zip(names, weights)]

def getItems(data):
    if not data:
        return initializeItems()
    else:
        dists, idx = sort_by_total_distance(data)
        skills = list(embed_df['name'][idx])
        return [{'skill': skill, 'weight': round(3000/weight, 2)} for skill, weight in zip(skills, dists)]

def getColumns():
    return {'skill': 'skill', 'weight': 'weight'}