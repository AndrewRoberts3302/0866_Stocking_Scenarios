from b_read_in_the_data_EDIT import df, huk_segment, mcbc_products, mcbc_outlets
from a_parameters_EDIT_THIS import control_product, activation_product
import numpy as np


# # Find the Control Products in the data.
# p = df[["product"]]
# p = p[p["product"].str.contains(control_product)]
# p = p.drop_duplicates()
# print("\nProducts in the data containing the control product name are:\n", p, "\n")
#
# # Find the Activation products in the data.
# p = df[["product"]]
# p = p[p["product"].str.contains(activation_product)]
# p = p.drop_duplicates()
# print("\nProducts in the data containing the activation product name are:\n", p, "\n")
#
# print(df.head(100))

# Find the Control Products in the data that exactly match the control product name.
p_control = df[["product"]]
p_control = p_control[p_control["product"] == control_product]
p_control = p_control.drop_duplicates()
print("\nProducts in the data exactly matching the control product name are:\n", p_control, "\n")

# Find the Activation Products in the data that exactly match the activation product name.
p_activation = df[["product"]]
p_activation = p_activation[p_activation["product"] == activation_product]
p_activation = p_activation.drop_duplicates()
print("\nProducts in the data exactly matching the activation product name are:\n", p_activation, "\n")

# print(df.head(100))