from . import __version__ as app_version

app_name = "ury_ru"
app_title = "URY RU"
app_publisher = "URY-RU Community"
app_description = "Russian market localization and integrations for URY"
app_email = ""
app_license = "AGPL-3.0"

# URY-RU is a companion app that layers Russian-market modules
# and integrations on top of URY (itself built on ERPNext).
required_apps = ["ury", "erpnext"]

# include js, css files in header of desk.html
# app_include_css = "/assets/ury_ru/css/ury_ru.css"
# app_include_js = ["/assets/ury_ru/js/ury_ru.js"]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Doctype" : "public/js/doctype.js"}
# doctype_list_js = {"Doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"Doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"Doctype" : "public/js/doctype_calendar.js"}

# Fixtures: RU-specific customizations that can be exported/imported.
# fixtures = []

# Scheduled tasks / hooks to register integrations here as they land.
# scheduler_events = {}
