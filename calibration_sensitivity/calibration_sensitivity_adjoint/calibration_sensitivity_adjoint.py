from calibration_sensitivity.calibration_sensitivity_adjoint.forward_mode import calibration_sensitivity_adjoint_forward
from calibration_sensitivity.calibration_sensitivity_adjoint.reverse_mode import calibration_sensitivity_adjoint_reverse
from calibration_sensitivity.calibration_sensitivity_adjoint.forward_pass import calibration_sensitivity_adjoint
from calibration_sensitivity.calibration_loss import Calibration_loss
from calibration_sensitivity.calibration_sensitivity_abstract import Calibration_sensitivity_abstract
from parameters import *
import numpy as np


class Calibration_sensitivity_adjoint(Calibration_sensitivity_abstract):
    def __init__(self, S, sigma, r: float, option_list: list,
                 loss: Calibration_loss) :
        self.S = S
        self.sigma = sigma
        self.r = r
        self.option_list = option_list
        self.loss = loss

    def __repr__(self):
        return "Calibration sensitivity adjoint: S=" + str(self.S) + ", sigma=" + str(self.sigma) + ", r=" + str(self.r) + \
               ", K=" + str(len(self.option_list))

    def copy(self) :
        return Calibration_sensitivity_adjoint(self.S, self.sigma, self.r, self.option_list, self.loss)

    def evaluate(self, is_complex=False) -> float:
        # same behavior for complex numbers
        return calibration_sensitivity_adjoint(self.S, self.sigma, self.r, self.option_list, self.loss)

    def forward(self, diff_u):
        assert len(diff_u) == 2
        diff_sigma, diff_r = diff_u
        return calibration_sensitivity_adjoint_forward(self.S, self.sigma, self.r, diff_sigma, diff_r, self.option_list,
                                                       self.loss)

    def reverse(self, loss_bar=1):
        return calibration_sensitivity_adjoint_reverse(self.S, self.sigma, self.r, self.option_list, self.loss, loss_bar)