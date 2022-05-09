# Projekt zaliczeniowy oparty o metode Pośrednika


## Wstęp teoretyczny

Zagadnienie pośrednika jest odwróconym zagadnieniem transportowym.


## Jak działa metoda Pośrednika


## Reguły tworzenia sieci

1. Wyznaczenie jednostkowego zysku zna poszczególnych trasach od dostawców do odbiorców na podstawie cen sprzedaży c, kosztów zakupu kzoraz kosztów jednostkowych transportu kt.

![1](https://user-images.githubusercontent.com/72975469/167386734-a019d276-81b8-4145-8396-d8a1689e7881.png)

      
2. Wprowadzenie do tablicy transportowej fikcyjnego dostawcyFD (o podaży równej całkowitemu popytowi) oraz fikcyjnego odbiorcyFO (o popycie równym całkowitej podaży) o jednostkowych zyskach zrównych „0”
3. W przypadku blokady wybranych dostawców lub odbiorców należy do tablicy wprowadzić odpowiadające im bloki z priorytetem obsadzania tras.
4. Wyznaczenie pierwszego przybliżenia z wykorzystaniem metody maksymalnego elementu macierzy.

5. Wyznaczenie zmiennych dualnych a i b na podstawie tras bazowych i formuły

![5](https://user-images.githubusercontent.com/72975469/167386720-334e46f6-c95f-4ba6-ac5c-331451b7a252.png)
       
6.Wyznaczenie zmiennych kryterialnych dla tras niebazowych na podstawie formuły

![6](https://user-images.githubusercontent.com/72975469/167386709-f901ac29-fa62-4ec7-87e7-83aa36d1a78e.png)

7. W przypadku jeżeli któraś ze zmiennych kryterialnych będzie miała wartość dodatnią należy wybrać pętlę zmian oraz dokonać na jej podstawie nowego obsadzenia tras i powrócić do punktu 5.


https://github.com/jonathansamines/transport-methods
https://github.com/malinowakrew/posrednik
