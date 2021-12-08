from . import formatreader
import pandas as pd

class FormatReaderXLS(formatreader.FormatReader):

    def __init__(self, name, orchestrator_ref, settings): 
        super().__init__(name = name, orchestrator_ref = orchestrator_ref, settings = settings)
    
    def read_df(self, file_path, dls):
        file_bytes = self._storage_proxy.read_file(file_path).get()
        if file_bytes != '':
            sheet = dls['acquisition']['channel']['sheet']
            df = pd.read_excel(file_bytes, sheet, header=None)
            df = df.dropna(how='all').dropna(how='all', axis=1)
            cols = df.iloc[0]
            df  = pd.DataFrame(df.values[1:], columns=cols)
        else:
            raise ValueError('can not read from empty bytes')
        return df