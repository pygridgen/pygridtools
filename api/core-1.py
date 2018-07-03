import matplotlib.pyplot as plt
import pandas
import pygridtools
domain1 = pandas.DataFrame({
    'x': [2, 5, 5, 2],
    'y': [6, 6, 4, 4],
    'beta': [1, 1, 1, 1]
})
domain2 = pandas.DataFrame({
    'x': [6, 11, 11, 5],
    'y': [5, 5, 3, 3],
    'beta': [1, 1, 1, 1]
})
grid1 = pygridtools.make_grid(domain=domain1, nx=6, ny=5, rawgrid=False)
grid2 = pygridtools.make_grid(domain=domain2, nx=8, ny=7, rawgrid=False)
merged = grid1.merge(grid2, how='horiz')
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(6, 6))
grid1.plot_cells(ax=ax1, cell_kws=dict(cmap='Blues'))
grid2.plot_cells(ax=ax1, cell_kws=dict(cmap='Greens'))
merged.plot_cells(ax=ax2, cell_kws=dict(cmap='BuPu'))
plt.show()