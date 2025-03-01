def profit_function(params):
    mu1, mu2 = params
    equation = Eq(((lambda_ + mu1 + gamme*alp) * z - lambda_ * z**2 - mu1 * (1 - r)) * (lambda_ + mu2 + gamme*alp - lambda_ * z) / lambda_**2 - mu1 * mu2 * r / lambda_**2, 0)
    #Finding the roots of the equation
    roots = solve(equation, z, domain='complex')
    # Compute the modulus manually using sqrt(re(z)^2 + im(z)^2)
    moduli_manual = [sqrt(re(root)**2 + im(root)**2).evalf() for root in roots]
    #Converting the roots to real numbers
    roots_real = [re(root.evalf()) for root in roots]
    
    z1 = roots_real[0]
    z2 = roots_real[1]
    z3 = roots_real[2]
    
    for i in range(0,3):
        if moduli_manual[i].evalf() <= 1:
            z1 = roots_real[i]
            if i==0:
                z2 = roots_real[i+1]
                z3 = roots_real[i+2]
            elif i==1:
                z2 = roots_real[i-1]
                z3 = roots_real[i+1]
            else:
                z2 = roots_real[i-2]
                z3 = roots_real[i-1]
                

    R = (gamme*alp) / (lambda_ + gamme*alp - lambda_ * z1)   #idle state probability

    n, k = symbols('n k', integer=True)

    

    p_values = []    #array storing probabilities p_n
    q_values = []    #array storing probabilities q_n

    p_0 = ((lambda_ + mu2 + gamme*alp) * R) / (lambda_ * z2 * z3)
    p_values.append(p_0)
    
    for n_value in range(1, n_max + 1):
        pn_expr = (R / (lambda_ * z2 * z3)) * (
        -lambda_ * summation(1 / (z2**(n - k - 1) * z3**k), (k, 0, n - 1))
        + (lambda_ + mu2 + gamme*alp) * summation(1 / (z2**(n - k) * z3**k), (k, 0, n)))
    
        pn_substituted = pn_expr.subs({
            n: n_value
        })
        pn_result = N(pn_substituted)
        p_values.append(pn_result)

    for n_value in range(0, n_max + 1):
        qn_expr = (mu1 * r * R) / (lambda_ * z2 * z3) * summation(1 / (z2**(n - k) * z3**k), (k, 0, n))
        
        qn_substituted = qn_expr.subs({
            n: n_value
        })
        qn_result = N(qn_substituted)
        q_values.append(qn_result)
        
    Lq = 0
    for j in range(1,n_max+1):
        Lq += j*(p_values[j]+q_values[j]) 
        
    Wq = Lq/lambda_
    
    Ls = 0
    for j in range(1,n_max+1):
        Ls += (j+1)*(p_values[j]+q_values[j]) 
    
    
    sum_p = sum(p_values)
    sum_q = sum(q_values)

    
    C_idle = 5
    C_holding = 1
    C_fes = mu1+0.1*mu1**2
    C_sos = mu2+0.1*mu2**2
    C_catastrophe = 2
    R_fes = 5
    R_sos = 10

    cost = R*C_idle + C_holding*Lq + C_fes*sum_p + C_sos*sum_q + C_catastrophe*alp*gamme*Ls
    revenue = R_fes*mu1*sum_p + R_sos*mu2*sum_q

    return (revenue - cost)