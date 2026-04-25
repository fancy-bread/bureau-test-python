from measure import Measure


def test_metric_to_imperial():
    m = Measure()
    assert abs(m.metric_to_imperial(1.60934) - 1.0) < 0.0001


def test_imperial_to_metric():
    m = Measure()
    assert abs(m.imperial_to_metric(1.0) - 1.60934) < 0.0001


def test_roundtrip():
    m = Measure()
    assert abs(m.imperial_to_metric(m.metric_to_imperial(10.0)) - 10.0) < 0.0001
