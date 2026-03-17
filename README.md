Celem laboratorium było utworzenie prostego modelu, nauczenie go na jednym z podstawowych zbiorów

## TWORZENIE MODELU ## 
W ramach laboratorium utworzony został model RFS który uczył się na zbiorze Iris z biblioteki sklearn.
Po utworzeniu zbioru podzieliłem go tak aby otrzymać zbiory train oraz test
W pierwszej wersji modelu użyłem hiperparametru n_estimators = 100. Następna wersja posiada zaktualizowaną wartość 200
Metryki modelu wskazują na to że model działa zgodnie z założeniem
Końcowym etapem było utworzenie pliku z modelem. Do utworzenia tego pliku skorzystałem z biblioteki pickle

## SKRYPT OTWIERAJĄCY ##
Po utworzeniu modelu następnym krokiem było przekazanie go do skryptu który go otwiera oraz sprawdza czy model działa
W tym celu stworzyłem daną testową o parametrach typowych dla kwiata setosa. Model poprawnie dopasował ją do typu.

## WERSJONOWANIE ##
Utworzone pliki dodałem do repozytorium. Należało również wprowadzić etykietę odpowiadającą stanowi naszego "Projektu".
W tym celu utworzyłem etykietę v1.0 w której znajduje się projekt początkowy(pierwsza wersja modelu).
Po aktualizacji modelu(model_iris_v2) dodałem nowego taga v2.

## ZASADY WERSJONOWANIA ##
vX.0: Zmiana hiperparametrów
v0.X: Poprawa jakości modelu

## RÓŻNICE MIĘDZY ŚRODOWISKIEM DEWELOPERSKIM A PRODUKCYJNYM ##
-środowisko i zależności
Gdy tworzymy pełnoprawny projekt musimy liczyć się z tym że użytkownicy mogą go uruchamiać na zupełnie innym sprzęcie.
Sposobem aby to kontrolować jest skorzystanie z narzędzi konteneryzacji np.docker które "dociągają" wszystkie potrzebne zależnośći

-Monitorowanie modelu na produkcji
W środowisku produkcyjnym dane mogą w pewnym momencie gwałtownie się zmienić, powodując spadek dokładności modelu.
Aby kontrolować takie wypadki należy wykorzystać system monitorujący. Ma on na celu powiadamiać deweloperów w momencie gdy 
statystyki danych przestają zgadzać się z danymi treningowymi

