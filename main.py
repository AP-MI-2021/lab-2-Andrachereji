
def is_palindrome(n):
	copie=n
	rasturnat=0
	while (n > 0):
		rasturnat=rasturnat*10+n%10
		n=n//10
	if rasturnat==copie:
		return True
	return False
def test_is_palindrom():
	assert is_palindrome(121)==True
	assert is_palindrome(111) == True
	assert is_palindrome(221) == False
	assert is_palindrome(41) == False

def get_temp(n,unit1,unit2):
	if unit1=='K':
		if unit2=="C":
			return n-273.15
		else: return (n-273.15)*1.8000+32.00
	elif unit1=='C':
		if unit2=='K':
			return n+273.15
		else: return n*1.8000+32.00
	elif unit1=='F':
		if unit2=='C':
			return (n-32)//1.8000
		else: return (n-32)//1.8000 + 273.15
def test_get_temp():
	assert get_temp(300,'K','C')==26.850000000000023
	assert get_temp(30, 'C', 'F')==86.0
	assert get_temp(10,'C','K')!=100
	assert get_temp(250,'K','C')!=10


def main():
	while True:
		print('1.Determinare palindrom')
		print('2.Transformare temperaturi')
		print ('x.Iesire din program')
		optiune=input('Alege optiunea')
		if optiune=='1':
			nr=int(input('dati un numar: '))
			if is_palindrome(nr)==True:
				print('numarul este palindrom')
			else:
				print('numarul nu este palindrom')
		elif optiune=='2':
			temperatura_initiala= float(input('Dati temperatura'))
			scara1= str(input('Dati prima scara'))
			scara2= str(input('Dati scara in care vreti sa transformati'))
			temperatura_finala= get_temp(temperatura_initiala,scara1,scara2)
			print(f'Temperatura finala este de {temperatura_finala} grade {scara2}')

		elif optiune=='x':
			break
test_is_palindrom()
test_get_temp()
main()