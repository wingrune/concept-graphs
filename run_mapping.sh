export REPLICA_ROOT=/hdd/wingrune/datasets/Replica

export CG_FOLDER=/home/wingrune/concept-graphs/
export REPLICA_CONFIG_PATH=${CG_FOLDER}/conceptgraph/dataset/dataconfigs/objectsorter.yaml
export HYDRA_FULL_ERROR=1 


#SCENE_NAME=2023-08-29-11-02-40_0_data
SCENE_NAME=6_find_cube
THRESHOLD=1.0

#python conceptgraph/slam/cfslam_pipeline_batch.py dataset_root=$REPLICA_ROOT dataset_config=$REPLICA_CONFIG_PATH stride=1 scene_id=$SCENE_NAME spatial_sim_type=overlap mask_conf_threshold=0.48 match_method=sim_sum sim_threshold=${THRESHOLD} dbscan_eps=0.1 gsa_variant=none class_agnostic=True skip_bg=True max_bbox_area_ratio=0.5 save_suffix=overlap_maskconf0.5_simsum${THRESHOLD}_dbscan.1_merge20_masksub merge_interval=20 merge_visual_sim_thresh=0.8 merge_text_sim_thresh=0.8 save_objects_all_frames=True
python conceptgraph/scripts/animate_mapping_save.py --input_folder $REPLICA_ROOT/$SCENE_NAME/objects_all_frames/none_overlap_maskconf0.5_simsum${THRESHOLD}_dbscan.1_merge20_masksub