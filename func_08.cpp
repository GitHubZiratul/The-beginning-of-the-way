#include <iostream>
#include <string>

using namespace std;

char Is5Latin(string);

int main()
{
  setlocale(LC_ALL, "Russian");
  
  
  string mystr;
  cout<<"������� ���� ������"<<endl;
  getline(cin, mystr);
  Is5Latin(mystr);
  system ("pause");
}
 
char Is5Latin(string str)
{
  int count=0;
  for(int i=0;i!=str.size();i++)
  {
    if(isalpha(str[i]))
    {
      count++;
    }
    else
      if(!isalpha(str[i]))
      {count=0;}
 
      if(count==5)
      {
        cout<<"� ����� ������ ���� 5 �������� � ���"<<endl;
        return 0;
        
      }
  }
  
  cout<<"� ����� ������ ��� 5 �������� � ���"<<endl;
}

