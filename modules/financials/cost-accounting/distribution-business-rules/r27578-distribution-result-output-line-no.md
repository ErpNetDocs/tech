# R27578 Distribution - Result Output Line No

|Code| R27578
|:----|:----
|**Entity**|Distribution
|**Name**|ResultOutputLineNo
|**Attribute**|DistributionResult.OutputLineNo
|**Layer**|Back-End
|**Events**|Planning +
|**Modify**|NO
|**Action**|For each DistributionResult line validate that: DistributionResult.OutputLineNo.CostDistribution == DistributionResult.CostDistribution**
|**Description**| The results of one cost distribution document should direct to the Output record which is part of the current document. The current validation provides that one Cost distribution document will only distribute cost to its outputs.
|**Message**|’Result Line No.{LineNo} of Document '{DocumentText}' has invalid Output line No. No such Output line number exists in the document.’
|**Introduced version**|2017

