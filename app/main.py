import pandas as pd

def read_orders_csv(file_path):
    return pd.read_csv(file_path, delimiter='\t')

def compute_monthly_revenue(orders):
    orders['order_date'] = pd.to_datetime(orders['order_date'], format='%d/%m/%y')
    orders['month'] = orders['order_date'].dt.to_period('M')
    return orders.groupby('month')['product_price'].sum()

def compute_product_revenue(orders):
    return orders.groupby('product_name')['product_price'].sum()

def compute_customer_revenue(orders):
    return orders.groupby('customerID')['product_price'].sum()

def identify_top_customers(orders, n=10):
    return orders.groupby('customerID')['product_price'].sum().nlargest(n)

if __name__ == "__main__":
    orders = read_orders_csv("https://github.com/roshniv6/Brine/blob/a8d33a5b928d47e45c11d92c841fd97be1169590/test.csv")

    monthly_revenue = compute_monthly_revenue(orders)
    product_revenue = compute_product_revenue(orders)
    customer_revenue = compute_customer_revenue(orders)
    top_customers = identify_top_customers(orders)

    print("Monthly Revenue:")
    print(monthly_revenue)

    print("\nProduct Revenue:")
    print(product_revenue)

    print("\nCustomer Revenue:")
    print(customer_revenue)

    print("\nTop 10 Customers:")
    print(top_customers)
