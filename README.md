# TER-M1-ALLBOT
TER Master1 sur le robot ALLBOT


# Lien dropbox
https://www.dropbox.com/sh/tm5589sb2md9syw/AAAq9r7uk_w1AIG6mhfV3F6Ja?dl=0

# Code sur github:
https://github.com/kchua/handful-of-trials


# Pour le robot sur mujoco

## Modelisation avec mujoco
 - Lien utile pour xml:
  - http://www.mujoco.org/forum/index.php?resources/dogbot-quadruped-from-react-robotics.23/
  - https://github.com/deepmind/dm_control/blob/master/dm_control/suite/quadruped.xml
  
  
### Degree of freedom

  - Yaw : 180 degree (Vertical, 2nd joint)
    - from Pi/2 to 3Pi/2
  - Pitch : 135 degree (Horizontal, 1st joint) 
    - from 0 to 7Pi/4
  - Roll : Not use for our robot
