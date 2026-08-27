#1(i)
sed -n '/and/p' question1.sh

#1(ii)
sed 's/language/lang/g' question1.sh

#1(iii)
sed '/is/d' question1.sh

#1(iv)
sed '=' question1.sh | sed 'N;s/\n/ /'

#1(v)
sed '1,2d' question1.sh

#1(vi)
sed -n '1~2p' question1.sh

#1(vii)
sed 's/Python/python/; s/language/lang/' question1.sh

