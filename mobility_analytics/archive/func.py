
def __CreateFeaturesDataFrame(df):
    

    target = df['Surge_Pricing_Type']
    df.drop(['Surge_Pricing_Type'], axis=1, inplace=True)


    # Make an entityset and add the entity
    es = ft.EntitySet(id = 'signa')
    es.entity_from_dataframe(entity_id = 'data', dataframe = df, 
                            index = 'Trip_ID')

    # Run deep feature synthesis with transformation primitives
    feature_matrix, feature_defs = ft.dfs(entityset = es, target_entity = 'data',
                                        trans_primitives = ['add_numeric', 'multiply_numeric'])
    feature_matrix = feature_matrix.reset_index()
    feature_matrix['Surge_Pricing_Type'] = cab_target
    return(feature_matrix)