import logging

from user_consumer import create_subscription
from user_publisher import create_topic

logging.getLogger().setLevel(logging.INFO)
create_topic("adapersonal", "order_req") # make sure to change the project id
create_subscription("adapersonal", "order_req", "order_req_sub")
create_topic("adapersonal", "inventory_status")
create_topic("adapersonal", "order_status")
create_topic("adapersonal", "order_status_user")
create_subscription("adapersonal", "order_status_user", "order_status_user_sub")
create_topic("adapersonal", "order_req")
create_topic("adapersonal", "inventory_status")
create_subscription("adapersonal", "inventory_status",
                    "inventory_status_sub")
create_subscription("adapersonal", "order_status","order_status_sub")
