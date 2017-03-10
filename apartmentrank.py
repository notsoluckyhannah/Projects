import pandas as pd
# this tool will calculate ranking scores for apartments. 
def scorecalc(trans,dep,twork,pam,am,rent,br):
	if trans <= 0.5:
		s=1
	elif trans > 0.5 and trans <= 1:
		s=2
	elif trans > 1 and trans <= 1.5:
		s=3
	elif trans > 1.5 and trans <= 2:
		s=4
	elif trans > 2: 
		s=5
	if dep <= 1000:
		s=s+1
	elif dep > 1000 and dep <= 1250:
		s=s+2
	elif dep > 1250 and dep <= 1500:
		s=s+3
	elif dep > 1500 and dep <= 1750:
		s=s+4
	elif dep > 1750: 
		s=s+5
	if twork <= 15:
		s=s+1
	elif twork > 15 and twork <= 25:
		s=s+2
	elif twork > 25 and twork <= 35:
		s=s+3
	elif twork > 35 and twork <= 45:
		s=s+4
	elif twork > 45: 
		s=s+5
	if pam >= 4:
		s=s+1
	elif pam < 4 and pam >= 3:
		s=s+2
	elif pam < 3 and pam >= 2:
		s=s+3
	elif pam < 2 and pam >= 1:
		s=s+4
	elif pam < 1 : 
		s=s+5
	if am >= 4:
		s=s+1
	elif am < 4 and am >= 3:
		s=s+2
	elif am < 3 and am >= 2:
		s=s+3
	elif am < 2 and am >= 1:
		s=s+4
	elif am < 1 : 
		s=s+5
	if br == 2 and rent < 1200:
		s=s+1
	elif br == 1 and rent >= 1200:
		s=s+5
	elif br == 2 and rent >= 1200 or rent < 1350:
		s=s+3
	elif br == 2 and rent >=1350:
		s=s+5
	elif br == 1 and rent < 1200:
		s=s+2
	return s

print 'Hello, this tool will help you select the aparment that is right for you.' 

print 'How many apartments are you viewing?'
 
apart_num = int(raw_input())
df=pd.DataFrame(columns=['Name','TransitDist','Deposit','TimeWork','PetAm','Am','Rent','Br','Score','OverallImpression'])
for i in range(apart_num):
	print 'Apartment Name:'
	name=str(raw_input())
	print 'Please enter distance from public transit.'
	trans = float(raw_input())
	print 'Please enter amount of deposit.'  
	dep = float(raw_input())
	print 'Please enter time to work.'
	twork = float(raw_input())
	print 'Please enter number of pet amenities.'  
	pam = int(raw_input())
	print 'Please enter number of amenities.'  
	am = int(raw_input())
	print 'Please enter rent amount.'
	rent=int(raw_input())
	print 'Please enter number bedrooms.'
	br=int(raw_input())
	print 'Please enter your overall impression 1 being the best, 5 being the worst'
	ovall=int(raw_input())
	score=scorecalc(trans,dep,twork,pam,am,rent,br)
	#print 'Score is: %s' %score 
	df.loc[i]=[name,trans,dep,twork,pam,am,rent,br,score,ovall]
print df.sort(['Score'])






