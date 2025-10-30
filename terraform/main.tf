terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "c01f98e4-f948-4055-a665-7972321f3605"
  tenant_id       = "ecf8c072-a04f-42d6-95ca-982b5cf51e4d"
}

resource "azurerm_resource_group" "rg" {
  name     = "expense-tracker-rg"
  location = "East US"
}

resource "azurerm_container_registry" "acr" {
  name                = "expensetrackeracr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "expense-tracker-aks"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "expense-tracker"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}