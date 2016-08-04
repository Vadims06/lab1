from ciscoconfparse import CiscoConfParse
def main():
	cisco_ios = CiscoConfParse("cisco_ipsec.txt")
	crypto_map = cisco_ios.find_objects(r'crypto map')
	for child in crypto_map:
    		print child.text
     		for i in child.children:
             		print i.text
if __name__ =='__main__':
	main()
