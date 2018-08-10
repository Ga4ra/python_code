'''
		2018.8.10
'''

'''
pt1 = "attack at dawn"è.ascii1,

pt2 = "attack at dusk"è ascii2,

ascii1 XOR k = 6c73d5240a948c86981bc294814d = ct1

    k = ct1 XOR ascii1

èct2=k XOR ascii2=6c73d5240a948c86981bc2808548
'''
import string

def xor(sHex_1,sHex_2):
	ans='';
	j=0;

	for i in range(len(sHex_1)/2):
		temp=''
		temp+=hex(string.atoi(sHex_1[j:j+2],16)^string.atoi(sHex_2[j:j+2],16));
		temp=temp.replace('0x','')
		if len(temp)<2:
			temp='0'+temp
		ans+=temp;
		j+=2;
	return ans;


asc_1 ='61747461636b206174206461776e'
ct    ='6c73d5240a948c86981bc294814d'
asc_2 ='61747461636b206174206475736b'
k=''
ct_2=''
k=xor(asc_1,ct)
print k
ct_2=xor(asc_2,k)

print ct_2