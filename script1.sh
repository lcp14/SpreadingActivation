shopt -s nullglob

mkdir -p Testes/as-22july06/PageRank/Plots/
mkdir -p Testes/as-22july06/PageRank/Tempo/
mkdir -p Testes/as-22july06/PageRank/SementesIniciais/

mkdir -p Testes/as-22july06/Grau/Plots/
mkdir -p Testes/as-22july06/Grau/Tempo/
mkdir -p Testes/as-22july06/Grau/SementesIniciais/

mkdir -p Testes/as-22july06/Random/Plots/
mkdir -p Testes/as-22july06/Random/Tempo/
mkdir -p Testes/as-22july06/Random/SementesIniciais/

mkdir -p PageRank/SementesIniciais
mkdir -p Grau/SementesIniciais
mkdir -p Random/SementesIniciais

mkdir -p Random/Tempo
mkdir -p PageRank/Tempo
mkdir -p Grau/Tempo

for var in 0.005 0.01 0.05 0.1
do
  for var2 in 0 1 2
  do
    python SpreadingActivation.py Grafos/grafo_as-22july06.txt False $var $var2
    if [[ $var2 == 0 ]]; then
      #statements
      for i in *.png *.PNG; do
        mv $i* Testes/as-22july06/Random/Plots
      done
    fi
    if [[ $var2 == 1 ]]; then
      #statements
      for i in *.png *.PNG; do
        mv $i* Testes/as-22july06/Grau/Plots
      done
    fi
    if [[ $var2 == 2 ]]; then
      #statements
      for i in *.png *.PNG; do
        mv $i* Testes/as-22july06/PageRank/Plots
      done
    fi
  done
done

mv Random/SementesIniciais/ Testes/as-22july06/Random/
mv Random/Tempo/ Testes/as-22july06/Random/
mv PageRank/SementesIniciais/ Testes/as-22july06/PageRank/
mv PageRank/Tempo/ Testes/as-22july06/PageRank/
mv Grau/SementesIniciais/ Testes/as-22july06/Grau/
mv Grau/Tempo/ Testes/as-22july06/Grau/
