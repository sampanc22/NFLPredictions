import pandas as pd
import time

from nfl_rb_data_scraping import rb_df as overall
time.sleep(1.5)

from Rbs_per_game_stats.aaron_jones_packers import rb_df as aaron_jones
time.sleep(1.5)

from Rbs_per_game_stats.aj_dillon_packers import rb_df as aj_dillon
time.sleep(1.5)

from Rbs_per_game_stats.alexander_mattison_vikings import rb_df as alexander_mattison
time.sleep(1.5)

from Rbs_per_game_stats.alvin_kamara_saints import rb_df as alvin_kamara
time.sleep(1.5)

from Rbs_per_game_stats.austin_ekeler_chargers import rb_df as austin_ekeler
time.sleep(1.5)

from Rbs_per_game_stats.bijan_robinson_falcons import rb_df as bijan_robinson
time.sleep(1.5)

from Rbs_per_game_stats.brian_robinsonjr_commanders import rb_df as brian_robinson
time.sleep(1.5)

from Rbs_per_game_stats.breece_hall_jets import rb_df as breece_hall
time.sleep(1.5)

from Rbs_per_game_stats.christian_mccaffrey_49ers import rb_df as christian_mccaffrey
time.sleep(1.5)

from Rbs_per_game_stats.chuba_hubbard_panthers import rb_df as chuba_hubbard
time.sleep(1.5)

from Rbs_per_game_stats.dameon_pierce_texans import rb_df as dameon_pierce
time.sleep(1.5)

from Rbs_per_game_stats.dandre_swift_eagles import rb_df as dandre_swift
time.sleep(1.5)

from Rbs_per_game_stats.david_montgomery_lions import rb_df as david_montgomery
time.sleep(1.5)

from Rbs_per_game_stats.derrick_henry_titans import rb_df as derrick_henry
time.sleep(1.5)

from Rbs_per_game_stats.devin_singletary_texans import rb_df as devin_singletary
time.sleep(1.5)

from Rbs_per_game_stats.devon_achane_dolphins import rb_df as devon_achane
time.sleep(1.5)

from Rbs_per_game_stats.donta_foreman_bears import rb_df as donta_foreman
time.sleep(1.5)

from Rbs_per_game_stats.ezekiel_elliot_patriots import rb_df as ezekiel_elliot
time.sleep(1.5)

from Rbs_per_game_stats.gus_edwards_ravens import rb_df as gus_edwards
time.sleep(1.5)

from Rbs_per_game_stats.isiah_pacheco_chiefs import rb_df as isiah_pacheco
time.sleep(1.5)

from Rbs_per_game_stats.jahmyr_gibbs_lions import rb_df as jahmyr_gibbs
time.sleep(1.5)

from Rbs_per_game_stats.jamaal_williams_saints import rb_df as jamaal_williams
time.sleep(1.5)

from Rbs_per_game_stats.james_conner_cardinals import rb_df as james_conner
time.sleep(1.5)

from Rbs_per_game_stats.james_cook_bills import rb_df as james_cook
time.sleep(1.5)

from Rbs_per_game_stats.javonte_williams_broncos import rb_df as javonte_williams
time.sleep(1.5)

from Rbs_per_game_stats.jaylen_warren_steelers import rb_df as jaylen_warren
time.sleep(1.5)

from Rbs_per_game_stats.jerome_ford_browns import rb_df as jerome_ford
time.sleep(1.5)

from Rbs_per_game_stats.joe_mixon_bengals import rb_df as joe_mixon
time.sleep(1.5)

from Rbs_per_game_stats.jonathan_taylor_colts import rb_df as jonathan_taylor
time.sleep(1.5)

from Rbs_per_game_stats.josh_jacobs_raiders import rb_df as josh_jacobs
time.sleep(1.5)

from Rbs_per_game_stats.joshua_kelley_chargers import rb_df as joshua_kelley
time.sleep(1.5)

from Rbs_per_game_stats.kareem_hunt_browns import rb_df as kareem_hunt
time.sleep(1.5)

from Rbs_per_game_stats.kenneth_walker_seahawks import rb_df as kenneth_walker
time.sleep(1.5)

from Rbs_per_game_stats.khalil_herbert_bears import rb_df as khalil_herbert
time.sleep(1.5)

from Rbs_per_game_stats.kyren_williams_rams import rb_df as kyren_williams
time.sleep(1.5)

from Rbs_per_game_stats.miles_sanders_panthers import rb_df as miles_sanders
time.sleep(1.5)

from Rbs_per_game_stats.najee_harris_steelers import rb_df as najee_harris
time.sleep(1.5)

from Rbs_per_game_stats.rachaad_white_buccaneers import rb_df as rachaad_white
time.sleep(1.5)

from Rbs_per_game_stats.raheem_mostert_dolphins import rb_df as raheem_mostert
time.sleep(1.5)

from Rbs_per_game_stats.rhamondre_stevenson_patriots import rb_df as rhamondre_stevenson
time.sleep(1.5)

from Rbs_per_game_stats.rico_dowdle_cowboys import rb_df as rico_dowdle
time.sleep(1.5)

from Rbs_per_game_stats.saquon_barkley_giants import rb_df as saquon_barkley
time.sleep(1.5)

from Rbs_per_game_stats.tony_pollard_cowboys import rb_df as tony_pollard
time.sleep(1.5)

from Rbs_per_game_stats.travis_etienne_jaguars import rb_df as travis_etienne
time.sleep(1.5)

from Rbs_per_game_stats.ty_chandler_vikings import rb_df as ty_chandler
time.sleep(1.5)

from Rbs_per_game_stats.tyjae_spears_titans import rb_df as tyjae_spears
time.sleep(1.5)

from Rbs_per_game_stats.tyler_allgeier_falcons import rb_df as tyler_allgeier
time.sleep(1.5)

from Rbs_per_game_stats.zach_charbonnet_seahawks import rb_df as zach_charbonnet
time.sleep(1.5)

from Rbs_per_game_stats.zack_moss_colts import rb_df as zack_moss
time.sleep(1.5)

from Rbs_per_game_stats.zamir_white_raiders import rb_df as zamir_white

file = "rb_data.xlsx"
writer = pd.ExcelWriter(file, engine='xlsxwriter')

overall.to_excel(writer, sheet_name="overall", index=False)
aaron_jones.to_excel(writer, sheet_name="aaron_jones", index=False)
aj_dillon.to_excel(writer, sheet_name="aj_dillon", index=False)
alexander_mattison.to_excel(writer, sheet_name="alexander_mattison", index=False)
alvin_kamara.to_excel(writer, sheet_name="alvin_kamara", index=False)
austin_ekeler.to_excel(writer, sheet_name="austin_ekeler", index=False)
bijan_robinson.to_excel(writer, sheet_name="bijan_robinson", index=False)
breece_hall.to_excel(writer, sheet_name="breece_hall", index=False)
brian_robinson.to_excel(writer, sheet_name="brian_robinson", index=False)
christian_mccaffrey.to_excel(writer, sheet_name="christian_mccaffrey", index=False)
chuba_hubbard.to_excel(writer, sheet_name="chuba_hubbard", index=False)
dameon_pierce.to_excel(writer, sheet_name="dameon_pierce", index=False)
dandre_swift.to_excel(writer, sheet_name="dandre_swift", index=False)
david_montgomery.to_excel(writer, sheet_name="david_montgomery", index=False)
derrick_henry.to_excel(writer, sheet_name="derrick_henry", index=False)
devin_singletary.to_excel(writer, sheet_name="devin_singletary", index=False)
devon_achane.to_excel(writer, sheet_name="devon_achane", index=False)
donta_foreman.to_excel(writer, sheet_name="donta_foreman", index=False)
ezekiel_elliot.to_excel(writer, sheet_name="ezekiel_elliot", index=False)
gus_edwards.to_excel(writer, sheet_name="gus_edwards", index=False)
isiah_pacheco.to_excel(writer, sheet_name="isiah_pacheco", index=False)
jahmyr_gibbs.to_excel(writer, sheet_name="jahmyr_gibbs", index=False)
jamaal_williams.to_excel(writer, sheet_name="jamaal_williams", index=False)
james_conner.to_excel(writer, sheet_name="james_conner", index=False)
james_cook.to_excel(writer, sheet_name="james_cook", index=False)
javonte_williams.to_excel(writer, sheet_name="javonte_williams", index=False)
jaylen_warren.to_excel(writer, sheet_name="jaylen_warren", index=False)
jerome_ford.to_excel(writer, sheet_name="jerome_ford", index=False)
joe_mixon.to_excel(writer, sheet_name="joe_mixon", index=False)
jonathan_taylor.to_excel(writer, sheet_name="jonathan_taylor", index=False)
josh_jacobs.to_excel(writer, sheet_name="josh_jacobs", index=False)
joshua_kelley.to_excel(writer, sheet_name="joshua_kelley", index=False)
kareem_hunt.to_excel(writer, sheet_name="kareem_hunt", index=False)
kenneth_walker.to_excel(writer, sheet_name="kenneth_walker", index=False)
khalil_herbert.to_excel(writer, sheet_name="khalil_herbert", index=False)
kyren_williams.to_excel(writer, sheet_name="kyren_williams", index=False)
miles_sanders.to_excel(writer, sheet_name="miles_sanders", index=False)
najee_harris.to_excel(writer, sheet_name="najee_harris", index=False)
rachaad_white.to_excel(writer, sheet_name="rachaad_white", index=False)
raheem_mostert.to_excel(writer, sheet_name="raheem_mostert", index=False)
rhamondre_stevenson.to_excel(writer, sheet_name="rhamondre_stevenson", index=False)
rico_dowdle.to_excel(writer, sheet_name="rico_dowdle", index=False)
saquon_barkley.to_excel(writer, sheet_name="saquon_barkley", index=False)
tony_pollard.to_excel(writer, sheet_name="tony_pollard", index=False)
travis_etienne.to_excel(writer, sheet_name="travis_etienne", index=False)
ty_chandler.to_excel(writer, sheet_name="ty_chandler", index=False)
tyjae_spears.to_excel(writer, sheet_name="tyjae_spears", index=False)
tyler_allgeier.to_excel(writer, sheet_name="tyler_allgeier", index=False)
zach_charbonnet.to_excel(writer, sheet_name="zach_charbonnet", index=False)
zack_moss.to_excel(writer, sheet_name="zack_moss", index=False)
zamir_white.to_excel(writer, sheet_name="zamir_white", index=False)
print("RB Data Written")

writer.close()
