from nuscenes.nuscenes import NuScenes
import yaml
import os

config_file = "tut_config.yaml"
with open(config_file, "r") as f:
    config = yaml.safe_load(f)
dataroot = os.path.join(config["nuscenes_root"], config["nuscenes_version"])

nusc = NuScenes(version=config["nuscenes_version"], dataroot=dataroot, verbose=True)


my_scene = nusc.scene[0]
first_sample_token = my_scene['first_sample_token']
my_sample = nusc.get('sample', first_sample_token)

sensor = 'CAM_FRONT'
cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])

nusc.render_sample_data(cam_front_data['token'])
print("Rendering Complete!")