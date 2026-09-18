# Azure DevOps Infrastructure Automation

A portfolio project demonstrating Infrastructure as Code and CI/CD automation using Terraform, Azure DevOps YAML, Ansible and Python.

## Architecture

GitHub → Azure DevOps Pipeline → Terraform → Azure Resource Group/VNet → Ansible → Validation

## Technologies

- Microsoft Azure
- Terraform
- Azure DevOps
- GitHub
- Ansible
- Python
- YAML
- Infrastructure as Code (IaC)

## What this project demonstrates

1. Terraform validates and provisions Azure infrastructure.
2. Azure DevOps executes the CI/CD pipeline.
3. Ansible can be used for post-provisioning configuration.
4. Python performs simple validation/report generation.
5. Pipeline artifacts contain validation output.

## Cost-conscious usage

The pipeline is designed so `terraform validate` and `terraform plan` can be run without creating Azure resources. Keep `terraform apply` optional and use only resources/regions covered by your Azure subscription's free or credit allowance. Always delete test resources after use and check Azure Cost Management.

## Repository structure

```text
azure-devops-automation-project/
├── README.md
├── terraform/
│   ├── providers.tf
│   ├── variables.tf
│   ├── main.tf
│   └── outputs.tf
├── ansible/
│   ├── inventory.ini.example
│   └── configure.yml
├── scripts/
│   └── validate_environment.py
└── azure-pipelines.yml
```

## Local Terraform validation

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
```

For an Azure plan, authenticate with Azure CLI and then:

```bash
az login
terraform plan
```

## Azure DevOps

Create a pipeline from `azure-pipelines.yml`. Configure an Azure Resource Manager service connection named `azure-service-connection` if you want the plan/apply stages to authenticate to Azure.

For a portfolio demo, keep the Apply stage disabled until you intentionally want to provision resources.

## GitHub

Create a public repository named:

`azure-devops-automation-project`

Then push these files and add the repository URL to LinkedIn.
