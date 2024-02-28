from typing import Optional
from pettingzoo import PettingZooEnv
from pettingzoo.utils import PublicAPI

@PublicAPI
class Connect4Env(PettingZooEnv):
    def reset(self, *, seed: Optional[int]=None, options: Optional[dict]=None):
        self.env.reset(seed=seed, options=options)
        return (
            {self.env.agent_selection: self.observe(self.env.agent_selection)}
        )
    def render(self):
        return self.env.render()
