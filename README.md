
# [C4MV: Contrastive Calibration on Consensus and Complementary Multi-view Representations](https://doi.org/10.1016/j.patcog.2026.113291)

[![Paper](https://img.shields.io/badge/Pattern_Recognition-2026-blue)](https://doi.org/10.1016/j.patcog.2026.113291) 
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)

Official implementation of the **C4MV** framework as presented in *Pattern Recognition (2026)*.

<p align="center">
  <img src="C4MV.svg" width="75%" alt="C4MV Framework Overview">
</p>

## 📖 Abstract
Multi-view representation learning (MRL) aims to exploit information from multiple views to learn discriminative data representations. While most existing methods emphasize consensus learning, they either neglect complementary view-specific information or lack principled mechanisms to balance shared and private representations. Moreover, although recent methods employ increasingly complex architectures to model local structure, they often fail to faithfully preserve the intrinsic structure of the data and lack explicit, strong structural regularization through contrastive objectives that jointly align both intra- and inter-view representations. To address these limitations, we propose C4MV, a novel MRL framework that explicitly integrates consensus and complementary representation learning with contrastive calibration. Unlike prior methods, C4MV jointly learns shared and view-specific representations through joint and disjoint self-representation factorizations, implemented via coordinated nonnegative matrix factorizations with diversity regularization to prevent redundancy across views. Furthermore, we introduce a contrastive calibration regularization that aligns intra- and inter-view representations using contrastive graph constraints, enhancing sample-level discriminability while reducing reliance on negative pairs. This unified formulation enables balanced fusion of multi-view information and faithful preservation of intrinsic data structure. The resulting optimization problem is solved using an efficient iterative algorithm. Extensive experiments on real-world datasets demonstrate that C4MV consistently outperforms state-of-the-art unsupervised multi-view representation learning methods. 

---

# 🚀 C4MV Setup & Installation Guide

Follow the steps below to clone the repository, install dependencies, and run the model.

## 📥 Clone the Repository

```bash
git clone https://github.com/yourusername/C4MV.git
cd C4MV
```

## 📦 Install Dependencies

```bash
pip install torch scikit-learn
```

## ▶️ Run the Model

```bash
python C4MV.py
```


## 🔗 Citation

If you use this repository or its implementation in your research, please cite **our paper**:

```bibtex
@article{JABARI2026C4MV,
  title   = {Contrastive Calibration on Consensus and Complementary Multi-View Representations},
  author  = {Jabari, Negin and Seyedi, Amjad and Mahmoodi, Reza and Akhlaghian Tab, Fardin},
  journal = {Pattern Recognition},
  year    = {2026},
  doi     = {10.1016/j.patcog.2026.113291}
}
```
