from . import __version__ as app_version

app_name = "quantbit_manufacturing"
app_title = "Quantbit Manufacturing"
app_publisher = "Quantbit Technologies Pvt. Ltd"
app_description = "it is modified manufacturing process"
app_email = "contact@erpdata.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/quantbit_manufacturing/css/quantbit_manufacturing.css"
# app_include_js = "/assets/quantbit_manufacturing/js/quantbit_manufacturing.js"

# include js, css files in header of web template
# web_include_css = "/assets/quantbit_manufacturing/css/quantbit_manufacturing.css"
# web_include_js = "/assets/quantbit_manufacturing/js/quantbit_manufacturing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "quantbit_manufacturing/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "quantbit_manufacturing.utils.jinja_methods",
#	"filters": "quantbit_manufacturing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "quantbit_manufacturing.install.before_install"
# after_install = "quantbit_manufacturing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "quantbit_manufacturing.uninstall.before_uninstall"
# after_uninstall = "quantbit_manufacturing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "quantbit_manufacturing.utils.before_app_install"
# after_app_install = "quantbit_manufacturing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "quantbit_manufacturing.utils.before_app_uninstall"
# after_app_uninstall = "quantbit_manufacturing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "quantbit_manufacturing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"quantbit_manufacturing.tasks.all"
#	],
#	"daily": [
#		"quantbit_manufacturing.tasks.daily"
#	],
#	"hourly": [
#		"quantbit_manufacturing.tasks.hourly"
#	],
#	"weekly": [
#		"quantbit_manufacturing.tasks.weekly"
#	],
#	"monthly": [
#		"quantbit_manufacturing.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "quantbit_manufacturing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "quantbit_manufacturing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "quantbit_manufacturing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["quantbit_manufacturing.utils.before_request"]
# after_request = ["quantbit_manufacturing.utils.after_request"]

# Job Events
# ----------
# before_job = ["quantbit_manufacturing.utils.before_job"]
# after_job = ["quantbit_manufacturing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"quantbit_manufacturing.auth.validate"
# ]
