clc
clear all

predict= textread('output_fit2.txt');
real=csvread('real.csv');
realdata=real(194:361,2:2863);
predictdata=predict(:,1:2862);
ERROR=realdata-predictdata;
ERRORloc=find(ERROR>50);
a=ERROR';
%a(all(a==0,2),:)=[];
a=a';
b=realdata';
%b(all(b==0,2),:)=[];
b=b';
ab=a./b*100;
percentE=zeros(1,2862);
for i=1:2862
    percentE(i)=ab(:,i)'*ab(:,i);
    percentE(i)=sqrt(percentE(i)/168);
end
RMSE=zeros(2862,1);
for i=1:2862
    RMSE(i)=a(:,i)'*a(:,i);
    RMSE(i)=sqrt(RMSE(i)/168);
end
figure(1)
plot(RMSE);
figure(2)
%plot(percentE);
location=zeros(54,53);
wushi=find(RMSE>50);
yibai=find(RMSE>100);
erbai=find(RMSE>200);
for i=1:54
    for j=1:53
        location(i,j)=RMSE(53*i-53+j);
    end
end
[X, Y] = meshgrid(1:53, 1:54);

surf(X, Y, location)