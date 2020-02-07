Huckel theory applied to molecular motors

Introduction
============
Huckel theory is a semi-empirical quantum chemical method that can be applied to unsaturated hydrocarbons. This method is often taught at the undergraduate level using pen and paper exercises. However, the use of computational methods is key in modern day research. The concept of matrix diagonalization is vital in computational sciences (not just quantum chemistry). As programing has become dominant in research and in the corporate world, it might not be unimportant that students need to think more in terms of computational nomenclature (e.g. numerical methods).  

A small computer exercise that predicts the red-shifting of the excitation wavelength upon substitution of the aromatic ring of a molecular motor is presented. Two approaches are given: i) an online Huckel code utilizing a graphical user interface and ii) a Python script that entails the algebraic basics of matrix diagonalization. From a computational viewpoint, both approaches are identical. The calculations are based on the following article: [T. Leeuwen et al., Visible-light excitation of a molecular motor with an extended aromatic core. Organic Letters, 2017, 19, 1402–1405](https://pubs.acs.org/doi/abs/10.1021/acs.orglett.7b00317). 

Installation
============
```bash
git clone https://github.com/Heinen1/huckel_exercise
```

Usage
=====
**Solve Huckel equations using Python**
```bash
python motor1.py
python motor2.py
```

**Solve Huckel equations using HuLiS:**

Load the 'motor1.com' and 'motor2.com' files into HuLiS and calculate the corresponding HOMO and LUMO orbitals.


