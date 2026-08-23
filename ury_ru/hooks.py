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

# Document Events
# ---------------
# Фискализация: при submit инвойса пробиваем чек, при cancel — возврат.
doc_events = {
    "POS Invoice": {
        "on_submit": "ury_ru.ury_ru.URY_RU_Fiscal.fiscal_hooks.on_submit",
        "on_cancel": "ury_ru.ury_ru.URY_RU_Fiscal.fiscal_hooks.on_cancel",
    },
}

# Fixtures: RU-specific customizations that can be exported/imported.
# fixtures = []

# Scheduled tasks / hooks to register integrations here as they land.
# scheduler_events = {}


def register_fiscal_driver_default():
    """Регистрирует фискальный драйвер при старте по настройкам.

    По умолчанию — NoOp (честная ошибка). Simulated включается в тестах/демо
    явно через URY RU Fiscal Settings (driver = "Simulated").
    """
    import frappe
    from ury_ru.ury_ru.URY_RU_Fiscal.fiscal_driver import (
        register_fiscal_driver,
    )

    if not frappe.db.exists("URY RU Fiscal Settings", "URY RU Fiscal Settings"):
        return

    settings = frappe.get_doc("URY RU Fiscal Settings", "URY RU Fiscal Settings")
    driver_name = (settings.get("driver") or "").lower()

    if driver_name == "simulated":
        from ury_ru.ury_ru.URY_RU_Fiscal.drivers.simulated import (
            SimulatedFiscalDriver,
        )
        register_fiscal_driver(SimulatedFiscalDriver())
    # ATOL / Shtrih-M — регистрируются только после реальной реализации,
    # пока NoOpFiscalDriver остаётся активным по умолчанию.
