resource "azurerm_app_service_plan" "test" {
  name                = ""
  location            = ""
  resource_group_name = ""

  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "test" {
  name                = ""
  location            = ""
  resource_group_name = ""
  app_service_plan_id = azurerm_app_service_plan.test.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }
  tags = "${var.tags}"
}