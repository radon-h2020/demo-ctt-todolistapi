# ctt_cli.py refers to the executable of the CTT CLI Tool
# https://github.com/radon-h2020/radon-ctt-cli

echo "Starting T001"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T001.yaml -v
echo "Starting T010"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T010.yaml -v
echo "Starting T020"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T020.yaml -v 
echo "Starting T030"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T030.yaml -v
echo "Starting T040"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T040.yaml -v
echo "Starting T050"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T050.yaml -v
echo "Starting T060"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T060.yaml -v
echo "Starting T070"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T070.yaml -v
echo "Starting T080"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T080.yaml -v
echo "Starting T090"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T090.yaml -v
echo "Starting T100"
ctt_cli.py -u "http://localhost:18080/RadonCTT" -c T100.yaml -v
