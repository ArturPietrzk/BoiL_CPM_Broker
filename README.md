# Projekt zaliczeniowy oparty o metode CPM

## Wstęp teoretyczny

CPM (Critical Path Method czyli metoda ścieżki krytycznej) należy do grupy deterministycznych technik planowania sieciowego. Jej podstawę stanowi budowa szczególnego rodzaju grafu sieciowego (przedstawiającego czynności i zdarzenia składające się na projekt) i dokonywanie wyliczeń na podstawie tego grafu. Dzięki tym wyliczeniem uzyskujemy plan realizacji projektu. Ten specyficzny rodzaj grafu jest określany siecią zależności lub wykresem sieciowym. Sieć ta opiera się na dwupunktowych modelach sieciowych, czyli takich gdzie czynności są reprezentowane za pomocą łuków grafu, a zdarzenia za pomocą węzłów grafu. Metodę ścieżki krytycznej wykorzystuje się do planowania i kontroli projektów, gdzie znana jest technologia i powiązania organizacyjne. Do takich projektów można zaliczyć inwestycje budowlane, remontowe, projekty związane z produkcję jednostkową skomplikowanych wyrobów (np. samolotów).


## Jak działa metoda CPM

Wiadomo z definicji, że metoda ta umożliwia przedstawienie wieloczynnościowego przedsięwzięcia, zmierzającego do osiagnięcia określonego celu, w sposób graficzny, jako
zbiór pojedynczych czynności oraz przeprowadzenia jego analizy. 
Gdzie:
- Zdarzenie to moment rozpoczęcia lub zakończenia jednej lub większej liczby czynności.
Graficznie przedstawiane jest za pomocą koła podzielonego na ćwiartki:

![czynnosc](https://user-images.githubusercontent.com/72975469/160156032-7038649a-9a72-4d29-aa26-fa0f64340474.png)

- Czynność to dowolnie wyodrębniony element przedsięwzięcia opisany czasem trwania w ramach którego zużywane są określone środki. Graficznie przedstawiane jest za pomocą strzałki:
  
![czynnosc2](https://user-images.githubusercontent.com/72975469/160156482-e6b70ad9-e839-4a2d-9848-055fa0e6b4b8.png)
  
- Zdarzają się sytuację, kiedy spotykamy się z czynnością, która nie wymaga zużywania ani czasu ani środków. Taka czynność nazywana jest czynnością pozorną i sluży do przedstawienia zależności między czynnościami:

![czynnosc3](https://user-images.githubusercontent.com/72975469/160157380-7032534f-43da-46cb-9bdb-1fe34e5e00bf.png)

## Reguły tworzenia sieci

1. Zdarzenie początkowe nie ma czynności poprzedzających,
2. Zdarzenie końcowe nie ma czynności następujących,
3. Dwa kolejne zdarzenia mogą być połączone tylko jedną czynnością,
4. Jeżeli czynność A jest bezpośrednim poprzednikiem czynności B to węzeł końcowy
(zdarzenie) czynności A staje się węzłem początkowym czynności B,
5. Jeżeli czynność X ma kilku poprzedników to końcowe węzły (zdarzenia) tych czynności są reprezentowane tylko przez jeden węzeł, który jest węzłem początkowym czynności X.
6. Jeżeli czynność X jest poprzednikiem dla kilku czynności to końcowy węzeł czynności X jest węzłem początkowym dla tych czynności. 

