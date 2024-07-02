#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <cstdint>
#include <bitset>

bool isPrime(uint64_t n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (uint64_t i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

long tribonacci(int n, std::unordered_map<int, uint64_t>& memo) {
    if (n < 3) return 1;
    if (memo.find(n) != memo.end()) return memo[n];
    memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo);
    return memo[n];
}

uint64_t FUN_00101230(int param_1, std::unordered_map<int, uint64_t>& memo) {
    int local_1c = param_1;
    
    while (true) {
        long uVar2 = tribonacci(local_1c, memo);
        if (isPrime(uVar2)) return uVar2;
        local_1c++;
    }
}

uint8_t FUN_0010126b(int param_1, std::unordered_map<int, uint64_t>& memo) {
    ushort local_1a = FUN_00101230(param_1, memo);
    local_1a = ~local_1a;
    int local_18 = 0;

    for (int i = 0; i < 8; ++i) {
        int local_10 = 0;

        for (int j = 0; j < 0xba04015; ++j) {
            local_10 = (ushort)(local_1a >> 12 ^ local_1a >> 8 ^ local_1a >> 10 ^ local_1a >> 11) & 1;
            local_1a = (ushort)((local_10 << 15) | (local_1a >> 1));
        }
        local_18 = local_18 * 2 + local_10;
    }

    return local_18;
}

int main() {
    int local_34 = 0x25;
    int local_38 = 0;

    std::vector<uint8_t> DAT_00104020 = {
        0x6e, 0x68, 0x78, 0x08, 0xb0, 0x77, 0x45, 0x00,
        0x6f, 0x89, 0x8b, 0x04, 0xbc, 0xe8, 0xc2, 0x99,
        0x3b, 0xdc, 0x0b, 0x43, 0x4f, 0x21, 0x72, 0x56,
        0xc8, 0xdd, 0xe3, 0xe8, 0x46, 0xed, 0x94, 0xd7,
        0x6f, 0x05, 0x01, 0xf4, 0xbf
    };

    std::vector<uint8_t> local_28(local_34 + 1);
    std::unordered_map<int, uint64_t> memo;

    for (local_38 = 0; local_38 < local_34; ++local_38) {
        uint8_t bVar1 = DAT_00104020[local_38];
        int iVar3 = pow(local_38, 3);
        uint8_t bVar2 = FUN_0010126b(iVar3, memo);
        local_28[local_38] = bVar1 ^ bVar2;

        for (int i = 0; i <= local_38; ++i) {
            std::cout << local_28[i];
        }

        std::cout << std::endl;
    }

    return 0;
}