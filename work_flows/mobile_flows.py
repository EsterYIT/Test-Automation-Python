import allure
import utilities.manage_pages as page
from extensions.mobile_actions import MobileActions


class MobileFlows:

    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def calculate_mortgage(amount, term, rate):
        MobileActions.update_text(page.mobile_mortgage_main.get_amount_field(), amount)
        MobileActions.update_text(page.mobile_mortgage_main.get_term_field(), term)
        MobileActions.update_text(page.mobile_mortgage_main.get_rate_field(), rate)
        MobileActions.tap(page.mobile_mortgage_main.get_calc_btn())
