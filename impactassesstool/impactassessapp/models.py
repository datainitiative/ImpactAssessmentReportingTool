from django.db import models

# Import from general utilities
from util import *

# Choices
year_choices_list = [(None,"---------"),(0,"No Data")]
for i in range (datetime.datetime.now().year,1899,-1):
	year_choices_list.append((i,str(i)))
YEAR_CHOICES = tuple(year_choices_list)

# Ref Table Models
# Organization Stage
class OrganizationStage(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = OrganizationStage.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return OrganizationStage.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = OrganizationStage.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return OrganizationStage.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'organization_stage'

# Report Due Type
class ReportDueType(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = ReportDueType.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return ReportDueType.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = ReportDueType.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return ReportDueType.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'report_due_type'
		
# Report Status
class ReportStatus(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = ReportStatus.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return ReportStatus.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = ReportStatus.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return ReportStatus.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'report_status'
		
# Investment Category		
class InvestmentCategory(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = InvestmentCategory.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return InvestmentCategory.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = InvestmentCategory.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return InvestmentCategory.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'investment_category'


# Investment Type
class InvestmentType(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	category = models.ForeignKey('InvestmentCategory', null=True)

	def __unicode__(self):
		return unicode("%s: %s" % (self.category.name,self.name))
	
	def previous(self):
	    try:
	        previous_records = InvestmentType.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return InvestmentType.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = InvestmentType.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return InvestmentType.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'investment_type'
		
# Geography
class Geography(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = Geography.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return Geography.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = Geography.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return Geography.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'geography'

# ThematicArea
class ThematicArea(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = ThematicArea.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return ThematicArea.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = ThematicArea.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return ThematicArea.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'thematic_area'

# Beneficiary Level Indicator
class BeneficiaryLevelIndicator(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	organization = models.ForeignKey('Organization')

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = BeneficiaryLevelIndicator.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return BeneficiaryLevelIndicator.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = BeneficiaryLevelIndicator.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return BeneficiaryLevelIndicator.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'beneficiary_level_indicator'
		
# Organization Level Indicator
class OrganizationLevelIndicator(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	organization = models.ForeignKey('Organization')

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = OrganizationLevelIndicator.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return OrganizationLevelIndicator.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = OrganizationLevelIndicator.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return OrganizationLevelIndicator.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'organization_level_indicator'
		
# M&E Capacity
class MECapacity(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = MECapacity.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return MECapacity.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = MECapacity.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return MECapacity.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'me_capacity'
		
class IsIndicatorMet(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = IsIndicatorMet.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return IsIndicatorMet.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = IsIndicatorMet.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return IsIndicatorMet.objects.get(id=next_id)
	    except:
	        return None	

	class Meta:
		db_table = u'is_indicator_met'

# Main Models
# Organization
class Organization(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500, blank=True, null=True)
	est_date = models.IntegerField(verbose_name='Established Date', choices=YEAR_CHOICES, null=True)
	org_stage = models.ForeignKey('OrganizationStage', null=True)
	org_stage_note = models.CharField(max_length=200, null=True, blank=True)
		
	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = Organization.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return Organization.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = Organization.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return Organization.objects.get(id=next_id)
	    except:
	        return None
		
	def _get_str_org_stage(self):
		if self.org_stage_note:
			return "%s (%s)" % (self.org_stage.name if self.org_stage else "", self.org_stage_note)
		else:
			return "%s" % self.org_stage.name if self.org_stage else ""
				
	class Meta:
		db_table = u'organization'
		
# Report Due Date
class ReportDueDate(models.Model):
#	id = models.IntegerField(primary_key=True)
	date = models.DateField()
	report_due_type = models.ForeignKey('ReportDueType', null=True)

	def __unicode__(self):
		return unicode("%s (%s);" % (self.date.strftime("%m/%d/%Y"),self.report_due_type.name))

	class Meta:
		db_table = u'report_due_date'

class Investment(models.Model):
#    id = models.IntegerField(primary_key=True)
	organization = models.ForeignKey('Organization')
	date_of_award = models.DateField(blank=True, null=True)
	report_due_date = models.ManyToManyField('ReportDueDate')
	report_status = models.ForeignKey('ReportStatus', null=True)
	amount = models.IntegerField(blank=True, null=True)
	amount_note = models.TextField(blank=True, null=True)
	investment_type = models.ManyToManyField('InvestmentType')
	geography = models.ForeignKey('Geography', null=True)
	geography_note = models.CharField(max_length=200, blank=True, null=True)
	thematic_area = models.ForeignKey('ThematicArea', null=True)
	cost_effectiveness = models.CharField(max_length=500, blank=True, null=True)
#	beneficiary_level_indicator = models.ManyToManyField('BeneficiaryLevelIndicator', null=True)
#	organization_level_indicator = models.ManyToManyField('OrganizationLevelIndicator', null=True)
	beneficiary_level_indicator = models.TextField(blank=True, null=True)
	organization_level_indicator = models.TextField(blank=True, null=True)
	me_capacity = models.ForeignKey('MECapacity', null=True)
	me_capacity_note = models.CharField(max_length=200, blank=True, null=True)
	is_indicator_met = models.ForeignKey('IsIndicatorMet', null=True)
	recommended_indicator = models.TextField(blank=True, null=True)
	notes = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
			return str(self.id)
		
	def previous(self):
		try:
			previous_records = Investment.objects.filter(id__lt=self.id)
			previous_id = previous_records.order_by('-id')[0].id
			return Investment.objects.get(id=previous_id)
		except:
			return None
		
	def next(self):
		try:
			next_records = Investment.objects.filter(id__gt=self.id)
			next_id = next_records.order_by('id')[0].id
			return Investment.objects.get(id=next_id)
		except:
			return None
		
	def _get_str_all_report_due_dates(self):
		report_due_dates = self.report_due_date.all()
		str_report_due_dates = []
		for rdd in report_due_dates:
			str_report_due_dates.append("%s (%s);" % (rdd.date.strftime("%m/%d/%Y"),rdd.report_due_type.name))
		display_report_due_dates = "\n".join(str_report_due_dates)
		return display_report_due_dates
	_get_str_all_report_due_dates.short_description = "Report Due Date"
			
	def _get_str_all_investment_types(self):
		investment_types = self.investment_type.all()
		str_investment_types = []
		for it in investment_types:
			str_investment_types.append("%s: %s" % (it.category.name,it.name))
		display_investment_types = "\n".join(str_investment_types)
		return display_investment_types
	_get_str_all_investment_types.short_description = "Investment Type"
				
	class Meta:
		db_table = u'investment'