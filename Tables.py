import streamlit as st

import pickle
import requests
import pandas as pd
import pdfplumber 
import requests

# import streamlit_pandas as sp


st.cache(allow_output_mutation = True)


def load_data():

    url = "https://nupco.com/wp-content/uploads/2023/02/NPT0003-23-WEBSITE-ANNOUNCEMENT-1.pdf"
    # url = "file:///C:/Users/kamran-%20khan/Kami_Practice/O_TEST_C_TST_R/OCR_PDF/NPT-0064-22-ITEM-LIST2.pdf"

    response = requests.get(url)
    with open('TEST_NEW.pdf', 'wb') as f:
        f.write(response.content)
    # with open('TEST_NEW.pdf', 'rb') as f:
    #     pdf_reader = PdfReader(f)
    #     num_pages = len(pdf_reader.pages)
    #     text = ''
    #     for page_num in range(num_pages):
    #         page = pdf_reader.pages[page_num]
    #         text += page.extract_text()


    pdf = pdfplumber.open("TEST_NEW.pdf")
    p1 = pdf.pages[0]
    table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                             "horizontal_strategy": "lines", 
                                             "snap_tolerance": 3,})
    df = pd.DataFrame(table[1:], columns=table[0])

    df.head(11)

    if None in df.columns or df.isnull().values.any() == True:
        print('yes_df')

        table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                     "horizontal_strategy": "lines", 
                                     "snap_tolerance": 4,})
        df1 = pd.DataFrame(table[1:], columns=table[0])

        if None in df1.columns or df1.isnull().values.any() == True:
            print('Yes_df1')
            table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                 "horizontal_strategy": "lines", 
                                 "snap_tolerance": 5,})
            df2 = pd.DataFrame(table[1:], columns=table[0])

            if None in df2.columns or df2.isnull().values.any() == True:
                print('Yes_df2')
                table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                             "horizontal_strategy": "lines", 
                             "snap_tolerance": 6,})
                df3 = pd.DataFrame(table[1:], columns=table[0])

                if None in df3.columns or df3.isnull().values.any() == True :
                    print('Yes_df3')
                    table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                 "horizontal_strategy": "lines", 
                                 "snap_tolerance": 7,})
                    df4 = pd.DataFrame(table[1:], columns=table[0])

                    if None in df4.columns or df4.isnull().values.any() == True:
                        print('Yes_df4')
                        table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                     "horizontal_strategy": "lines", 
                                     "snap_tolerance": 8,})
                        df5 = pd.DataFrame(table[1:], columns=table[0])

                        if None in df5.columns or df5.isnull().values.any() == True :
                            print('Yes_df5')
                            table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                         "horizontal_strategy": "lines", 
                                         "snap_tolerance": 9,})
                            df6 = pd.DataFrame(table[1:], columns=table[0])

                            if None in df6.columns or df6.isnull().values.any() == True :
                                print('Yes_df6')
                                table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                             "horizontal_strategy": "lines", 
                                             "snap_tolerance": 10,})
                                df7 = pd.DataFrame(table[1:], columns=table[0])

                                if None in df7.columns or df7.isnull().values.any() == True :
                                    print('Yes_df7')
                                    table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                                 "horizontal_strategy": "lines", 
                                                 "snap_tolerance": 11,})
                                    df8 = pd.DataFrame(table[1:], columns=table[0])

                                    if None in df8.columns or df8.isnull().values.any() == True:
                                        print('Yes_df8')
                                        table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                                     "horizontal_strategy": "lines", 
                                                     "snap_tolerance": 12,})
                                        df9 = pd.DataFrame(table[1:], columns=table[0])


                                        if None in df9.columns or df9.isnull().values.any() == True :
                                            print('Yes_df9')
                                            table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                                         "horizontal_strategy": "lines", 
                                                         "snap_tolerance": 13,})
                                            df10 = pd.DataFrame(table[1:], columns=table[0])

                                            if None in df10.columns or df10.isnull().values.any() == True:
                                                print('Yes_df10')
                                                table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                                             "horizontal_strategy": "lines", 
                                                             "snap_tolerance": 14,})
                                                df11 = pd.DataFrame(table[1:], columns=table[0])

                                                if None in df11.columns or df11.isnull().values.any() == True :
                                                    print('Yes_df11')
                                                    table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                                                 "horizontal_strategy": "lines", 
                                                                 "snap_tolerance": 15,})
                                                    df12 = pd.DataFrame(table[1:], columns=table[0])

                                                    if None in df12.columns or df12.isnull().values.any() == True:
                                                        print('Yes_df12')
                                                        table = p1.extract_table(table_settings={"vertical_strategy": "lines", 
                                                                     "horizontal_strategy": "lines", 
                                                                     "snap_tolerance": 16,})
                                                        df13 = pd.DataFrame(table[1:], columns=table[0])


                                                    else:
                                                        print('df12')
                                                        print(df12.head())
                                                        df_t = df12
                                                else:
                                                    print('df11')
                                                    print(df11.head())
                                                    df_t = df11
                                            else:
                                                print('df10')
                                                print(df10.head())
                                                df_t = df10
                                        else:
                                            print('df9')
                                            print(df9.head(14))
                                            df_t = df9
                                    else:
                                        print('df8')
                                        print(df8.head())
                                        df_t = df8
                                else:
                                    print('df7')
                                    print(df7.head())
                                    df_t = df7
                            else:
                                print('df6')
                                print(df6.head())
                                df_t = df6
                        else:
                            print('df5')
                            print(df5.head())
                            df_t = df5
                    else:
                        print('df4')
                        print(df4.head())
                        df_t = df4
                else:
                        print('df3')
                        print(df3)
                        df_t = df3
            else:
                print('df2')
                print(df2.head())
                df_t = df2
        else:
            print('df1')
            print(df1.head())
            df_t = df1
    else:
        print('No')
        print('df')
        print(df.head(10))

    return (df_t)        
        
#+++++++++++++++++++++++++++++++++++++==============================================================+++++++++++++++++++++

if st.button("Satrt") :

    df1 = load_data()
    st.write(df1)
