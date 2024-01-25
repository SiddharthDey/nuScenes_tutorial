from nuscenes.nuscenes import NuScenes

# nusc = NuScenes(version='v1.0-test', dataroot='/home/captainlevi/Documents/UCSD_lab_project/AVL/data/nuScenes_dataset/nuScenes/v1.0-test', verbose=True)
nusc = NuScenes(version='v1.0-mini', dataroot='/home/captainlevi/Documents/UCSD_lab_project/AVL/data/nuScenes_dataset/nuscenes_pgp/nuscenes_mini', verbose=True)


my_scene = nusc.scene[0]
first_sample_token = my_scene['first_sample_token']
my_sample = nusc.get('sample', first_sample_token)

sensor = 'CAM_FRONT'
cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])

nusc.render_sample_data(cam_front_data['token'])
print("Rendering Complete!")