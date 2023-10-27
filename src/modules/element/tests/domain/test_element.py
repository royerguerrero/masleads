"""Test for Element Aggregate Root"""

# Testing
import pytest

# Element
from src.modules.element.domain import Element, ElementStatusEnum
from src.modules.element.domain.business_rules import ElementStatusMustExits

# Shared
from src.modules.shared.domain import BusinessRuleException

# Build-ins
import random


@pytest.mark.unit
def test_create_element_happy_path():
    element_status = random.choice(list(ElementStatusEnum)).value
    element = Element.register(
        bulk_id=1,
        retries=0,
        status=element_status,
        name='Element 1',
    )

    assert isinstance(element, Element)
    assert element.id == 1
    assert element.retries == 0
    assert element.status == element_status
    assert element.name == 'Element 1'


@pytest.mark.unit
@pytest.mark.parametrize(
    'data,exception',
    [(
        {
            'bulk_id': 1,
            'retries': 0,
            'status': 404,
            'name': 'Element 1',
        },
        ElementStatusMustExits
    )]
)
def test_create_element_wrong_path(data, exception):
    with pytest.raises(BusinessRuleException) as exc_info:
        element = Element.register(**data)

    assert isinstance(exc_info.value.args[0], exception)
