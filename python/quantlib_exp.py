from QuantLib import *
maturity_date = Date(15, 1, 2016)
spot_price = 127.62
strike_price = 130
volatility = 0.20 # the historical vols for a year
dividend_rate =  0.0163
option_type = Option.Call
risk_free_rate = 0.001
day_count = Actual365Fixed()
calendar = UnitedStates()
calculation_date = Date(8, 5, 2015)
Settings.instance().evaluationDate = calculation_date
payoff = PlainVanillaPayoff(option_type, strike_price)
settlement = calculation_date
am_exercise = AmericanExercise(settlement, maturity_date)
american_option = VanillaOption(payoff, am_exercise)
spot_handle = QuoteHandle(
            SimpleQuote(spot_price)
        )
flat_ts = YieldTermStructureHandle(
    FlatForward(calculation_date,
                risk_free_rate,
                day_count)
)
dividend_yield = YieldTermStructureHandle(
    FlatForward(calculation_date,
                dividend_rate,
                day_count)
)
flat_vol_ts = BlackVolTermStructureHandle(
    BlackConstantVol(calculation_date,
                     calendar,
                     volatility,
                     day_count)
)
bsm_process = BlackScholesMertonProcess(spot_handle,
                                        dividend_yield,
                                        flat_ts,
                                        flat_vol_ts)
binomial_engine = BinomialVanillaEngine(bsm_process, "crr", 100)
american_option.setPricingEngine(binomial_engine)
import pdb; pdb.set_trace()
print(american_option.vega())
