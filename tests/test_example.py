from hexlet_pytest.example import reverse

def test_reverse():
	assert reverse('Hexlet') == 'telxeH'

def test_reverse_empty():
	assert reverse('') == ''
