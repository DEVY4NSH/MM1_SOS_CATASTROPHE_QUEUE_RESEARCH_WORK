def pso(optimize_func, bounds, num_particles=30, max_iter=10, w=0.7, c1=1.5, c2=1.5):
    """
    Particle Swarm Optimization (PSO) for maximizing the given profit function.
    
    Parameters:
    - optimize_func: Function that takes a list of parameters and returns the profit value.
    - bounds: List of (min, max) tuples for each parameter.
    - num_particles: Number of particles in the swarm.
    - max_iter: Maximum number of iterations.
    - w: Inertia weight.
    - c1, c2: Cognitive and social coefficients.
    
    Returns:
    - Best parameter set that maximizes the profit function.
    - Best profit value found.
    """
    num_dimensions = len(bounds)
    
    particles = np.array([
        [random.uniform(bounds[d][0], bounds[d][1]) for d in range(num_dimensions)]
        for _ in range(num_particles)
    ])
    velocities = np.zeros_like(particles)

    personal_best_positions = np.copy(particles)
    personal_best_values = np.array([optimize_func(p) for p in particles])
    global_best_idx = np.argmax(personal_best_values)
    global_best_position = personal_best_positions[global_best_idx]
    global_best_value = personal_best_values[global_best_idx]

    history = []
    
    for _ in range(max_iter):
        history.append(np.copy(particles))
        for i in range(num_particles):
            velocities[i] = (w * velocities[i] +
                             c1 * random.random() * (personal_best_positions[i] - particles[i]) +
                             c2 * random.random() * (global_best_position - particles[i]))
            
            particles[i] += velocities[i]
            
            particles[i] = np.clip(particles[i], [b[0] for b in bounds], [b[1] for b in bounds])
            
            profit = optimize_func(particles[i])
            
            if profit > personal_best_values[i]:
                personal_best_positions[i] = particles[i]
                personal_best_values[i] = profit
                
                if profit > global_best_value:
                    global_best_position = particles[i]
                    global_best_value = profit
    
    return global_best_position, global_best_value, history



bounds = [(0.1, 50), (0.1, 50)]

best_params, best_profit, history = pso(profit_function, bounds)
print("Best Parameters:", best_params)
print("Best Profit:", best_profit)
