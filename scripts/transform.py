import rospy
import cv2
import numpy as np
import tf2_ros
import yaml
import tf

import roslib; roslib.load_manifest('transformations_in_ros')

if __name__ == '__main__':
    euler_pitch = rospy.get_parm('pitch')
    euler_yaw   = rospy.get_parm('yaw')
    euler_roll  = rospy.get_parm('roll')
    t_x = rospy.get_parm('x')
    t_y = rospy.get_parm('y')
    t_z = rospy.get_parm('z')
    child = rospy.get_parm('child')
    parent = rospy.get_parm('parent')
    r = tf.transformations.quaternion_from_euler(euler_roll, euler_pitch, euler_yaw)
    print quaternion_val
    yaml_stream = open('dump_test.yaml', 'w')
    test_yaml = {'test_yaml': {'child_frame_id': child, 'header': {'frame_id': parent}, 'transform': {'translation': {'x': t_x, 'y': t_y, 'z': t_z}, 'rotation': {'x': r[0], 'y': r[1], 'z': r[2], 'w': r[3]}}}}
    print yaml.dump(test_yaml, default_flow_style=False)
    yaml.dump(test_yaml, yaml_stream, default_flow_style=False)
    yaml_stream.close()
