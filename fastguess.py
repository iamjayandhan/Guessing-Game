# Sequential search based guess function 
def guesser(): 
	if not hasattr(guesser, "value"):
		guesser.value = 2
	else:
		guesser.value += 1
	return guesser.value
	
# Fast and efficient guess function 
# Any idea what algorithm this is? 

def fguesser(resp):
	if not hasattr(fguesser, "left"):
		fguesser.left = 2
		fguesser.right = 100
	else: 
		if resp == "l" or resp == "L":
			fguesser.right = fguesser.mid - 1
		else:
			fguesser.left = fguesser.mid + 1 
	
	fguesser.mid = (fguesser.left + fguesser.right) // 2
	return fguesser.mid
