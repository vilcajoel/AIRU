%file methionine_model.m
%from Martinov et al. (2000) Journal of Theoretical Biology vol. 204 pp. 521-532
%generates figures 5.10, 5.11, 5.12
%problem 5.6.6

function methionine_model

global n1adomet;

%parameter declaration
%MATI
global v_MATI_max ;
global K_MATI_m ;
global K_MATI_i ;
global Met;

%MATIII
global v_MATIII_max ;
global K_MATIII_m2 ;

%MET
global v_MET_max ;
global A_over_K_MET_m2 ;

%GNMT
global v_GNMT_max ;
global K_GNMT_m ;
global K_GNMT_i ;

%D
global alpha_d ;

%AHC
global K_AHC;
global Adenosine

%parameter assignment
%METI
v_MATI_max = 561;
K_MATI_m = 41;
K_MATI_i = 50;

%MATIII
v_MATIII_max = 22870; %22.87 mmol/hr/l;
K_MATIII_m2 = 21.1;

%MET
v_MET_max = 4544;
A_over_K_MET_m2 = 0.1;

%GNMT
v_GNMT_max = 10600; %10.6 mmol/hr/l;
K_GNMT_m = 4500;
K_GNMT_i = 20;

%D
alpha_d = 1333;

%AHC
K_AHC = 0.1;
Adenosine = 1;

%Methionine concentration
Met=48.5; 

%set simulation length
Tend=5;

%initial concentrations
S0=[10,10];

%specification of dynamics
ODEFUN=@methdt;

%simulation
[t,S]=ode45(ODEFUN, [0,Tend], S0);

%figure 5.10
fig1=figure(1)
set(gca,'fontsize',14)
plot(t, S(:,1), 'k', t, S(:,2), 'k--', 'LineWidth', 3)
axis([0 1 0 90])
xlabel('Time (hr)')
ylabel('Concentration (\muM)')
legend('AdoMet', 'AdoHcy')

    
     
%Figure 5.11A
      
%define nullclines:
myfun1 = @(m,h) (v_MATI_max * (1/(1+ (K_MATI_m/Met)*(1+m/K_MATI_i))) + v_MATIII_max * (1/(1+ ((20000/(1+ 5.7*(m/(m+600))^2))*K_MATIII_m2)/(Met^2+Met*K_MATIII_m2)))) - (v_GNMT_max * (1/(1+(K_GNMT_m/m)^2.3)) * (1/(1+h/K_GNMT_i))+v_MET_max * (1/(1+ (10 * (1 + h/4))/m + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*((10 * (1 + h/4))/m))))
myfun2 = @(m,h) ((v_GNMT_max * (1/(1+(K_GNMT_m/m)^2.3)) * (1/(1+h/K_GNMT_i))+v_MET_max * (1/(1+ (10 * (1 + h/4))/m + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*((10 * (1 + h/4))/m)))) - alpha_d * (h*K_AHC/Adenosine))/(1+K_AHC/Adenosine)

figure(2)
hold on

[m,h] = meshgrid(0:1:1200);   %# Create a mesh of m and h points
f = (v_MATI_max.*(1./(1+ (K_MATI_m./Met).*(1+m./K_MATI_i))) + v_MATIII_max.*(1./(1+ ((20000./(1+ 5.7*(m./(m+600)).^2))*K_MATIII_m2)./(Met^2+Met*K_MATIII_m2)))) - (v_GNMT_max.*(1./(1+(K_GNMT_m./m).^2.3)).*(1./(1+h./K_GNMT_i))+v_MET_max.*(1./(1+ (10.*(1 + h./4))./m + 1./A_over_K_MET_m2 + (1./A_over_K_MET_m2).*((10.*(1 + h./4))./m))));             %# Evaluate f at those points
contour(m,h,f,[0 0],'b');     %# Generate the contour plot
setcurve('color',[0.5 0.5 0.5],'Linewidth', 2) 
axis([0 1200 0 6])

%adohcy nullcline
a2=ezplot(@(m,h) myfun2(m,h), [0 1200 0 6])
setcurve('color','black','Linewidth', 2) 

set(gca, 'fontsize', 14)
axis([0 1200 0 6])
legend('AdoMet nullcline', 'AdoHcy nullcline')
xlabel('[AdoMet] (\muM) ')
ylabel('[AdoHcy] (\muM)')
title('')
str1(1) = {'A'};
text(-140,6,str1, 'Fontsize', 40)

%set simulation length
Tend=15;

% generate simualtion traces 
%[t1,S1]=ode45(ODEFUN, [0,Tend], [0,0]);
[t1,S1]=ode45(ODEFUN, [0,Tend], [500,1.5]);
[t2,S2]=ode45(ODEFUN, [0,Tend], [900,2.5]);
[t3,S3]=ode45(ODEFUN, [0,Tend], [1100,3.5]);
[t4,S4]=ode45(ODEFUN, [0,Tend], [400,5.0]);
[t5,S5]=ode45(ODEFUN, [0,Tend], [800,5.5]);
[t6,S6]=ode45(ODEFUN, [0,Tend], [1000,5.75]);
[t7,S7]=ode45(ODEFUN, [0,Tend], [300,1]);
[t8,S8]=ode45(ODEFUN, [0,Tend], [700,2]);
[t9,S9]=ode45(ODEFUN, [0,Tend], [200,5]);
[t10,S10]=ode45(ODEFUN, [0,Tend], [600,5.25]);

%plot traces
plot(S1(:,1),S1(:,2),'k--','LineWidth',2)
plot(S2(:,1),S2(:,2),'k--','LineWidth',2)
plot(S3(:,1),S3(:,2),'k--','LineWidth',2)
plot(S4(:,1),S4(:,2),'k--','LineWidth',2)
plot(S5(:,1),S5(:,2),'k--','LineWidth',2)
plot(S6(:,1),S6(:,2),'k--','LineWidth',2)
plot(S7(:,1),S7(:,2),'k--','LineWidth',2)
plot(S8(:,1),S8(:,2),'k--','LineWidth',2)
plot(S9(:,1),S9(:,2),'k--','LineWidth',2)
plot(S10(:,1),S10(:,2),'k--','LineWidth',2)

%Figure 5.11A

%set Methionine level
Met=51 
      
%define nullclines:
myfun11 = @(m,h) (v_MATI_max * (1/(1+ (K_MATI_m/Met)*(1+m/K_MATI_i))) + v_MATIII_max * (1/(1+ ((20000/(1+ 5.7*(m/(m+600))^2))*K_MATIII_m2)/(Met^2+Met*K_MATIII_m2)))) - (v_GNMT_max * (1/(1+(K_GNMT_m/m)^2.3)) * (1/(1+h/K_GNMT_i))+v_MET_max * (1/(1+ (10 * (1 + h/4))/m + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*((10 * (1 + h/4))/m))))
myfun22 = @(m,h) ((v_GNMT_max * (1/(1+(K_GNMT_m/m)^2.3)) * (1/(1+h/K_GNMT_i))+v_MET_max * (1/(1+ (10 * (1 + h/4))/m + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*((10 * (1 + h/4))/m)))) - alpha_d * (h*K_AHC/Adenosine))/(1+K_AHC/Adenosine)

figure(3)
hold on

[m,h] = meshgrid(0:1:1200);   %# Create a mesh of m and h points
f = (v_MATI_max.*(1./(1+ (K_MATI_m./Met).*(1+m./K_MATI_i))) + v_MATIII_max.*(1./(1+ ((20000./(1+ 5.7*(m./(m+600)).^2))*K_MATIII_m2)./(Met^2+Met*K_MATIII_m2)))) - (v_GNMT_max.*(1./(1+(K_GNMT_m./m).^2.3)).*(1./(1+h./K_GNMT_i))+v_MET_max.*(1./(1+ (10.*(1 + h./4))./m + 1./A_over_K_MET_m2 + (1./A_over_K_MET_m2).*((10.*(1 + h./4))./m))));             %# Evaluate f at those points
contour(m,h,f,[0 0],'b');     %# Generate the contour plot
setcurve('color',[0.5 0.5 0.5],'Linewidth', 2) 
axis([0 1200 0 6])

%adohcy nullcline
a2=ezplot(@(m,h) myfun22(m,h), [0 1200 0 6])
setcurve('color','black','Linewidth', 2) 

set(gca, 'fontsize', 14)
axis([0 1200 0 6])
legend('AdoMet nullcline', 'AdoHcy nullcline')
xlabel('[AdoMet] (\muM)')
ylabel('[AdoHcy] (\muM)')
title('')

str1(1) = {'B'};
text(-140,6,str1, 'Fontsize', 40)

% generate simulation traces     
[t1,S1]=ode45(ODEFUN, [0,Tend], [420,1.5]);
[t2,S2]=ode45(ODEFUN, [0,Tend], [820,2.5]);
[t3,S3]=ode45(ODEFUN, [0,Tend], [1120,3.5]);
[t4,S4]=ode45(ODEFUN, [0,Tend], [520,5.0]);
[t5,S5]=ode45(ODEFUN, [0,Tend], [620,2]);
[t6,S6]=ode45(ODEFUN, [0,Tend], [240,4.5]);
[t7,S7]=ode45(ODEFUN, [0,Tend], [720,5.25]);

%plot simulation traces
plot(S1(:,1),S1(:,2),'k--','LineWidth',2)
plot(S2(:,1),S2(:,2),'k--','LineWidth',2)
plot(S3(:,1),S3(:,2),'k--','LineWidth',2)
plot(S4(:,1),S4(:,2),'k--','LineWidth',2)
plot(S5(:,1),S5(:,2),'k--','LineWidth',2)
plot(S6(:,1),S6(:,2),'k--','LineWidth',2)
plot(S7(:,1),S7(:,2),'k--','LineWidth',2)


%Figure 5.12
%numerical calculation of bifurcation curve. The separation of time-scales
%in this model makes bifurcation analysis with AUTO challenging.  The code
%below implements a `brute force' approach of sampling the stady state by
%running a sequence of simulations.

%toggle: set the if statement to "1==1" to run this part of the code. As written, it may take
%more than an hour to run.  Reduce the value of N to run a shorter version
%of the code (with a reduced mesh size).
if 1==0
    
N=400

%declare vectors to hold points on the bifurcation curve
m1_values1=zeros(1,N);
adom1_states1=zeros(1,N);
m1_values2=zeros(1,N);
adom1_states2=zeros(1,N);
m1_values3=zeros(1,N);
adom1_states3=zeros(1,N);

for i=1:N
    %set Methionine level
    Met=40+20*(i-1)/(N-1);
    %output step index (for tracking progress in the command window)
    i
    %find steady state from low S1
    [t,S]=ode45(ODEFUN, [0,200], [0,1000]);
    m1_values1(i)=Met;
    adom1_states1(i)=S(length(t),1);
    
    %find steady state from high S1
    [t,S]=ode45(ODEFUN, [0,200], [1000,0]);
    m1_values2(i)=Met;
    adom1_states2(i)=S(length(t),1);
    
    %find unstable steady state by solving steady state condition from a
    %point near the unstable steady state
    displacement= @(x) ((v_MATI_max * (1/(1+ (K_MATI_m/Met)*(1+x(1)/K_MATI_i))) + v_MATIII_max * (1/(1+ ((20000/(1+ 5.7*(x(1)/(x(1)+600))^2))*K_MATIII_m2)/(Met^2+Met*K_MATIII_m2)))) - (v_GNMT_max * (1/(1+(K_GNMT_m/x(1))^2.3)) * (1/(1+x(2)/K_GNMT_i))+v_MET_max * (1/(1+ (10 * (1 + x(2)/4))/x(1) + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*((10 * (1 + x(2)/4))/x(1))))))^2 + (((v_GNMT_max * (1/(1+(K_GNMT_m/x(1))^2.3)) * (1/(1+x(2)/K_GNMT_i))+v_MET_max * (1/(1+ (10 * (1 + x(2)/4))/x(1) + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*((10 * (1 + x(2)/4))/x(1))))) - alpha_d * (x(2)*K_AHC/Adenosine))/(1+K_AHC/Adenosine))^2;
    [steady_state, FVAL]=fminsearch(@(x) displacement(x), [500 3]);
    m1_values3(i)=Met;
    if FVAL<0.0001
    adom1_states3(i)=steady_state(1);
    else
        adom1_states3(i)=NaN;
    end
end

%plot points
figure(4)
set(gca,'fontsize',14)
hold on
c=[0 0 0;0.4 0.4 0.4;0.8 0.8 0.8];
set(0,'DefaultAxesColorOrder',c)
plot(m1_values1, adom1_states1, 'k*')
plot(m1_values2, adom1_states2, 'k*')
plot(m1_values3, adom1_states3,  'Linewidth', 3, 'color',[0.5 0.5 0.5])
xlabel('[Met] (\mu M)')
ylabel('steady state [AdoMet] (\mu M)')
     
end

end

%dynamics
function dS = methdt(t,S)

%parameter declaration
%MATI
global v_MATI_max ;
global K_MATI_m ;
global K_MATI_i ;
global Met;

%MATIII
global v_MATIII_max ;
global K_MATIII_m2 ;

%MET
global v_MET_max ;
global A_over_K_MET_m2 ;

%GNMT
global v_GNMT_max ;
global K_GNMT_m ;
global K_GNMT_i ;

%D
global alpha_d ;

%AHC
global K_AHC;
global Adenosine

%define states locally
AdoMet=S(1);
AdoHcy=S(2);

%auxilliary variables
K_MATIII_m1 = 20000/(1+ 5.7*(AdoMet/(AdoMet+600))^2);
K_MET_m1 = 10 * (1 + AdoHcy/4);
Hcy = AdoHcy*K_AHC/Adenosine;


v_MATI= v_MATI_max * (1/(1+ (K_MATI_m/Met)*(1+AdoMet/K_MATI_i))) ; 
v_MATIII = v_MATIII_max * (1/(1+ (K_MATIII_m1*K_MATIII_m2)/(Met^2+Met*K_MATIII_m2)));
v_GNMT = v_GNMT_max * (1/(1+(K_GNMT_m/AdoMet)^2.3)) * (1/(1+AdoHcy/K_GNMT_i));
v_MET = v_MET_max * (1/(1+ K_MET_m1/AdoMet + 1/A_over_K_MET_m2 + (1/A_over_K_MET_m2)*(K_MET_m1/AdoMet)));
V_D = alpha_d * Hcy;

dAdoMetdt = (v_MATI + v_MATIII) - (v_GNMT+v_MET);
dAdoHcydt = ((v_GNMT+v_MET) - V_D)/(1+K_AHC/Adenosine);

dS=[dAdoMetdt; dAdoHcydt];

end

%graphics function:
%change properties of last curve in current figure
%Examples:
%     setcurve('color','red')
%     setcurve('color','green','linestyle','--')
%Type  help plot  to see available colors and line styles 
function setcurve(varargin)
h=get(gca,'children');
set(h(1),varargin{:})
end
