import awswrangler as wr
for file in wr.s3.list_objects('s3://data_store/Release 3.5/workday_2018-1'):
    print('/n Source file name: ', file)
    old_cost_center_df = wr.s3.read_csv(path=file, sep='|')
    print('Source data >>>')
    print(old_cost_center_df)
    new_cost_center_df = old_cost_center_df[['referenceID', 'name']]
    new_cost_center_df.rename(columns={'referenceID': 'Cost_Center_ID', 'name': 'Cost_Center_Name'}, inplace=True)
    print('Transformed data >>>')
    print(new_cost_center_df)
    wr.s3.to_csv(df=new_cost_center_df, path="s3://procoreit-airflow-stage/local_dev/workday/sj-dev/dim_cost_center/" + str(file).replace('s3://procoreit-airflow-stage/prod/workday/dim_cost_center/', ''), index=False, sep='|')