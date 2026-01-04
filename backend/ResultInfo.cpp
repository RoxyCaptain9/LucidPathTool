#include "ResultInfo.h"
#include <algorithm>
using namespace std;

ResultInfo::ResultInfo(string n, string p, uintmax_t s)
    : name(n), path(p), size(s) {}

string ResultInfo::toJson() const {
    string safePath = path;
    replace(safePath.begin(), safePath.end(), '\\', '/');

    return "{\"name\": \"" + name + 
           "\", \"path\": \"" + safePath + 
           "\", \"size\": \"" + to_string(size) + " bytes\"}";
          }
