import awswrangler as wr
for file in wr.s3.list_objects('s3://data_store/Release 3.5/MCS_2020-12'):
    print('/n Source file name: ', file)
    old_emp_df = wr.s3.read_csv(path=file, sep='|')
    print('Source data >>>')
    print(old_cost_center_df)
    new_emp_df = old_cost_center_df[['referenceID', 'name']]
    new_emp_df.rename(columns={'referenceID': 'Emp_ID', 'name': 'Emp_Name'}, inplace=True)
    print('Transformed data >>>')
    print(new_emp_df)
    wr.s3.to_csv(df=new_emp_df, path="s3://MCS/local_dev/emp/sj-dev/" + str(file).replace('s3://MCS/prod/emp/center2/', ''), index=False, sep='|')
