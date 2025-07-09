
---

## 🧪 Test Problem: Linear Singular Perturbation

We solve:
\[
\varepsilon u''(x) - u(x) = 0, \quad u(0)=0,\quad u(1)=1
\]

- For ε ≪ 1, the solution forms a boundary layer near \( x = 0 \)
- PINN accurately captures the solution using physics-based training
- Matches the analytical solution:
\[
u(x) = \frac{e^{x/\sqrt{\varepsilon}} - 1}{e^{1/\sqrt{\varepsilon}} - 1}
\]

---

## 🧠 Upcoming Goals

- ✔ Add adaptive sampling near boundary layers
- ✔ Extend to 2D Gray–Scott and Schnakenberg models
- ✔ Perform convergence analysis
- ✔ Publish benchmark datasets and training curves
- ✔ Submit findings to a journal or conference in computational mathematics

---

## 🧑‍💻 Author

**Mudassar Rehman**  
PhD Researcher (Mathematics & Deep Learning)  
mudassarandgroup1@gmail.com  
[LinkedIn](https://www.linkedin.com/in/mudassar-rehman-0224441b2/) • [Google Scholar](https://scholar.google.com/citations?user=t52lpvcAAAAJ&hl=en) • [GitHub](https://github.com/mudassarandgroup1)

---

## 📚 References

- Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). *Physics-Informed Neural Networks*. JCP.
- Hao et al. (2024). *PINNacle Benchmark*. NeurIPS.
- Hu et al. (2024). *Stiff PINNs for high dimensions*. Neural Networks.

---

## 🧾 License

This project is open for academic collaboration. Please cite or contact the author before reusing parts in publications.
