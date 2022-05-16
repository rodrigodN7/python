#
#By Rodrigo Noriega
#
#intro to data science: dynamic visualizations
#
#
#

"""Dynamically graphing frequencies of die rolls"""
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def udpdate(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each animation frame."""

#roll die and update frequencies
for i in range(rolls):
    frequencies[random.randrange(1,7) - 1] += 1

#reconfigure plot for updated die frequencies
plt.cla()
axes = sns.barplot(faces, frequencies, palette='bright')
axes.set_title(f'Die Frequencies for {sum(frequencies):,} Rolls')
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequencies) * 1.10)

#display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_x = bar.get_height()
    text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
    axes.text(text_x, text_y, text, ha='center', va='bottom')

#read command-line arguments for number of frames and rolls 
number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')
figure = plt.figure('Rolling a six-sided die')
values = list(range(1,7))
frequencies = [0] * 6

#configure and start animation that calls function update
die_animation = animation.FuncAnimation(
                figure, update, repeat=False, frames=number_of_frames, interval=30,
                fargs=(rolls_per_frame, values, frequencies))

plt.show()