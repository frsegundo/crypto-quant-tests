# crypto-quant-tests
## Testing trading ideas in crypto markets

As I try to apply to crypto markets some techniques already widely used in tradional markets, I will share the few success and many mistakes here through python scripts.

### /studies

Maybe a tough as to execute, there is the phase to think and research trading ideas. In this folder there will be some scripts used in these steps. 

[/studies/studiesLib.py](https://github.com/frsegundo/crypto-quant-tests/blob/main/studies/studiesLib.py) 

I am never sure if this is a good practice or not, but i like to concentrated too operational functions in a separated module. Why?
  1 - So i can use the same function in another script
  2 - To keep the main script clean, which makes future analyses really easier.
  
[/studies/tradingData.py](https://github.com/frsegundo/crypto-quant-tests/blob/main/studies/tradingData.py)

Basically, extract some volume data from FTX Perpetual Contracts. 

*Perpetuals are the crypto derivatives with deepest liquidity, besides that they have a interesting characteristic: not having a delivery time (perpetuals), the way they make the contract price to stay close to the underlying asset (the index, a proxy for the spot) is by charging a fee from the buyers (sellers) if the perpetual price is higher (lower) than the spot price, giving that fee for the sellers (buyers). Almost like a swap, interesting right?* -> [Binance guide to understand it](https://www.binance.com/en/support/faq/d2a1afd5f829455c9ded23f0ca561a40)

Why do I care about volume? Some strategies works better for markets with deep liquidity and lower spreads, some work in the opposite way, is always good to understand where you are stepping in.

To get the volume data a more usual approach would be to read the [FTX API Documentation](https://docs.ftx.com/#overview) and see the methods that provide this kind of data. For those who want to work in crypto, having a basic understanding of these documentations is really useful, these exchanges provide a great amount of data for us to have fun with. Fortunately, in the fund i work for, we have a proprietary solution to get data (redis, a special kind of database), which save lots of time when doing this kind of research.
