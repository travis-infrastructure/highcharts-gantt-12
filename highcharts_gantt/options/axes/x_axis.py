from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_stock.options.axes.x_axis import XAxis as XAxisBase

from highcharts_gantt.decorators import class_sensitive
from highcharts_gantt.options.axes.plot_bands import PlotLine
from highcharts_gantt.options.axes.grids import GridOptions


class XAxis(XAxisBase):

    def __init__(self, **kwargs):
        self._current_date_indicator = None
        self._grid = None
        self._max_range = None

        self.current_date_indicator = kwargs.get('current_date_indicator', None)
        self.grid = kwargs.get('grid', None)
        self.max_range = kwargs.get('max_range', None)

        super().__init__(**kwargs)

    @property
    def current_date_indicator(self) -> Optional[PlotLine]:
        """Configuration for an indicator on the axis to provide the current date and
        time. Accepts either a :class:`bool <python:bool>`, or a
        :class:`PlotLine <highcharts_gantt.options.axes.plot_bands.PlotLine>`
        instance.

        :rtype: :class:`PlotLine <highcharts_gantt.options.axes.plot_bands.PlotLine>`
        """
        return self._current_date_indicator

    @current_date_indicator.setter
    @class_sensitive(PlotLine)
    def current_date_indicator(self, value):
        self._current_date_indicator = value

    @property
    def grid(self) -> Optional[GridOptions]:
        """Grid options for the axis labels.

        :rtype: :class:`GridOptions <highcharts_gantt.options.axes.grids.GridOptions>`
        """
        return self._grid

    @grid.setter
    @class_sensitive(GridOptions)
    def grid(self, value):
        self._grid = value

    @property
    def max_range(self) -> Optional[int | float | Decimal]:
        """Maximum range which can be set using the navigator's handles. Defaults to
        :obj:`None <python:None>`.

        .. note::

          This setting is the opposite of
          :meth:`.min_range <Highcharts_Stock.options.axes.x_axis.XAxis.min_range>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_range

    @max_range.setter
    def max_range(self, value):
        self._max_range = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_decimals': as_dict.get('allowDecimals', None),
            'alternate_grid_color': as_dict.get('alternateGridColor', None),
            'angle': as_dict.get('angle', None),
            'breaks': as_dict.get('breaks', None),
            'categories': as_dict.get('categories', None),
            'ceiling': as_dict.get('ceiling', None),
            'class_name': as_dict.get('className', None),
            'date_time_label_formats': as_dict.get('dateTimeLabelFormats', None),
            'end_on_tick': as_dict.get('endOnTick', None),
            'events': as_dict.get('events', None),
            'floor': as_dict.get('floor', None),
            'grid_line_color': as_dict.get('gridLineColor', None),
            'grid_line_dash_style': as_dict.get('gridLineDashStyle', None),
            'grid_line_interpolation': as_dict.get('gridLineInterpolation', None),
            'grid_line_width': as_dict.get('gridLineWidth', None),
            'grid_z_index': as_dict.get('gridZIndex', None),
            'id': as_dict.get('id', None),
            'labels': as_dict.get('labels', None),
            'linked_to': as_dict.get('linkedTo', None),
            'margin': as_dict.get('margin', None),
            'max': as_dict.get('max', None),
            'max_padding': as_dict.get('maxPadding', None),
            'min': as_dict.get('min', None),
            'minor_grid_line_color': as_dict.get('minorGridLineColor', None),
            'minor_grid_line_dash_style': as_dict.get('minorGridLineDashStyle', None),
            'minor_grid_line_width': as_dict.get('minorGridLineWidth', None),
            'minor_tick_color': as_dict.get('minorTickColor', None),
            'minor_tick_interval': as_dict.get('minorTickInterval', None),
            'minor_tick_length': as_dict.get('minorTickLength', None),
            'minor_tick_position': as_dict.get('minorTickPosition', None),
            'minor_ticks': as_dict.get('minorTicks', None),
            'minor_tick_width': as_dict.get('minorTickWidth', None),
            'min_padding': as_dict.get('minPadding', None),
            'min_range': as_dict.get('minRange', None),
            'min_tick_interval': as_dict.get('minTickInterval', None),
            'offset': as_dict.get('offset', None),
            'opposite': as_dict.get('opposite', None),
            'pane': as_dict.get('pane', None),
            'panning_enabled': as_dict.get('panningEnabled', None),
            'plot_bands': as_dict.get('plotBands', None),
            'plot_lines': as_dict.get('plotLines', None),
            'reversed': as_dict.get('reversed', None),
            'reversed_stacks': as_dict.get('reversedStacks', None),
            'show_first_label': as_dict.get('showFirstLabel', None),
            'show_last_label': as_dict.get('showLastLabel', None),
            'soft_max': as_dict.get('softMax', None),
            'soft_min': as_dict.get('softMin', None),
            'start_of_week': as_dict.get('startOfWeek', None),
            'start_on_tick': as_dict.get('startOnTick', None),
            'tick_amount': as_dict.get('tickAmount', None),
            'tick_color': as_dict.get('tickColor', None),
            'tick_interval': as_dict.get('tickInterval', None),
            'tick_length': as_dict.get('tickLength', None),
            'tickmark_placement': as_dict.get('tickmarkPlacement', None),
            'tick_pixel_interval': as_dict.get('tickPixelInterval', None),
            'tick_position': as_dict.get('tickPosition', None),
            'tick_positioner': as_dict.get('tickPositioner', None),
            'tick_positions': as_dict.get('tickPositions', None),
            'tick_width': as_dict.get('tickWidth', None),
            'title': as_dict.get('title', None),
            'type': as_dict.get('type', None),
            'unique_names': as_dict.get('uniqueNames', None),
            'units': as_dict.get('units', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),
            'zoom_enabled': as_dict.get('zoomEnabled', None),

            'crosshair': as_dict.get('crosshair', None),
            'height': as_dict.get('height', None),
            'left': as_dict.get('left', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'show_empty': as_dict.get('showEmpty', None),
            'top': as_dict.get('top', None),
            'width': as_dict.get('width', None),

            'max_color': as_dict.get('maxColor', None),
            'min_color': as_dict.get('minColor', None),
            'stack_labels': as_dict.get('stackLabels', None),
            'stops': as_dict.get('stops', None),
            'tooltip_value_format': as_dict.get('tooltipValueFormat', None),

            'grid': as_dict.get('grid', None),
            'current_date_indicator': as_dict.get('currentDateIndicator', None),
            'max_range': as_dict.get('maxRange', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'currentDateIndicator': self.current_date_indicator,
            'grid': self.grid,
            'maxRange': self.max_range,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
