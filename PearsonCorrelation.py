from math import sqrt

def main():
	# A dictionary of movie critics and their ratings of a small
	# set of movies
	critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
	 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
	 'The Night Listener': 3.0},
	'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
	 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
	 'You, Me and Dupree': 3.5},
	'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
	 'Superman Returns': 3.5, 'The Night Listener': 4.0},
	'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
	 'The Night Listener': 4.5, 'Superman Returns': 4.0,
	 'You, Me and Dupree': 2.5},
	'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
	'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
	'You, Me and Dupree': 2.0},
	'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
	'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
	'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}
	print sim_pearson(critics,'Lisa Rose','Gene Seymour')

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1
	
	# Find the number of elements
	n=len(si)
	
	# if they are no ratings in common, return 0
	if n==0: return 0
	
	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])
	
	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
	
	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
	
	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	
	if den==0: return 0
	
	r=num/den
	
	return r

if __name__ == "__main__":
    main()