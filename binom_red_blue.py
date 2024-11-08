from matplotlib import pyplot as plt
import numpy as np

rend = None

# function that places the label give the desired position
def place_label(label, xy, position, color, ax=None, pad=0.02, alpha=0.7):

  if ax is None:
    ax = plt.gca()

  # annotate in the initial position, xy is the top right corner of the bounding box
  t_ = ax.text(x=xy[0], y=xy[1], s=label, fontsize=20, color=color, bbox=dict(facecolor='white', alpha=alpha, ec='none'))

  # find useful values
  tbb = t_.get_window_extent(renderer=rend)
  abb = ax.get_window_extent(renderer=rend)
  a_xlim, a_ylim = ax.get_xlim(), ax.get_ylim()

  # now adjust the position if needed
  new_xy = [xy[0], xy[1]]

  relative_width = tbb.width/abb.width * (a_xlim[1] - a_xlim[0])
  pad_x = pad * (a_xlim[1] - a_xlim[0])
  assert(position[0] in ['l', 'c', 'r'])
  if position[0] == 'c':
    new_xy[0] -= relative_width/2
  elif position[0] == 'l':
    new_xy[0] -= relative_width + pad_x
  else:
    new_xy[0] += pad_x

  relative_height =  tbb.height/abb.height * (a_ylim[1] - a_ylim[0])
  pad_y = pad * (a_ylim[1] - a_ylim[0])
  assert(position[1] in ['b', 'c', 't'])
  if position[1] == 'c':
    new_xy[1] -= relative_height/2
  elif position[1] == 'b':
    new_xy[1] -= relative_height + pad_y
  else:
    new_xy[1] += pad_y

  t_.set_position(new_xy)

  return t_


fig = plt.figure(figsize=[20, 10])
plt.ylim(-6, 6)
plt.xlim(-0.5, 5.9)
rend = fig.canvas.get_renderer()

for xlabel_i in plt.gca().get_yticklabels():
  xlabel_i.set_fontsize(0.0)
  xlabel_i.set_visible(False)
for tick in plt.gca().get_yticklines():
  tick.set_visible(False)

def num_to_label_coeff(letter, n): 
  if n == 0:
    return letter
  if n < 0:
    return f"{letter}-{-n}"
  return f"{letter}+{n}"

for x in range(5):
   for y in range(x+1):
        plt.plot([x, x+1], [2*y-x, 2*y-x-1], 'b')
        plt.plot([x, x+1], [2*y-x, 2*y-x+1], 'r')

if False:
  plt.plot([4, 5], [2, 1], 'b', linewidth=5)
  plt.plot([4, 5], [0, 1], 'r', linewidth=5)

for cols, style in [('rrrbb', ':'), ('bbrrr', '--')]:
  ys = [cols[:i].count('r') - cols[:i].count('b')  for i in range(6)]
  plt.plot(range(6), ys, "white")
  for x, col in enumerate(cols):
    plt.plot([x, x+1], [ys[x], ys[x+1]], col+style, linewidth=5)

for x in range(6):
    for y in range(x+1):
        place_label(label=num_to_label_coeff("r'",   y), xy=[x, 2*y-x], position='ct', color='red', alpha=0)
        place_label(label=num_to_label_coeff("b'", x-y), xy=[x, 2*y-x], position='cb', color='blue', alpha=0)

plt.show()
