#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ayx import Alteryx
import pandas as pd
from scipy.interpolate import interp1d

# Lire les flux
isins_df = Alteryx.read("#1")  # TEST TV
courbe_df = Alteryx.read("#2")  # EUR 3M

# Préparer les colonnes
isins_df['Maturity'] = pd.to_datetime(isins_df['Maturity'])
courbe_df['date_valorisation'] = pd.to_datetime(courbe_df['date_valorisation'])
courbe_df['maturite_point_courbe'] = pd.to_datetime(courbe_df['maturite_point_courbe'])

# Résultat final
results = []

# Liste des dates de valorisation
dates_valo = courbe_df['date_valorisation'].unique()

# Pour chaque date de valorisation
for dte in dates_valo:
    courbe_du_jour = courbe_df[courbe_df['date_valorisation'] == dte]
    
    if not courbe_du_jour.empty:
        maturite_array = (courbe_du_jour['maturite_point_courbe'] - dte).dt.days.to_numpy()
        taux_array = courbe_du_jour['taux_marche_point_courbe'].to_numpy()

        try:
            linear_interp = interp1d(maturite_array, taux_array, kind='linear', fill_value="extrapolate")

            for _, row in isins_df.iterrows():
                delta = (row['Maturity'] - dte).days
                taux_interp = float(linear_interp(delta))

                results.append({
                    'Isin_benchmark': row['Isin_benchmark'],
                    'Type_benchmark': row['Type_benchmark'],
                    'date_valorisation': dte,
                    'Maturity': row['Maturity'],
                    'Taux_interpolé': taux_interp
                })

        except Exception:
            for _, row in isins_df.iterrows():
                results.append({
                    'Isin_benchmark': row['Isin_benchmark'],
                    'Type_benchmark': row['Type_benchmark'],
                    'date_valorisation': dte,
                    'Maturity': row['Maturity'],
                    'Taux_interpolé': None
                })

# Convertir en DataFrame
result_df = pd.DataFrame(results)

# Sortie vers Alteryx
Alteryx.write(result_df, 1)

