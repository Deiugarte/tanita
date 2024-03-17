import csv
from mapping import headerMapping
import pandas as pd


def get_data_frame(user_id: int):
  with open(f'data/TANITA/GRAPHV1/DATA/DATA{user_id}.CSV') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      headers = headerMapping.keys()
      data = []
      for row in csv_reader:
          filterRow = []
          for header in headers:
              index = row.index(header)
              filterRow.append(row[index+1])
          data.append(filterRow)


      dataFormated = pd.DataFrame(data, columns = headerMapping.values())
      dataFormated.sort_values([headerMapping["DT"], headerMapping["Ti"]], ascending=[False, False], inplace=True, ignore_index= True)
      return dataFormated








