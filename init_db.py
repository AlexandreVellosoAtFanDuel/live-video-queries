from sports import Sport

QUERY_INIT_TBL_TYPE_SPORTS = f"""
INSERT INTO DATA_VIDEO.TBL_TYPE_SPORTS
(SPORTS_ID, SPORTS_DESCRIPTION)
VALUES(%1, '%2');
"""

def init_tbl_type_sports():
    for sport in Sport:
        query = QUERY_INIT_TBL_TYPE_SPORTS\
            .replace('%1', str(sport.value))\
            .replace('%2', sport.description)
        print(query)

if __name__ == "__main__":
    init_tbl_type_sports()