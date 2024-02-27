from pettingzoo.classic import connect_four_v3

env_creator = lambda config: connect_four_v3.env(render_mode="rgb_array")

register_env("connect4", lambda config: Connect4Env(env_creator(config)))

from ray.rllib.agents import ppo


# import ray
# # from ray import tune
# from ray.rllib.agents import ppo
# from pettingzoo.classic import connect_four_v3

# num_iterations = 5

# def env_creator(env_config):
#     return connect_four_v3.env()

# config = {
#     "env": "custom_env",
#     # Define other RLlib config parameters as needed
# }

# ray.init()

# trainer = ppo.PPOTrainer(config=config, env=env_creator)
# for i in range(num_iterations):
#     trainer.train()

# ray.shutdown()


# from pettingzoo.classic import connect_four_v3

# env = connect_four_v3.env(render_mode="human")
# env.reset(seed = 17)

# for agent in env.agent_iter():
#     observation, reward, termination, truncation, info = env.last()

#     if termination or truncation:
#         action = None
#     else:
#         mask = observation["action_mask"]
#         # this is where you would insert your policy
#         action = env.action_space(agent).sample(mask)

#     env.step(action)
 
# env.close()

# # Agent tells the player's turn