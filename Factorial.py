def F(x):
	assert(x>=0);
	if x==0:
		return 1;
	s=1;
	while(x!=0):
		s=s*x;
		x=x-1;
	return s;

def main():
	flag=1;
	while(flag):
		x=int(raw_input("input x for x!:"));
		res=F(x);
		print res;
		flag=int(raw_input("one more try?(1/0):"));

if __name__ == '__main__':
	main();