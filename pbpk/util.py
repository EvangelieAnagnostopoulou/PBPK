import re
import sqlite3
import numpy as np

def isnumber(bw):
    try:
        bw = float(bw)
    except ValueError:
        bw = None
    return bw

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and USER_RE.match(password)

def valid_email(email):
    return not email or EMAIL_RE.match(email)

def insert_to_db(username, name1, bw1, h1, cardiac_output1, k_met1, k_bile1, k_kidney1, max_liver1, max_kidney1, max_influx1,
                 skin_flow_factor1, skin_volume_fraction1, blood_skin_fraction1, P_skin1, Pi_skin1, kidney_flow_factor1,
                 kidney_volume_fraction1, blood_kidney_fraction1, P_kidney1, Pi_kidney1, bladder_flow_factor1, bladder_volume_fraction1,
                 blood_bladder_fraction1, P_bladder1, Pi_bladder1, blood_rest_fraction1, P_rest1, Pi_rest1, liver_flow_factor1,
                 liver_volume_fraction1, blood_liver_fraction1, P_liver1, Pi_liver1, blood_volume_fraction1, Pi_rbc1, Pi_plasma1,
                 lung_flow_factor1, lung_volume_fraction1, blood_lung_fraction1, P_lung1, Pi_lung1):
    # Creates or opens a file called models with a SQLite3 DB.
    db = sqlite3.connect('models')
    # Get a cursor object.
    cursor = db.cursor()
    # Check if table models does not exist and create it.
    cursor.execute('''CREATE TABLE IF NOT EXISTS
models(id INTEGER PRIMARY KEY, userName TEXT, modelName TEXT, bw REAL, h REAL, cardiac_output REAL,
k_met REAL, k_bile REAL, k_kidney REAL, max_liver REAL, max_kidney REAL, max_influx REAL,
skin_flow_factor REAL, skin_volume_fraction REAL, blood_skin_fraction REAL, P_skin REAL,
Pi_skin REAL, kidney_flow_factor REAL, kidney_volume_fraction REAL, blood_kidney_fraction REAL,
P_kidney REAL, Pi_kidney REAL, bladder_flow_factor REAL, bladder_volume_fraction REAL,
blood_bladder_fraction REAL, P_bladder REAL, Pi_bladder REAL, blood_rest_fraction REAL,
P_rest REAL, Pi_rest REAL, liver_flow_factor REAL, liver_volume_fraction REAL,
blood_liver_fraction REAL, P_liver REAL, Pi_liver REAL, blood_volume_fraction REAL,
Pi_rbc REAL, Pi_plasma REAL, lung_flow_factor REAL, lung_volume_fraction REAL,
blood_lung_fraction REAL, P_lung REAL, Pi_lung REAL)''')
    cursor.execute('''INSERT INTO models(userName, modelName, bw, h, cardiac_output, k_met, k_bile, k_kidney,
max_liver, max_kidney, max_influx, skin_flow_factor, skin_volume_fraction, blood_skin_fraction,
P_skin, Pi_skin, kidney_flow_factor, kidney_volume_fraction, blood_kidney_fraction, P_kidney,
Pi_kidney, bladder_flow_factor, bladder_volume_fraction, blood_bladder_fraction, P_bladder,
Pi_bladder, blood_rest_fraction, P_rest, Pi_rest, liver_flow_factor, liver_volume_fraction,
blood_liver_fraction, P_liver, Pi_liver, blood_volume_fraction, Pi_rbc, Pi_plasma,
lung_flow_factor, lung_volume_fraction, blood_lung_fraction, P_lung, Pi_lung)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
?,?,?,?,?,?,?,?,?,?,?,?)''',
                   (username, name1, bw1, h1, cardiac_output1, k_met1, k_bile1, k_kidney1, max_liver1, max_kidney1, max_influx1,
                    skin_flow_factor1, skin_volume_fraction1, blood_skin_fraction1, P_skin1, Pi_skin1, kidney_flow_factor1,
                    kidney_volume_fraction1, blood_kidney_fraction1, P_kidney1, Pi_kidney1, bladder_flow_factor1, bladder_volume_fraction1,
                    blood_bladder_fraction1, P_bladder1, Pi_bladder1, blood_rest_fraction1, P_rest1, Pi_rest1, liver_flow_factor1,
                    liver_volume_fraction1, blood_liver_fraction1, P_liver1, Pi_liver1, blood_volume_fraction1, Pi_rbc1, Pi_plasma1,
                    lung_flow_factor1, lung_volume_fraction1, blood_lung_fraction1, P_lung1, Pi_lung1))
    db.commit()
    id = cursor.lastrowid
    return id

def read_from_db(username):
    db = sqlite3.connect('models')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM models WHERE userName=?''', (username,))
    res = cursor.fetchall()
    return res

def read_from_db_secure(name, n):
    db = sqlite3.connect('models')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM models WHERE id=? AND modelName=?''', (str(n), name,))
    res = cursor.fetchone()
    return res

def read_for_edit(username, modelname):
    db = sqlite3.connect('models')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM models WHERE userName=? AND modelName=?''', (username, modelname,))
    res = cursor.fetchone()
    return res

def update_db(model_id, username, oldmodelname, newmodelname, bw, h, cardiac_output, k_met, k_bile, k_kidney,
              max_liver, max_kidney, max_influx, skin_f_f, skin_v_f, skin_b_f, p_skin, pi_skin,
              kidney_f_f, kidney_v_f, kidney_b_f, p_kidney, pi_kidney, bladder_f_f, bladder_v_f, bladder_b_f, p_bladder,
              pi_bladder, rest_b_f, p_rest, pi_rest, liver_f_f, liver_v_f, liver_b_f, p_liver, pi_liver, blood_v_f,
              pi_rbc, pi_plasma, lung_f_f, lung_v_f, lung_b_f, p_lung, pi_lung):
    db = sqlite3.connect('models')
    cursor = db.cursor()
    cursor.execute('''UPDATE models SET modelname=?, bw=?, h=?, cardiac_output=?, k_met=?, k_bile=?, k_kidney=?,
max_liver=?, max_kidney=?, max_influx=?, skin_flow_factor=?, skin_volume_fraction=?, blood_skin_fraction=?, P_skin=?, Pi_skin=?,
kidney_flow_factor=?, kidney_volume_fraction=?, blood_kidney_fraction=?, P_kidney=?, Pi_kidney=?, bladder_flow_factor=?,
bladder_volume_fraction=?, blood_bladder_fraction=?, P_bladder=?, Pi_bladder=?, blood_rest_fraction=?, P_rest=?, Pi_rest=?,
liver_flow_factor=?, liver_volume_fraction=?, blood_liver_fraction=?, P_liver=?, Pi_liver=?, blood_volume_fraction=?,
Pi_rbc=?, Pi_plasma=?, lung_flow_factor=?, lung_volume_fraction=?, blood_lung_fraction=?, P_lung=?, Pi_lung=?
WHERE id=? AND modelName=? AND userName=?''',
                   (newmodelname, bw, h, cardiac_output, k_met, k_bile, k_kidney, max_liver, max_kidney, max_influx,
                    skin_f_f, skin_v_f, skin_b_f, p_skin, pi_skin, kidney_f_f, kidney_v_f, kidney_b_f, p_kidney,
                    pi_kidney, bladder_f_f, bladder_v_f, bladder_b_f, p_bladder, pi_bladder, rest_b_f, p_rest, pi_rest,
                    liver_f_f, liver_v_f, liver_b_f, p_liver, pi_liver, blood_v_f, pi_rbc, pi_plasma, lung_f_f, lung_v_f,
                    lung_b_f, p_lung, pi_lung, model_id, oldmodelname, username))
    
    db.commit()
                            
def check_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False



def find_zero_rows_cols(matrix):
    [rows, cols] = matrix.shape
    rows_zeros = []
    cols_zeros = []
    for i in range(rows):
        if matrix[i].any() == 0:
            rows_zeros.append(i)
    for j in range(cols):
        if matrix[:,j].any() == 0:
            cols_zeros.append(j)
    return rows_zeros

def del_zeros(matrix):
    to_del = find_zero_rows_cols(matrix)
    [rows, cols] = matrix.shape
    newmatrix1 = np.ones((1, cols))
    for i in range(rows):
        if i not in to_del:
            newmatrix1 = np.append(newmatrix1, [matrix[i]], axis = 0)
    newmatrix1 = np.delete(newmatrix1, (0), axis = 0)
    [rows, cols] = newmatrix1.shape
    newmatrix2 = np.ones((rows,1))
    for j in range(cols):
        if j not in to_del:
            newmatrix2 = np.append(newmatrix2, newmatrix1[:,[j]], axis = 1)
    newmatrix2 = np.delete(newmatrix2, (0), axis = 1)
    return newmatrix2

#update_db(3, 'sotiris', 'arcticmonkeys4', 'arcticmonkeys5', 0.03, 0.45, 16.5, 0.07, 0.0, 0.0164, 1.4e-6, 3.0e-6, 8e-8, 0.058, 0.165,
#             0.03, 1.6, 0.0095, 0.091, 0.017, 0.24, 0.14, 0.12, 0.0033, 0.0009, 0.03, 1.6, 0.0095, 0.04, 1.6, 0.0095,
#             0.162, 0.055, 0.31, 1.6, 0.0095, 0.5, 1.3, 0.81, 1.0, 0.007, 0.5, 0.44, 0.94)
#print read_from_db_secure('arcticmonkeys6', 3)
