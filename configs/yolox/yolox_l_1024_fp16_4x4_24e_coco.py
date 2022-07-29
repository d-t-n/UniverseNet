_base_ = './yolox_s_1024_fp16_4x4_24e_coco.py'

# model settings
model = dict(
    backbone=dict(deepen_factor=1.0, widen_factor=1.0),
    neck=dict(
        in_channels=[256, 512, 1024], out_channels=256, num_csp_blocks=3),
    bbox_head=dict(in_channels=256, feat_channels=256))

resume_from = '../logs/coco/yolox_l_1024_fp16_4x4_36e_coco_20220719_030444/epoch_22.pth'  # noqa
