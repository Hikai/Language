#include<fstream>
#include<iostream>

int main(void)
{
    std::ofstream file_out ("tmp.exe", std::ofstream::binary)

    BYTE * buf;
    file_out.rite(buf, sizeof(buf));

    return 0;
}
