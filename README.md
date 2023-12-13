# Characterizing Feature Selection Techniques on Transcriptomic Data
# Introduction
In biomedical research, particularly in the analysis of transcriptomic data for cancer type characterization, the sheer volume of information poses a significant challenge. With datasets comprising thousands of genes, the need for efficient and effective dimension reduction techniques, particularly feature selection, becomes paramount. Transcriptomic datasets in cancer research often contain many thousands of genes, each potentially contributing to the intricacies of disease manifestation. While advancements in technology have enabled the generation of massive datasets, their analysis and interpretation have become increasingly intricate. The curse of dimensionality introduces computational and interpretative challenges that demand sophisticated analytical approaches.

Previous research in the field has made significant strides in uncovering potential biomarkers and elucidating gene expression patterns associated with various cancer types. However, as we accumulate more data, many genes may not be relevant to the specific classification task at hand. Consequently, the noise introduced by irrelevant features can overshadow the signal, hindering the development of robust and interpretable predictive models. The main issue is not merely the abundance of data but the ability to distill meaningful information from it. Traditional machine learning models, when applied to high-dimensional datasets, face computational inefficiencies, increased risk of overfitting, and a lack of interpretability. Furthermore, in biomedical contexts, where the emphasis lies on identifying clinically relevant biomarkers, the inclusion of irrelevant genes may hinder the translational potential of the findings.

Feature selection emerges as a crucial component of the analytical pipeline, offering a strategic means to address the challenges associated with high-dimensional data. By systematically identifying and retaining only the most informative features, feature selection techniques not only reduce computational complexity but also enhance the interpretability of models. In the context of biomedical research, this translates into the identification of a concise set of genes that are not only predictive but also biologically meaningful.

The dataset used in this study is publicly available from UC Irvine Machine Learning Repository. This collection of data is part of the RNA-Seq (HiSeq) PANCAN data set, having transcriptomic expressions of patients having different types of tumors: Breast Invasive Carcinoma (BRCA), Kidney Renal Clear Cell Carcinoma (KIRC), Colon Adenocarcinoma (COAD), Lung Adenocarcinoma (LUAD) and Prostate Adenocarcinoma (PRAD). There are 801 patient samples with transcriptomic expression data across all 20,531 genes, considered as features here.

# Learning Objectives
1. Do different feature selection methods (filter vs embedded) impact the clustering performance? 
2. Do different feature selection methods enhance or worsen result 	interpretability?
3. Are we more easily able to examine the underlying 	biological 	mechanisms with feature selection techniques? 

# 


