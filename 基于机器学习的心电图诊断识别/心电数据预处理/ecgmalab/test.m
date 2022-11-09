level=4;         
sr=360; 
ecg_i=DenoisingSignal'; 
swa=zeros(4,points);%存储近似信息 
swd=zeros(4,points);%存储细节信息   


%计算近似系数和细节系数 
%低通滤波器  1/4 3/4 3/4 1/4 
%高通滤波器  -1/4 -3/4 3/4 1/4 
%二进样条小波  
for i=1:points-3       
    swa(1,i+3)=1/4*ecg_i(i+3-2^0*0)+3/4*ecg_i(i+3-2^0*1)+3/4*ecg_i(i+3-2^0*2)+1/4*ecg_i(i+3-2^0*3);       
    swd(1,i+3)=-1/4*ecg_i(i+3-2^0*0)-3/4*ecg_i(i+3-2^0*1)+3/4*ecg_i(i+3-2^0*2)+1/4*ecg_i(i+3-2^0*3); 
end 
j=2; 
while j<=level       
    for i=1:points-24           
        swa(j,i+24)=1/4*swa(j-1,i+24-2^(j-1)*0)+3/4*swa(j-1,i+24-2^(j-1)*1)+3/4*swa(j-1,i+24-2^(j-1)*2)+1/4*swa(j-1,i+24-2^(j-1)*3);           
        swd(j,i+24)=-1/4*swa(j-1,i+24-2^(j-1)*0)-3/4*swa(j-1,i+24-2^(j-1)*1)+3/4*swa(j-1,i+24-2^(j-1)*2)+1/4*swa(j-1,i+24-2^(j-1)*3);       
    end       
    j=j+1; 
end 
%*********************求正负极大值对**********************% 
ddw=zeros(size(swd)); 
pddw=ddw; 
nddw=ddw; 
%小波系数的大于0 的点 
posw=swd.*(swd>0); 
%斜率大于0 
pdw=((posw(:,1:points-1)-posw(:,2:points))<0); 
%正极大值点 
pddw(:,2:points-1)=((pdw(:,1:points-2)-pdw(:,2:points-1))>0); 
%小波系数小于0 的点 
negw=swd.*(swd<0); 
%斜率小于0 
ndw=((negw(:,1:points-1)-negw(:,2:points))>0); 
%负极大值点 
nddw(:,2:points-1)=((ndw(:,1:points-2)-ndw(:,2:points-1))>0); 
%或运算 
ddw=pddw|nddw; 
ddw(:,1)=1; 
ddw(:,points)=1; 
%求出极值点的值,其它点置0 
wpeak=ddw.*swd; 
wpeak(:,1)=wpeak(:,1)+1e-10; 
wpeak(:,points)=wpeak(:,points)+1e-10; 
interva2=zeros(1,points); 
intervaqs=zeros(1,points); 
Mj1=wpeak(1,:); 
Mj3=wpeak(3,:); 
Mj4=wpeak(4,:); 
%使用Mj3 3 层细节系数判断R 波 
posi=Mj3.*(Mj3>0); 
%求正极大值的平均 
thposi=(max(posi(1:round(points/4)))+max(posi(round(points/4):2*round(points/4)))+max(posi(2*round(points/4):3*round(points/4)))+max(posi(3*round(points/4):4*round(points/4))))/4; 
posi=(posi>thposi/3); 
nega=Mj3.*(Mj3<0); 
%求负极大值的平均 
thnega=(min(nega(1:round(points/4)))+min(nega(round(points/4):2*round(points/4)))+min(nega(2*round(points/4):3*round(points/4)))+min(nega(3*round(points/4):4*round(points/4))))/4; 
nega=-1*(nega<thnega/4); 
%找出非0 点 
interva=posi+nega; 
loca=find(interva); 
for i=1:length(loca)-1         
    if abs(loca(i)-loca(i+1))<80               
        diff(i)=interva(loca(i))-interva(loca(i+1));         
    else               
        diff(i)=0;         
    end 
end 
%找出极值对 
loca2=find(diff==-2); 
%负极大值点 
interva2(loca(loca2(1:length(loca2))))=interva(loca(loca2(1:length(loca2)))); 
%正极大值点 
interva2(loca(loca2(1:length(loca2))+1))=interva(loca(loca2(1:length(loca2))+1)); 
intervaqs(1:points-10)=interva2(11:points); 
countR=zeros(1,1); 
countQ=zeros(1,1); 
countS=zeros(1,1); 
mark1=0; 
mark2=0; 
mark3=0; 
i=1; 
j=1; 
Rnum=0; 
%*********求正负极值对过零。即R 波峰值，并检測出QRS 波起点及终点******% 
while i<points         
    if interva2(i)==-1               
        mark1=i;               
        i=i+1;               
        while(i<points&interva2(i)==0)                     
            i=i+1;               
        end               
        mark2=i; 
 %求极大值对的过零点               
 mark3= round((abs(Mj3(mark2))*mark1+mark2*abs(Mj3(mark1)))/(abs(Mj3(mark2))+abs(Mj3(mark1)))); 
 %R 波极大值点               
 R_result(j)=mark3;               
 countR(mark3)=1; 
 %求出QRS 波起点               
 kqs=mark3;               
 markq=0;           
 while (kqs>1)&&( markq< 3)                   
     if Mj1(kqs)~=0                         
         markq=markq+1;                   
     end                   
     kqs= kqs -1;           
 end     
 countQ(kqs)=-1;      
 %求出QRS 波终点         
 kqs=mark3;%-10     
 marks=0;     
 while (kqs<points)&&( marks<3)             
     if Mj1(kqs)~=0 
             marks=marks+1;             
     end             
     kqs= kqs+1;     
 end     
 countS(kqs)=-1;     
 i=i+50;     
 j=j+1;     
 Rnum=Rnum+1;   
    end 
 i=i+1; 
end 
%********************删除多检点，补偿漏检点**************************% 
num2=1; 
while(num2~=0)       
    num2=0; %j=3,过零点       
    R=find(countR); 
    %过零点间隔       
    R_R=R(2:length(R))-R(1:length(R)-1);       
    RRmean=mean(R_R); 
    %当两个R 波间隔小于0.4RRmean 时,去掉值小的R 波 
for i=2:length(R)         
        if (R(i)-R(i-1))<=0.4*RRmean                 
            num2=num2+1;                 
            if ecg_i(R(i))>ecg_i(R(i-1))                         
                countR(R(i-1))=0;                 
            else                         
                countR(R(i))=0;                 
            end         
        end 
end 
end  
num1=2; 
while(num1>0)       
    num1=num1-1;       
    R=find(countR);       
    R_R=R(2:length(R))-R(1:length(R)-1);      
    RRmean=mean(R_R); 
%当发现R 波间隔大于1.6RRmean 时,减小阈值,在这一段检測R 波 
for i=2:length(R)         
    if (R(i)-R(i-1))>1.6*RRmean                 
        Mjadjust=wpeak(4,R(i-1)+80:R(i)-80);                 
        points2=(R(i)-80)-(R(i-1)+80)+1; 
        %求正极大值点                 
        adjustposi=Mjadjust.*(Mjadjust>0);                 
        adjustposi=(adjustposi>thposi/4); 
        %求负极大值点                 
        adjustnega=Mjadjust.*(Mjadjust<0);                 
        adjustnega=-1*(adjustnega<thnega/5); 
        %或运算                 
        interva4=adjustposi+adjustnega; 
        %找出非0 点                 
        loca3=find(interva4);                 
        diff2=interva4(loca3(1:length(loca3)-1))-interva4(loca3(2:length(loca3))); 
        %假设有极大值对,找出极大值对                 
        loca4=find(diff2==-2);                 
        interva3=zeros(points2,1)';                 
        for j=1:length(loca4)                       
            interva3(loca3(loca4(j)))=interva4(loca3(loca4(j)));                       
            interva3(loca3(loca4(j)+1))=interva4(loca3(loca4(j)+1));                 
        end                 
        mark4=0;                 
        mark5=0;                 
        mark6=0;         
        while j<points2                   
            if interva3(j)==-1;                         
                mark4=j;                         
                j=j+1;                         
                while(j<points2&interva3(j)==0)                                   
                    j=j+1;                         
                end                        
                mark5=j; 
                %求过零点                         
                mark6= round((abs(Mjadjust(mark5))*mark4+mark5*abs(Mjadjust(mark4)))/(abs(Mjadjust(mark5))+abs(Mjadjust(mark4))));                         
                countR(R(i-1)+80+mark6-10)=1; 
           j=j+60;                   
            end                   
            j=j+1;           
        end         
    end   
   end 
end 
%画出原图及标出检测结果 
%%%%%%%%%%%%%%%%%%%%%%%%%%开始求PT 波段  
Mj4posi=Mj4.*(Mj4>0); 
%求正极大值的平均 
Mj4thposi=(max(Mj4posi(1:round(points/4)))+max(Mj4posi(round(points/4):2*round(points/4)))+max(Mj4posi(2*round(points/4):3*round(points/4)))+max(Mj4posi(3*round(points/4):4*round(points/4))))/4; 
Mj4posi=(Mj4posi>Mj4thposi/3); 
Mj4nega=Mj4.*(Mj4<0); 
%求负极大值的平均 
Mj4thnega=(min(Mj4nega(1:round(points/4)))+min(Mj4nega(round(points/4):2*round(points/4)))+min(Mj4nega(2*round(points/4):3*round(points/4)))+min(Mj4nega(3*round(points/4):4*round(points/4))))/4; 
Mj4nega=-1*(Mj4nega<Mj4thnega/4); 
Mj4interval=Mj4posi+Mj4nega; 
Mj4local=find(Mj4interval); 
Mj4interva2=zeros(1,points); 
for i=1:length(Mj4local)-1         
    if abs(Mj4local(i)-Mj4local(i+1))<80               
        Mj4diff(i)=Mj4interval(Mj4local(i))-Mj4interval(Mj4local(i+1));         
    else               
        Mj4diff(i)=0;         
    end 
end 
%找出极值对 
Mj4local2=find(Mj4diff==-2); 
%负极大值点 
Mj4interva2(Mj4local(Mj4local2(1:length(Mj4local2))))=Mj4interval(Mj4local(Mj4local2(1:length(Mj4local2)))); 
%正极大值点 
Mj4interva2(Mj4local(Mj4local2(1:length(Mj4local2))+1))=Mj4interval(Mj4local(Mj4local2(1:length(Mj4local2))+1)); 
mark1=0; 
mark2=0; 
mark3=0; 
Mj4countR=zeros(1,1); 
Mj4countQ=zeros(1,1); 
Mj4countS=zeros(1,1); 
flag=0; 
while i<points         
    if Mj4interva2(i)==-1               
        mark1=i;               
        i=i+1;               
        while(i<points&Mj4interva2(i)==0)                     
            i=i+1;               
        end               
        mark2=i; 
        %求极大值对的过零点,在R4 中极值之间过零点就是R 点。               
        mark3= round((abs(Mj4(mark2))*mark1+mark2*abs(Mj4(mark1)))/(abs(Mj4(mark2))+abs(Mj4(mark1))));               
        Mj4countR(mark3)=1;               
        Mj4countQ(mark1)=-1;               
        Mj4countS(mark2)=-1;               
        flag=1;         
    end         
    if flag==1                 
        i=i+200;                 
        flag=0;         
    else                 
        i=i+1;         
    end 
end 
%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%% 
%figure(200); 
%plot(Mj4); %
% title('j=4'); 
%hold on; 
%plot(Mj4countR,'r'); 
%plot(Mj4countQ,'g'); 
%plot(Mj4countS,'g'); 
%%%%%%%%%%%%%%%%%%%%%%%%%%Mj4 过 零 点 找到%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
Rlocated=find(Mj4countR); 
Qlocated=find(Mj4countQ); 
Slocated=find(Mj4countS); 
countPMj4=zeros(1,1); 
countTMj4=zeros(1,1); 
countP=zeros(1,1); 
countPbegin=zeros(1,1); 
countPend=zeros(1,1); 
countT=zeros(1,1); 
countTbegin = zeros(1,1); 
countTend = zeros(1,1); 
windowSize=100; 









%********************P 波检測********************% 、
%Rlocated Qlocated  是在尺度4 下的坐标 

for i=2:length(Rlocated)        
    flag=0;        
    mark4=0;        
    RRinteral=Rlocated(i)-Rlocated(i-1);        
    for j=1:5:(RRinteral*2/3)              
        % windowEnd=Rlocated(i)-30-j;               
        windowEnd=Qlocated(i)-j;                
         windowBegin=windowEnd-windowSize;              
        if windowBegin<Rlocated(i-1)+RRinteral/3                  
            break;               
        end                
        %求窗内的极大极小值                
        %windowposi=Mj4.*(Mj4>0);                
        %windowthposi=(max(Mj4(windowBegin:windowBegin+windowSize/2))+max(Mj4(windowBegin+windowSize/2+1:windowEnd)))/2;          
        [windowMax,maxindex]=max(Mj4(windowBegin:windowEnd));              
        [windowMin,minindex]=min(Mj4(windowBegin:windowEnd));              
        if minindex < maxindex &&((maxindex-minindex)<windowSize*2/3)&&windowMax>0.01&&windowMin<-0.1       
            flag=1;                       
            mark4=round((maxindex+minindex)/2+windowBegin);        
            countPMj4(mark4)=1;                  
            countP(mark4-20)=1;                  
            countPbegin(windowBegin+minindex-20)=-1;            
            countPend(windowBegin+maxindex-20)=-1;           
        end             
        if flag==1                 
            break;              
        end     
    end     
    if mark4==0&&flag==0 %假设没有P 波，在R 波左间隔1/3 处赋值-1            
        mark4=round(Rlocated(i)-RRinteral/3);              
        countP(mark4-20)=-1;        
    end 
end  
%plot(countPMj4,'g'); 









%********************T 波检測********************% 
clear windowBegin windowEnd maxindex minindex windowMax windowMin mark4 RRinteral;  
windowSizeQ=60; 
for i=1:length(Rlocated)-1;        
flag=0;     
mark5=0;        
RRinteral=Rlocated(i+1)-Rlocated(i);     
for j=1:5:(RRinteral*2/3)        
    % windowBegin=Rlocated(i)+30+j;             
    windowBegin=Slocated(i)+j;          
    windowEnd    =windowBegin+windowSizeQ;      
    if windowEnd >Rlocated(i+1)-RRinteral/4                
        break;
    end                
    %%%%%求窗体内的极大极小值             
    [windowMax,maxindex]=max(Mj4(windowBegin:windowEnd));          
    [windowMin,minindex]=min(Mj4(windowBegin:windowEnd)); 
    if minindex < maxindex &&((maxindex-minindex)<windowSizeQ)&&windowMax>0.1&&windowMin<-0.1       
          flag=1;                       
          mark5=round((maxindex+minindex)/2+windowBegin);              
          countTMj4(mark5)=1;                    
          countT(mark5-20)=1;%找到T 波峰值点 
                       
            %%%%%确定T 波起始点和终点                      
            countTbegin(windowBegin+minindex-20)=-1;                   
            countTend(windowBegin+maxindex-20)=-1;              
    end               
    if flag==1          
          break;              
    end     
    end       
    if mark5==0 %假设没有T 波。在R 波右  间隔1/3 处赋值-2            
        mark5=round(Rlocated(i)+ RRinteral/3);                
        countT(mark5)=-2;       
    end
end 
%plot(countTMj4,'g'); 
%hold off;                
figure(4); 
plot(ecg_i(0*points+1:1*points)),grid on,axis tight,axis([1,points,-2,5]); 
title('ECG 信号的各波波段检测');
hold on 
plot(countR,'r'); 
plot(countQ,'k'); 
plot(countS,'k');  
for i=1:Rnum     
    if R_result(i)==0;        
        break      
    end       
    plot(R_result(i),ecg_i(R_result(i)),'bo','MarkerSize',10,'MarkerEdgeColor','g'); 
end 
plot(countP,'r'); 
plot(countT,'r');
plot(countPbegin,'k'); 
plot(countPend,'k'); 
plot(countTbegin,'k'); 
plot(countTend,'k'); 

hold off