clc;
clear all;

k=[0  .5  .5  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0.2 0 0 ;
   .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  .5  .5  .5  0  0  0  0  0  0  0  0  0  0  0  0  0.2 0 0 ;
   0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  0  .5  .5  .5  0  0  0  0  0  0  0  0  0 0.2 0 ;
   0  0  0  0  0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  0  0  0  0  0  .5  .5  .5  0  0  0  0  0 0.2 0 ;
   0  0  0  0  0  0  0  0  0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  0  0  0  0  .5  0  0  0  0  0  0  0  0  0  0 ;  
   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  0  0  .5 ;  
   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0 ;   
   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0 ;   
   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0 ;   
   0.2 0 0  0  0.2 0 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  .5 ;  
   0  0  0  0  0  0  0  0  0.2 0 0  0  0.2 0 0  0  0  0  0  0  0  0  .5 ;  
   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  .5  0  0  0  .5 .5  0 ; 
   ]    

N = 23;
Step= 10000;
Theta=zeros(Step,N);
Omega =zeros(Step,N);
DeltaT=0.01;
Theta(1,:)=[0 pi/2 pi 3*pi/2  pi/4 3*pi/4 5*pi/4  7*pi/4   pi/2  pi 3*pi/2 0   3*pi/4 5*pi/4 7*pi/4  pi/4  pi 3*pi/2 0  pi/2 7*pi/4 pi/4 3*pi/4 ];
Omega = [2  2.8   3  3.2   2    2.8  3   3.2    2  2.8   3 3.2    2      2.8 3    3.2   2  2.8  3  3.2  2  2  1.5 ];

%   求解微分方程
for n = 1:Step
    for i = 1:N
            Sigma = 0; 
        for j = 1:N        
            Sigma = Sigma + k(i,j) * sin( Theta(n,i) - Theta(n,j) );
        end
            Theta(n+1,i) = ( Omega(i) - Sigma ) * DeltaT + Theta(n,i);
    end
end


%   求解序参量r(t)
showStep = 150;
deltaN = 60;
x= DeltaT: deltaN * DeltaT: DeltaT + DeltaT * deltaN * ( showStep-1 );
r(1,:)= cal (Theta,[1,2,3,4],showStep,deltaN);
r(2,:)= cal (Theta,[5,6,7,8],showStep,deltaN);
r(3,:)= cal (Theta,[9,10,11,12],showStep,deltaN);
r(4,:)= cal (Theta,[13,14,15,16],showStep,deltaN);
r(5,:)= cal (Theta,[17,18,19,20],showStep,deltaN);
 
 figure;
 plot(x,r(1,:),'--rs');hold on;
 plot(x,r(2,:),':go');hold on;
 plot(x,r(3,:),'-yv');hold on;
 plot(x,r(4,:),'-mp');hold on;
 plot(x,r(5,:),'-bd');hold on;

axis([0 DeltaT*deltaN*showStep 0 1 ]);
xlabel('t/s');
ylabel('r(t)');
legend('分组1','分组2','分组3','分组4','分组5',4);