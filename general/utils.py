#from restaurants.models import RestaurantReview
from .functions import *

def updateRestaurantReview(restaurantObj, review):
	try:
		r_review = RestaurantReview.objects.get(restaurant=review.restaurant)
		if r_review.reviewed_people_no == 0:
			r_review.food        		 = review.food
			r_review.price       		 = review.price

		else:
			r_review.food        		 = round( ((r_review.food  + review.food) / 2.0), 1)
			r_review.price       		 = round(((r_review.price + review.price) / 2.0), 1)

		r_review.reviewed_people_no += 1
		result = sum([r_review.food, r_review.price, r_review.service, r_review.environment])/4.0
		r_review.average             = round(result, 1)
		r_review.status              = getReviewStatus(r_review.average)
		r_review.star2			     = r_stars[1]
		r_review.star3	             = r_stars[2]
 		r_review.save()
		return True
	except:
		return False


