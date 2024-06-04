# Lab 02 - Manage Resource Group and RBAC
## Lab introduction

In this lab, you learn about role-based access control. You learn how to use permissions and scopes to control what actions identities can and cannot perform. 
You will be work with your Training partner

## Estimated timing: 20 minutes

## Task 1 Review and assign a built-in Azure role

In this task, you will review the built-in roles and assign the VM Contributor role to a your Training partner. Azure provides a large number of [built-in roles](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles). 
X - your traing number
Y - your partenr traing number

1. Select the **workshop-X** resource group.

1. Select the **Access control (IAM)** blade, and then the **Roles** tab.

1. Scroll through the built-in role definitions that are available. **View** a role to get detailed information about the **Permissions**, **JSON**, and **Assignments**. You will often use *owner*, *contributor*, and *reader*. 

1. Select **+ Add**, from the drop-down menu, select **Add role assignment**. 

1. On the **Add role assignment** blade, search for and select the **Virtual Machine Contributor**. The Virtual machine contributor role lets you manage virtual machines, but not access their operating system or manage the virtual network and storage account they are connected to. This is a good role for the Help Desk. Select **Next**.

1. On the **Members** tab, **Select Members**.

    >**Note:** The next step assigns the role to the **your Training partner** 

1. Search for and select the `your Training partner` user. Click **Select**. 

1. Click **Review + assign** twice to create the role assignment.

1. Continue on the **Access control (IAM)** blade. On the **Role assignments** tab, confirm the **your Training partner**  has the **Virtual Machine Contributor** role. 

    >**Note:** As a best practice always assign roles to groups not individuals. 

    >**Did you know?** This assignment might not actually grant you any additional privileges. If you already have the Owner role, that role includes all permissions associated with the VM Contributor role.

## Task 2 Check permission in partner Resource Group

In this task, you will review the built-in roles and assign the VM Contributor role to a your Training partner. Azure provides a large number of [built-in roles](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles). 
X - your traing number
Y - your partenr traing number

1. Go to the **workshop-Y** resource group.
1. Click **Create**
1. In search tab 'Search the Marketplace' type 'Virtual Machine'
1. In Virtual Machine box select **Create**, from the drop-down menu, select **Virtual Machine**.

    >**Note:** You shouldn't create Virtual machine
1. Go to the **workshop-Y** resource group.
1. Click **Create**
1. In search tab 'Search the Marketplace' type 'Storage account'
1. In Storage Account box select **Create**, from the drop-down menu, select **Storage account**.

    >**Note:** You shouldn't create Storage account
