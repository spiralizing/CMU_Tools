# RelatedMaterial

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the related material; can be used to add existing materials of the same account to items. | [optional] 
**identifier** | **str** | The related material identifier (e.g., DOI, Handle, ISBN). Mandatory if creating a new material. | [optional] 
**title** | **str** | The related material title | [optional] 
**relation** | **str** | The relation between the item and the related material; defaults to &#39;References&#39;. Mandatory if creating a new material. | [optional] [default to 'References']
**identifier_type** | **str** | The type of the identifier of the related material; defaults to &#39;URL&#39;. Mandatory if creating a new material. | [optional] [default to 'URL']
**is_linkout** | **bool** | Flag for highlighting this related material in the call-out box | [optional] 
**link** | **str** | The full hyperlink for the identifier. Automatically generated by Figshare. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


