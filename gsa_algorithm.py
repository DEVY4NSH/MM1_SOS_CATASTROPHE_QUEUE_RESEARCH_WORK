def gsa(optimize_func, bounds, num_agents=50, max_iter=30, G0=100, alpha=2):
    """
    Gravitational Search Algorithm (GSA) for function optimization.
    
    Parameters:
    - optimize_func: Function that takes a list of parameters and returns a fitness value.
    - bounds: List of (min, max) tuples for each parameter.
    - num_agents: Number of agents in the population.
    - max_iter: Maximum number of iterations.
    - G0: Initial gravitational constant.
    - alpha: Decay rate for gravitational constant.
    
    Returns:
    - Best parameter set found.
    - Best fitness value found.
    - History of agent positions.
    """
    num_dimensions = len(bounds)
    
    agents = np.array([
        [random.uniform(bounds[d][0], bounds[d][1]) for d in range(num_dimensions)]
        for _ in range(num_agents)
    ], dtype=np.float64)
    
    velocities = np.zeros_like(agents, dtype=np.float64)
    
    history = []
    
    for iteration in range(max_iter):
        history.append(np.copy(agents))
        
        fitness_values = np.array([optimize_func(agent) for agent in agents], dtype=np.float64)
        best_fitness = np.max(fitness_values)
        worst_fitness = np.min(fitness_values)
        
        masses = (fitness_values - worst_fitness) / (best_fitness - worst_fitness + 1e-10)
        masses /= np.sum(masses) + 1e-10 
        
        G = G0 * (1 - iteration / max_iter) ** alpha 
        forces = np.zeros_like(agents, dtype=np.float64)
        
        for i in range(num_agents):
            total_force = np.zeros(num_dimensions, dtype=np.float64)
            for j in range(num_agents):
                if i != j:
                    dist = np.linalg.norm(agents[i] - agents[j]) + 1e-10
                    force = G * (masses[i] * masses[j]) / dist * (agents[j] - agents[i])
                    total_force += random.random() * force
            forces[i] = total_force
        
        accelerations = forces / (masses[:, np.newaxis] + 1e-10)
        
        velocities = np.random.rand(num_agents, num_dimensions) * velocities + accelerations
        agents += velocities

        agents = np.clip(agents, [b[0] for b in bounds], [b[1] for b in bounds])
    
    best_idx = np.argmax(fitness_values)
    best_params = agents[best_idx]
    best_fitness = fitness_values[best_idx]
    
    return best_params, best_fitness, history
