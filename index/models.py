from django.db import models
import os

# Create your models here.

class Journal(models.Model):
	journal_name 		= models.CharField(verbose_name = "Journal", max_length=100)
	abbr_title			= models.CharField(verbose_name = "Abbr. Title", max_length=100, blank=True, default="N/A")
	subject				= models.CharField(verbose_name = "subject", max_length=30, null= True, blank=True)
	issn_print 			= models.CharField(verbose_name = "ISSN Print", max_length=20 )
	issn_online			= models.CharField(verbose_name = "ISSN Online", max_length=20 )
	frequency			= models.CharField(verbose_name = "Frequency", max_length=20, blank=True, default="N/A")
	chief_editor		= models.CharField(verbose_name = "chief editor", max_length=50)
	origin_country		= models.CharField(verbose_name = "Origin", max_length=20,  blank=True, default="N/A")
	language			= models.CharField(verbose_name = "Language", max_length=20, blank=True, default="N/A")
	publisher			= models.CharField(verbose_name = "Publisher", max_length=50, blank=True, default="N/A")
	journal_info		= models.TextField(verbose_name = "Info", max_length=2000)
	indexing_factor		= models.CharField(verbose_name = "Index Factor", max_length=20)
	journal_cover		= models.ImageField(upload_to ='journals/', verbose_name = "Cover")
	journal_thumb		= models.ImageField(upload_to ='journals/', verbose_name = "Thumbnail")
	
	def __str__(self):
		return self.journal_name


class Volume(models.Model):
	journal 			= models.ForeignKey(Journal, on_delete=models.CASCADE)
	volume_name			= models.CharField(verbose_name = "Volume name", max_length=50)
	volume_year			= models.PositiveIntegerField(verbose_name="Year")
	issue_name			= models.CharField(verbose_name="Issue", max_length=20)

	def __str__(self):
		return self.volume_name

class Article(models.Model):
	volume 				= models.ForeignKey(Volume, on_delete=models.CASCADE)
	article_type		= models.CharField(verbose_name="Type", max_length=40)
	article_name 		= models.CharField(verbose_name = "Article", max_length=100)
	author				= models.CharField(verbose_name = "Author", max_length=50)
	article 			= models.FileField(upload_to='articles/')
	publish_date		= models.DateField()

	def __str__(self):
		return self.article_name

class Editor(models.Model):
	journal 			= models.ForeignKey(Journal, on_delete=models.CASCADE )
	designation 		= models.CharField(verbose_name="Designation", max_length=50)
	editor_name 		= models.CharField(verbose_name="Name", max_length=50)
	editor_info 		= models.CharField(verbose_name="Info", max_length=1000)
	profile				= models.ImageField(upload_to='editors/', blank=True)

	def __str__(self):
		return self.editor_name


#Featured Articles
def validate_only_ten(obj):
    model = obj.__class__
    if (model.objects.count() > 9 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 10 %s instance" % model.__name__)

class FeaturedArticle(models.Model):
	article_name 		= models.CharField(verbose_name = "Article", max_length=100)
	author				= models.CharField(verbose_name = "Author", max_length=50)
	article 			= models.FileField(upload_to='features_articles/', blank=True)
	publish_date		= models.DateField()

	def clean(self):
		validate_only_ten(self)

	def __str__(self):
		return self.article_name

class TopEditor(models.Model):
	designation 		= models.CharField(verbose_name="Designation", max_length=50)
	editor_name 		= models.CharField(verbose_name="Name", max_length=50)
	editor_info 		= models.CharField(verbose_name="Info", max_length=1000)
	profile				= models.ImageField(upload_to='editors/', blank=True)

	def __str__(self):
		return self.editor_name

	def clean(self):
		validate_only_ten(self)

#Processing Fees
class JournalFee(models.Model):
	journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
	usd 	= models.PositiveIntegerField(verbose_name="USD")
	inr 	= models.PositiveIntegerField(verbose_name="INR")

class MemberIn(models.Model):
	company_logo = models.ImageField(upload_to='membersin/', blank=True)
	company_name = models.CharField(verbose_name='Company name', blank=True, max_length=200)