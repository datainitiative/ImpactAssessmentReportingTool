from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('impactassessapp.views',
	# Home page URL
	url(r'^home/$','home'),
	
	# Import data URLs
	url(r'^import/org_stage/$','import_organization_stage'),
	url(r'^import/organization/$','import_organization'),
	url(r'^import/report_due_type/$','import_report_due_type'),
	url(r'^import/report_status/$','import_report_status'),
	url(r'^import/investment_category/$','import_investment_category'),
	url(r'^import/investment_type/$','import_investment_type'),
	url(r'^import/geography/$','import_geography'),
	url(r'^import/thematic_area/$','import_thematic_area'),
	url(r'^import/me_capacity/$','import_me_capacity'),
	url(r'^import/is_indicator_met/$','import_is_indicator_met'),
	url(r'^import/investment/$','import_investment'),

#	# Login,Logout,Register,User
#	url(r'^logout/$',logout,{'template_name': 'registration/logged_out.html'}),
#	url(r'^register/$','register'),
#	url(r'^user/profile/$','user_profile'),
#	url(r'^user/password/$','user_change_password'),
)