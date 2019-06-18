function oput = cal( theta, rangeA, step, n )
len = length(rangeA);
for i = 1 : step
    index = 1 + n * (i-1);
    sigma1 = 0;
    sigma2 = 0;
    groupN = 0;
   for j = 1 : len  %表示相应的群组
        indexCol = rangeA(j);
        sigma1=sigma1+cos(theta(index,indexCol));
        sigma2=sigma2+sin(theta(index,indexCol));
    end 
    oput(i) = sqrt( sigma1^2+sigma2^2 ) / len;
end