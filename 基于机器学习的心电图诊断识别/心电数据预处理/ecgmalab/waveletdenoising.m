%*********************去除噪声和基线漂移*********************% 
level=8; 
wavename='bior2.6'; 
ecgdata=M(:,1); 
figure(2); 
plot(ecgdata(1:points));grid on ;axis tight;axis([1,points,-2,5]); 
title('原始ECG 信号'); 
%%%%%%%%%%进行小波变换8 层 
[C,L]=wavedec(ecgdata,level,wavename); 
%%%%%%%提取近似系数， 
A1=appcoef(C,L,wavename,1); 
A2=appcoef(C,L,wavename,2);
A3=appcoef(C,L,wavename,3); 
A4=appcoef(C,L,wavename,4); 
A5=appcoef(C,L,wavename,5); 
A6=appcoef(C,L,wavename,6); 
A7=appcoef(C,L,wavename,7); 
A8=appcoef(C,L,wavename,8); 
%%%%%%%提取细节系数 
D1=detcoef(C,L,1); 
D2=detcoef(C,L,2); 
D3=detcoef(C,L,3); 
D4=detcoef(C,L,4); 
D5=detcoef(C,L,5); 
D6=detcoef(C,L,6); 
D7=detcoef(C,L,7); 
D8=detcoef(C,L,8); 
%%%%%%%%%%%%重构 
A8=zeros(length(A8),1); %去除基线漂移,8 层低频信息 
RA7=idwt(A8,D8,wavename); 
RA6=idwt(RA7(1:length(D7)),D7,wavename); 
RA5=idwt(RA6(1:length(D6)),D6,wavename); 
RA4=idwt(RA5(1:length(D5)),D5,wavename); 
RA3=idwt(RA4(1:length(D4)),D4,wavename); 
RA2=idwt(RA3(1:length(D3)),D3,wavename); 
D2=zeros(length(D2),1); %去除高频噪声，2 层高频噪声 
RA1=idwt(RA2(1:length(D2)),D2,wavename); 
D1=zeros(length(D1),1);%去除高频噪声，1 层高频噪声 
DenoisingSignal=idwt(RA1,D1,wavename); 
figure(3); 
plot(DenoisingSignal); 
title('去除噪声的ECG 信号'); grid on; axis tight;axis([1,points,-2,5]); 
clear ecgdata;