import numpy as np

class Tariffs :
    def __init__(self, scheme_name):
        self.scheme_name = scheme_name
    
    def get_variable_tariff(self, date_time):
        return 0.30

    def get_local_solar_tariff(self,date_time):
        return 0.10

    def get_central_batt_tariff(self,date_time):
        return self.get_local_solar_tariff(date_time) + 0.02
    
    def get_retail_solar_tariff(self,date_time):
        return 0.06
    
    def get_central_batt_buy_tariff(self,date_time):
        return 0.08

    def get_fixed_tariff(self, fixed_period_minutes):
        return 1.20 * (fixed_period_minutes/(60*24))

    # Things the network is paid
    # Apply to amounts consumer each time period then sum for total network income
    def get_duos_on_grid_import(self,date_time):
        return 0.10
    
    def get_duos_on_local_solar_import(self,date_time):
        return 0.08

    def get_duos_on_central_batt_import(self,date_time):
        return 0.08

    # Things the retailer is paid
    def get_retail_income_on_grid_import(self,date_time):
        return 0.05
    
    def get_retail_income_on_local_solar_import(self,date_time):
        return 0.04

    def get_retail_income_on_central_batt_import(self,date_time):
        return 0.04