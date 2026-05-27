"""Tests for the Patient model."""

from inflammation.models import Patient

def test_create_patient():

    name = 'Alice'
    weight = 50
    height = 1.8
    p = Patient(name=name, weight = weight, height=height)

    assert p.name == name
    assert p.weight == weight
    assert p.height == height
