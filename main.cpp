#include <iostream>
#include <cstdlib>
#include <list>
#include <string>
#include <cstring>
#include <iterator>
#include <fstream>
#include <cmath>

using namespace std;

class cityPoint
{
private:
    int x;
    int y;
    
    
public:
    cityPoint(int x,int y):x(x),y(y){};
    
    int get_x(){ return x; }
    int get_y(){ return y; }
    
    void set_x(int x){ this->x = x; }
    void set_y(int y){ this->y = y; }
};

class Ride
{
private:
    cityPoint start;
    cityPoint end;
    
    
public:
    Ride(int s1,int s2,int e1,int e2,int t1,int t2):start(s1,s2),end(e1,e2){};
    int get_start_point_x(){return start.get_x();}
    int get_start_point_y(){return start.get_y();}
    int get_ending_point_x(){return end.get_x();}
    int get_ending_point_y(){return end.get_y();}
};

class Vehicle
{
private:
    cityPoint position;
    int free;
    
    
public:
    Vehicle(): position(0,0), free(0){}
    int move(int a, int b)
    {
        position.set_x(abs(a - position.get_x()));
        position.set_y(abs(b - position.get_y()));
        return (position.get_x()+position.get_y());
    }
};

int main()
{
    int** Grid;
    ifstream inputF("a_example.in");
    int R,C,F,N,B,T;
    list <Ride> Rides;
    inputF >> R >> C >> F >> N >> B >> T;
    Grid = new int*[R];


    for(int i = 0; i < R; i++)
    {
        Grid[i] = new int[C];
    }

    while(inputF >> R >> C >> F >> N >> B >> T)
    {
        Ride NewRide(R,C,F,N,B,T);
        Rides.push_back(NewRide);
    }

//    for_each Ride in Rides
//    {
//        cout<<'To jest rajd!'<<endl;
//    }
}