# C4MV

  ## Contrastive Calibration on Consensus and Complementary Multi-view Representations
  
  *Negin Jabari, Amjad Seyedi, Reza Mahmoodi, and Fardin Akhlaghian Tab*
  
  *Pattern Recognition (176), 2026*
  
  *[[https://doi.org/10.1016/j.eswa.2018.07.075](https://doi.org/10.1016/j.patcog.2026.113291)](https://doi.org/10.1016/j.patcog.2026.113291)*

<p align=center><img src="C4MV.svg" width="50%" height="50%"></p>

  # Abstract

Multi-view representation learning (MRL) aims to exploit information from multiple views to learn discriminative data representations. While most existing methods emphasize consensus learning, they either neglect complementary view-specific information or lack principled mechanisms to balance shared and private representations. Moreover, although recent methods employ increasingly complex architectures to model local structure, they often fail to faithfully preserve the intrinsic structure of the data and lack explicit, strong structural regularization through contrastive objectives that jointly align both intra- and inter-view representations. To address these limitations, we propose C4MV, a novel MRL framework that explicitly integrates consensus and complementary representation learning with contrastive calibration. Unlike prior methods, C4MV jointly learns shared and view-specific representations through joint and disjoint self-representation factorizations, implemented via coordinated nonnegative matrix factorizations with diversity regularization to prevent redundancy across views. Furthermore, we introduce a contrastive calibration regularization that aligns intra- and inter-view representations using contrastive graph constraints, enhancing sample-level discriminability while reducing reliance on negative pairs. This unified formulation enables balanced fusion of multi-view information and faithful preservation of intrinsic data structure. The resulting optimization problem is solved using an efficient iterative algorithm. Extensive experiments on real-world datasets demonstrate that C4MV consistently outperforms state-of-the-art unsupervised multi-view representation learning methods. 


## Citation

If you use this repository or its implementations in your research, please cite **our paper**:

```bibtex
@article{JABARI2026C4MV,
  title   = {Contrastive Calibration on Consensus and Complementary Multi-View Representations},
  author  = author = {Negin Jabari and Amjad Seyedi and Reza Mahmoodi and Fardin {Akhlaghian Tab}},
  journal = {Pattern Recognition},
  year    = {2026}
}
