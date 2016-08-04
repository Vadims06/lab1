from ciscoconfparse import CiscoConfParse

def main():
	cisco_ios = CiscoConfParse("cisco_ipsec.txt")
	crypto_map = cisco_ios.find_objects(r'crypto map')
	for child in crypto_map:
     		print child.text
     		for i in child.children:
             		if "AES" in i.text:
                     		print i.text
if __name__ == "__main__":
    main()
'''
crypto map CRYPTO 10 ipsec-isakmp
 set transform-set AES-SHA
crypto map CRYPTO 20 ipsec-isakmp
 set transform-set AES-SHA
crypto map CRYPTO 30 ipsec-isakmp
 set transform-set AES-SHA
crypto map CRYPTO 40 ipsec-isakmp
 set transform-set AES-SHA
crypto map CRYPTO 50 ipsec-isakmp 
'''
