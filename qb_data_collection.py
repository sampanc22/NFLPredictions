import pandas as pd
import time

from nfl_qb_data_scraping import qb_df as overall
time.sleep(1.5)

from Qbs_per_game_stats.aidan_oconnell_raiders import qb_df as oconnell
time.sleep(1.5)

from Qbs_per_game_stats.baker_mayfield_buccaneers import qb_df as mayfield
time.sleep(1.5)

from Qbs_per_game_stats.brock_purdy_49ers import qb_df as purdy
time.sleep(1.5)

from Qbs_per_game_stats.bryce_young_panthers import qb_df as young
time.sleep(1.5)

from Qbs_per_game_stats.cj_stroud_texans import qb_df as stroud
time.sleep(1.5)

from Qbs_per_game_stats.dak_prescott_cowboys import qb_df as prescott
time.sleep(1.5)

from Qbs_per_game_stats.derek_carr_saints import qb_df as carr
time.sleep(1.5)

from Qbs_per_game_stats.desmond_ridder_falcons import qb_df as ridder
time.sleep(1.5)

from Qbs_per_game_stats.gardner_minshew_colts import qb_df as minshew
time.sleep(1.5)

from Qbs_per_game_stats.geno_smith_seahawks import qb_df as smith
time.sleep(1.5)

from Qbs_per_game_stats.jake_browning_bengals import qb_df as browning
time.sleep(1.5)

from Qbs_per_game_stats.jalen_hurts_eagles import qb_df as hurts
time.sleep(1.5)

from Qbs_per_game_stats.jared_goff_lions import qb_df as goff
time.sleep(1.5)

from Qbs_per_game_stats.joe_burrow_bengals_ir import qb_df as burrow
time.sleep(1.5)

from Qbs_per_game_stats.joe_flacco_browns import qb_df as flacco
time.sleep(1.5)

from Qbs_per_game_stats.jordan_love_packers import qb_df as love
time.sleep(1.5)

from Qbs_per_game_stats.josh_allen_bills import qb_df as allen
time.sleep(1.5)

from Qbs_per_game_stats.joshua_dobbs_cardinals_vikings import qb_df as dobbs
time.sleep(1.5)

from Qbs_per_game_stats.justin_fields_bears import qb_df as fields
time.sleep(1.5)

from Qbs_per_game_stats.justin_herbert_chargers_ir import qb_df as herbert
time.sleep(1.5)

from Qbs_per_game_stats.kenny_pickett_steelers import qb_df as pickett
time.sleep(1.5)

from Qbs_per_game_stats.kirk_cousins_vikings_ir import qb_df as cousins
time.sleep(1.5)

from Qbs_per_game_stats.kyler_murray_cardinals import qb_df as murray
time.sleep(1.5)

from Qbs_per_game_stats.lamar_jackson_ravens import qb_df as jackson
time.sleep(1.5)

from Qbs_per_game_stats.mac_jones_patriots import qb_df as jones
time.sleep(1.5)

from Qbs_per_game_stats.matthew_stafford_rams import qb_df as stafford
time.sleep(1.5)

from Qbs_per_game_stats.patrick_mahomes_chiefs import qb_df as mahomes
time.sleep(1.5)

from Qbs_per_game_stats.russell_wilson_broncos import qb_df as russell_wilson
time.sleep(1.5)

from Qbs_per_game_stats.ryan_tannehill_titans import qb_df as tannehill
time.sleep(1.5)

from Qbs_per_game_stats.sam_howell_commanders import qb_df as howell
time.sleep(1.5)

from Qbs_per_game_stats.trevor_lawrence_jaguars import qb_df as lawrence
time.sleep(1.5)

from Qbs_per_game_stats.tua_tagovailoa_dolphins import qb_df as tagovailoa
time.sleep(1.5)

from Qbs_per_game_stats.will_levis_titans import qb_df as levis
time.sleep(1.5)

from Qbs_per_game_stats.zach_wilson_jets_ir import qb_df as zach_wilson


file = "Data/qb_data.xlsx"
writer = pd.ExcelWriter(file, engine='xlsxwriter')

overall.to_excel(writer, sheet_name="overall", index=False)
oconnell.to_excel(writer, sheet_name="aidan_o'connell", index=False)
mayfield.to_excel(writer, sheet_name="baker_mayfield", index=False)
purdy.to_excel(writer, sheet_name="brock_purdy", index=False)
young.to_excel(writer, sheet_name="bryce_young", index=False)
stroud.to_excel(writer, sheet_name="cj_stroud", index=False)
prescott.to_excel(writer, sheet_name="dak_prescott", index=False)
carr.to_excel(writer, sheet_name="derek_carr", index=False)
ridder.to_excel(writer, sheet_name="desmond_ridder", index=False)
minshew.to_excel(writer, sheet_name="garnder_minshew", index=False)
smith.to_excel(writer, sheet_name="geno_smith", index=False)
browning.to_excel(writer, sheet_name="jake_browning", index=False)
hurts.to_excel(writer, sheet_name="jalen_hurts", index=False)
goff.to_excel(writer, sheet_name="jared_goff", index=False)
burrow.to_excel(writer, sheet_name="joe_burrow", index=False)
flacco.to_excel(writer, sheet_name="joe_flacco", index=False)
love.to_excel(writer, sheet_name="jordan_love", index=False)
allen.to_excel(writer, sheet_name="josh_allen", index=False)
dobbs.to_excel(writer, sheet_name="joshua_dobbs", index=False)
fields.to_excel(writer, sheet_name="justin_fields", index=False)
herbert.to_excel(writer, sheet_name="justin_herbert", index=False)
pickett.to_excel(writer, sheet_name="kenny_pickett", index=False)
cousins.to_excel(writer, sheet_name="kirk_cousins", index=False)
murray.to_excel(writer, sheet_name="kyler_murray", index=False)
jackson.to_excel(writer, sheet_name="lamar_jackson", index=False)
jones.to_excel(writer, sheet_name="mac_jones", index=False)
stafford.to_excel(writer, sheet_name="matthew_stafford", index=False)
mahomes.to_excel(writer, sheet_name="patrick_mahomes", index=False)
russell_wilson.to_excel(writer, sheet_name="russell_wilson", index=False)
tannehill.to_excel(writer, sheet_name="ryan_tannehill", index=False)
howell.to_excel(writer, sheet_name="sam_howell", index=False)
lawrence.to_excel(writer, sheet_name="trevor_lawrence", index=False)
tagovailoa.to_excel(writer, sheet_name="tua_tagovailoa", index=False)
levis.to_excel(writer, sheet_name="will_levis", index=False)
zach_wilson.to_excel(writer, sheet_name="zach_wilson", index=False)
print("QB Data Written")

writer.close()
