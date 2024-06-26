# Lab 11 - Implement Azure Container Instances

## Lab introduction

In this lab, you learn how to implement and deploy Azure Container Instances.

## Estimated timing: 15 minutes

## Task 1: Deploy an Azure Container Instance using a Docker image

In this task, you will create a simple web application using a Docker image. Docker is a platform that provides the ability to package and run applications in isolated environments called containers. Azure Container Instances provides the compute environment for the container image.

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

1. In the Azure portal, search for and select `Container instances` and then, on the **Container instances** blade, click **+ Create**.

1. On the **Basics** tab of the **Create container instance** blade, specify the following settings (leave others with their default values):

    | Setting | Value |
    | ---- | ---- |
    | Subscription | Select your Azure subscription |
    | Resource group | `workshop-X` |
    | Container name | `container-X-c1` |
    | Region | **(Europe) West/North Europe**|
    | Image Source | **Quickstart images** |
    | Image | **mcr.microsoft.com/azuredocs/aci-helloworld:latest (Linux)** |

1. Click **Next: Networking >** and specify the following settings (leave others with their default values):

    | Setting | Value |
    | --- | --- |
    | DNS name label | any valid, globally unique DNS host name |

    >**Note**: Your container will be publicly reachable at dns-name-label.region.azurecontainer.io. If you receive a **DNS name label not available** error message, specify a different value.

1. Click **Next: Advanced >**, review the settings without making any changes.

 1. Click **Review + Create**, ensure that the validation passed and then select **Create**.

    >**Note**: Wait for the deployment to complete. This should take 2-3 minutes.

## Task 2: Test and verify deployment of an Azure Container Instance 

In this task, you review the deployment of the container instance. By default, the Azure Container Instance is accessible over port 80. After the instance has been deployed, you can navigate to the container using the DNS name that you provided in the previous task.

1. On the deployment blade, click the **Go to resource** link.

1. On the **Overview** blade of the container instance, verify that **Status** is reported as **Running**.

1. Copy the value of the container instance **FQDN**, open a new browser tab, and navigate to the corresponding URL.

1. Verify that the **Welcome to Azure Container Instance** page is displayed. Refresh the page several times to create some log entries then close the browser tab.  

1. In the **Settings** section of the container instance blade, click **Containers**, and then click **Logs**.

1. Verify that you see the log entries representing the HTTP GET request generated by displaying the application in the browser.
