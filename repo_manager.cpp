// Repository manager for testing
#include <vector>
#include <string>

class RepoManager {
private:
    std::vector<std::string> repositories;
    
public:
    void addRepository(const std::string& repo) {
        repositories.push_back(repo);
    }
    
    size_t getCount() const {
        return repositories.size();
    }
};

