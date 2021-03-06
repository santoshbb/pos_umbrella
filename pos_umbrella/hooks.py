# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pos_umbrella"
app_title = "Pos Umbrella"
app_publisher = "jan"
app_description = "POS Umbrella"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "janlloydangeles@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pos_umbrella/css/pos_umbrella.css"
# app_include_js = "/assets/pos_umbrella/js/pos_umbrella.js"

# include js, css files in header of web template
# web_include_css = "/assets/pos_umbrella/css/pos_umbrella.css"
# web_include_js = "/assets/pos_umbrella/js/pos_umbrella.js"

# include js in page
page_js = {
    "pos": "public/js/pos.js",
    "point-of-sale": "public/js/pos.js"
}
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

# Website user home page (by function)
# get_website_user_home_page = "pos_umbrella.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pos_umbrella.install.before_install"
# after_install = "pos_umbrella.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pos_umbrella.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"before_insert": "pos_umbrella.doc_events.sales_invoice.before_insert_si",
		"validate": "pos_umbrella.doc_events.sales_invoice.validate_si",
		"after_submit": "pos_umbrella.doc_events.sales_invoice.on_submit_si",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pos_umbrella.tasks.all"
# 	],
# 	"daily": [
# 		"pos_umbrella.tasks.daily"
# 	],
# 	"hourly": [
# 		"pos_umbrella.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pos_umbrella.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pos_umbrella.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pos_umbrella.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pos_umbrella.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pos_umbrella.task.get_dashboard_data"
# }


fixtures = [
    {
        "doctype": "Print Format",
        "filters": [
            [
                "name",
                "in",
                [
                    "Customer Invoice"
                ]
            ]
        ]
    },
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "POS Profile-default_loyalty_program",
                    "POS Settings-loyalty_program",
                    "POS Settings-enable_submit_and_print",
                    "POS Settings-allowed_mobile_number_length"
                ]
            ]
        ]
    }
]
