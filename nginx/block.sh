#!/bin/bash

BLOCK_CONF_PATH="/root/nginx/conf/ip_block.conf"
ACCESS_LOG_PATH="/root/nginx/log/access.log"

echo "blocked ip:"
i=0
for ip in $(tail -n 50 ${ACCESS_LOG_PATH} | awk '$7!="/" && $7!="/gz.html" && $7!="/test1.html" {print $1}')
do
    ips[$i]=$ip
    let i=$i+1
    echo $ip
done

echo "# block time: "$(date) >> ${BLOCK_CONF_PATH}
for ip in ${ips[@]}
do
    echo "deny "$ip";">> ${BLOCK_CONF_PATH}
done

# todo: 对ip_block.conf去重
# cat -n ${BLOCK_CONF_PATH} | sort -k2,2 -k1,1n | uniq -f1 | sort -k1,1n | cut -f2-

# reload
bash reload.sh
