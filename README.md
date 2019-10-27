## Use
```
glu.py [file_name] [output_file] [variable_names]

#Example on file "main.cpp" and output "out.cpp":
glu.py main.cpp out.cpp var1 var2 var3
```
# Input "main.cpp"
```cpp
#include <stdio.h>
int main()
{
    int var1, var2, var3;
    return 0;
}
```
# Output "out.cpp"
```cpp
#include <stdio.h>
int main()
{
    int glu, gluglu, glugluglu;
    return 0;
}
```
