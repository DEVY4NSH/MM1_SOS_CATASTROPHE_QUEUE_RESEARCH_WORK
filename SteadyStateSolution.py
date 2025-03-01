from sympy import sqrt, im, symbols, Eq, solve, I, re, summation, N
lambda_, mu1, mu2, r, gamme, n = symbols('lambda mu1 mu2 r gamme n', real=True)
z = symbols('z')

def solution(params):
    lambda_,mu1,mu2,r,alp,gamme,n_max = params
    n, k = symbols('n k', integer=True)

    #Finding Roots
    equation = Eq((((lambda_ + mu1 + gamme*alp) * z - lambda_ * z**2 - mu1 * (1 - r)) * (lambda_ + mu2 + gamme*alp - lambda_ * z)) / lambda_**2 - mu1 * mu2 * r / lambda_**2, 0)
    #Finding the roots of the equation
    roots = solve(equation, z, domain='complex')
    moduli_manual = [sqrt(re(root)**2 + im(root)**2).evalf() for root in roots]
    #Converting the roots to real numbers
    roots_real = [re(root.evalf()) for root in roots]
    
    #Roots of the denominator of the generating function P(z)
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
    print(R)
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
    print(f'Normalization Condition Value : {R + sum(p_values) + sum(q_values)}')


calculate([8,15,20,0.4,0.5,0.01,100])