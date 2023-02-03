int main(){
int x
int i
int fact
int T_0
int T_1
//(inp,x,_,_)
L_1:scanf(x);
//(:=,1,_,fact)
L_2: fact=1;
//(:=,1,_,i)
L_3: i=1;
//(<=,i,x,6)
L_4: if(i<=x) goto L6;
//(jump,_,_,11)
L_5: goto L_11;
//(*,fact,i,T_0)
L_6: T_0=fact*i;
//(:=,T_0,_,fact)
L_7: fact=T_0;
//(+,i,1,T_1)
L_8: T_1=i+1;
//(:=,T_1,_,i)
L_9: i=T_1;
//(jump,_,_,4)
L_10: goto L_4;
//(out,fact,_,_)
L_11:printf(fact);
}