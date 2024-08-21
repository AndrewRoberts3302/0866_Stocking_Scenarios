"""
Here you edit the parameters for the SQL data pulls
"""
# 717 Cider

# start_date = 20230101  # The start date of the data pull
# end_date = 20240401  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS_HUK"
# di_database = "DI_LIVE.dbo.vw_DI_Heineken"
# product_class = "PT_ClassificationLevel5Description"
# product_group = "PT_CL5_CGA"
# serve_format = "PT_AT_Format"
# serve_format_predicate = "Packaged"


#######################################################################
# Normal

start_date = 20230501  # The start date of the data pull
end_date = 20240801  # The end date of the data pull, notes that this is a < statement, so is not inclusive
cs_database = "CS_LIVE.dbo.vw_CS_CUK"
di_database = "DI_LIVE.dbo.vw_DI_CUK"
product_class = "PT_CL5_CGA"
product_group = "PT_CL6_CGA"
product_group_predicate = "LAD"
serve_format = "PT_ClassificationLevel5Description"
serve_format_predicate = "Draught"


########################################################################
# 0708 Guinnes Dual Stocking Scenario

# Stocking scenario analysis for Carlsberg using their product segment.

# start_date = 20220901  # The start date of the data pull
# end_date = 20231201  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS"
# di_database = "DI_LIVE.dbo.vw_DI"
# product_class = "PT_ClassificationLevel4Description"
# product_group = "PT_ClassificationLevel5Description"
# product_group_predicate = "Total Beer"
# serve_format = "PT_AT_Format"
# serve_format_predicate = "Draught"


##############################################################################

# 0610 CMBC Poretti Sales Stories

# Stocking scenario analysis for Carlsberg using their product segment.

# start_date = 20221201  # The start date of the data pull
# end_date = 20240301  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS"
# di_database = "DI_LIVE.dbo.vw_DI"
# product_class = "PT_ClassificationLevel4Description"
# product_group = "PT_ClassificationLevel5Description"
# product_group_predicate = "Total Beer"
# serve_format = "PT_AT_Format"
# serve_format_predicate = "Draught"
##############################################################################

# 0525 CMBC Sales Stories

# Stocking scenario analysis for Carlsberg using their product segment.

# start_date = 20220901  # The start date of the data pull
# end_date = 20231201  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS_CUK"
# di_database = "DI_LIVE.dbo.vw_DI_CUK"
# product_class = "PT_AT_Segment"  # This contains World Lager, Cask Ale etc.
# product_class = "PT_CL3_CGA"  # This contains "Total Ale (Cask)"
# # product_group = "PT_CL4_CGA"  # This contains Total Lager, Total Vodka etc.
# product_group = "PT_CL5_CGA"  # This contains Total Beer.
# product_group_predicate = "Total Beer"  # The predicate to use on the product group.
# serve_format = "PT_AT_Format"  # The column to use for serve formats in HUK data.
# # serve_format = "PT_ClassificationLevel5Description"  # The column to use for serve formats in CUK and Diageo data.
# serve_format_predicate = "= N'Draught'"  # Select for Draught serves.

##############################################################################

# SB163 CMBC Super Premium Sales Stories
# start_date = 20220101  # The start date of the data pull
# end_date = 20230401  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS_HUK"
# di_database = "DI_LIVE.dbo.vw_DI_Heineken"
# # product_class = "PT_AT_Segment"  # This contains World Lager, Cask Ale etc.
# product_class = "PT_CL3_CGA"  # This contains "Total Ale (Cask)"
# # product_group = "PT_CL4_CGA"  # This contains Total Lager, Total Vodka etc.
# product_group = "PT_CL5_CGA"  # This contains Total Beer.
# product_group_predicate = "Total Beer"  # The predicate to use on the product group.
# serve_format = "PT_AT_Format"  # The column to use for serve formats in HUK data.
# # serve_format = "PT_ClassificationLevel5Description"  # The column to use for serve formats in CUK and Diageo data.
# serve_format_predicate = "= N'Draught'"  # Select for Draught serves.

##############################################################################

# SB153 MCBC Premium Lager Scenario Analysis parameters.
# start_date = 20220101  # The start date of the data pull
# end_date = 20230401  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS_HUK"
# di_database = "DI_LIVE.dbo.vw_DI_Heineken"
# product_class = "PT_CL3_CGA"  # This contains "Total Ale (Cask)"
# # product_class = "PT_CL4_CGA"  # This contains Total Lager.
# product_group = "PT_CL4_CGA"  # This contains Total Lager.
# # product_group = "PT_CL5_CGA"  # This contains Total Beer.
# # product_group_predicate = "Total Beer"  # The predicate to use on the product group.
# product_group_predicate = "Total Lager"  # The predicate to use on the product group.
# serve_format = "PT_AT_Format"  # The column to use for serve formats in HUK data.
# serve_format_predicate = "= N'Draught'"  # Select for Draught serves.

# SB141 Greene King Guinness Replacement Analysis parameters.
# start_date = 20211201  # The start date of the data pull
# end_date = 20230301  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS_HUK"
# di_database = "DI_LIVE.dbo.vw_DI_Heineken"
# product_class = "PT_CL3_CGA"  # This contains "Total Ale (Cask)"
# product_group = "PT_CL5_CGA"  # This contains Total Beer.
# product_group_predicate = "Total Beer"  # The predicate to use on the product group.
# serve_format = "PT_AT_Format"  # The column to use for serve formats in HUK data.
# serve_format_predicate = "= N'Draught'"  # Select for Draught serves.

# SB134 CMBC Sales Stories.
# start_date = 20220101  # The start date of the data pull
# end_date = 20230401  # The end date of the data pull, notes that this is a < statement, so is not inclusive
# cs_database = "CS_LIVE.dbo.vw_CS_HUK"
# di_database = "DI_LIVE.dbo.vw_DI_Heineken"
# product_class = "PT_CL3_CGA"  # This contains Premium World Lager, Premium 4% Lager etc.
# product_group = "PT_CL4_CGA"  # This contains Total Lager, Total Vodka etc.
# product_group_predicate = "Total Lager"  # The predicate to use on the product group.
# serve_format = "PT_AT_Format"  # The column to use for serve formats.
# serve_format_predicate = "= N'Draught'"  # Select for Draught serves.

# Select the dates to use for the data pull.
# Ideally this should be a 15 month period.
# start_date = 20211201  # The start date of the data pull
# end_date = 20230201  # The end date of the data pull, notes that this is a < statement, so is not inclusive

# Select the databases to use - HUK.
# cs_database = "CS_LIVE.dbo.vw_CS_HUK"
# di_database = "DI_LIVE.dbo.vw_DI_Heineken"
# Select the databases to use - CUK.
# cs_database = "CS_LIVE.dbo.vw_CS_CUK"
# di_database = "DI_LIVE.dbo.vw_DI_CUK"

# Select product data to use.
# product_class = "PT_CL5_CGA"  # This contains Total Beer, Total Cider etc.
# product_group = "PT_CL6_CGA"  # This contains LAD, Spirits etc.
# serve_format = "PT_AT_Format"  # The column to use for serve formats.

# Product data to use for CUK Draught Lager projects.
# product_class = "PT_AT_Segment"  # This contains World Lager, Cask Ale etc.
# product_group = "PT_CL4_CGA"  # This contains Total Lager, Total Vodka etc.
# product_group_predicate = "Total Lager"  # The predicate to use on the product group.
# serve_format = "PT_ClassificationLevel5Description"  # The column to use for serve formats in CUK and Diageo data.

# Product data to use for HUK Draught Lager projects.
# product_class = "PT_CL3_CGA"  # This contains Premium World Lager, Premium 4% Lager etc.
# product_group = "PT_CL4_CGA"  # This contains Total Lager, Total Vodka etc.
# product_group_predicate = "Total Lager"  # The predicate to use on the product group.
# serve_format = "PT_AT_Format"  # The column to use for serve formats in HUK data.

# Serve format predicate
# serve_format_predicate = "in (N'Draught', N'Packaged')"  # Select for both serve formats.
# serve_format_predicate = "= N'Draught'"  # Select for Draught s