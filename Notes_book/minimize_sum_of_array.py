y = [2,7,4,9,1,0,21,8,22,19,4,78]
result_list = []
x=y.copy() # that is not the same as x=y!!!! important
for i in y:
    if len(x):
        result_list.append(max(x)*min(x))
        print(f"Maksimum: {max(x)} Minimum: {min(x)}")
        print(f"lista x: {x}\n")
        x.remove(max(x))
        x.remove(min(x))
print("#####################")
print(f"{x} wejściowa lista" )
print(f"{result_list} result_list z mnożeń")
print(f"{sum(result_list)} wynik")
