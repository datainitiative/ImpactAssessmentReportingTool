from django.contrib import admin

from impactassesstool.settings import ADMIN_ROOT_URL, ROOT_APP_URL
from impactassessapp.models import *

class OrganizationStageAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(OrganizationStage,OrganizationStageAdmin)

class ReportDueTypeAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(ReportDueType,ReportDueTypeAdmin)

class ReportStatusAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(ReportStatus,ReportStatusAdmin)

class InvestmentCategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(InvestmentCategory,InvestmentCategoryAdmin)

class InvestmentTypeAdmin(admin.ModelAdmin):
    fields = ['name','category']
    list_display = ['name','category']
admin.site.register(InvestmentType,InvestmentTypeAdmin)

class GeographyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(Geography,GeographyAdmin)

class ThematicAreaAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(ThematicArea,ThematicAreaAdmin)

class BeneficiaryLevelIndicatorAdmin(admin.ModelAdmin):
    fields = ['name','organization']
    list_display = ['name','organization']
admin.site.register(BeneficiaryLevelIndicator,BeneficiaryLevelIndicatorAdmin)

class MECapacityAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(MECapacity,MECapacityAdmin)

class IsIndicatorMetAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(IsIndicatorMet,IsIndicatorMetAdmin)

class OrganizationLevelIndicatorAdmin(admin.ModelAdmin):
    fields = ['name','organization']
    list_display = ['name','organization']
admin.site.register(OrganizationLevelIndicator,OrganizationLevelIndicatorAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    fields = ['name','description','est_date','org_stage','org_stage_note']
    list_display = ['name','description','est_date','_get_str_org_stage']
    list_filter = ['org_stage']
admin.site.register(Organization,OrganizationAdmin)

class ReportDueDateAdmin(admin.ModelAdmin):
    fields = ['date','report_due_type']
    list_display = ['date','report_due_type']
admin.site.register(ReportDueDate,ReportDueDateAdmin)


class InvestmentAdmin(admin.ModelAdmin):
    fields = ['organization','date_of_award','report_due_date','report_status',
              'amount','amount_note','investment_type','geography','geography_note',
              'thematic_area','cost_effectiveness',
              'beneficiary_level_indicator',
              'organization_level_indicator',
              'me_capacity','me_capacity_note','is_indicator_met',
              'recommended_indicator','notes']
    list_display = ['organization','date_of_award','_get_str_all_report_due_dates','report_status',
                    'amount','_get_str_all_investment_types','geography',
                    'thematic_area','cost_effectiveness',
                    'me_capacity','is_indicator_met',] 
#    list_display = ['organization','date_of_award','_get_str_all_report_due_dates','report_status',
#                    'amount','amount_note','_get_str_all_investment_types','geography','geography_note',
#                    'thematic_area','cost_effectiveness',
#                    'beneficiary_level_indicator',
#                    'organization_level_indicator',
#                    'me_capacity','me_capacity_note','is_indicator_met',
#                    'recommended_indicator','notes']
    list_filter = ['organization','report_status','geography','thematic_area',
                    'me_capacity','is_indicator_met',]
    actions = ['delete_selected']
admin.site.register(Investment,InvestmentAdmin)
