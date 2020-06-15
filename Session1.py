"""
			Day1			Profits					SBI
OnePlus		150 units		200.27 per phone		3000.12 per phone
			Day2			Profits					SBI
OnePlus		250 units		200.27					3000.12
			Day3			Profits					SBI
OnePlus		100 units		200.27					3000.12


			Day1			Profits					SBI
HomeAppl 	120 units		50	per appl			100 per appl
			Day2			Profits					SBI
HomeAppl 	220 units		50	per appl			100 per appl
			Day3			Profits					SBI
HomeAppl 	180 units		50	per appl			100 per appl

"""


# MODEL : Data for your Problem Statement
# onePlusDay1Sales = 150      # A generic Programming Language Variable name declaration
one_plus_day_1_sales = 150    # Python Way :)
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profits_to_amazon_from_one_plus = 200.27

discounts_from_sbi_to_one_plus = 3000.12

home_appl_day1_sales = 120
home_appl_day2_sales = 220
home_appl_day3_sales = 180

profits_to_amazon_from_home_appl = 50

discounts_from_sbi_to_home_appl = 3000.12

# CONTROLLER : Mathematical Computation or Logical Processing on model

total_one_plus_sales = one_plus_day_1_sales + one_plus_day_2_sales + one_plus_day_3_sales
total_home_appl_sales = home_appl_day1_sales + home_appl_day2_sales + home_appl_day3_sales

net_one_plus_profits = total_one_plus_sales * profits_to_amazon_from_one_plus
net_home_appl_profits = total_home_appl_sales * profits_to_amazon_from_home_appl

# View : User Interface to display the data as Text
print("One Plus Sale Profits Made by Amazon", net_one_plus_profits)
print("Home Appl Sale Profits Made by Amazon", net_home_appl_profits)

# Computation : Where do Amazon made more Profits ?

if net_one_plus_profits > net_home_appl_profits:
    print("Amazon Made more Profits on One Plus by", (net_one_plus_profits - net_home_appl_profits))
else:
    print("Amazon Made more Profits on Home Appl by", (net_home_appl_profits - net_one_plus_profits))

"""
    Assignment #1
        Evaluate SBI should invest in selling credit cards to Home Appliances Shops or Mobile Shops to have more customers
    
    Assignment #2
        Evaluate if SBI spends more on Home Appliances on Amazon Portal can it get more customers and can Amazon have the similar profiits
    
    Assignment #3
        Install Git on your System -> Please refer google or any youtube video	

"""