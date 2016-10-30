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
    list_filter = ['category']
admin.site.register(InvestmentType,InvestmentTypeAdmin)

class GeographyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(Geography,GeographyAdmin)

class ThematicAreaAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(ThematicArea,ThematicAreaAdmin)

class CostEffectivenessAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(CostEffectiveness,CostEffectivenessAdmin)

class BeneficiaryVsOrganizationalImpactAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(BeneficiaryVsOrganizationalImpact,BeneficiaryVsOrganizationalImpactAdmin)

class BeneficiaryLevelIndicatorAdmin(admin.ModelAdmin):
    fields = ['name','organization']
    list_display = ['name','organization']
admin.site.register(BeneficiaryLevelIndicator,BeneficiaryLevelIndicatorAdmin)

class ExternalEvaluationAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
admin.site.register(ExternalEvaluation,ExternalEvaluationAdmin)

class IndexOfReflectiveReportingAdmin(admin.ModelAdmin):
    fields = ['index','description']
    list_display = ['index','description']
admin.site.register(IndexOfReflectiveReporting,IndexOfReflectiveReportingAdmin)

class IndexOfQuantitativeReportingAdmin(admin.ModelAdmin):
    fields = ['index','description']
    list_display = ['index','description']
admin.site.register(IndexOfQuantitativeReporting,IndexOfQuantitativeReportingAdmin)

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
              'thematic_area',
              'cost_effectiveness',
              'beneficiary_level_indicator',
              'organization_level_indicator',
              'beneficiary_vs_organizational_impact',
              'summary_of_data_reported',
              'collaborations',
              'external_evaluation',
              'index_of_reflective_reporting',
              'index_of_quantitative_reporting',
              'lessons_learned',
              'me_capacity','me_capacity_note','is_indicator_met',
              'recommended_indicator','notes']
    filter_horizontal = ['report_due_date','investment_type','thematic_area']
    list_display = ['organization','date_of_award','_get_str_all_report_due_dates','report_status',
                    'amount','_get_str_all_investment_types','geography',
                    '_get_str_all_thematic_areas',
                    'cost_effectiveness',
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

class CodebookAdmin(admin.ModelAdmin):
    fields = ['field_name','description','source','comments','data_type_for_database','notes_on_initial_database','model_name']
    readonly_fields = ['model_name']
    list_display = ['field_name','description','source','comments','data_type_for_database','notes_on_initial_database','_url_list_all','_url_add_new']
    search_fields = ['field_name','description','source','comments','data_type_for_database','notes_on_initial_database','model_name']
admin.site.register(Codebook,CodebookAdmin)


