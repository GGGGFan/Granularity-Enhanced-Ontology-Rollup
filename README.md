# Granularity-Enhanced-Ontology-Rollup
#### Jifan Gao<sup>1,2</sup>, Guanhua Chen<sup>1,2</sup>
<sup>1</sup> Department of Biostatistics and Medical Informatics, University of Wisconsin-Madison, Madison, Wisconsin, USA <br/>
<sup>2</sup> Contact: J.G. (jifan.gao@wisc.edu), G.C. (gchen25@wisc.edu)


>### Abstract

We developed a granularity-enhanced ontology rollup pipeline to mitigate performance bias for machine learning models that are developed using structured EHR data. Ontology rollup is a powerful method to encode structured EHR data. However, important details can be lost as all the medical concepts are rolled up to their parent concepts. Choosing the proper level of granularity of the features is important for risk prediction as the same features for different groups of the population may not be measured at the same precision. Our method adaptively increases granularity on features that are essential to a specific subgroup in order to provide more necessary details on this subgroup to a machine learning model. As the granularity is enhanced before the model training process, the method is model-agnostic and task-agnostic. Our experiment on the MIMIC-III dataset demonstrates that this method can improve discriminative power on the black group for a mortality prediction task.
