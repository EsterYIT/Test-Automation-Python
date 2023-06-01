import allure
import test_cases.conftest as conf


class DBActions:

    @staticmethod
    @allure.step('Query Builder')
    def query_builder(columns, table_name, where_name, where_value):
        cols = ','.join(columns)
        query = "SELECT " + cols + " FROM " + table_name + " WHERE " + where_name + " = '" + where_value + "'"
        return query

    @staticmethod
    @allure.step('Get Query Results')
    def get_query_result(columns, table_name, where_name, where_value):
        query = DBActions.query_builder(columns, table_name, where_name, where_value)
        db_cursor = conf.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        return result  #Returns a List of Tuples