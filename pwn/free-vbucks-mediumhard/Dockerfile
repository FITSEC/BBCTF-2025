from debian as base

run apt update -y
run apt upgrade -y
run apt update -y

run apt install -y socat --fix-missing

copy ./chall /chall
run chmod 755 /chall

copy ./flag.txt /flag.txt
run chmod +r /flag.txt

expose 5003

entrypoint ["socat", "-dd", "TCP4-LISTEN:5003,fork,reuseaddr", "EXEC:\"/chall\",pty,echo=0,raw,iexten=0"] 
