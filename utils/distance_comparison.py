import pickle
import numpy as np
from scipy.optimize import linear_sum_assignment

with open('/hdd/wingrune/datasets/Replica/6_find_cube/pcd_saves/full_pcd_none_overlap_maskconf0.5_simsum1.0_dbscan.1_merge20_masksub_post.pkl', 'rb') as f:
    data = pickle.load(f)

objects_concept_graphs = []
for i, object in enumerate(data['objects']):
    objects_concept_graphs.append({
        'class_name': object['class_name'][0],
        'class_id': object['class_id'][0],
        'pose': np.array([
            np.mean(object['pcd_np'][:,0]),
            np.mean(object['pcd_np'][:,1]),
            np.mean(object['pcd_np'][:,2])
            ])
    })


with open('/home/wingrune/tidy_bot_cv_ws/src/tidy_bot_cv/scripts/6_find_cube/message_66.pkl', 'rb') as f:
    data = pickle.load(f)


objects_tidy_bot = []
for i, class_id in enumerate(data['classes_ids']):
    objects_tidy_bot.append({
        'class_id': class_id,
        'pose': data['positions'][i]
    })


# Create a cost matrix where each element represents the cost of matching two elements
cost_matrix = 100*np.ones((len(objects_concept_graphs), len(objects_tidy_bot)))

for i, o_cg in enumerate(objects_concept_graphs):
    for j, o_tb in enumerate(objects_tidy_bot):
        if o_cg['class_id'] != o_tb['class_id']:
            cost_matrix[i,j] = 100
        else:
            cost_matrix[i,j] = np.linalg.norm(o_cg['pose'] - o_tb['pose'])

# Use the linear_sum_assignment function to find the best possible matches
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Print the matches
for row, col in zip(row_ind, col_ind):
    if row < len(objects_concept_graphs):
        print(f'Concept Graph element {row} matches with Tidy Bot element {col}')
        print("distance", cost_matrix[row, col]*10, " cm")
        print(objects_concept_graphs[row])
        print(objects_tidy_bot[col])