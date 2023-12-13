# Characterizing Feature Selection Techniques on Transcriptomic Data
## Introduction
In biomedical research, particularly in the analysis of transcriptomic data for cancer type characterization, the sheer volume of information poses a significant challenge. With datasets comprising thousands of genes, the need for efficient and effective dimension reduction techniques, particularly feature selection, becomes paramount. Transcriptomic datasets in cancer research often contain many thousands of genes, each potentially contributing to the intricacies of disease manifestation. While advancements in technology have enabled the generation of massive datasets, their analysis and interpretation have become increasingly intricate. The curse of dimensionality introduces computational and interpretative challenges that demand sophisticated analytical approaches.

Previous research in the field has made significant strides in uncovering potential biomarkers and elucidating gene expression patterns associated with various cancer types. However, as we accumulate more data, many genes may not be relevant to the specific classification task at hand. Consequently, the noise introduced by irrelevant features can overshadow the signal, hindering the development of robust and interpretable predictive models. The main issue is not merely the abundance of data but the ability to distill meaningful information from it. Traditional machine learning models, when applied to high-dimensional datasets, face computational inefficiencies, increased risk of overfitting, and a lack of interpretability. Furthermore, in biomedical contexts, where the emphasis lies on identifying clinically relevant biomarkers, the inclusion of irrelevant genes may hinder the translational potential of the findings.

Feature selection emerges as a crucial component of the analytical pipeline, offering a strategic means to address the challenges associated with high-dimensional data. By systematically identifying and retaining only the most informative features, feature selection techniques not only reduce computational complexity but also enhance the interpretability of models. In the context of biomedical research, this translates into the identification of a concise set of genes that are not only predictive but also biologically meaningful.

The dataset used in this study is publicly available from UC Irvine Machine Learning Repository. This collection of data is part of the RNA-Seq (HiSeq) PANCAN data set, having transcriptomic expressions of patients having different types of tumors: Breast Invasive Carcinoma (BRCA), Kidney Renal Clear Cell Carcinoma (KIRC), Colon Adenocarcinoma (COAD), Lung Adenocarcinoma (LUAD) and Prostate Adenocarcinoma (PRAD). There are 801 patient samples with transcriptomic expression data across all 20,531 genes, considered as features here.

## Learning Objectives
1. Do different feature selection methods (filter vs embedded) impact the clustering performance? 
2. Do different feature selection methods enhance or worsen result 	interpretability?
3. Are we more easily able to examine the underlying 	biological 	mechanisms with feature selection techniques? 

## Methods
<img width="778" alt="Screenshot 2023-12-12 at 9 29 42 PM" src="https://github.com/AarzuGupta/DimReduction/assets/21696736/78f3b15f-15d2-49ba-891a-ae044a9de96d">
Figure 1. The overall pipeline we followed. We explored supervised feature selection methods. However, since Wrapper methods prove to be incredibly time-taxing, they are not considered in this study. We evaluated 6 Filter and Embedded models (3 each). The same algorithm, Multilayer Perceptron (MLP), was then used to test all the methods to ensure consistency. MLP is well suited for this study due to its capacity for modeling non-linear relationships, ability to learn hierarchical representations, and flexibility to handle complex datasets. 

## Results
<img width="304" alt="Screenshot 2023-12-12 at 9 30 47 PM" src="https://github.com/AarzuGupta/DimReduction/assets/21696736/cdd54d28-1397-4e81-a6b1-049fa1267a89">
Figure 2. The line graphs (zoomed in: 200 out of 20K+ genes) show the performance (2a: accuracy, 2b: AUC) of each feature selection method across the number of features chosen. Both accuracy and AUC follow very similar patterns. All models converge at around 100 genes, at the latest, with Fisher and Correlation Coefficient converging the slowest. 

<img width="260" alt="Screenshot 2023-12-12 at 9 31 14 PM" src="https://github.com/AarzuGupta/DimReduction/assets/21696736/c17a1b22-ae31-4c1a-b4ca-3f1b58f70826">
Figure 3. These polar plots  visualize the 31 top overlapping genes, with each plot illustrating the importance of these genes for each feature selection method. The more blue and larger the points are, the higher the importance they have. A different gene had the greatest significance for each model. Correlation Coefficient (Fig. 3b) had the greatest number of these top overlapping genes be more important while Fisher (Fig. 3c) had the least.

<img width="475" alt="Screenshot 2023-12-12 at 9 31 46 PM" src="https://github.com/AarzuGupta/DimReduction/assets/21696736/79f73b8a-65c0-4c31-9a3b-854439d412cc">
 Figure 4. The clustermaps in Fig 4a. depict clustering of all the data while Fig 4b. is of only the selected features data. On both plots, the rows are the samples, while the columns are the genes. The selected features are the 31 genes that overlapped between all the important genes chosen by each method. Dark blue and dark red areas mean a high correlation, just in different directions. Although there is a vague clustering of 5 classes (5 cancer types) from the dendrogram in Fig 4a., it is much more distinct in Fig 4b. with just the 31 genes.

<img width="458" alt="Screenshot 2023-12-12 at 9 32 14 PM" src="https://github.com/AarzuGupta/DimReduction/assets/21696736/c1bc6548-0457-4a52-ad9c-6759f2f02c2d">

## Discussion
Analyzing the Filter vs Embedded feature selection methods, from Fig 2., Correlation Coefficient and Fisher, both Filter models, take the longest to converge. This may be because, unlike Embedded methods, Filter methods ignore feature dependencies and have no interaction with the classification model for selecting the features. With Embedded, considering features together, it may be able to take advantage of genes’ relationships earlier on. We can see in Fig 3. that although both Correlation Coefficient and Fisher selected majority of the features, most of the top overlapping features were quite significant for Correlation Coefficient, unlike Fisher.  This may be an artifact of Fisher being more successful at picking up non-linear relationships, making its selections more focused.

Despite that slight discrepancy between the Filter and Embedded methods, there are still 31 genes that overlap between all 6 of the feature selection methods. While we did not dig deeper into the selected genes that were different, this finding is consistent with our hypothesis of the signal in the data being stronger than any variance between the models. 

We decided to explore these top overlapping genes after looking at the clustermap before and after the dimension reduction. The map with just the 31 genes is significantly more interpretable and shows the 5 cancer type clusters clearly. This implies that all 20K of the initial features may detract from the overall performance in addition to using much compute power. Furthermore, the bar plots (for each cancer type) allow us to examine those tight gene clusters, potentially understanding how those differences link to these varying cancer types.

## Conclusions
The convergence is similar across all feature selection methods — all methods converge to almost the same point. Different feature selection methods will eventually choose similar subsets of features, but with different internal importance assignments. 

From initial exploration, the overlap in features from these methods seems to produce results that help explain the differences between these 5 cancer types. It would be interesting to re-run these analyses using a combination of feature selection and expanding to feature extraction methods. Looking into gene networks rather than individual genes and their biological mechanisms in greater depth could also help explain these discrepancies. Lastly, this dataset is well-balanced, which is unrepresentative of the real world. Comparing these results to those on imbalanced data could lead to methodology developments.

## References
[1] Park, S., Shin, B., Sang Shim, W. et al. Wx: a neural network-based feature selection algorithm for transcriptomic data. Sci Rep 9, 10500 (2019).
[2] Liu, S., & Motoda, H. Feature selection for knowledge discovery and data mining. Springer Science & Business Media (2007).
[3] He, Y., Tang, X., Huang, J. et al. ClusterMap for multi-scale clustering analysis of spatial gene expression. Nat Commun 12, 5909 (2021). 
[4] Stańczyk, U. Feature Evaluation by Filter, Wrapper, and Embedded Approaches. In: Stańczyk, U., Jain, L. (eds) Feature Selection for Data and Pattern Recognition. Studies in Computational Intelligence, vol 584. Springer, Berlin, Heidelberg (2015).
[5] Vogelstein, B., Kinzler, K. Cancer genes and the pathways they control. Nat Med 10, 789–799 (2004).





