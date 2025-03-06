from debian as base

run apt update -y
run apt upgrade -y
run apt update -y

run apt install -y socat --fix-missing


copy ./chal /chal
run chmod 755 /chal

copy ./flag.txt /flag.txt
run chmod +r /flag.txt

expose 5000

entrypoint ["socat", "-dd", "TCP4-LISTEN:5000,fork,reuseaddr", "EXEC:\"/chal\",pty,echo=0,raw,iexten=0"] 
