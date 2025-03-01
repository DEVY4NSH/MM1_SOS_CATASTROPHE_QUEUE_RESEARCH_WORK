def sca(optimize_func, bounds, num_particles=30, max_iter=10, a=2):
    """
    Sine Cosine Algorithm (SCA) for maximizing the given profit function.

    Parameters:
    - optimize_func: Function that takes a list of parameters and returns the profit value.
    - bounds: List of (min, max) tuples for each parameter.
    - num_particles: Number of search agents.
    - max_iter: Maximum number of iterations.
    - a: Parameter controlling exploration and exploitation.

    Returns:
    - Best parameter set that maximizes the profit function.
    - Best profit value found.
    """
    num_dimensions = len(bounds)

    agents = np.array([
        [random.uniform(bounds[d][0], bounds[d][1]) for d in range(num_dimensions)]
        for _ in range(num_particles)
    ])

    fitness = np.array([optimize_func(agent) for agent in agents])
    best_idx = np.argmax(fitness)
    best_agent = np.copy(agents[best_idx])
    best_value = fitness[best_idx]

    history = []

    # SCA main loop
    for t in range(max_iter):
        history.append(np.copy(agents))
        r1 = a - t * (a / max_iter)

        for i in range(num_particles):
            r2 = 2 * np.pi * random.random()
            r3 = 2 * random.random()
            r4 = random.random()

            new_agent = np.copy(agents[i])
            if r4 < 0.5:
                new_agent += r1 * np.sin(r2) * abs(r3 * (best_agent - new_agent))
            else:
                new_agent += r1 * np.cos(r2) * abs(r3 * (best_agent - new_agent))

            new_agent = np.clip(new_agent, [b[0] for b in bounds], [b[1] for b in bounds])

            new_profit = optimize_func(new_agent)

            if new_profit > fitness[i]:
                agents[i] = new_agent
                fitness[i] = new_profit

            if new_profit > best_value:
                best_agent = new_agent
                best_value = new_profit

    return best_agent, best_value, history