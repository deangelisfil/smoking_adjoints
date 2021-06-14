from bs_pde.forward_mode import bs_pde_forward
from bs_pde.reverse_mode import bs_pde_reverse
from bs_pde.forward_pass import bs_pde
from bs_pde_abstract import Bs_pde_abstract
from payoff import Payoff

class Bs_pde(Bs_pde_abstract):
    def __init__(self, S0: float, sigma: float, r: float, option: Payoff, american: bool = False) -> None:
        self.S0 = S0
        self.sigma = sigma
        self.r = r
        self.option = option
        self.american = american

    def __repr__(self):
        if self.american:
            return "BS PDE for American option: S0=" + str(self.S0) + ", sigma=" + str(self.sigma) + ", r=" + str(self.r) \
                   + ", option: " + str(self.option)
        else:
            return "BS PDE: S0=" + str(self.S0) + ", sigma=" + str(self.sigma) + ", r=" + str(self.r) +\
                   ", option: " + str(self.option)

    def copy(self):
        return Bs_pde(self.S0, self.sigma, self.r, self.option, self.american)

    def evaluate(self, is_complex=False) -> float:
        return bs_pde(self.S0, self.sigma, self.r, self.option, self.american, is_complex)

    def forward(self, diff_u):
        diff_S0, diff_sigma, diff_r = diff_u
        return bs_pde_forward(self.S0, self.sigma, self.r, diff_S0, diff_sigma, diff_r, self.option, self.american)

    def reverse(self, qoi_bar=1):
        return bs_pde_reverse(self.S0, self.sigma, self.r, self.option, qoi_bar, self.american)












