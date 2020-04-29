import pytest

from ubbi_dubbi import translate_to_Ubbi_dubbi_1, translate_to_Ubbi_dubbi_2


def test_ubbi_dubbi_appraoch_1():
    assert translate_to_Ubbi_dubbi_1('octopus') == 'uboctubopubus'
    assert translate_to_Ubbi_dubbi_1('elephant') == 'ubelubephubant'
    assert translate_to_Ubbi_dubbi_1('soap') == 'suboubap'


def test_ubbi_dubbi_appraoch_2():
    assert translate_to_Ubbi_dubbi_2('octopus') == 'uboctubopubus'
    assert translate_to_Ubbi_dubbi_2('elephant') == 'ubelubephubant'
    assert translate_to_Ubbi_dubbi_2('soap') == 'suboubap'
