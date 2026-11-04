"""Heat index calculations based on the National Weather Service procedure."""

import math


def calculate_heat_index(temperature_f: float, humidity: float) -> float:
    """Return heat index in °F using the NWS simple formula and Rothfusz regression.

    The NWS procedure first averages the simple result with air temperature.
    If that result is below 80°F, it is returned. Otherwise the Rothfusz
    regression is used, with the documented dry and humid air adjustments.
    """
    temp = float(temperature_f)
    rh = float(humidity)
    if not 0 <= rh <= 100:
        raise ValueError("Relative humidity must be between 0 and 100 percent.")

    simple = 0.5 * (temp + 61.0 + ((temp - 68.0) * 1.2) + (rh * 0.094))
    simple = (simple + temp) / 2.0
    if simple < 80.0:
        return simple

    hi = (
        -42.379
        + 2.04901523 * temp
        + 10.14333127 * rh
        - 0.22475541 * temp * rh
        - 0.00683783 * temp**2
        - 0.05481717 * rh**2
        + 0.00122874 * temp**2 * rh
        + 0.00085282 * temp * rh**2
        - 0.00000199 * temp**2 * rh**2
    )

    if rh < 13 and 80 <= temp <= 112:
        adjustment = ((13 - rh) / 4) * math.sqrt((17 - abs(temp - 95)) / 17)
        hi -= adjustment
    elif rh > 85 and 80 <= temp <= 87:
        hi += ((rh - 85) / 10) * ((87 - temp) / 5)
    return hi


def risk_category(heat_index_f: float) -> str:
    """Return a general NWS heat-index category using non-overlapping bounds."""
    if heat_index_f < 80:
        return "Below caution"
    if heat_index_f < 90:
        return "Caution"
    if heat_index_f < 103:
        return "Extreme Caution"
    if heat_index_f < 125:
        return "Danger"
    return "Extreme Danger"
