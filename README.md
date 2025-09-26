# MM1_SOS_CATASTROPHE_QUEUE_RESEARCH_WORK

This repository contains the programming part of my research work, used for generating numerical results as part of my **B.Tech Project and M.Tech Thesis**. It provides a computational framework for analyzing and optimizing a single-server **Markovian queueing system** with optional service and catastrophes.

## Abstract

- This work studies the **transient** and **steady-state** behavior of an **infinite-buffer**, **single-server** Markovian queueing system with optional service **(SOS)** and **catastrophes**:

- Units arrive following a Poisson process and receive a first essential service (FES).

- Upon completion of FES, each unit can opt for a second optional service (SOS) with a probability defined by a Bernoulli distribution.

- The single server provides exponential service for both **FES** and **SOS**, serving one unit at a time.

- Catastrophes occur according to a **Poisson process** and may eliminate all units in the system. With a **protection** mechanism, units may survive catastrophes based on a **Bernoulli** probability.

- The probability-generating function for the system length distribution is derived for both transient and steady states.

- Transient-state probabilities are computed numerically using the **Runge-Kutta** method.

- Steady-state solutions are obtained in closed form.

- Finally, **metaheuristic optimization** techniques are applied to maximize the system’s overall profit by tuning system parameters, including the protection parameter.

## Repository Contents

- **steady_state_solution.py** – Closed-form steady-state solution script.

- **transient_runge_kutta_method.py** – Transient-state numerical approximation using Runge-Kutta.

### Optimization algorithms:

- **gsa_algorithm.py** – Gravitational Search Algorithm

- **pso_algorithm.py** – Particle Swarm Optimization Algorithm

- **sca_algorithm.py** – Sine-Cosine Algorithm

- **contour_plotting.py** – Scripts for visualizing results.

## Usage

### Clone the repository:
git clone https://github.com/DEVY4NSH/MM1_SOS_CATASTROPHE_QUEUE_RESEARCH_WORK.git


Run the desired scripts to replicate results or generate new simulations.

### Notes

Each script contains inline comments to explain the algorithms and workflow.

Suitable for research, academic projects, and further development in queueing theory and system optimization.
