#当bash的只能执行命令,python也用不了的时候启用php打印好命令使用：php curl.php >> curl.sh 

<?php
for ($i=1; $i<=255; $i++)
{
    echo "timeout 0.1 curl http://172.16.123.$i/flag.php\n";
}
?>
