variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "weather-app-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry"
  type        = string
  default     = "weatherappacr"
}

variable "aks_cluster_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "weather-app-aks"
}