## Run with
docker build . -t labtest
docker run --mount type=bind,src=$(pwd),dst=/out labtest