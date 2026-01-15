// Network utilities for API communication
#include <string>
#include <curl/curl.h>

namespace NetworkUtils {
    class HTTPClient {
    private:
        CURL* curl;
        std::string baseUrl;
        
    public:
        HTTPClient(const std::string& url) : baseUrl(url) {
            curl = curl_easy_init();
        }
        
        ~HTTPClient() {
            if (curl) {
                curl_easy_cleanup(curl);
            }
        }
        
        std::string get(const std::string& endpoint) {
            std::string response;
            if (curl) {
                std::string url = baseUrl + endpoint;
                curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
                curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeCallback);
                curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
                curl_easy_perform(curl);
            }
            return response;
        }
        
    private:
        static size_t writeCallback(void* contents, size_t size, 
                                   size_t nmemb, std::string* data) {
            data->append((char*)contents, size * nmemb);
            return size * nmemb;
        }
    };
}

