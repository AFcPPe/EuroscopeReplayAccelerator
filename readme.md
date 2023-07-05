# Euroscope Replay Accelerator

Euroscope Replay Accelerator is an open-source project written in native Python 3.11. It allows you to accelerate Euroscope's replay files by modifying the time data within the file. By adjusting the timestamps, you can effectively speed up the playback of Euroscope's recorded sessions.

## Usage

To use Euroscope Replay Accelerator, follow these steps:

1. Open the source code file `replay_accelerator.py` in a text editor.
2. Modify the following variables:
   - `inputFilePath`: Specify the path to the input replay file (`replay.txt`).
   - `outputFilePath`: Specify the desired path for the output accelerated replay file (`result.txt`).
   - `multiplyTime`: Set the acceleration factor by adjusting the value of `multiplyTime`. For example, if you set `multiplyTime` to 5, the resulting replay will be five times faster than the original. In principle, this number should not exceed 5 because the position of the aircraft is typically updated every five seconds.
3. Save the modified source code file.

After configuring the variables, run the script using a Python interpreter. The accelerated replay file will be generated at the specified output file path.

**Note:** Ensure that you have Python 3 installed before running the script. (Python3.11 is strongly recommended).

## How it Works

Euroscope Replay Accelerator modifies the provided Euroscope replay file by adjusting the timestamps within the file. The script reads the input replay file (`replay.txt`) and processes each line containing timestamp data. It calculates the new timestamp based on the acceleration factor (`multiplyTime`) and updates the corresponding line in the output replay file (`result.txt`).

The general steps followed by Euroscope Replay Accelerator are as follows:

1. Read the contents of the input replay file into memory.
2. Split the replay file data into individual lines.
3. Iterate over each line of the replay data:
   - Extract the original timestamp from the line.
   - Convert the original timestamp to a Unix timestamp.
   - If it is the first timestamp encountered, save it as the reference timestamp.
   - Calculate the processed timestamp by adjusting the original timestamp based on the acceleration factor.
   - Convert the processed timestamp back to the desired format.
   - Update the line with the adjusted timestamp in the result data.
4. Write the modified replay data to the output file (`result.txt`).

Euroscope Replay Accelerator doesn't require any external libraries and operates solely on native Python functionality.

## License

Euroscope Replay Accelerator is open-source software licensed under the [GPL v3](LICENSE).

## Disclaimer

Euroscope Replay Accelerator is provided as-is without any warranty. The developers are not responsible for any consequences resulting from the use of this software.

Please use Euroscope Replay Accelerator responsibly and respect the terms and conditions of the Euroscope software.

## Contact

If you have any questions, suggestions, or feedback, you can reach us at [harry6184@skylineflyleague.cn](mailto:harry6184@skylineflyleague.cn). We would be happy to hear from you!