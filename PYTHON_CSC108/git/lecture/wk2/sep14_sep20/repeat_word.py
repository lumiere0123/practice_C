def repeat_word(word, repeat_count):
	''' (str, int) -> str
	Return word repeated repeat_count times.
	
	>>> repeat_word('cat', 5)
	'catcatcatcatcat'
	>>> repeat_word('class ', 3)
	'class class class '
	>>> repeat_word('cat', 0)
	''
	>>> repeat_word('', 5)
	''
	'''
  return word * repeat_count
