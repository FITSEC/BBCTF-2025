#include <unistd.h>
#include <string.h>
#include <stdio.h>

int shuffle_arr[29][2] = {{28, 9},
{27, 15},
{26, 11},
{25, 8},
{24, 13},
{23, 22},
{22, 11},
{21, 22},
{20, 15},
{19, 6},
{18, 24},
{17, 7},
{16, 14},
{15, 9},
{14, 28},
{13, 13},
{12, 19},
{11, 5},
{10, 28},
{9, 2},
{8, 1},
{7, 17},
{6, 3},
{5, 27},
{4, 17},
{3, 20},
{2, 19},
{1, 12},
{0, 22},
};

char enc[29] = "h0w{3winsh}3tslc_e3_sf3!t1cs_";

int main() {
    for (int i = 0; i < 29; i++) {
        int index_1 = shuffle_arr[i][0];
        int index_2 = shuffle_arr[i][1];
        char tmp = enc[index_1];
        enc[index_1] = enc[index_2];
        enc[index_2] = tmp;
    }
    printf(enc);
    puts("\n");
}
