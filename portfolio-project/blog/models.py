from django.db import models

# Create your models here for Blog
# title
# publish Date
# image
# body || summary
class Blog(models.Model):
	title = models.CharField(max_length=225)
	pub_date = models.DateTimeField()
	image = models.ImageField('images/')
	body = models.TextField(max_length=200)

	def summary(self):
		return self.body[:100]
	
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e, %Y')

	def __str__(self):
		return self.title
		



# create blog app to settings





#create migrations



# migrate



# add app to the admin page
