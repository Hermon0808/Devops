variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "expense-tracker-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry"
  type        = string
  default     = "expensetrackeracr"
}

variable "aks_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "expense-tracker-aks"
}