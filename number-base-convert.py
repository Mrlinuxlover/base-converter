print("\t"+"="*18+"\n\t[x y]\n\tx=number in 10base\n\ty=base number\n\te.x. 12 7\n\tprints 12 in 7base\n\t"+"="*18+"\n\t[x z y]\n\tx=number in zbase\n\ty=base to convert\n\te.x. 1100 2 11\n\tprints 1100(2) in \n\t10base and 12(10)\n\tin 11base")
while True:
	c=10
	print("\t"+"="*18)
	q=input("\t")
	if len(q.split(" "))==2:
	    a,b=q.split(" ")
	else:
	    if len(q.split(" "))==3:
	        a,c,b=q.split(" ")
	    else:
	        print("\tError")
	        continue
	if int(b)<2:
		print("\tError")
	else:
		e=0
		ers=0
		for i in range(1,int(len(str(a)))+1):
		    e=e+int(a[-i])*int(c)**(i-1)
		    if int(a[-i])>int(c):
		        ers=1
		if ers==1:
		    print("\tError")
		    continue
		else:
		    print("\t"+str(a)+" in "+str(c)+" base:")
		print("\t\t=> "+str(e))
		a,b,c=int(a),int(b),int(c)
		d=0
		s=0
		i=0
		g=e
		if e==0:
		    e=a
		while e//b!=0:
			d=d+(e%b)*10**i
			e=e//b
			i+=1
		d=d+(e%b)*10**i
		print("\t"+str(g)+" in "+str(b)+" base:\n\t\t=> "+str(d))