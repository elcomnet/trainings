# Lab 03 - Manage Governance via Azure Policy

## Lab introduction

In this lab, you learn how to implement your organization’s governance plans. You learn how Azure policies can ensure operational decisions are enforced across the organization. You learn how to use resource tagging to improve reporting. 

## Estimated timing: 25 minutes

## Task 1: Enforce tagging via an Azure Policy

In this task, you will assign the built-in *Require a tag and its value on resources* policy to the resource group and evaluate the outcome. Azure Policy can be used to enforce configuration, and in this case, governance, to your Azure resources. 

1. In the Azure portal, search for and select `Policy`. 

1. In the **Authoring** blade, select **Definitions**. Take a moment to browse through the list of [built-in policy definitions](https://learn.microsoft.com/azure/governance/policy/samples/built-in-policies) that are available for you to use. 
Search policy **Require a tag and its value on resources**

1. Click the entry representing the **Require a tag and its value on resources** built-in policy.

1. On the **Require a tag and its value on resources** built-in policy definition blade, click **Assign**.

1. Specify the **Scope** by clicking the ellipsis button and selecting the following values. Click **Select** when you are done. 

    | Setting | Value |
    | --- | --- |
    | Subscription | *your subscription* |
    | Resource Group | **workshop-X** |

    >**Note**: You can assign policies on the management group, subscription, or resource group level. You also have the option of specifying exclusions, such as individual subscriptions, resource groups, or resources. In this scenario, we want the tag on all the resources in the resource group.

1. Configure the **Basics** properties of the assignment by specifying the following settings (leave others with their defaults):

    | Setting | Value |
    | --- | --- |
    | Assignment name | `Require Cost Center tag with Default value`|
    | Description | `Require Cost Center tag with default value for all resources in the resource group`|
    | Policy enforcement | Enabled |

    >**Note**: The **Assignment name** is automatically populated with the policy name you selected, but you can change it. The **Description** is optional. Notice you can disable the policy at any time. 

1. Click **Next** twice and set **Parameters** to the following values:

    | Setting | Value |
    | --- | --- |
    | Tag Name | `Cost Center` |
    | Tag Value | `000` |

1. Click **Next** and review the **Remediation** tab. Leave the **Create a Managed Identity** checkbox unchecked. 

1. Click **Review + Create** and then click **Create**.

    >**Note**: Now you will verify that the new policy assignment is in effect by attempting to create an Azure Storage account in the resource group. You will create the storage account without adding the required tag. 
    
    >**Note**: It might take between 5 and 10 minutes for the policy to take effect.

1. In the portal, search for and select `Storage Account`, and select **+ Create**. 

1. On the **Basics** tab of the **Create storage account** blade, complete the configuration.

    | Setting | Value |
    | --- | --- |
    | Subscription | your Azure subscription |
    | Resource group | **workshop-X** |
    | Storage account name | **azworkshopstudentXpolicy** |

1. Select **Review** and then click **Create**.

## Task 2: Apply tagging via an Azure policy

In this task, we will use the new policy definition to remediate any non-compliant resources. In this scenario, we will make any child resources of a resource group inherit the **Cost Center** tag that was defined on the resource group.

1. In the Azure portal, search for and select `Policy`. 

1. In the **Authoring** section, click **Assignments**. 

1. In the list of assignments, click the ellipsis icon in the row representing the **Require Cost Center tag with Default value** policy assignment and use the **Delete assignment** menu item to delete the assignment.

1. Click **Assign policy** and specify the **Scope** by clicking the ellipsis button and selecting the following values:

    | Setting | Value |
    | --- | --- |
    | Subscription | your Azure subscription |
    | Resource Group | **workshop-X** |

1. To specify the **Policy definition**, click the ellipsis button and then search for and select `Inherit a tag from the resource group if missing`.

1. Select **Add** and then configure the remaining **Basics** properties of the assignment.

    | Setting | Value |
    | --- | --- |
    | Assignment name | `Inherit the Cost Center tag and its value 000 from the resource group if missing` |
    | Description | `Inherit the Cost Center tag and its value 000 from the resource group if missing` |
    | Policy enforcement | Enabled |

1. Click **Next** twice and set **Parameters** to the following values:

    | Setting | Value |
    | --- | --- |
    | Tag Name | `Cost Center` |

1. Click **Next** and, on the **Remediation** tab, configure the following settings (leave others with their defaults):

    | Setting | Value |
    | --- | --- |
    | Create a remediation task | enabled |
    | Policy to remediate | **Inherit a tag from the resource group if missing** |

    >**Note**: This policy definition includes the **Modify** effect. So, a managed identity is required. 

1. Click **Review + Create** and then click **Create**.

    >**Note**: To verify that the new policy assignment is in effect, you will create another Azure storage account in the same resource group without explicitly adding the required tag. 
    
    >**Note**: It might take between 5 and 10 minutes for the policy to take effect.

1. Search for and select `Storage Account`, and click **+ Create**. 

1. On the **Basics** tab of the **Create storage account** blade, verify that you are using the Resource Group that the Policy was applied to and specify the following settings (leave others with their defaults) and click **Review**:

    | Setting | Value |
    | --- | --- |
    | Subscription | your Azure subscription |
    | Resource group | **workshop-X** |
    | Storage account name | **azworkshopstudentXpolicy** |

1. Verify that this time the validation passed and click **Create**.

1. Once the new storage account is provisioned, click **Go to resource**.

1. On the **Tags** blade, note that the tag **Cost Center** with the value **000** has been automatically assigned to the resource.

    >**Did you know?** If you search for and select **Tags** in the portal, you can view the resources with a specific tag. 

## Task 3: Configure and test resource locks

In this task, you configure and test a resource lock. Locks prevent either deletions or modifications of a resource. 

1. Go to Storage account **azworkshopstudentXpolicy**.
   
1. In the **Settings** blade, select **Locks**.

1. Select **Add** and complete the resource lock information. When finished select **Ok**. 

    | Setting | Value |
    | --- | --- |
    | Lock name | `sa-lock` |
    | Lock type | **delete** (notice the selection for read-only) |
    
1. Navigate to **Overview** blade, and select **Delete**.

1. In the **Enter storage account name to confirm deletion** textbox provide the storage account name, `azworkshopstudentXpolicy`. Notice you can copy and paste the storage account name. 

1. Notice the warning: Deleting this resource group and its dependent resources is a permanent action and cannot be undone. Select **Delete**.

1. You should receive a notification denying the deletion. 

1. You should receive a **Validation failed** message. View the message to identify the reason for the failure. Verify the error message states that the resource deployment was disallowed by the policy. 


>**Note**: By clicking the **Raw Error** tab, you can find more details about the error, including the name of the role definition **Require Cost Center tag with Default value**. The deployment failed because the storage account you attempted to create did not have a tag named **Cost Center** with its value set to **Default**.
