IMP_TABLE = [0, 20, 50, 90, 130 ,170, 220, 270, 320, 370, 430, 500, 600, 750, 900, 1100, 1300, 1500, 1750, 2000, 2250, 2500, 3000, 3500, 4000, 1000000]

def score_to_imps(score):
	"Given an integer score, it is tranformed to IMPs via IMP_TABLE, mantaing the same sign of score (positive/negative)"
	i = 0
	while score > IMP_TABLE[i]:
		i += 1
	
	if score > 0:
		return i
	else
		return -i
