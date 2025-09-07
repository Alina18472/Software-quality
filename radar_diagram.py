import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


class RadarDiagram():
    def radar_factory(self, num_vars, frame='circle'):
        """
        Create a radar chart with `num_vars` axes.

        This function creates a RadarAxes projection and registers it.

        Parameters
        ----------
        num_vars : int
            Number of variables for radar chart.
        frame : {'circle', 'polygon'}
            Shape of frame surrounding axes.

        """
        # calculate evenly-spaced axis angles
        theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

        class RadarAxes(PolarAxes):

            name = 'radar'
            # use 1 line segment to connect specified points
            RESOLUTION = 1

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # rotate plot such that the first axis is at the top
                self.set_theta_zero_location('N')

            def fill(self, *args, closed=True, **kwargs):
                """Override fill so that line is closed by default"""
                return super().fill(closed=closed, *args, **kwargs)

            def plot(self, *args, **kwargs):
                """Override plot so that line is closed by default"""
                lines = super().plot(*args, **kwargs)
                for line in lines:
                    self._close_line(line)

            def _close_line(self, line):
                x, y = line.get_data()
                # FIXME: markers at x[0], y[0] get doubled-up
                if x[0] != x[-1]:
                    x = np.append(x, x[0])
                    y = np.append(y, y[0])
                    line.set_data(x, y)

            def set_varlabels(self, labels):
                self.set_thetagrids(np.degrees(theta), labels)

            def _gen_axes_patch(self):
                # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
                # in axes coordinates.
                if frame == 'circle':
                    return Circle((0.5, 0.5), 0.5)
                elif frame == 'polygon':
                    return RegularPolygon((0.5, 0.5), num_vars,
                                          radius=.5, edgecolor="k")
                else:
                    raise ValueError("Unknown value for 'frame': %s" % frame)

            def _gen_axes_spines(self):
                if frame == 'circle':
                    return super()._gen_axes_spines()
                elif frame == 'polygon':
                    # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                    spine = Spine(axes=self,
                                  spine_type='circle',
                                  path=Path.unit_regular_polygon(num_vars))
                    # unit_regular_polygon gives a polygon of radius 1 centered at
                    # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                    # 0.5) in axes coordinates.
                    spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                        + self.transAxes)
                    return {'polar': spine}
                else:
                    raise ValueError("Unknown value for 'frame': %s" % frame)

        register_projection(RadarAxes)
        return theta

    def example_data(self):
        # The following data is from the Denver Aerosol Sources and Health study.
        # See doi:10.1016/j.atmosenv.2008.12.017
        #
        # The data are pollution source profile estimates for five modeled
        # pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical
        # species. The radar charts are experimented with here to see if we can
        # nicely visualize how the modeled source profiles change across four
        # scenarios:
        #  1) No gas-phase species present, just seven particulate counts on
        #     Sulfate
        #     Nitrate
        #     Elemental Carbon (EC)
        #     Organic Carbon fraction 1 (OC)
        #     Organic Carbon fraction 2 (OC2)
        #     Organic Carbon fraction 3 (OC3)
        #     Pyrolized Organic Carbon (OP)
        #  2)Inclusion of gas-phase specie carbon monoxide (CO)
        #  3)Inclusion of gas-phase specie ozone (O3).
        #  4)Inclusion of both gas-phase species is present...
        data = [
            ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'],
            ('Basecase', [
                [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00]])
        ]
        return data
    def draw(self, filename, data, label, title):
        N = 28
        theta = self.radar_factory(N, frame='polygon')

        # data = self.example_data()
        spoke_labels = label

        fig, axs = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='radar'))
        fig.subplots_adjust(wspace=1, hspace=1, top=0.85, bottom=0.05)

        colors = ['b', 'r']
        # Plot the four cases from the example data on separate axes
        # for s in slice:
        np.average(data)
        axs.set_rgrids((np.min(data),  (np.min(data) + np.max(data))/2, np.max(data)*3/4, np.max(data)))
        # axs.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
        #               horizontalalignment='center', verticalalignment='center')

        for ind, i in enumerate(data):
            axs.plot(theta, i, color=colors[ind])
        # axs.fill(theta, d, facecolor=color, alpha=0.25)
        axs.set_varlabels(spoke_labels)

        # add legend relative to top-left plot
        labels = ('Начальные вычисления', 'Вычисления через 1/4 проходов', 'Вычисления через 3/4 проходов', 'Конечные вычисления')
        legend = axs.legend(labels, loc=(-.13, .99),
                            labelspacing=0.1, fontsize='medium')

        fig.text(0.5, 0.965, title,
                 horizontalalignment='center', color='black', weight='bold',
                 size='large')

        fig.savefig(filename)
