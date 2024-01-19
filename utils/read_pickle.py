import pickle
import numpy as np

with open('/hdd/wingrune/datasets/Replica/6_find_cube/pcd_saves/full_pcd_none_overlap_maskconf0.5_simsum1.0_dbscan.1_merge20_masksub_post.pkl', 'rb') as f:
    data = pickle.load(f)

print(data['objects'][0]['num_detections'])

for i, object in enumerate(data['objects']):
    print(object['class_name'])
    print(object['class_id'])
    print("x", np.mean(object['pcd_np'][:,0]), "y", np.mean(object['pcd_np'][:,1]), "z", np.mean(object['pcd_np'][:,2]))

with open('/home/wingrune/tidy_bot_cv_ws/src/tidy_bot_cv/scripts/6_find_cube/message_66.pkl', 'rb') as f:
    data = pickle.load(f)

print(len(data['classes_ids']))
