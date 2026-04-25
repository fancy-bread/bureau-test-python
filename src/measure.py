KM_PER_MILE = 1.60934


class Measure:
    def metric_to_imperial(self, km: float) -> float:
        return km / KM_PER_MILE

    def imperial_to_metric(self, miles: float) -> float:
        return miles * KM_PER_MILE
