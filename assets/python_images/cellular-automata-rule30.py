
#| label: fig-rule30-ca
#| fig-cap: "Rule 30 Cellular Automaton Evolution"
#| fig-width: 5
#| fig-height: 3
#| echo: false

import numpy as np
import matplotlib.pyplot as plt

def rule30(cells):
    """Applies Rule 30 to the input cells."""
    new_cells = np.zeros_like(cells)
    extended_cells = np.concatenate(([cells[-1]], cells, [cells[0]]))
    
    for i in range(1, len(extended_cells) - 1):
        left, center, right = extended_cells[i-1:i+2]
        
        # Rule 30 logic: binary 00011110
        pattern = int(f"{int(left)}{int(center)}{int(right)}", 2)
        rule_table = [0, 1, 1, 1, 1, 0, 0, 0]  # Rule 30
        new_cells[i-1] = rule_table[pattern]
            
    return new_cells

# Initialize the cellular automaton
width = 401
steps = 200
cells = np.zeros(width, dtype=int)
cells[width // 2] = 1  # Start with one cell in the middle

# Generate evolution history
history = [cells.copy()]
for i in range(steps):
    cells = rule30(cells)
    history.append(cells.copy())

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(history, cmap='binary', aspect='auto', interpolation='nearest', origin='upper')
ax.set_title('Rule 30 Cellular Automaton Evolution', fontsize=14, pad=20)
ax.set_xlabel('Cell Position')
ax.set_ylabel('Time Step')
ax.set_xlim(0, width-1)
ax.set_ylim(steps, 0)  # Reverse the y-axis: start from steps and go to 0

# Clean up the plot
plt.tight_layout()
plt.show()