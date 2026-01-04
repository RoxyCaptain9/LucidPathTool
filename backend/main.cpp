#include <iostream>
#include <string>
#include <filesystem>
#include <clocale>
#include "FileSearcher.h"
using namespace std;
namespace fs = filesystem;

int main(int argc, char* argv[]) {
    setlocale(LC_ALL, "");
    string searchPath;
    string query;

    if (argc >= 3) {
        searchPath = argv[1];
        query = argv[2];
    } else {
        cout << "--- MANUAL MODE ---\n";
        cout << "Enter directory path (e.g. C:/Windows/Fonts): ";
        getline(cin, searchPath);

        cout << "Enter search query (e.g. arial): ";
        getline(cin, query);
    }

    FileSearcher engine;
    if (fs::exists(searchPath)) {
        engine.search(searchPath, query);
        engine.printResultsJSON();
    } else {
        cout << "[]" << endl;
    }
    return 0;
}
