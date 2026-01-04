#include "FileSearcher.h"
#include <iostream>
#include <filesystem>
using namespace std;
namespace fs = filesystem;

void FileSearcher::search(const string& directory, const string& searchQuery) {
    results.clear();

    try {
        for (const auto& entry : fs::recursive_directory_iterator(directory, fs::directory_options::skip_permission_denied)) {
            try {
                if (entry.is_regular_file()) {
                    string filename = entry.path().filename().string();
                    if (filename.find(searchQuery) != string::npos) {
                        results.emplace_back(filename, entry.path().string(), entry.file_size());
                    }
                }
            } catch (...) {
                continue; 
            }
        }
    } catch (const fs::filesystem_error& e) {
        cerr << "Error accessing directory: " << e.what() << endl;
    }
}

void FileSearcher::printResultsJSON() {
    cout << "[";
    for (size_t i = 0; i < results.size(); ++i) {
        cout << results[i].toJson();
        if (i < results.size() - 1) cout << ",";
    }
    cout << "]" << endl;
}
