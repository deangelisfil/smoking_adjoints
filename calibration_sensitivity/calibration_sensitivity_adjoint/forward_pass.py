from B_construction.b_construction_time_invariant import *
from bs_pde.bs_pde_adjoint.forward_pass import bs_pde_adjoint_auxiliary, bs_pde_adjoint_auxiliary_f
from calibration_sensitivity.calibration_loss import Calibration_loss
from parameters import *

def calibration_sensitivity_adjoint(S0: float, sigma: float, r: float, option_list: list, loss: Calibration_loss) :
    S = np.array([S0 + j * delta_S for j in range(-J, J + 1)])
    B = B_construction_time_invariant_f(S, sigma, r, delta_t, delta_S)
    p = bs_pde_adjoint_auxiliary(B)
    f = np.array(list(map(lambda x : x.evaluate(S), option_list)))
    P_model = np.dot(f, p)
    loss = loss.evaluate(P_model)
    return loss

def calibration_sensitivity_adjoint_f(S0: float, sigma: float, r: float, option_list: list) :
    S = np.array([S0 + j * delta_S for j in range(-J, J + 1)])
    B = B_construction_time_invariant_f(S, sigma, r, delta_t, delta_S)
    p_all_list = bs_pde_adjoint_auxiliary_f(B)
    f = np.array(list(map(lambda x : x.evaluate(S), option_list)))
    P_model = np.dot(f, p_all_list[-1])
    return S, B, p_all_list, f, P_model
