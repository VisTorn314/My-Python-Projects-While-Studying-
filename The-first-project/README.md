# Conventor Currency

A simple converter of rubles into US dollars with interface in the command line.  
The program requests the amount in rubles, multiplies it by a fixed rate (1 RUB = 0.0128 USD) and outputs the result.

![Python](https://img.shields.io/badge/Python-3.x-blube?logo=python)
![Licensee](https://img.shields.io/badge/License-MIT-green)

---

## 📦 Installation

1. Make sure you have Python 3.x installed.
2. Download the file `Conventor_currency.py`.
3. Launch in the terminal:
   ```bash
   python Conventor_currency.py
   ```

Usage

    When starting, the ASCII logo is displayed.
    Enter the amount in rubles (whole number).
    The program will show the equivalent in dollars.
    After each calculation, you will be asked:
    Continue (Y/N)?
        Click N – the program will be completed.
        Press Y – the program will continue to work.
        (Please note: this is non-standard behavior, see the section "Familiar problems".)

� Employee Example
text

Enter the rubles for conversion into dollars: 1000
Rubles: 1000 in Dollars: 12.8
Continue (Y/N)? N
Enter the rubles for conversion into dollars: 500
Rubles: 500 in Dollars: 6.4
Continue (Y/N)? N
The program is closed


Plans for improvement

    Change the condition of exit: complete under 'N', continue with 'Y'.
    Add correct processing of exceptions (re-enter for input request when an error).
    Remove the calculation at money == 0 or process it separately.
    Make the course dynamic (for example, request from the API).
    Add the possibility of conversion to other currencies.

📄 License

Distributed under the MIT license.
You can freely use, modify and distribute this code.

✍️ ️Author:
VisTorn314

[github](https://github.com/VisTorn314)