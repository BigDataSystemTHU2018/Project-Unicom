clc
clear all

predict= textread('output_fit2.txt');
real=csvread('real.csv');
realdata=real(194:361,2:2863);
predictdata=predict(:,1:2862);
ERROR=realdata-predictdata;
ERRORloc=find(ERROR>50);
a=ERROR';
a(all(a==0,2),:)=[];
a=a';
b=realdata';
b(all(b==0,2),:)=[];
b=b';
ab=a./b*100;
percentE=zeros(168,1);
for i=1:168
    percentE(i)=ab(i,:)*ab(i,:)';
    percentE(i)=sqrt(percentE(i)/2265);
end
RMSE=zeros(168,1);
for i=1:168
    RMSE(i)=a(i,:)*a(i,:)';
    RMSE(i)=sqrt(RMSE(i)/2265);
end
figure(1)
plot(RMSE);
figure(2)
plot(percentE);
