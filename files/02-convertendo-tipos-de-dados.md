> **Convertendo tipos de dados (casting)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### 1. Convertendo para int
```py

a = int(5)
b = int(5.7)
c = int("5")

print(a,type(a))  # Retorna: 5 <class 'int'>
print(b,type(b))  # 5 <class 'int'>
print(c,type(c))  # 5 <class 'int'>
print(a + b)  # 10
print(a + c)  # 10
```

&nbsp;  

### 2. Convertendo  para float
```py

a = float(5)
b = float(5.7)
c = float("5")
d = float("5.7")

print(a,type(a)) # Retorna: 5.0 <class 'float'>
print(b,type(b)) # 5.7 <class 'float'>
print(c,type(c)) # 5.0 <class 'float'>
print(d,type(d)) # 5.7 <class 'float'>
print(a + b)  # 10.7
print(a + c)  # 10.0
```

&nbsp;  

### 3. Convertendo para string
```py

a = str("exemplo")
b = str(2)
c = str(3.0)

print(a,type(a)) # Retorna: exemplo <class 'str'>
print(b,type(b)) # 2 <class 'str'>
print(c,type(c)) # 3.0 <class 'str'>
print(b + c) # 23.0
```

&nbsp;  

### 4. Convertendo para boolean
```py

print(bool(''))   # False
print(bool('abc')) # True
print(bool(0)) # False
print(bool(2)) # True
```
&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>