import csv, os, datetime, time, stdiomask
from termcolor import colored
from prettytable import from_csv, PrettyTable

#fontcolors using termcolor
class fontcolor():
	def green(string):
		return colored(string, "green", attrs=['bold'])
	def white(string):
		return colored(string, "white", attrs=['bold'])
	def yellow(string):
		return colored(string, "yellow", attrs=['bold'])
	def cyan(string):
		return colored(string, "cyan", attrs=['bold'])
	def red(string):
		return colored(string, "red", attrs=['bold'])
	def blue(string):
		return colored(string, "blue", attrs=['bold'])

#smb ==> symbols
class smb:
	WARN = fontcolor.red(" [-] ")
	DONE = fontcolor.green(" [+] ")
	INPUT = fontcolor.cyan(" [»] ")
	INFO = fontcolor.yellow(" [!] ")
	ARROW = fontcolor.cyan(" > ")

banr = '''
            ╔═══╗   ╔═══   ╔═╗     ACADEMIC    
            ║═══║   ║═══   ╚═╗     EVALUATION
            ║   ║   ╚═══   ╚═╝     SYSTEM
        '''

def banner():
	print(fontcolor.cyan(banr))

class num:
	one = fontcolor.yellow("[1] ")
	two = fontcolor.yellow("[2] ")
	three = fontcolor.yellow("[3] ")
	four = fontcolor.yellow("[4] ")
	five = fontcolor.yellow("[5] ")
	six = fontcolor.yellow("[6] ")
def border_msg(msg):
    row = len(msg)
    m = ''.join(['        +'] + ['-' *row] + ['+'])
    h = fontcolor.cyan(m)
    result= h + '\n' + fontcolor.cyan("        |") + fontcolor.white(msg) + fontcolor.cyan("|") + '\n' + h
    print((result))
choice_one = fontcolor.white("Add New Student")
choice_two = fontcolor.white("Search Student")
choice_three = fontcolor.white("Update Student")
choice_four = fontcolor.white("Delete Student")
choice_five = fontcolor.white("Project Development Team")
choice_six = fontcolor.white("Exit")

#choice menu 
def display_menu():
	banner()
	border_msg(" Welcome To Academic Evaluation System ! ")
	print("\n" + smb.ARROW + fontcolor.cyan("CHOOSE ANY OPTION :") + "\n")
	print(smb.ARROW + num.one + choice_one)
	print(smb.ARROW + num.two + choice_two)
	print(smb.ARROW + num.three + choice_three)
	print(smb.ARROW + num.four + choice_four)
	print(smb.ARROW + num.five + choice_five)
	print(smb.ARROW + num.six + choice_six)
raw_database = 'raw_data.csv'
student_database = 'students.csv'

#function for clearing screen
def clr_scr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#press enter to continue message
def continue_msg():
	input("\n" + smb.ARROW + fontcolor.cyan("Press Enter To Continue : "))
	clr_scr()


# main-function-1
#function to add students in database
def add_student():
	clr_scr()
	print("\n")
	border_msg(" Add a New Student's Information To Database ")
	print("\n")
	paswrd = stdiomask.getpass( smb.ARROW + fontcolor.cyan("Enter password to continue : "))
	if(paswrd == 'Admin@123') :
		print("\n")
		stu_name = input(smb.DONE + fontcolor.green("Student's Name : "))
		stu_father = input(smb.DONE + fontcolor.green("Father's Name : "))
		stu_sem = input(smb.DONE + fontcolor.green("Semester (1-8) : "))
		roll_num = input(smb.DONE + fontcolor.green("Roll No : "))
		stu_dob = input(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : "))
		stu_sex = input(smb.DONE + fontcolor.green("Sex (M/F/T) : "))
		phone_num = input(smb.DONE + fontcolor.green("Contact No. (+91) : "))
		marks1 = input(smb.DONE + fontcolor.green("CO marks : "))
		marks2 = input(smb.DONE + fontcolor.green("DAA marks : "))
		marks3 = input(smb.DONE + fontcolor.green("AUTOMATA marks : "))
		marks4 = input(smb.DONE + fontcolor.green("MICROPROCESSOR marks : "))
		marks5 = input(smb.DONE + fontcolor.green("JAVA marks : "))
		student_data = []
		student_data.append(stu_name)
		student_data.append(stu_father)
		student_data.append(stu_sem)
		student_data.append(roll_num)
		student_data.append(stu_dob)
		student_data.append(stu_sex)
		student_data.append(phone_num)
		student_data.append(marks1)
		student_data.append(marks2)
		student_data.append(marks3)
		student_data.append(marks4)
		student_data.append(marks5)
		avg=(int(marks1)+int(marks2)+int(marks3)+int(marks4)+int(marks5))/5
		student_data.append(avg)
		if avg >= 95 :
			g='A+'
		elif avg >=  90 and avg<= 94.9 :
			g='A'
		elif avg >=  80 and avg<= 89.9 :
			g='B'
		elif avg >=  70 and avg<= 79.9 :
			g='C'
		elif avg >=  60 and avg<= 69.9 :
			g='D'
		elif avg >=  40 and avg<= 59.9 :
			g='E'
		elif avg <40 :
			g='Fail'
		student_data.append(g)
		header = ['Student','Father','Semester','Roll No','DOB','Sex(M/F/T)','Contact','CO','DAA','AUTOMATA','MICROPROCESSOR','JAVA','AVERAGE','GRADE']
		with open(raw_database, 'a') as f:
			writer = csv.writer(f)
			writer.writerow(i for i in header)
			writer.writerows([student_data])
			f.close()
		
	#removing duplicate headers and writing new file 'students.csv'
		inFile = open(raw_database, 'r')
		outFile = open(student_database, 'w')
		listLines = []
		for line in inFile:
			if line in listLines:
				continue
			else:
				outFile.write(line)
				listLines.append(line)
		outFile.close()
		inFile.close()
		try:
			x = PrettyTable()
			x.field_names = header
			x.add_row([student_data[0],student_data[1],student_data[2],student_data[3],student_data[4],student_data[5],student_data[6],student_data[7],student_data[8]
				,student_data[9],student_data[10],student_data[11],student_data[12],student_data[13]])
			print("\n" + smb.DONE + fontcolor.green("Quick Overview :"))
			print(fontcolor.white(x))
			print("\n" + smb.DONE + fontcolor.green("Data Saved Successfully !"))
		except Exception:
			print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check Your Code !"))
		finally:
			continue_msg()
	else:
		print("\n" + smb.WARN + fontcolor.red("ERROR ! Wrong Password !"))
		continue_msg()	

# main-function-2
#function to search student with roll num
def search_student():
	clr_scr()
	print("\n")
	border_msg(" Search For a Student Inside Database ")
	roll = input("\n" + smb.DONE + fontcolor.green("Enter Roll No. To Search : "))
	try:
		fd = open(student_database, "r", encoding="utf-8")
		reader = csv.reader(fd)
		for row in reader:
			if len(row) > 0:
				if roll == row[3]:
					print("\n")
					print(fontcolor.green("\t----- STUDENT FOUND -----") + "\n")
					print(smb.DONE + fontcolor.green("Student's Name : ") + row[0])
					print(smb.DONE + fontcolor.green("Father's Name : ") + row[1])
					print(smb.DONE + fontcolor.green("Semester : ") + row[2])
					print(smb.DONE + fontcolor.green("Roll No : ") + row[3])
					print(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : ") + row[4])
					print(smb.DONE + fontcolor.green("Sex (M/F/T) : ") + row[5])
					print(smb.DONE + fontcolor.green("Phone No : ") + row[6])
					print(smb.DONE + fontcolor.green("CO : ") + row[7])
					print(smb.DONE + fontcolor.green("DAA : ") + row[8])
					print(smb.DONE + fontcolor.green("AUTOMATA : ") + row[9])
					print(smb.DONE + fontcolor.green("MICROPROCESSOR : ") + row[10])
					print(smb.DONE + fontcolor.green("JAVA : ") + row[11])
					print(smb.DONE + fontcolor.green("AVERAGE : ") + row[12])
					print(smb.DONE + fontcolor.green("GRADE : ") + row[13])
					break
		else:
		    print("\n" + smb.WARN + fontcolor.red("Student Not Found In Our Database !!!"))
	except FileNotFoundError:
		print("\n" + smb.WARN + fontcolor.red("No Records To Search !"))
	finally:
		continue_msg()

#main-function-3
#function to update student data
def update_student():
	clr_scr()
	print("\n")
	border_msg(" Update Student's Record In Database ")
	paswrd = stdiomask.getpass("\n" + smb.ARROW + fontcolor.cyan("Enter password to continue : "))
	if(paswrd == 'Admin@123') :
		roll_num = input("\n" + smb.DONE + fontcolor.green("Enter Roll No. To Update : "))
		try:
			index_student = None
			updated_data = []
			fe = open(student_database, "r", encoding="utf-8")
			reader = csv.reader(fe)
			counter = 0
			for row in reader:
				if len(row) > 0:
					if roll_num == row[3]:
						index_student = counter
						print("\n" + fontcolor.green('\t----- RECORD FOUND -----') + "\n")
						print(smb.DONE + fontcolor.cyan("Student's Name =>"), row[0])
						student_data = []
						print("\n")
						new_stu_name = input(smb.DONE + fontcolor.green("Enter Student's New Name : "))
						new_stu_father = input(smb.DONE + fontcolor.green("Enter Father's New Name : "))
						new_stu_sem = input(smb.DONE + fontcolor.green("Enter New Semester (1-10) : "))
						new_roll_num = input(smb.DONE + fontcolor.green("Enter New Roll No : "))
						new_stu_dob = input(smb.DONE + fontcolor.green("Enter New DOB (DD/MM/YYYY) : "))
						new_stu_sex = input(smb.DONE + fontcolor.green("Enter New Sex (M/F/T) : "))
						new_phone_num = input(smb.DONE + fontcolor.green("Enter New Phone No (+91) : "))
						new_marks1 = input(smb.DONE + fontcolor.green("CO marks : "))
						new_marks2 = input(smb.DONE + fontcolor.green("DAA marks : "))
						new_marks3 = input(smb.DONE + fontcolor.green("AUTOMATA marks : "))
						new_marks4 = input(smb.DONE + fontcolor.green("MICROPROCESSOR marks : "))
						new_marks5 = input(smb.DONE + fontcolor.green("JAVA marks : "))
						student_data.append(new_stu_name)
						student_data.append(new_stu_father)
						student_data.append(new_stu_sem)
						student_data.append(new_roll_num)
						student_data.append(new_stu_dob)
						student_data.append(new_stu_sex)
						student_data.append(new_phone_num)
						student_data.append(new_marks1)
						student_data.append(new_marks2)
						student_data.append(new_marks3)
						student_data.append(new_marks4)
						student_data.append(new_marks5)
						avg=(int(new_marks1)+int(new_marks2)+int(new_marks3)+int(new_marks4)+int(new_marks5))/5
						student_data.append(avg)
						if avg >= 95 :
							g='A+'
						elif avg >=  90 and avg<= 94.9 :
							g='A'
						elif avg >=  80 and avg<= 89.9 :
							g='B'
						elif avg >=  70 and avg<= 79.9 :
							g='C'
						elif avg >=  60 and avg<= 69.9 :
							g='D'
						elif avg >=  40 and avg<= 59.9 :
							g='E'
						elif avg <40 :
							g='Fail'
						student_data.append(g)
						updated_data.append(student_data)
					else:
						updated_data.append(row)
					counter+=1
		except FileNotFoundError:
			print("\n" + smb.WARN + fontcolor.red("No Records To Update !"))

		#writing update to csv file
		if index_student is not None:
			with open(student_database, "w", encoding="utf-8") as f:
				writer = csv.writer(f)
				writer.writerows(updated_data)
				print("\n" + smb.DONE + fontcolor.green("Data Updated Successfully ! "))
				continue_msg()
		else:
			print("\n" + smb.WARN + fontcolor.red("Student Not Found In Our Database !!!"))
			continue_msg()
	else:
		print("\n" + smb.WARN + fontcolor.red("ERROR ! Wrong Password !"))
		continue_msg()
        
# main-function-4
#function to delete student record
def delete_student():
	clr_scr()
	print("\n")
	border_msg(" Delete Student's Record From Database ")
	paswrd = stdiomask.getpass("\n" + smb.ARROW + fontcolor.cyan("Enter password to continue : "))
	if(paswrd == 'Admin@123') :
		roll = input("\n" + smb.WARN + fontcolor.red("Enter Roll No. To Delete : "))
		try:
			student_found = False
			updated_data = []
			ff = open(student_database, "r", encoding="utf-8")
			reader = csv.reader(ff)
			counter = 0
			for row in reader:
				if len(row) > 0:
					if roll != row[3]:
						updated_data.append(row)
						counter += 1
					else:
						student_found = True
		except FileNotFoundError:
			print("\n" + smb.WARN + fontcolor.red("No Records To Delete !"))
		if student_found is True:
			with open(student_database, "w", encoding="utf-8") as f:
				writer = csv.writer(f)
				writer.writerows(updated_data)
				print("\n" + smb.DONE + fontcolor.green("Roll No. Deleted Successfully"))
				continue_msg()
		else:
			print("\n" + smb.WARN + fontcolor.red("Roll No. Not Found In Our Database !!!"))
			continue_msg()
	else :
		print("\n" + smb.WARN + fontcolor.red("ERROR ! Wrong Password !"))
		continue_msg()

#main-function-5
#about team
def about_me():
	clr_scr()
	print("\n")
	border_msg(" Project Development Team ")
	#print("\n")
	z = PrettyTable()
	field_1 = fontcolor.green("Team Member")
	field_2 = fontcolor.green("Designation")
	field_3 = fontcolor.green("Semester")
	z.field_names = [field_1,field_2,field_3]
	z.add_row(['Yash Chauhan', 'Project Developer','4th'])
	print(z)
	continue_msg()

#looping the whole program
while True:
    display_menu()
    choice = input("\n" + smb.ARROW + fontcolor.cyan("Enter Your Choice : "))
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
    	about_me()
    elif  choice == '6':
    	clr_scr()
    	border_msg(" EXITING ")
    	print("\n" + smb.DONE + fontcolor.green("Thanks For Using My Academic Evaluation System"))
    	time.sleep(2)
    	quit()
    else:
    	   print("\n" + smb.WARN + fontcolor.red("Please, Enter a Valid Input !"))
    	   break
