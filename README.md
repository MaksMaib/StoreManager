# StoreManager

This is a small store maintenance project to learn the basics of OOP. 
It allows you to track the receipts and sale of goods. Calculate expenses, income, profit for all time and for periods of time.

The application saves data changes to the *data* folder and creates it automatically.
To work in test mode, this package contains test data.
Remove it to start from scratch.

## Requirements
* pandas

**Note**:

You can install all the python packages you needed by running:
```bash
pip install -r requirements.txt
```

## Start application
```bash
python main.py 
```

## Available features

| Command                         | Description                 |
| :---                            |                         ---:|
|help| show available features|
|receive **product price quantity** | receiving                   |
|sell **product price quantity**    | selling                    |
|goods_list                     | incoming and outgoing items |
|n_goods **product**                |quantity of selected item    |
|expenses                       |cost of purchasing items     |
|income                         |cost of sold items           |
|profit                         |shop profit                  |
|report **days**                    |report for n days                  |
|exit                           |to exit                      |

