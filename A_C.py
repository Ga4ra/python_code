def F(x):
	assert(x>=0);
	if x==0:
		return 1;
	s=1;
	while(x!=0):
		s=s*x;
		x=x-1;
	return s;

def A(n,a):
	return F(n)/F(n-a);

def C(n,c):
	return F(n)/(F(n-c)*F(c));

def main():
	big_num=int(raw_input("the big number:"))
	small_num=int(raw_input("the small number:"))

	flag=raw_input("A or C:");
	if flag=='A':
		res=A(big_num,small_num);

	elif flag=='C':
		res=C(big_num,small_num);

	print res;


if __name__ == '__main__':
	flag=1;
	while(flag):
		main();
		flag=int(raw_input("one more try?(1/0):"))