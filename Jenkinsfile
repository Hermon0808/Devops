pipeline {
  agent any
  environment {
    ACR_NAME = 'expensetrackeracr'
    ACR_LOGIN_SERVER = 'expensetrackeracr.azurecr.io'
    IMAGE_NAME = 'expense-tracker'
    AKS_CLUSTER_NAME = 'expense-tracker-aks'
    RESOURCE_GROUP = 'expense-tracker-rg'
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${BUILD_NUMBER} .'
      }
    }
    stage('Push to ACR') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'acr-credentials', usernameVariable: 'ACR_USER', passwordVariable: 'ACR_PASS')]) {
          sh 'docker login ${ACR_LOGIN_SERVER} -u $ACR_USER -p $ACR_PASS'
          sh 'docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${BUILD_NUMBER}'
        }
      }
    }
    stage('Deploy to AKS') {
      steps {
        withCredentials([azureServicePrincipal('azure-sp')]) {
          sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID'
          sh 'az aks get-credentials --resource-group ${RESOURCE_GROUP} --name ${AKS_CLUSTER_NAME}'
          sh 'ansible-playbook ansible/deploy.yml'
        }
      }
    }
  }
}