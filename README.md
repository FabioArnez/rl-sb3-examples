# rl-sb3-examples

Reinforcement learning examples using [Stable-Baselines3](https://stable-baselines3.readthedocs.io/) and [Gymnasium](https://gymnasium.farama.org/). Covers classic control, highway driving, and robotic manipulation tasks.

---

## Installation

### pip
```bash
pip install -r requirements.txt
```

### uv
```bash
uv pip install -r requirements.txt
```

### miniconda
```bash
conda create -n rl-sb3 python=3.11
conda activate rl-sb3
# Optional: install PyTorch with GPU support before the rest
# conda install pytorch torchvision -c pytorch
pip install -r requirements.txt
```

---

## Examples

### 1 — DQN on LunarLander (`sb3_example_1.py`)

Trains a DQN agent on `LunarLander-v3`, saves the model, reloads it, and runs a visual rollout.

```bash
python sb3_example_1.py
```

---

### 2 — PPO on CartPole with vectorized envs (`sb3_example_2.py`)

Trains PPO on `CartPole-v1` using 4 parallel workers via `SubprocVecEnv`.

```bash
python sb3_example_2.py
```

---

### 3 — SAC + HER on highway parking (`sb3_example_3_train.py` / `sb3_example_3_test.py`)

Trains a SAC agent with Hindsight Experience Replay on the `parking-v0` highway environment.

```bash
# Train (saves her_sac_highway.zip)
python sb3_example_3_train.py

# Test a saved model
python sb3_example_3_test.py
```

---

### 4 — Highway-env exploration (`gym_highway_env_test.py`)

Runs the `parking-v0` environment for a few steps and renders a frame with matplotlib — no training involved.

```bash
python gym_highway_env_test.py
```

---

### 5 — DQN on highway-fast (`gym_highway_sb3_env_test.py`)

Trains DQN on `highway-fast-v0` and logs to TensorBoard.

```bash
python gym_highway_sb3_env_test.py

# View training curves
tensorboard --logdir highway_dqn/
```

---

### 6 — MuJoCo / Gymnasium-Robotics CLI (`gym_mujoco_sb3_test_.py`)

Generic train/test script for any Gymnasium or Gymnasium-Robotics environment. Supports SAC, TD3, and A2C. Checkpoints are saved to `models/` every 25 000 steps.

```bash
# Train (runs indefinitely, Ctrl-C to stop)
python gym_mujoco_sb3_test_.py <env_id> <algo> --train
# e.g.
python gym_mujoco_sb3_test_.py FetchReach-v3 TD3 --train

# Test a saved checkpoint
python gym_mujoco_sb3_test_.py <env_id> <algo> --test <path_to_model>
# e.g.
python gym_mujoco_sb3_test_.py FetchReach-v3 TD3 --test models/TD3_25000.zip
```

---

### 7 — FetchPickAndPlace skeleton (`gym_robotics_example.py`)

Minimal environment loop for `FetchPickAndPlace-v3`. Expects a user-defined `policy` function — use as a starting template.

```bash
python gym_robotics_example.py
```
