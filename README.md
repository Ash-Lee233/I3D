# I3D

The paucity of videos in current action classification
datasets (UCF-101 and HMDB-51) has made it difficult
to identify good video architectures, as most methods obtain similar performance on existing small-scale benchmarks. 

Carreira J ,  Zisserman A . Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset[J]. IEEE, 2017.
[论文链接](https://arxiv.org/pdf/1705.07750.pdf)

# Dataset
- [HMDB51](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/) 
- process HMDB51：

    - Download ```hmdb51_org1.rar```和```test_train_splits.rar``` and decompress
    - run ```generate_rgb_jpgs.py```，convert vedio to image. ```avi_video_dir_path```is the original file path，```jpg_video_dir_path```is the save image path

        ```bash
        python -m generate_rgb_jpgs avi_video_dir_path jpg_video_dir_path hmdb51
        ```

    - run```convert_rgb_to_flow.py```，convert RGB image to flow.```RGB_PATH```is the file path of rgb image，```FLOW_PATH```is the save path of flow image。FYI, if appear Error like module 'cv2' has no attribute 'DualTVL1OpticalFlow_create'，please try older version of opencv-python，like3.x.x.xx version.

      ```bash
      python convert_rgb_to_flow.py --rgb_path=[RGB_PATH] --flow_path=[FLOW_PATH]
      ```

    - run```hmdb51_json.py``` to generate annotation file。```annotation_dir_path``` is ```test_train_splits.rar```，```jpg_video_dir_path```is the rgb file get before```dst_json_path```is the save path of json file. flow image also use this json.

      ```bash
      python -m hmdb51_json annotation_dir_path jpg_video_dir_path dst_json_path
      ```

    - run```generate_n_frames.py```to generate n_frames file。```jpg_video_directory```is the file path of rgb and flow image get before. both of rgb dataset and flow dataset need n_frames file.

      ```bash
      python generate_n_frames.py jpg_video_directory
      ```

- [UCF101](https://www.crcv.ucf.edu/research/data-sets/ucf101/)  same process as HMDB51

- data path：

```text
├── datasets
│   ├── flow
│   │   ├─ hmdb51
│   │   │   ├─ jpg
│   │   │   │   ├─ brush_hair
│   │   │   │   ├─ cartwheel
│   │   │   │   ├─ ...
│   │   │   ├─ annotation
│   │   │   │   ├─ hmdb51_1.json
│   │   │   │   ├─ hmdb51_2.json
│   │   │   │   ├─ hmdb51_3.json
│   │   ├─ ucf101
│   │   │   ├─ jpg
│   │   │   │   ├─ ApplyEyeMakeup
│   │   │   │   ├─ ApplyLipstick
│   │   │   │   ├─ ...
│   │   │   ├─ annotation
│   │   │   │   ├─ ucf101_01.json
│   │   │   │   ├─ ucf101_02.json
│   │   │   │   ├─ ucf101_03.json
│   ├── rgb
│   │   ├─ hmdb51
│   │   │   ├─ jpg
│   │   │   │   ├─ brush_hair
│   │   │   │   ├─ cartwheel
│   │   │   │   ├─ ...
│   │   │   ├─ annotation
│   │   │   │   ├─ hmdb51_1.json
│   │   │   │   ├─ hmdb51_2.json
│   │   │   │   ├─ hmdb51_3.json
│   │   ├─ ucf101
│   │   │   │   ├─ ApplyEyeMakeup
│   │   │   │   ├─ ApplyLipstick
│   │   │   │   ├─ ...
│   │   │   ├─ annotation
│   │   │   │   ├─ ucf101_01.json
│   │   │   │   ├─ ucf101_02.json
│   │   │   │   ├─ ucf101_03.json
```

# Train

[Pretrained TF](https://github.com/deepmind/kinetics-i3d/tree/master/data/checkpoints)

[Pretrained community Pytorch](https://github.com/hassony2/kinetics_i3d_pytorch/tree/master/model)
```bash
python pt2ckpt.py --pretrained_path=[PRETRAINED_PATH] --save_path=[SAVE_PATH]
bash run_standalone_train.sh [device_id] [dataset] [mode] [num_epochs] 
```

- HMDB51 rgb mode

    ```text
    epoch: 1 step: 56, loss is 14.464891
    epoch time: 308488.012 ms, per step time: 5508.715 ms
    epoch: 2 step: 56, loss is 6.3676977
    epoch time: 127061.488 ms, per step time: 2268.955 ms
    epoch: 3 step: 56, loss is 4.588459
    epoch time: 127578.249 ms, per step time: 2278.183 ms
    epoch: 4 step: 56, loss is 2.4345832
    epoch time: 122955.708 ms, per step time: 2195.638 ms
    epoch: 5 step: 56, loss is 3.6290636
    epoch time: 126541.872 ms, per step time: 2259.676 ms
    ...
    ...
    ```

- HMDB51 flow mode

    ```text
    epoch: 1 step: 56, loss is 15.534042
    epoch time: 288257.892 ms, per step time: 5147.462 ms
    epoch: 2 step: 56, loss is 5.654072
    epoch time: 119883.500 ms, per step time: 2140.777 ms
    epoch: 3 step: 56, loss is 4.9139385
    epoch time: 135799.968 ms, per step time: 2424.999 ms
    epoch: 4 step: 56, loss is 1.7731495
    epoch time: 136061.834 ms, per step time: 2429.676 ms
    epoch: 5 step: 56, loss is 2.97477
    epoch time: 121972.934 ms, per step time: 2178.088 ms
    ...
    ...
    ```

- UCF101 rgb mode

    ```text
    epoch: 1 step: 148, loss is 4.1663394
    epoch time: 371017.286 ms, per step time: 2506.874 ms
    epoch: 2 step: 148, loss is 2.9134295
    epoch time: 238646.173 ms, per step time: 1612.474 ms
    epoch: 3 step: 148, loss is 1.7739947
    epoch time: 228499.503 ms, per step time: 1543.916 ms
    epoch: 4 step: 148, loss is 1.1962743
    epoch time: 241279.213 ms, per step time: 1630.265 ms
    epoch: 5 step: 148, loss is 1.1757829
    epoch time: 232278.085 ms, per step time: 1569.447 ms
    ...
    ...
    ```

- UCF101 flow mode

    ```text
    epoch: 1 step: 148, loss is 3.0665674
    epoch time: 223182.687 ms, per step time: 1507.991 ms
    epoch: 2 step: 148, loss is 2.4819078
    epoch time: 90178.436 ms, per step time: 609.314 ms
    epoch: 3 step: 148, loss is 2.622658
    epoch time: 91545.521 ms, per step time: 618.551 ms
    epoch: 4 step: 148, loss is 0.45071584
    epoch time: 90573.475 ms, per step time: 611.983 ms
    epoch: 5 step: 148, loss is 0.5305861
    epoch time: 92125.260 ms, per step time: 622.468 ms
    ...
    ...
    ```


# Eval
```bash
bash run_single_eval.sh [device_id] [mode] [dataset] [ckpt_path]

OR

HMDB51 
rgb： python eval.py --dataset=hmdb51 --video_path=[rgb jpg PATH] --annotation_path=[json PATH] --rgb_path=[rgb ckpt PATH] --test_mode=rgb --num_classes=51 --device_id=[device id]
flow：python eval.py --dataset=hmdb51 --video_path=[flow jpg PATH] --annotation_path=[json PATH] --flow_path=[flow ckpt PATH] --test_mode=flow --num_classes=51 --device_id=[device id]

UCF101 
rgb： python eval.py --dataset=ucf101 --video_path=[rgb jpg PATH] --annotation_path=[json PATH] --rgb_path=[rgb ckpt PATH] --test_mode=rgb --num_classes=101 --device_id=[device id]
flow：python eval.py --dataset=ucf101 --video_path=[flow jpg PATH] --annotation_path=[json PATH] --flow_path=[flow ckpt PATH] --test_mode=flow --num_classes=101 --device_id=[device id]

rgb+flow 
HMDB51：python eval.py --dataset=hmdb51 --video_path=[rgb jpg PATH] --annotation_path=[json PATH] --video_path_joint_flow=[flow jpg PATH] --annotation_path_joint_flow=[json PATH] --rgb_path=[rgb ckpt PATH] --flow_path=[flow ckpt PATH] --test_mode=joint --num_classes=51 --device_id=[device id]
UCF101：python eval.py --dataset=ucf101 --video_path=[rgb jpg PATH] --annotation_path=[json PATH] --video_path_joint_flow=[flow jpg PATH] --annotation_path_joint_flow=[json PATH] --rgb_path=[rgb ckpt PATH] --flow_path=[flow ckpt PATH] --test_mode=joint --num_classes=101 --device_id=[device id]
```