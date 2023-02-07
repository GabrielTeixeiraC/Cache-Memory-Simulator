# Cache Memory Simulator

This program was developed by:

[Gabriel Lima Barros](https://github.com/GabrielLimab)

[Gabriel Teixeira Carvalho](https://github.com/GabrielTeixeiraC)

[Thiago Pádua de Carvalho](https://github.com/paduathiago)

To run the simulator, create a .txt file with the memory addresses and pass the name of this file in the command line along with the other arguments when calling the program.
The passing of parameters follows the format below:

     python3 simulator.py <cache size> <line size> <group size> <file name>

## Example:

### file.txt 

     0xDEABEEF
     0x00000000
     0x12345678

### Input: 
     python3 simulator.py 4096 1024 4 file.txt

### Output
     
     ================
     IDX V ** ADDR **
     000 1 0x0037AB6F
     001 0
     002 0
     003 0
     ================
     IDX V ** ADDR **
     000 1 0x0037AB6F
     001 1 0x00000000
     002 0
     003 0
     ================
     IDX V ** ADDR **
     000 1 0x0037AB6F
     001 1 0x00000000
     002 1 0x00048D15
     003 0
