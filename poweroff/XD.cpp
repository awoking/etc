#include <cstdlib>

int main() {
    // '/s' はシャットダウン、'/t 0' はタイムアウトを0秒に設定し即時シャットダウン
    std::system("shutdown /s /t 0"); 
    return 0;
}