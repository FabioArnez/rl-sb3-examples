import gymnasium
import highway_env
from matplotlib import pyplot as plt
# %matplotlib inline

config = {
    "observation": {
        "type": "Kinematics"
    },
    "action": {
        "type": "DiscreteMetaAction",
    },
    "lanes_count": 4,
    "vehicles_count": 50,
    "duration": 40,  # [s]
    "initial_spacing": 2,
    "collision_reward": -1,  # The reward received when colliding with a vehicle.
    "reward_speed_range": [20, 30],  # [m/s] The reward for high speed is mapped linearly from this range to [0, HighwayEnv.HIGH_SPEED_REWARD].
    "simulation_frequency": 25,  # 15[Hz]
    "policy_frequency": 1,  # [Hz]
    "other_vehicles_type": "highway_env.vehicle.behavior.IDMVehicle",
    "screen_width": 640,  # 600[px]
    "screen_height": 480,  # 150[px]
    "centering_position": [0.3, 0.5],
    "scaling": 5.5,
    "show_trajectories": False,
    "render_agent": False,
    "offscreen_rendering": False
}

# env = gymnasium.make('highway-v0', render_mode='human')
# env = gymnasium.make('highway-v0', render_mode = 'rgb_array', config=config)
env = gymnasium.make("parking-v0", render_mode = 'rgb_array', config=config)
env.reset()
for _ in range(15):
    action = env.unwrapped.action_type.actions_indexes["IDLE"]
    obs, reward, done, truncated, info = env.step(action)
    env.render()

plt.imshow(env.render())
plt.show()