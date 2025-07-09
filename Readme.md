# Adaptive PINNs for Singularly Perturbed Reaction–Diffusion Systems

This repository contains research code and experiments for a PhD project focused on solving **singularly perturbed reaction–diffusion partial differential equations (PDEs)** using **Physics-Informed Neural Networks (PINNs)**. The project explores the intersection of numerical analysis and deep learning, with the goal of developing stable, efficient, and adaptive neural solvers for stiff PDEs that arise in multiscale physical and biological systems.

---

## 🔍 Motivation

Singular perturbation problems involve small parameters multiplying the highest-order derivatives. These lead to steep gradients, boundary layers, and stiffness, making them difficult to solve with classical methods like finite differences or finite elements.

This research investigates whether PINNs — a class of neural networks that embed the PDE physics into the loss function — can:
- Handle such stiffness without mesh refinement
- Adaptively resolve sharp features in the solution
- Offer generalizable architectures for a wide class of stiff PDEs

---

## 📈 Current Status

| Component               | Status           | Notes                                                |
|------------------------|------------------|------------------------------------------------------|
| ✅ 1D toy PDE solver    | Complete         | Linear singularly perturbed ODE with ε → 0           |
| ✅ PINN implementation  | TensorFlow-based | Uses autodiff and PDE residual loss                  |
| ✅ Analytical comparison| Done             | Matches exact solution with high accuracy            |
| 🔄 Next steps           | In progress      | Extending to nonlinear and 2D reaction–diffusion PDEs|

---

## 📌 Problem Statement

> **How can we develop a physics-informed deep learning framework that solves stiff reaction–diffusion systems characterized by singular perturbations, with accuracy and stability comparable to (or better than) classical solvers?**

We aim to address:
- Convergence challenges when ε is small
- Generalizability of network architecture
- Adaptive strategies like residual-based sampling or homotopy methods

---

## 📂 Repository Structure

