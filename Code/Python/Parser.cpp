#include <iostream>
#include <map>
#include <string>
#include <variant>
#include <vector>

using ValueType = std::variant<int, double, std::string, std::vector<std::string>>;

/*
Variables:
command: Incoming string from serial
instructions: Map containing processed instruction sets
*/

std::string command =
    "IT:1;L1:0;L2:0;L4:1;L3:0;S1:1,=,200.39;hT:1;y1:0;y2:0;u4:1;o3:0";

// Function for reading
std::map<std::string, std::vector<std::string>> readCommand(std::string x)
{
    std::map<std::string, std::vector<std::string>> instructions{};

    // Separate command into individual instructions using ';'
    int start = 0;

    while (start < x.length())
    {
        int end = x.find(';', start);

        if (end == std::string::npos)
            break;

        std::string item = x.substr(start, end - start);

        // Find ':'
        size_t delimiter = item.find(':');

        if (delimiter != std::string::npos)
        {
            std::string key = item.substr(0, delimiter);
            std::string value = item.substr(delimiter + 1);

            // Separate values using ','
            std::vector<std::string> values;

            int valueStart = 0;

            while (valueStart < value.length())
            {
                int comma = value.find(',', valueStart);

                if (comma == std::string::npos)
                {
                    // Last value
                    values.push_back(value.substr(valueStart));
                    break;
                }

                values.push_back(value.substr(valueStart, comma - valueStart));

                valueStart = comma + 1;
            }

            instructions[key] = values;
        }

        start = end + 1;
    }

    return instructions;
}

int main()
{
    std::map<std::string, std::vector<std::string>> instructions =
        readCommand(command);

    // Print the map
    for (const auto& [key, values] : instructions)
    {
        std::cout << key << " -> ";

        for (const std::string& value : values)
        {
            std::cout << "[" << value << "]";
        }

        std::cout << std::endl;
    }
}