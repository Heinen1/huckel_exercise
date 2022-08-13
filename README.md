Introduction
============
Huckel theory is a semi-empirical quantum chemical method that can be applied to unsaturated hydrocarbons. This method is often taught at the undergraduate level using pen and paper exercises. However, the use of computational methods, and programming in general, becomes more and more relevant in academic and industrial research. For this reason it can be argued that students should learn at an early stage to think in computational concepts. A key concept in quantum chemistry is matrix diagonalization, which can be easliy programmed with only a few lines of code.

Huckel theory computer exericses
============
A small computer exercise that predicts the red-shifting of the excitation wavelength upon substitution of the aromatic ring of a molecular motor is presented. Two approaches are given: 1) an online Huckel code utilizing a graphical user interface and 2) a Python script that performs matrix diagonalization. From a computational viewpoint, both approaches are identical. The calculations are based on the following article: [T. Leeuwen et al., Visible-light excitation of a molecular motor with an extended aromatic core. Organic Letters, 2017, 19, 1402–1405](https://pubs.acs.org/doi/abs/10.1021/acs.orglett.7b00317). 

Installation
============
```bash
git clone https://github.com/Heinen1/huckel_exercise.git
```

Usage
=====
**1) Solve Huckel equations using HuLiS:**

Load the 'motor1.com' and 'motor2.com' files into HuLiS and calculate the corresponding HOMO and LUMO orbitals.

**2) Solve Huckel equations using Python**
```bash
python motor1.py
python motor2.py
```




