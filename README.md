# MM1_SOS_CATASTROPHE_QUEUE_RESEARCH_WORK

This repository contains the programming part of my research work, used for generating numerical results as part of my **B.Tech Project and M.Tech Thesis**. It provides a computational framework for analyzing and optimizing a single-server **Markovian queueing system** with optional service and catastrophes.

## Abstract

- This study investigates both the transient and steady-state dynamics of an **infinite-buffer**, **single-server** Markovian queueing system that incorporates optional service (SOS) and the occurrence of catastrophes.

- Units enter the system following a **Poisson arrival** process and initially receive a first essential service (FES). After completing FES, each unit has a probabilistic choice to undergo a second optional service (SOS), modeled using a Bernoulli distribution.

- The server provides exponentially distributed service times for both **FES** and **SOS**, serving one unit at a time. Catastrophic events also arrive according to a **Poisson process**, potentially removing all units from the system. However, with a **protection mechanism** in place, units may survive **catastrophes** based on a **Bernoulli probability**.

- The system length distribution is characterized through a **probability-generating function** for both **transient** and **steady states**. Transient probabilities are approximated numerically using the **Runge-Kutta method**, while steady-state probabilities are derived in closed form.

Finally, several **metaheuristic optimization** techniques are employed to tune system parameters, including the protection mechanism, with the goal of maximizing overall **system performance and profit**.
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
