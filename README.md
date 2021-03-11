# How to deploy

```pip install virtualenv```
```virtualenv venv --python=python3```
```source venv/bin/activate```
```python main.py```



# KAMBISTA
URL: https://kambista.com
SALE PRICE: //div[@class="km_calc-encabezado"]/strong[@id="valventa"]/text()
PURCHASE PRICE: //div[@class="km_calc-encabezado"]/strong[@id="valcompra"]/text()

# REXTIE
URL: https://www.rextie.com
SALE PRICE: //div[@class="price sell active"]/div[@class="amount"]/span[@class="number"]/text()
PURCHASE PRICE: //div[@class="price buy active"]/div[@class="amount"]/span[@class="number"]/text()