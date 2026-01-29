#Solve Tipping problem using fuzzy logic
#pip install scikit-fuzzy
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1️⃣ Define fuzzy variables
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')  # Food quality
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')  # Service quality
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')          # Tip percentage

# 2️⃣ Define membership functions
quality.automf(3)  # poor, average, good
service.automf(3)  # poor, average, good

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Optional: View membership functions
# quality['average'].view()
# service.view()
# tip.view()

# 3️⃣ Define fuzzy rules
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Optional: view a rule
# rule1.view()

# 4️⃣ Create control system and simulation
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# 5️⃣ Pass input values
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# 6️⃣ Compute output
tipping.compute()

# 7️⃣ Print result
print("Recommended tip:", tipping.output['tip'])

# 8️⃣ View tip membership with result
tip.view(sim=tipping)
plt.show()