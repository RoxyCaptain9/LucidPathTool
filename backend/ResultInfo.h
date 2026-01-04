#pragma once
#include <string>
#include <cstdint>
using namespace std;

class ResultInfo {
public:
    string name;
    string path;
    uintmax_t size; 

    //Конструктор
    ResultInfo(string n, string p, uintmax_t s);
    string toJson() const;
};
