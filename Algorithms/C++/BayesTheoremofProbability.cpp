//Baye's Theorem is used to calculate probailities of events based on prior knowledge
//add arguments -static-libgcc and -static-libstdc++ to command line when using MinGW EXE compiler for windows
//Bash Command to create Favicon Resource Object x86_64-w64-mingw32-windres resources.rc myresources.o
//Bash Command to compile as EXE with Favicon Resource Object
//x86_64-w64-mingw32-g++ -o BayesTheoremofProbability.exe BayesTheoremofProbability.cpp myresources.o -static-libstdc++ -static-libgcc
#include <iostream>
#include <cmath>
using namespace std;
double BayesProbability(double xA, double xB)
{
    double xFirstEvent = xA;
    double xSecondEvent = xB;
    double xMarginofError = (1-xSecondEvent);
    double xUnaffected = (1-xFirstEvent);
    double xProbability = ((xFirstEvent*xSecondEvent)/((xFirstEvent*xSecondEvent)+(xUnaffected*xMarginofError)));
    cout << ceil((xFirstEvent*100)) << " percent of the population have been diagnosed for Technophobia using a test with " << ceil((xSecondEvent*100)) << " percent accuracy and a " << ceil((xMarginofError*100)) << " percent margin of error, which means there's a " << ceil((xProbability*100)) << " percent probability that you may also suffer from Tehcnophobia. \n On a positive note, however " << ceil((xUnaffected*100)) << " percent of our Cyber Citizens are most likely to be Source Code Fanatics! \n CyberNation: Code or DIY!" << endl;
    return xProbability;
}
int main()
{
int xExit = 0;
BayesProbability(.05, .9);
cout << "Press any key and press enter to exit.";
cin >> xExit;
}
