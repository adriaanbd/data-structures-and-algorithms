def group_by(sequence, key_func=None):
	d = dict()
	if key_func is None:
		key_func = lambda x: x
	for item in sequence:
		key = key_func(item)
		d[key] = d.get(key, [])
		d[key].append(item)
	return d
