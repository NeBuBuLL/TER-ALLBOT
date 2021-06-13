# from gym import envs
# import os
import gym

env = gym.make('CartPole-v0')
env.reset()
env.render()

# for i in envs.registry.all(): print(i)

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
