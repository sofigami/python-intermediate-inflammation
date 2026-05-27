"""Tests for the Patient model."""

from inflammation.models import Patient

import numpy.testing as npt

def test_create_patient():

    name = 'Alice'
    weight = 50
    height = 1.8
    p = Patient(name=name, weight = weight, height=height)

    assert p.name == name
    assert p.weight == weight
    assert p.height == height

def test_compute_bmi():
    name = 'maria'
    weight = 60
    height = 1.6
    p = Patient(name=name,  height=height, weight = weight)

    result = p.get_body_mass_index()
    expected_result = 23.4375
    npt.assert_almost_equal(result, expected_result)






