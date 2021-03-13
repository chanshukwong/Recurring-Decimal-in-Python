
import sys

def gcd(p:int, q:int):
	if p==0 or q==0:
		return p+q
	if q>p:
		return gcd(p, q%p)
	else:
		return gcd(p%q, q)

def DivisbleTimes(p:int, q:int):
	n = 0
	while p%q==0:
		p//=q
		n+=1
	return n

def FractionToDecimal(numerator:int,denominator:int):
	(quotient,numerator) = divmod(numerator,denominator)
	ans = str(quotient)
	if numerator==0:
		return ans

	ans+="."
	v = gcd(numerator,denominator)
	if v>1:
		numerator//=v
		denominator//=v

	for i in range(max(DivisbleTimes(denominator,2), DivisbleTimes(denominator,5))):
		(quotient,numerator) = divmod(numerator*10,denominator)
		ans+=str(quotient)
	if numerator==0:
		return ans

	ans+="("
	repeat = False
	Last_numerator = numerator
	while not repeat:
		(quotient,numerator) = divmod(numerator*10,denominator)
		ans+=str(quotient)
		if Last_numerator==numerator:
			repeat=True
	return ans+")"

def main():
	try:
		numerator = int(sys.argv[1])
		denominator = int(sys.argv[2])
	except IndexError as e:
		sys.exit("Missing arguments: python recurring.py numerator denominator")
	
	print(FractionToDecimal(numerator,denominator))

if __name__ == "__main__":
	main()
