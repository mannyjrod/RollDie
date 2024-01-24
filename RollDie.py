# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
# Libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
# Roll the die and calculate die frequencies
rolls = [random.randrange(1, 7) for i in range(600)] # List comprehension to create a list of 600 random die values

values, frequencies = np.unique(rolls, return_counts=True) # Note: Numpy will convert the list to an ndarray for better performance
# Roll the die and calculate die frequencies
rolls = [random.randrange(1, 7) for i in range(600)] # List comprehension to create a list of 600 random die values

values, frequencies = np.unique(rolls, return_counts=True) # Note: Numpy will convert the list to an ndarray for better performance
# Create initial bar plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x=values, y=frequencies, palette='bright')
# Create initial bar plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
# Create initial bar plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
# Finalize the bar plot
axes.set_ylim(top=max(frequencies)*1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
# Create initial bar plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
# Finalize the bar plot
axes.set_ylim(top=max(frequencies)*1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
# Create initial bar plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')

# Finalize the bar plot
axes.set_ylim(top=max(frequencies)*1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
get_ipython().run_line_magic('pinfo', 'axes.set_ylim')
get_ipython().run_line_magic('pinfo', 'axes.set_ylim')
axes.patches
get_ipython().run_line_magic('pinfo', 'axes.set_ylim')
get_ipython().run_line_magic('pinfo', 'axes.set_ylim')
get_ipython().run_line_magic('pinfo', 'axes.set_ylim')
get_ipython().run_line_magic('pinfo', 'zip')
get_ipython().run_line_magic('pinfo', 'zip')
# Clear existing graph
get_ipython().run_line_magic('pinfo', 'plt.cla')
# Clear existing graph
plt.cla()
get_ipython().run_line_magic('recall', '4')
# Roll the die and calculate die frequencies
rolls = [random.randrange(1, 7) for i in range(60000)] # List comprehension to create a list of 60000 random die values
values, frequencies = np.unique(rolls, return_counts=True) # Note: Numpy will convert the list to an ndarray for better performance
get_ipython().run_line_magic('recall', '11')
# Create initial bar plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')

# Finalize the bar plot
axes.set_ylim(top=max(frequencies)*1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
