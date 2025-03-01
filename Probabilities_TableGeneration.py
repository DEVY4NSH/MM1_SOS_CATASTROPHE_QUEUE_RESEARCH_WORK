import json

with open('output.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

R = data["R"]
lambda_ = data["λ"]
mu1 = data["μ1"]
mu2 = data["μ2"]
gamme = data["γ"]
r = data["r"]
p_values = data["p_n"]
q_values = data["q_n"]

sum_pn = sum(p_values)
sum_qn = sum(q_values)
normalization_value = R + sum_pn + sum_qn

print("\\begin{table}[h]")
print("\\centering")
print("\\caption{Numerical Results for Different Parameter Values}")
print("\\begin{minipage}{0.45\\textwidth}")
print("\\centering")
print("\\subcaption{{Table for Set 1 ($\\lambda = {:.2f}, \\mu_1 = {:.2f}, \\mu_2 = {:.2f}, \\gamma = {:.2f}, r = {:.2f}$)}}".format(lambda_, mu1, mu2, gamme, r))
print("\\textbf{Value of $R$: %.9f}" % R)
print("\\begin{tabular}{|c|c|c|}")
print("\\hline")
print("$n$ & $p_n$ & $q_n$ \\\\")
print("\\hline")


for n_value in range(min(21, len(p_values))):
    pn = p_values[n_value]
    qn = q_values[n_value]
    print(f"{n_value} & {pn:.9f} & {qn:.9f} \\\\")

print("\\vdots & \\vdots & \\vdots \\\\")
print("\\hline")
print(f"\\textbf{{Sum}} & {sum_pn:.9f} & {sum_qn:.9f} \\\\")

print("\\hline")
print(f"\\textbf{{Normalization}} & \\multicolumn{{2}}{{|c|}}{{Total = $R + \\sum p_n + \\sum q_n = {normalization_value:.9f}$}} \\\\")
print("\\hline")

print("\\end{tabular}")
print("\\end{minipage}")
print("\\end{table}")