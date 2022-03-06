def zipcodes(fromx="79-900",tox="80-155"):
	fromx_sep = fromx.replace("-", "")
	tox_sep = tox.replace("-", "")
	fromx_sepint = int(fromx_sep)
	tox_sepint = int(tox_sep)
	while fromx_sepint != tox_sepint :
			fromx_sepints = fromx_sepint
			if fromx_sepints == 79900:
				fromx_sepint = fromx_sepint + 1
			else:
				fromx_sepints = str(fromx_sepints)
				print(fromx_sepints[:2] + "-" + fromx_sepints[2:])
				fromx_sepint = fromx_sepint + 1
zipcodes()