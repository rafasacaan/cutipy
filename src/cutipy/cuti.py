import matplotlib.pyplot as plt

def apply_style():
  style_params = {
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.figsize': (10, 6),
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'lines.linewidth': 2,
    'lines.markersize': 6,
    'font.family': 'serif',
    'font.serif': 'Times New Roman',
  }
  plt.rcParams.update(style_params)
