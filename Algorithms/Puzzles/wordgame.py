'''
permainan kata kata pas kecil. dimana tiap dua suku kata atau kata mati dipisahkan dengan suatu keyword pemisah.

1. misal keyword pemisah = 'f'

sample input :
hefellofo woforfold

sample output :
hello world


2. keyword pemisah = 'g'

sample input : 
nagamaga sagayaga agaqigil

sample output : 
nama saya aqil

'''

pemisah = input()
secret_msg = input()

secret_msg = secret_msg.replace(pemisah+"a", "")
secret_msg = secret_msg.replace(pemisah+"i", "")
secret_msg = secret_msg.replace(pemisah+"u", "")
secret_msg = secret_msg.replace(pemisah+"e", "")
secret_msg = secret_msg.replace(pemisah+"o", "")

print(secret_msg)