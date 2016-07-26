from django.db import models
from impactassesstool.settings import ADMIN_ROOT_URL

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
		
class CostEffectiveness(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
		try:
			previous_records = CostEffectiveness.objects.filter(id__lt=self.id)
			previous_id = previous_records.order_by('-id')[0].id
			return CostEffectiveness.objects.get(id=previous_id)
		except:
			return None
		
	def next(self):
		try:
			next_records = CostEffectiveness.objects.filter(id__gt=self.id)
			next_id = next_records.order_by('id')[0].id
			return CostEffectiveness.objects.get(id=next_id)
		except:
			return None	

	class Meta:
		db_table = u'cost_effectiveness'

class BeneficiaryVsOrganizationalImpact(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
		try:
			previous_records = BeneficiaryVsOrganizationalImpact.objects.filter(id__lt=self.id)
			previous_id = previous_records.order_by('-id')[0].id
			return BeneficiaryVsOrganizationalImpact.objects.get(id=previous_id)
		except:
			return None
		
	def next(self):
		try:
			next_records = BeneficiaryVsOrganizationalImpact.objects.filter(id__gt=self.id)
			next_id = next_records.order_by('id')[0].id
			return BeneficiaryVsOrganizationalImpact.objects.get(id=next_id)
		except:
			return None	

	class Meta:
		db_table = u'beneficiary_vs_organizational_impact'
		
class ExternalEvaluation(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
		try:
			previous_records = ExternalEvaluation.objects.filter(id__lt=self.id)
			previous_id = previous_records.order_by('-id')[0].id
			return ExternalEvaluation.objects.get(id=previous_id)
		except:
			return None
		
	def next(self):
		try:
			next_records = ExternalEvaluation.objects.filter(id__gt=self.id)
			next_id = next_records.order_by('id')[0].id
			return ExternalEvaluation.objects.get(id=next_id)
		except:
			return None	

	class Meta:
		db_table = u'external_evaluation'
		
class IndexOfReflectiveReporting(models.Model):
#	id = models.IntegerField(primary_key=True)
	index = models.IntegerField(default=-1)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.index)
	
	def previous(self):
		try:
			previous_records = IndexOfReflectiveReporting.objects.filter(id__lt=self.id)
			previous_id = previous_records.order_by('-id')[0].id
			return IndexOfReflectiveReporting.objects.get(id=previous_id)
		except:
			return None
		
	def next(self):
		try:
			next_records = IndexOfReflectiveReporting.objects.filter(id__gt=self.id)
			next_id = next_records.order_by('id')[0].id
			return IndexOfReflectiveReporting.objects.get(id=next_id)
		except:
			return None	

	class Meta:
		db_table = u'index_of_reflective_reporting'
		
class IndexOfQuantitativeReporting(models.Model):
#	id = models.IntegerField(primary_key=True)
	index = models.IntegerField(default=-1)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.index)
	
	def previous(self):
		try:
			previous_records = IndexOfQuantitativeReporting.objects.filter(id__lt=self.id)
			previous_id = previous_records.order_by('-id')[0].id
			return IndexOfQuantitativeReporting.objects.get(id=previous_id)
		except:
			return None
		
	def next(self):
		try:
			next_records = IndexOfQuantitativeReporting.objects.filter(id__gt=self.id)
			next_id = next_records.order_by('id')[0].id
			return IndexOfQuantitativeReporting.objects.get(id=next_id)
		except:
			return None	

	class Meta:
		db_table = u'index_of_quantitative_reporting'

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
	_get_str_org_stage.short_description = "Organization Stage"
				
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
	thematic_area = models.ManyToManyField('ThematicArea')
	cost_effectiveness = models.ForeignKey('CostEffectiveness', null=True)
#	beneficiary_level_indicator = models.ManyToManyField('BeneficiaryLevelIndicator', null=True)
#	organization_level_indicator = models.ManyToManyField('OrganizationLevelIndicator', null=True)
	beneficiary_level_indicator = models.TextField(blank=True, null=True)
	organization_level_indicator = models.TextField(blank=True, null=True)
	beneficiary_vs_organizational_impact = models.ForeignKey('BeneficiaryVsOrganizationalImpact', null=True)
	summary_of_data_reported = models.TextField(max_length=500, blank=True, null=True)
	collaborations = models.TextField(max_length=500, blank=True, null=True)
	external_evaluation = models.ForeignKey('ExternalEvaluation', null=True)
	index_of_reflective_reporting = models.ForeignKey('IndexOfReflectiveReporting', null=True)
	index_of_quantitative_reporting = models.ForeignKey('IndexOfQuantitativeReporting', null=True)
	me_capacity = models.ForeignKey('MECapacity', null=True)
	me_capacity_note = models.CharField(max_length=200, blank=True, null=True)
	is_indicator_met = models.ForeignKey('IsIndicatorMet', null=True)
	recommended_indicator = models.TextField(blank=True, null=True)
	lessons_learned = models.TextField(max_length=200, blank=True, null=True)
	notes = models.TextField(verbose_name="Reporting comments and notes", blank=True, null=True)
	
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
	
	def _get_str_all_thematic_areas(self):
		thematic_areas = self.thematic_area.all()
		str_thematic_areas = []
		for ta in thematic_areas:
			str_thematic_areas.append(ta.name)
		display_thematic_areas = "\n".join(str_thematic_areas)
		return display_thematic_areas
	_get_str_all_thematic_areas.short_description = "Thematic Area"	
				
	class Meta:
		db_table = u'investment'
		
class Codebook(models.Model):
#	id = models.IntegerField(primary_key=True)
	field_name = models.CharField(max_length=200, blank=True, null=True)
	description = models.TextField(max_length=500, blank=True, null=True)
	source = models.TextField(max_length=500, blank=True, null=True)
	comments = models.TextField(max_length=500, blank=True, null=True)
	data_type_for_database = models.CharField(max_length=200, blank=True, null=True)
	notes_on_initial_database = models.TextField(max_length=500, blank=True, null=True)
	model_name = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return unicode(self.name)
	
	def previous(self):
	    try:
	        previous_records = Codebook.objects.filter(id__lt=self.id)
	        previous_id = previous_records.order_by('-id')[0].id
	        return Codebook.objects.get(id=previous_id)
	    except:
	        return None
	    
	def next(self):
	    try:
	        next_records = Codebook.objects.filter(id__gt=self.id)
	        next_id = next_records.order_by('id')[0].id
	        return Codebook.objects.get(id=next_id)
	    except:
	        return None
		
	def _url_list_all(self):
		if self.model_name:
			path = "%s/admin/impactassessapp/%s/" % (ADMIN_ROOT_URL,self.model_name)
			url = '<a href="%s" target="_blank">View All</a>' % path
		else:
			url = ""
		return url
	_url_list_all.short_description = "View All"
	_url_list_all.allow_tags = True
	
	def _url_add_new(self):
		if self.model_name:
			path = "%s/admin/impactassessapp/%s/add/" % (ADMIN_ROOT_URL,self.model_name)
			url = '<a href="%s" target="_blank">Add New</a>' % path
		else:
			url = ""
		return url
	_url_add_new.short_description = "Add New"
	_url_add_new.allow_tags = True	
	
	class Meta:
		db_table = u'codebook'
