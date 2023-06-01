import allure

from extensions.db_actions import DBActions
from work_flows.web_flows import WebFlows


class DBFlows:
    @staticmethod
    @allure.step('Login to Grafana via database flow')
    def login_conduit_via_db():
        columns = ['email', 'password']
        result = DBActions.get_query_result(columns, 'users', 'id', '3')
        WebFlows.sign_in_to_conduit_web_with_db_details(result[0][0], result[0][1])