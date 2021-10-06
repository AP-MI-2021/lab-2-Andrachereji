
def is_palindrome(n):
	'''
	verifica daca un numar este palindrom
	:param n: un numar
	:return: returneaza True daca numarul e palindrom si False in caz contrar
	'''
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
	'''
	Transforma o temepratura dintr-o unitate in alta
	:param n: temperatura pe care dorim sa o transformam
	:param unit1: unitatea temperaturii initiale
	:param unit2: unitatea temperaturii modificate
	:return:
	'''
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
def get_cmmmc_doua_numere(a,b):
	p=a*b
	while a!=b:
		if a>b:
			a=a-b
		else:
			b=b-a
	return p//a
def get_cmmmc(lst):
	'''
	se calculeaza cel mai mic multiplu comun dintr-un sir de numere
	:param lst: sirul de numere
	:return: cel mai mic multiplu comun
	'''
	cmmmc=lst[0]
	i=1
	for i in range(len(lst)):
		cmmmc=get_cmmmc_doua_numere(cmmmc,lst[i])
	return cmmmc
def test_get_cmmmc():
	assert get_cmmmc([8,12,24])==24
	assert get_cmmmc([8,12,20])==120
	assert get_cmmmc([10,3,5])!=5
	assert get_cmmmc([50,23,14])!=10



def main():
	while True:
		print('1.Determinare palindrom')
		print('2.Transformare temperaturi')
		print('3.Cel mai mic multiplu comun')
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
		elif optiune=='3':
			numere_str = input('dati numerele separate prin spatiu')
			numere_str_lst = numere_str.split(' ')
			numere_int_lst = []
			for nr_str in numere_str_lst:
				numere_int_lst.append(int(nr_str))
			cmmmc = get_cmmmc(numere_int_lst)
			print(f'Cel mai mare multiplu comun al listei este {cmmmc}')

		elif optiune=='x':
			break
test_is_palindrom()
test_get_temp()
test_get_cmmmc()
if __name__ == '__main__':
    main()
