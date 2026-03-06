
from servicenow_api.servicenow_api import Api


username = "nathan.dolor.stack.ai"
password = "l0Cx=hNBKzKeuCuaM}&X&>3OkVeevsG"
servicenow_url = "https://testgcinc.service-now.com"

client = Api(
    url=servicenow_url,
    username=username,
    password=password
)

#table = client.get_incidents(sysparm_limit=1)
# print(f"Incident: {table.model_dump()}")

#table = client.get_knowledge_articles(sysparm_limit=1)
#print(f"Incident: {table.model_dump()}")

ticket = client.get_table_records(table="ticket")
print(f"Ticket:  {ticket.model_dump()}")