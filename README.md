## Installation

The shell script to install all dependencies has been added. You just need to run the following command:-

```bash
./build.sh
```
If you get a permission denied error, just type the following command and then run the previous command

```bash
chmod +x build.sh
```
## Usage
The code is currently using hardcoded values. In Eval.py, y list is the bit representation of the threshold values. So for a given model these, values remain the same.
The client input is stored in list x in binary format. x[0] is the lsb of the input. Just change the client inputs and run the following command:-

```bash
python3 Eval.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
