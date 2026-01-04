#pragma once
#include <vector>
#include <string>
#include "ResultInfo.h"
using namespace std;

class FileSearcher {
private:
  vector<ResultInfo> results;

public:
    void search(const string& directory, const string& searchQuery);
    void printResultsJSON();
};
