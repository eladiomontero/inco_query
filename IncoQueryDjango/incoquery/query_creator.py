__author__ = 'eladio'

class QueryCreator():

    def get_querytext(self, fields):
        ## TODO CONSOLIDAR LA TABLA DE NOMBRES DE CAMPO
        regimen = fields["regimen"]
        country = fields["country"]
        db_fields = self.get_fields_db(country, regimen)
        table = self.get_table_db(country, regimen)
        querytext = "select * from " & table & "where "
        for (key,value) in fields.iteritems():
            if (key != "" and value != ""):
                querytext = querytext & key & "=" & value
        return querytext

    def get_fields_db(self, country, regimen):
        ## TODO IR A CONSULTAR LA TABLA DE VARIABLES PARA CADA PAIS.
        dict_countries = {}
        filtered_dict = {k:v for (k,v) in dict_countries.iteritems() if country in v and regimen in v}
        return filtered_dict["field_db"]

    def get_table_db(self, country, regimen):
        table = ""
        countries = {
            "Costa Rica" : "cr",
            "Panama" : "pan",
            "Venezuela" : "ven",
            "Ecuador" : "ecu"
        }

        if "export" in regimen.lower():
            table = "export"
        else:
            table = "import"

        table += "_"
        table += countries[country]
        return table


