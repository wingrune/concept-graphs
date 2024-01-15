import numpy as np
import os 

old_traj_path = '/hdd/wingrune/datasets/Replica/2023-08-29-11-30-20_0_data/traj_ori.txt'
new_traj_path = '/hdd/wingrune/datasets/Replica/2023-08-29-11-30-20_0_data/traj.txt'

def pose_to_matrix(camera_position, rotation_matrix):
    # Создаем 4x4 матрицу трансформации
    transformation_matrix = np.eye(4)

    # Заполняем верхний левый 3x3 блок матрицы поворота
    transformation_matrix[:3, :3] = np.array(rotation_matrix).reshape(3,3)

    # Заполняем правый столбец матрицы положения камеры
    transformation_matrix[:3, 3] = camera_position

    return transformation_matrix.flatten()

with open(old_traj_path, "r") as f:
    lines = f.readlines()

poses = []
for i in range(0, len(lines)):
    line = list(map(float, lines[i].split()))
    camera_position = line[1:4]
    rotation_matrix = line[4:]
    result_matrix = pose_to_matrix(camera_position, rotation_matrix)
    poses.append(result_matrix)

with open(new_traj_path, 'w') as file:
    for pose in poses:
        for number in pose:
            file.write(str(number) + ' ')
        file.write('\n')
