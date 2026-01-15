// File handler utility for testing
#include <fstream>
#include <string>
#include <vector>

class FileHandler {
public:
    static bool readFile(const std::string& filename, std::string& content) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            return false;
        }
        content.assign((std::istreambuf_iterator<char>(file)),
                       std::istreambuf_iterator<char>());
        return true;
    }
    
    static bool writeFile(const std::string& filename, const std::string& content) {
        std::ofstream file(filename);
        if (!file.is_open()) {
            return false;
        }
        file << content;
        return true;
    }
};

