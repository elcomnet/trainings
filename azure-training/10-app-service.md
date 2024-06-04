# Lab 10 - Implement Web Apps

## Lab introduction

In this lab, you learn about Azure web apps. You learn to configure a web app to display a Hello World application in an external GitHub repository. You learn to create a staging slot and swap with the production slot. You also learn about autoscaling to accommodate demand changes.

## Estimated timing: 20 minutes

## Task 1: Create and configure an Azure web app

In this task, you create an Azure web app. Azure App Services is a Platform As a Service (PAAS) solution for web, mobile, and other web-based applications. Azure web apps is part Azure App Services hosting most runtime environments, such as PHP, Java, and .NET. The app service plan that you select determines the web app compute, storage, and features. 

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

1. Search for and select `App services`.

1. Select **+ Create**, from drop-down menu, **Web App**. Notice the other choices. 

1. On the **Basics** tab of the **Create Web App** blade, specify the following settings (leave others with their default values):

    | Setting | Value |
    | --- | ---|
    | Subscription | your Azure subscription |
    | Resource group | `woskshop-X` |
    | Web app name | any globally unique name |
    | Publish | **Code** |
    | Runtime stack | **PHP 8.2** |
    | Operating system | **Linux** |
    | Region | **(Europe) West/North Europe** |
    | Pricing plans | accept the defaults |
    | Zone redundancy | accept the defaults |

 1. Click **Review + create**, and then **Create**.

    >**Note**: Wait until the Web App is created before you proceed to the next task. This should take about a minute.

1. After the deployment, select **Go to resource**.

## Task 2: Create and configure a deployment slot

In this task, you will create a staging deployment slot. Deployment slots enable you to perform testing prior to making your app available to the public (or your end users). After you have performed testing, you can swap the slot from development or staging to production. Many organizations use slots to perform pre-production testing. Additionally, many organizations run multiple slots for every application (for example, development, QA, test, and production).

1. On the blade of the newly deployed Web App, click the **Default domain** link to display the default web page in a new browser tab.

1. Close the new browser tab and, back in the Azure portal, in the **Deployment** section of the Web App blade, click **Deployment slots**.

    >**Note**: The Web App, at this point, has a single deployment slot labeled **PRODUCTION**.

1. Click **+ Add slot**, and add a new slot with the following settings:

    | Setting | Value |
    | --- | ---|
    | Name | `staging` |
    | Clone settings from | **Do not clone settings**|

1. Select **Add**.

1. Back on the **Deployment slots** blade of the Web App, click the entry representing the newly created staging slot.

    >**Note**: This will open the blade displaying the properties of the staging slot.

1. Review the staging slot blade and note that its URL differs from the one assigned to the production slot.

## Task 3: Configure Web App deployment settings

In this task, you will configure Web App deployment settings. Deployment settings allow for continuous deployment. This ensures that the app service has the latest version of the application.

1. In the staging slot, select **Deployment Center** and then select **Settings**.

    >**Note:** Make sure you are on the staging slot blade (instead than the production slot).
    
1. In the **Source** drop-down list, select **External Git**. Notice the other choices. 

1. In the repository field, enter `https://github.com/Azure-Samples/php-docs-hello-world`

1. In the branch field, enter `master`.

1. Select **Save**.

1. From the staging slot, select **Overview**.

1. Select the **Default domain** link, and open the URL in a new tab. 

1. Verify that the staging slot displays **Hello World**.

>**Note:** The deployment may take a minute. Be sure to **Refresh** the application page.

## Task 4: Swap deployment slots

In this task, you will swap the staging slot with the production slot. Swapping a slot allows you to use the code that you have tested in your staging slot, and move it to production. The Azure portal will also prompt you if you need to move other application settings that you have customized for the slot. Swapping slots is a common task for application teams and application support teams, especially those deploying routine app updates and bug fixes.

1. Navigate back to the **Deployment slots** blade, and then select **Swap**.

1. Review the default settings and click **Swap**.

1. On the **Overview** blade of the Web App select the **Default domain** link to display the website home page.

1. Verify the production web page displays the **Hello World!** page.

    >**Note:** Copy the Default domain **URL** you will need it for load testing in the next task. 
