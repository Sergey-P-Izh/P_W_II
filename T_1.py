#Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
 #а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
 # а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает
  # как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!


A = []
for _ in range(5):
    a = int(input('Введите целое число...'))
    A.append(int(a))

m_max = A[0]  #Самый тяжелый арбуз.
m_min = A[0]  #Самый легкий арбуз.
for i in A:
    if m_max < i:
        m_max = i
    if m_min > i:
        m_min = i

print(f'Тяжелый арбуз: {m_max}' , f'Легкий арбуз: {m_min}' )