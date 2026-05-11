from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

model = BayesianModel([('Rain', 'Traffic')])

cpd_rain = TabularCPD('Rain', 2, [[0.7],[0.3]])
cpd_traffic = TabularCPD('Traffic', 2,
                         [[0.8, 0.3],
                          [0.2, 0.7]],
                         evidence=['Rain'],
                         evidence_card=[2])

model.add_cpds(cpd_rain, cpd_traffic)

print("Model check:", model.check_model())
