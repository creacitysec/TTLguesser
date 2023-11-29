# TTL OS Guessing Tool

## Description
The TTL OS Guessing Tool is a simple Python script designed to guess the operating system of a remote host. It uses the Time To Live (TTL) value from the ping response, as different operating systems set different default TTL values for their IP packets.

## How It Works
1. **OS Detection**: Detects the OS of the host running the script to use the correct ping command syntax.
2. **Ping Execution**: Pings the specified IP address(es) and captures the TTL value from the response.
3. **OS Guessing**: Makes an educated guess about the target system's OS based on the TTL value (Windows typically uses 128, Unix/Linux uses 64).
4. **Input Options**: Users can input a single IP with `-i` or a list of IPs from a file with `-l`.

## Reference on TTL and OS
For more information on how TTL varies by OS, see: [TTL and Operating Systems](https://en.wikipedia.org/wiki/Time_to_live#Default_TTL_values_in_different_operating_systems)

## Note
This tool is a basic utility for quick guesses and not an advanced diagnostic tool.
