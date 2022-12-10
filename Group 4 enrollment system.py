from datetime import date
from datetime import datetime
import fileinput
import random
strdTF = 0  
print ("Senior High School Enrollment System")

mystrand = ['1. HUMSS','2. GAS','3. ABM','4. STEM','5. ICT']
for i in mystrand:
	print(i)

strand = True
while strand == True:
	choose = str(input("Choose Strand: "))
	if choose == '1':
		print("HUMSS")
		strd = 'HUMSS'
		strdTF = 10000.00
		break
	elif choose == '2':
		print("GAS")
		strd = 'GAS'
		strdTF = 9000.00 
		break
	elif choose == '3':
		print("ABM")
		strd = 'ABM'
		strdTF = 11000.00
		break
	elif choose == '4':
		print("STEM")
		strd = 'STEM'
		strdTF = 12000.00
		break
	elif choose == '5':
	    print("ICT")
	    strd = 'ICT'
	    strdTF = 10500.00
	    break
	else:
		print("Invalid Keyword")
		strand = True

info = True
while info == True:
	lname = str(input("Last Name: "))
	fname = str(input("First Name: "))
	mname = str(input("Middle Name: "))
	sffx = str(input("Suffix: "))
	sx = str(input('Sex: '))
	bdate = str(input("Birth Date MM / DD / YYYY: "))
	rlgn = str(input("Religion:­ "))
	ntnlty = str(input("Nationali­ty: "))
	hmddrss = str(input("Home Address: "))
	emailddrss = str(input("Email Address: "))
	cvlstts = str(input("Civil Status: "))
	lrn = str(input('LRN: '))
	print("Strand: ", strd)
	prvsvrggrd = str(input("Previous Average Grade: "))
	prvsschlnrll = str(input("Previous School Enroll: "))
	stdntcntctn = str(input("Student Contact Number: "))
	mothersmn = str(input("Mother's Maiden Name: "))
	mthrsoccup = str(input("Mother's Occupation: "))
	mthrscntcn = str(input("Mother's Contact Number: "))
	fathersnm = str(input("Father's Name: "))
	fthrsoccup = str(input("Father's Occupation: "))
	fthrscntcn = str(input("Father's Contact Number: "))
	guardnm = str(input("Guardian'­s Name: "))
	grdnoccup = str(input("Guardian'­s Occupation: "))
	grdncntcn = str(input("Guardian'­s Contact Number: "))
	print('='*65)
	a = True
	while a == True :
		a = str(input("Do you want to make changes? y/n: "))
		if a.lower() == 'y':
			strand = True
		elif a.lower() == 'n':
			a = False
			strand = False
			print('='*65) 
			cashP = True
			while cashP == True:
				print("Tuition Fee: ", strdTF)
				DPayment = input("Down Payment: ")
				if DPayment.isalpha():
					print("Invalid Input")
					cashP = True
					
				else:
					cashDP = strdTF - float(DPayment)
					
					if float(DPayment) >= 500:
					    print("Remaining Balance: ", cashDP)
					    today = date.today()
					    now = datetime.now()
					    current_time = now.strftime("%H:%M:%S")
					    print("Registered Date: ")
					    print("Date:",today,"Time:",current_time)
					    info = False
					    break
					else:
					    print("Your payment is not enough to reach the required amount of payment")
					    cashP = True
					
		else:
			print("Invalid keyword")
			a = True

print("YOUR RECEIPT")
print("="*65)
print("Student's name:", lname, fname, mname, sffx )
print ("Strand:", strd)
print("Sex:", sx)
print ("LRN:", lrn)
print ("Contact number:", stdntcntctn )
print ("Birth Date:", bdate)
print("Your student ID:", (random.randint(0,999999)) )
print("Registered Date: ")
print("Date:",today,"Time:",current_time)
print("Your remaining payment:", cashDP)
print ("You're now officially Enrolled")