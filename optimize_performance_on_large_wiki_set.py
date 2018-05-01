import os

os.listdir("wiki")

'''
['%C3%81lvaro_Sierra.html',
 '%C3%89cole_des_Mines_de_Douai.html',
 '%C3%89taule.html',
 '%C3%96lm%C3%BCs_bir_kadinin_evraki_metrukesi.html',
 '%C5%81osie-Do%C5%82%C4%99gi.html',
 '%C5%8Cnog%C5%8D_Station.html',
 '%C5%9Eah%C3%AEn%C3%AA_Bekir%C3%AA_Sorekl%C3%AE.html',
 '(1-4)-a-D-glucan_1-a-D-glucosylmutase.html',
 '1._FC_Eschborn.html',
 '100%25_Banco.html',
 '100_Greatest_Romanians.html',
 '100_mm_field_gun_M1944_(BS-3).html',
 '104th_Logistic_Support_Brigade_(United_Kingdom).html',
 '1208_(band).html',
 '125th_(Lancashire_Fusiliers)_Brigade.html',
 '16th_Virginia_Infantry.html',
 '1860_in_science.html',
 '1866_in_birding_and_ornithology.html',
 '1879_FA_Cup_Final.html',
 '1896_Indiana_Hoosiers_football_team.html',
 '1898_Colgate_football_team.html',
 '1904_Case_football_team.html',
 '1905%E2%80%9306_FC_Barcelona_season.html',
 '1910_in_literature.html',
 '1915_Montana_football_team.html',
 '1937_Social_Credit_backbenchers%27_revolt.html',
 '1947_Notre_Dame_Fighting_Irish_football_team.html',
 '1951_National_League_tie-breaker_series.html',
 '1953%E2%80%9354_FA_Cup_qualifying_rounds.html',
 '1958_Wightman_Cup.html',
 '1963_Pittsburgh_Panthers_football_team.html',
 '1968_Duke_Blue_Devils_football_team.html',
 '1970_African_Cup_of_Nations.html',
 '1975%E2%80%9376_FIBA_Kora%C4%87_Cup.html',
 '1976_Kansas_State_Wildcats_football_team.html',
 '1978_College_Football_All-America_Team.html',
 '1982_Kentucky_Derby.html',
 '1982_World_Series.html',
 '1984%E2%80%9385_Southern_Football_League.html',
 '1984_WAC_Men%27s_Basketball_Tournament.html',
 '1987_Football_League_Trophy_Final.html',
 '1988_Chatham_Cup.html',
 '1988_State_of_Origin_series.html',
 '1989_Preakness_Stakes.html',
 '1990%E2%80%9391_Southern_Football_League.html',
 '1991%E2%80%9392_BHL_season.html',
 '1991_RTHK_Top_10_Gold_Songs_Awards.html',
 '1991_uprising_in_Basra.html',
 '1991_US_Open_%E2%80%93_Women%27s_Doubles.html',
 '1992_European_Athletics_Indoor_Championships.html',
 '1994_French_Open_%E2%80%93_Men%27s_Doubles.html',
 '1994_Scotland_rugby_union_tour_of_Argentina.html',
 '1995_FINA_Men%27s_Water_Polo_World_Cup.html',
 '1996_UEFA_Futsal_Championship.html',
 '1997_Edmonton_Eskimos_season.html',
 '1999%E2%80%932000_UEFA_Champions_League_second_group_stage.html',
 '1999_Caribbean_Cup.html',
 '1999_MTV_Video_Music_Awards.html',
 '1st_Strategic_Aerospace_Division.html',
 '2000_Pepsi_Southern_500.html',
 '2001%E2%80%9302_NBA_season.html',
 '2001_Australian_Individual_Speedway_Championship.html',
 '2001_Copa_del_Rey_Final.html',
 '2001_NCAA_Division_I_Field_Hockey_Championship.html',
 '2002%E2%80%9303_Scottish_Second_Division.html',
 '2003_World_Championships_in_Athletics_%E2%80%93_Women%27s_hammer_throw.html',
 '2004_Tuvalu_A-Division.html',
 '2005%E2%80%9306_in_Welsh_football.html',
 '2005_Asian_Women%27s_Club_Volleyball_Championship.html',
 '2005_in_radio.html',
 '2005_NCAA_Division_I_Men%27s_Basketball_Tournament.html',
 '2006_European_Athletics_Championships_%E2%80%93_Women%27s_triple_jump.html',
 '2007%E2%80%9308_Huddersfield_Town_A.F.C._season.html',
 '2007%E2%80%9308_Women%27s_EHF_Cup.html',
 '2007_in_Belgian_television.html',
 '2007_Kilkenny_Senior_Hurling_Championship.html',
 '2008_2._deild_karla.html',
 '2008_Fed_Cup_World_Group_II.html',
 '2008_Swedish_Open.html',
 '2009_English_cricket_season.html',
 '2009_European_Junior_Swimming_Championships.html',
 '2009_Giro_di_Lombardia.html',
 '2009_Open_Costa_Adeje_%E2%80%93_Isla_de_Tenerife_%E2%80%93_Singles.html',
 '2009_World_Junior_Ice_Hockey_Championships_rosters.html',
 '2010_Karshi_Challenger_%E2%80%93_Singles.html',
 '2010_New_Year%27s_Eve_tornado_outbreak.html',
 '2011%E2%80%9312_Western_Collegiate_Hockey_Association_women%27s_ice_hockey_season.html',
 '2011_Dutch_National_Track_Championships_%E2%80%93_Men%27s_1_km_time_trial.html',
 '2011_ITU_Duathlon_World_Championships.html',
 '2011_Mosconi_Cup.html',
 '2011_UK_Open_Qualifier_4.html',
 '2011_Wainwright_Roaming_Buffalo_Classic.html',
 '2012%E2%80%9313_Liga_Na%C8%9Bional%C4%83_(women%27s_handball).html',
 '2012%E2%80%9313_SVB_Hoofdklasse.html',
 '2013%E2%80%9314_Stirling_%26_District_Amateur_Football_Association.html',
 '2013_Curlers_Corner_Autumn_Gold_Curling_Classic.html',
 '2013_FIA_WTCC_Race_of_Russia.html',
 '2013_Mississippi_State_Bulldogs_baseball_team.html',
 '2013_San_Luis_Open_Challenger_%E2%80%93_Doubles.html',
 '2013_World_Grand_Prix_(darts).html',
 '2014%E2%80%9315_Albanian_Third_Division.html',
 '2014%E2%80%9315_Kansas_State_Wildcats_men%27s_basketball_team.html',
 '2014%E2%80%9316_European_Nations_Cup_Second_Division.html',
 '2014_Kano_bombing.html',
 '2014_Special_Honours.html',
 '2014_World_RX_of_Turkey.html',
 '2015%E2%80%9316_PLK_season.html',
 '2015%E2%80%9316_Washington_Huskies_men%27s_basketball_team.html',
 '2015_NWSL_College_Draft.html',
 '2015_Thai_League_Cup.html',
 '2016%E2%80%9317_Little_Rock_Trojans_women%27s_basketball_team.html',
 '2016%E2%80%9317_New_Zealand_Football_Championship.html',
 '2016_Danmark_Rundt.html',
 '2016_FK_Haugesund_season.html',
 '2016_Minnesota_Vikings_season.html',
 '2017_Orange_County_Breakers_season.html',
 '23rd_Reserve_Battalion,_CEF.html',
 '24th_Genie_Awards.html',
 '25B-NBOMe.html',
 '26th_Illinois_Volunteer_Infantry_Regiment.html',
 '3-(Trifluoromethyl)aniline.html',
 '33rd_New_Jersey_Volunteer_Infantry.html',
 '427.html',
 '4_Way_Street.html',
 '50_caliber_Mark_7_gun.html',
 '55th_parallel_south.html',
 '59th_Oza.html',
 '83_(number).html',
 '877_Naval_Air_Squadron.html',
 '985_Innovative_Platforms_for_Key_Disciplines_Project.html',
 'A%C3%A9ro_Services_Gu%C3%A9pard_Gu%C3%A9pard_912.html',
 'A._P._Komala.html',
 'A_Beautiful_Valley.html',
 'A_Month_of_Sundays_(miniseries).html',
 'A_Slow_Messe.html',
 'A_Sport_and_a_Pastime.html',
 'Aaron_Paul.html',
 'Aaron_Williams_and_the_Hoodoo.html',
 'Aaronsburg_Historic_District.html',
 'Aattanayagann.html',
 'AAU_Junior_Olympic_Games.html',
 'AB_v_CD.html',
 'Abanycha_bicolor.html',
 'Abbas_Jadidi.html',
 'Abbeville_Sluggers.html',
 'Abdelwahid_Aboud_Mackaye.html',
 'Abdulla_Majid_Al_Naimi.html',
 'Abdulrahman_al-Awlaki.html',
 'Abortion_in_Italy.html',
 'Abortion_in_Oklahoma.html',
 'Abou_Redis.html',
 'Abraham_Booth.html',
 'Abraham_Stanyan.html',
 'Absolutely_Zippo.html',
 'Abu_Oleymeh,_Ramshir.html',
 'Abyssobela_atoxica.html',
 'Acacia_dermatophylla.html',
 'Academic_grading_in_Bosnia_and_Herzegovina.html',
 'Acceptance_(Heroes).html',
 'Acceptilation.html',
 'Accommodation_bridge.html',
 'Achaea_faber.html',
 'Acharapakkam_(State_Assembly_Constituency).html',
 'Achim_Schwarze.html',
 'ACM_Transactions_on_Computational_Biology_and_Bioinformatics.html',
 'Acrocercops_calycophthalma.html',
 'Acrolophus_simulatus.html',
 'Adelaide%E2%80%93Darwin_railway.html',
 'Adios_(B%C3%B6hse_Onkelz_album).html',
 'Adish_Aggarwala.html',
 'ADNI.html',
 'Adolf%C3%B3w,_%C5%81%C3%B3d%C5%BA_Voivodeship.html',
 'Adolf_Schulte.html',
 'Adoration_of_the_Magi_(Filippino_Lippi).html',
 'Adrian_Bawtree.html',
 'Adrian_Clarke_(footballer).html',
 'Aechmea_%27Pica%27.html',
 'Agaritine_gamma-glutamyltransferase.html',
 'Agesarchus_of_Tritaea.html',
 'Agnes_Tait.html',
 'Agnolin.html',
 'Agostino_Gemelli.html',
 'Agripina_Samper_Agudelo.html',
 'Agullent.html',
 'Agyneta_allosubtilis.html',
 'Ahanta_West_District.html',
 'Ahmad_Khatami_(professor).html',
 'AIM_Phoneline.html',
 'Air_Barons.html',
 'Aiva.html',
 'Ajminal.html',
 'Aku_Partanen.html',
 'Al-Midan.html',
 'Al-Nurayn_Mosque.html',
 'Al_Azim_Mosque.html',
 'Al_Mahon.html',
 'Al_Sherman.html',
 'Alan_Oakley.html',
 'Alan_Orr.html',
 'Alan_Sheehan.html',
 'Albanians_in_Egypt.html',
 'Albert_French.html',
 'Album-equivalent_unit.html',
 'Aldona_Orman.html',
 'Aleksandra_Jagie%C5%82o.html',
 'Aleksei_Lazarev.html',
 'Alex_Karalexis.html',
 'Alex_Kurtzman.html',
 'Alex_McEachern.html',
 'Alexander_Armstrong_(explorer).html',
 'Alexander_King_(author).html',
 'Alexander_McCue.html',
 'Alexander_Rizzoni.html',
 'Alexandru_Greab.html',
 'Alexei_Vinogradov.html',
 'Alexios_Aspietes.html',
 'Alexis_Lloyd.html',
 'Ali_Al_Bulaihi.html',
 'Aliabad-e_Robat.html',
 'Alireza_JJ.html',
 'Alisa_(soap_opera).html',
 'All-Polish_Youth.html',
 'All_Ceylon_Tamil_Congress.html',
 'All_Lights_Fucked_on_the_Hairy_Amp_Drooling.html',
 'All_Tangled_Up_in_Love.html',
 'All_the_Fun.html',
 'All_You_Get_from_Love_Is_a_Love_Song.html',
 'Allama_Iqbal_Medical_College.html',
 'Allan_Egolf.html',
 'Allan_Lister_Samuel_Brown.html',
 'Allen_Snyder_(lawyer).html',
 'Alnwick_District_Council_election,_2007.html',
 'Alojz_Knafelc.html',
 'Alpine_skiing_at_the_1994_Winter_Olympics_%E2%80%93_Men%27s_combined.html',
 'Amanda_Peet.html',
 'Amano_Artisan_Chocolate.html',
 'Amber_Butchart.html',
 'Amborella.html',
 'AMD_XGP.html',
 'Ameenapuram.html',
 'American_Federation_of_Labor_Building.html',
 'American_Journal_of_Kidney_Diseases.html',
 'Aminonaphthalenesulfonic_acids.html',
 'Amorphogynia.html',
 'Ampelasia.html',
 'Amphidromia.html',
 'Amy_Watkins.html',
 'Ana_Beatriz.html',
 'Anatolii_Sloiko.html',
 'Ancita_antennata.html',
 'Ancylostoma_duodenale.html',
 'Anders_Ahlgren.html',
 'Andrei_Gamalyan.html',
 'Andrew_McNally.html',
 'Andrew_S._Tanenbaum.html',
 'Andrew_Wilson_(classical_archaeologist).html',
 'Angelic_non-determinism.html',
 'Angolan_Union_for_Peace,_Democracy_and_Development.html',
 'Aniavan.html',
 'Anish_Giri.html',
 'Anjada_Gandu.html',
 'Anne_Whateley.html',
 'Annopole_Stare.html',
 'Annunciation_Church,_Walsall.html',
 'Ant%C3%B3nio_Maria_Baptista.html',
 'Ant%C3%B3nio_Marinho_e_Pinto.html',
 'Antae_temple.html',
 'Anthony_Cesario.html',
 'Anthony_Marten.html',
 'Antibiotic_use_in_livestock.html',
 'Antigonadotropin.html',
 'Antipater_of_Thessalonica.html',
 'Antoine_Gakeme.html',
 'Anton_von_Troeltsch.html',
 'Antonio_Ciano.html',
 'Antonio_de_Zayas_(bishop).html',
 'Anuradhapura_West_Electoral_District.html',
 'Apache_Bloodhound.html',
 'Aphonopelma_chiricahua.html',
 'Apocephalus_borealis.html',
 'Appa_(film).html',
 'Aq_Dash,_East_Azerbaijan.html',
 'Aquaphobia.html',
 'ARA_Garibaldi.html',
 'Arabic_Toilers%27_Movement.html',
 'Arcadio_Gonz%C3%A1lez.html',
 'Archibald_Gordon_(British_Army_officer).html',
 'Archiepiscopal_Palace,_Rouen.html',
 'Area_code_218.html',
 'Area_of_refuge.html',
 'Argentina_at_the_2015_World_Championships_in_Athletics.html',
 'Arkansas_gubernatorial_election,_1968.html',
 'Arkansas_Highway_178.html',
 'Arnold_Freiherr_von_Biegeleben.html',
 'Arrest_warrant.html',
 'Arrondissements_of_the_Yvelines_department.html',
 'Art_collection_of_Fondazione_Cassa_di_Risparmio_di_Perugia.html',
 'Arthur_Baldwinson.html',
 'Arthur_L._Aidala.html',
 'Arthur_Lelyveld.html',
 'Arthur_Mendes.html',
 'Arthur_Norman.html',
 'Arturo_Liebstein.html',
 'Arun_K._Pati.html',
 'Arvind_Gokhale.html',
 'Ash_Rees.html',
 'Asheqlu.html',
 'Ashley,_Wisconsin.html',
 'Ashu_Dani.html',
 'Asparuh_Peak.html',
 'Assegaaibosch_Nature_Reserve.html',
 'Asun_Balzola.html',
 'Athletics_at_the_1994_Commonwealth_Games_%E2%80%93_Men%27s_pole_vault.html',
 'Athletics_at_the_2007_Games_of_the_Small_States_of_Europe.html',
 'Athletics_at_the_2012_Summer_Paralympics_%E2%80%93_Women%27s_200_metres_T36.html',
 'Atlanta_Area_School_for_the_Deaf.html',
 'Atlantic_Studios.html',
 'Atractaspis_duerdeni.html',
 'Atrypanius_scitulus.html',
 'Attila,_Illinois.html',
 'Aubrey_Fair.html',
 'Audefroi_le_Bastart.html',
 'August_Duranowski.html',
 'Augustine_Chacon.html',
 'Austral_Alien.html',
 'Australian_federal_election,_1954.html',
 'Australian_hardcore.html',
 'Australian_Musician_(magazine).html',
 'Australiteuthis_aldrichi.html',
 'Avalara.html',
 'Avengers_Academy.html',
 'Avenira.html',
 'AVM_GmbH.html',
 'Avyarud.html',
 'Awali.html',
 'Axel_Revold.html',
 'Ayish_Bayou.html',
 'Aylon_Darwin_Tavella.html',
 'Ayodhya_Mandapam.html',
 'Baadj.html',
 'Baadshah_(1999_film).html',
 'Bad_Axe_River.html',
 'Bad_Luck_(Social_Distortion_song).html',
 'Baddiewinkle.html',
 'Bagrat_VI_of_Georgia.html',
 'Bahia_bigelovii.html',
 'Bahmanabad-e_Olya.html',
 'Baigts-de-B%C3%A9arn.html',
 'Baithakata_College.html',
 'Bal%C3%A1zs_Vill%C3%A1m.html',
 'Ballard_Memorial_High_School.html',
 'Ballonet.html',
 'Balloon_light.html',
 'Baltic_Peak.html',
 'Ban_On.html',
 'Bandar_Botanik_LRT_Station.html',
 'Banovina_of_Croatia.html',
 'Bar_One_Racing_Juvenile_Hurdle.html',
 'Baraf.html',
 'Barbara_McKinzie.html',
 'Barbus_caudosignatus.html',
 'Baritius_cyclozonata.html',
 'Barn.html',
 'Barnsdall_Art_Park.html',
 'Barra_do_Rocha.html',
 'Barren_vegetation.html',
 'Bart_van_Leeuwen.html',
 'Bartrum_Glacier.html',
 'Batfink.html',
 'Battle_of_Abydos.html',
 'Battle_of_Finta.html',
 'Battle_of_Isonzo_(489).html',
 'Battle_of_Sulukh.html',
 'Battle_of_Wattignies.html',
 'Battleford-Cut_Knife.html',
 'Bawdrip_Halt_railway_station.html',
 'Bay_of_Concepci%C3%B3n.html',
 'Bayandalai,_%C3%96mn%C3%B6govi.html',
 'Bazemore,_Alabama.html',
 'BBCH-scale_(rice).html',
 'BBG_Academy.html',
 'Be%C5%82chat%C3%B3w_Power_Station.html',
 'Beaubassin_East,_New_Brunswick.html',
 'Beaune_Altarpiece.html',
 'Beaupr%C3%A9,_Quebec.html',
 'Bebearia_romboutsi.html',
 'Bechdel_test.html',
 'Bed_and_Breakfast_(album).html',
 'Begin_(Riyu_Kosaka_album).html',
 'Beijing_Dongyue_Temple.html',
 'Belgium_women%27s_national_field_hockey_team.html',
 'Beli_language_(South_Sudan).html',
 'Bellanca_28-92.html',
 'Belmont_Estate.html',
 'Belosavci.html',
 'Belvedere,_London.html',
 'Belvedere_Park,_Georgia.html',
 'Ben_H._Williams.html',
 'Ben_Rimalower.html',
 'Bengt_Forsberg.html',
 'Benidorm_Bastards.html',
 'Benktander_type_II_distribution.html',
 'Benny_Lee.html',
 'Bernard-Augustin_Conroy.html',
 'Bert_Leboe.html',
 'Bertilda_Samper_Acosta.html',
 'Berzeliustinden.html',
 'Bethoncourt.html',
 'Beverley_Hills_Apartment_Block.html',
 'Beyond_Magnetic.html',
 'Bhimnagar,_Supaul.html',
 'Bhubanananda_Das.html',
 'Bianna_Golodryga.html',
 'Bias.html',
 'Bibiana_Beglau.html',
 'Bibliography_of_Niue.html',
 'Bicycle_basket.html',
 'Bifidocarpus.html',
 'Bijou,_California.html',
 'Bilan_d%27aptitude_d%C3%A9livr%C3%A9_par_les_grandes_%C3%A9coles.html',
 'Bill_Overstreet.html',
 'Bill_Price_(baseball).html',
 'Bill_Widenhouse.html',
 'Bill_Williamson_(footballer).html',
 'Billi%C3%A8me.html',
 'Billy_Grammer.html',
 'Billy_McNeill.html',
 'Biorock.html',
 'Bishop_of_Kingston.html',
 'Biz_Kid$.html',
 'Black_Moshannon_State_Park_Historic_Districts.html',
 'Black_Pond_Township,_Oregon_County,_Missouri.html',
 'Blackshear_Prison.html',
 'Blick_nach_Rechts.html',
 'Blohm.html',
 'Blomheller_Station.html',
 'Blommersia.html',
 'Blue_Heelers_(season_8).html',
 'Blue_Sky_Mining.html',
 'Blue_SWAT.html',
 'Bluesin%27_Around.html',
 'Board_of_Jewish_Education_(Toronto).html',
 'Boardman_Township,_Mahoning_County,_Ohio.html',
 'Bob_Allen_(shortstop).html',
 'Bob_Bass.html',
 'Bob_Lustig.html',
 'Bobo_Sikorski.html',
 'Bon_Accord_Free_Church.html',
 'Bone_morphogenetic_protein_4.html',
 'Bones_Apart.html',
 'Bonny_River.html',
 'Boogie_Bunnies.html',
 'Boone_Square.html',
 'Boothapandi.html',
 'Botswana_passport.html',
 'Bowie_Race_Track.html',
 'Bowlers%27_Club_of_New_South_Wales.html',
 'Boynton_baronets.html',
 'Br%C3%A9zina_District.html',
 'Brachylogus.html',
 'Brady_Hicks.html',
 'Braille_pattern_dots-126.html',
 'Branko_Maru%C5%A1i%C4%8D.html',
 'Brede_Waterworks.html',
 'Brendan_Foster.html',
 'Brian_Collins_(2010s_singer).html',
 'Brian_G._W._Manning.html',
 'Brian_Sims.html',
 'Brightside_Apartments.html',
 'British_Academy_Television_Award_for_Best_Comedy_(Programme_or_Series).html',
 'Bro_Safari.html',
 'Brograve_Mill.html',
 'Brownfield_(software_development).html',
 'Bruce_Conte.html',
 'Bruce_Lyon.html',
 'Bryan_Payton.html',
 'Bryzg%C3%B3w.html',
 'Buchanan_%26_Press.html',
 'Buffington_Township,_Indiana_County,_Pennsylvania.html',
 'Buford,_North_Dakota.html',
 'Buko_pie.html',
 'Bukovica_(Cazin).html',
 'Bulbonaricus.html',
 'Bulbophyllum_biflorum.html',
 'Burbridge_Creek.html',
 'Burmese_shrike.html',
 'Burnin%27_Sneakers.html',
 'Burnley_(surname).html',
 'Burnley_Borough_Council_election,_2011.html',
 'Burrough_Court.html',
 'Busan%E2%80%93Gimhae_Light_Rail_Transit_Operation_Corporation.html',
 'Business.com.html',
 'BW_Vulpeculae.html',
 'Bycz,_Kuyavian-Pomeranian_Voivodeship.html',
 'Bye!_My_Boy!.html',
 'Bye_Bye_Mon_Cowboy.html',
 'C%27est_la_vie_(Khaled_song).html',
 'C%C3%AA.html',
 'C10H8.html',
 'C11orf30.html',
 'C18H23NO6.html',
 'Cabrini%E2%80%93Green,_Chicago.html',
 'Caladenia_amoena.html',
 'Caldelas,_Sequeiros_e_Paranhos.html',
 'California_Historical_Landmarks_in_San_Bernardino_County,_California.html',
 'California_roach.html',
 'California_Unfair_Competition_Law.html',
 'Calin_Rovinescu.html',
 'Calvin_Harrell.html',
 'Camp_Liberty_killings.html',
 'Camp_Nelson_Confederate_Cemetery.html',
 'Campus_of_Texas_A%26M_University.html',
 'Canada_Bay.html',
 'Canbelego_County.html',
 'Caney_Creek_(Matagorda_Bay).html',
 'Cannabis_in_Spain.html',
 'Canyamars.html',
 'Cape_Bonavista.html',
 'Cape_Mayo.html',
 'Cappella_San_Donato,_Venafro.html',
 'Capriccio_Italien.html',
 'Caprinia_versicolor.html',
 'Caramel_Box_Yarukibako.html',
 'Cardinals_created_by_Alexander_VIII.html',
 'Cardipeltis.html',
 'Carley_State_Park.html',
 'Carlos_Martins_(musician).html',
 'Carmen_Weber.html',
 'Carroll_O._Switzer.html',
 'Carrollwood_Day_School.html',
 'Carte_Imagine%27R.html',
 'Carthage,_Cincinnati.html',
 'Caryl_Nowson.html',
 'Cascade_Summit,_Oregon.html',
 'Cascate_del_Rio_Verde.html',
 'Caste_system_in_India.html',
 'Castle_of_Cardona.html',
 'Catlett_House_(Staunton,_Virginia).html',
 'CCL8.html',
 'CDC42EP3.html',
 'Cechenena_sperlingi.html',
 'Cecil,_Oregon.html',
 'Cecil_Biggs.html',
 'Cecil_Bothwell.html',
 'Cecil_Peak.html',
 'Cecile_of_Baux.html',
 'Cecyl%C3%B3wka-Brz%C3%B3zka.html',
 'Celebrity_doll.html',
 'Celta_de_Vigo_B.html',
 'Center_(group_theory).html',
 'Central_District_(Rezvanshahr_County).html',
 'Central_Luzon.html',
 'Central_Park_(Tolyatti).html',
 'Centzon_Totochtin.html',
 'Ceryx_hageni.html',
 'Ch%C3%A2telet_surface.html',
 'Ch%C3%A9nens.html',
 'Chadefaudiellaceae.html',
 'Chah-e_Zakaria.html',
 'Challenger_Banque_Nationale_de_Drummondville.html',
 'Channel_48_digital_TV_stations_in_the_United_States.html',
 'Chapel_of_Mercy,_Monaco-Ville.html',
 'Charalampos_Brilakis.html',
 'Charged_Records.html',
 'Charles_Golding_Constable.html',
 'Charles_Micallef.html',
 'Charles_Page_(cricketer).html',
 'Charles_S._Benton.html',
 'Charles_Sears.html',
 'Charles_Smith_Wilcox.html',
 'Charles_Stuart_(rugby_union).html',
 'Charles_Trudeau_(politician).html',
 'Charles_Wadsworth.html',
 'Charlton_baronets.html',
 'Chaun_Thompson.html',
 'Checkerspot_(magazine).html',
 'Cheddar_Ales.html',
 'Chef_Wan.html',
 'Chemin_d%27Aylmer.html',
 'Cherechiu.html',
 'Cheryl_Prewitt.html',
 'Chester_Morris.html',
 'Chestnut_pie.html',
 'Chhaparband_(Muslim).html',
 'Chhatrasal.html',
 'Chicoreus_cervicornis.html',
 'Chief_Justice_of_New_Zealand.html',
 'Chihuahuan_Desert_Nature_Center_and_Botanical_Gardens.html',
 'Chilango_(magazine).html',
 'Children_of_Air_India.html',
 'Children_of_the_Grave.html',
 'Chile_de_%C3%A1rbol.html',
 'Chilo_auricilius.html',
 'Chinlone.html',
 'Chionodes_retiniella.html',
 'Chiriguelo.html',
 'Chisocheton_cumingianus_subsp._kinabaluensis.html',
 'Chocolate_Factory.html',
 'Choseng_Trungpa.html',
 'Christia_Mercer.html',
 'Christian_Amoroso.html',
 'Christian_Jessen.html',
 'Christianity_and_antisemitism.html',
 'Christine_Gardner.html',
 'Christopher_Speer.html',
 'Chromis_iomelas.html',
 'Church_of_St_Mary_the_Virgin,_Keysoe.html',
 'Church_of_the_SubGenius.html',
 'CIE_1964_color_space.html',
 'Circle_Repertory_Company.html',
 'Circus_Avenue.html',
 'Cisy,_Byt%C3%B3w_County.html',
 'Cit%C3%A9_du_Vin.html',
 'City_of_Mandaluyong_Science_High_School.html',
 'Claire_Danes.html',
 'Clarinet_Quintet_(T%C3%A4glichsbeck).html',
 'Clarksville,_Pennsylvania.html',
 'Class_C_GPCR.html',
 'Claude%27s_syndrome.html',
 'Claude-Godefroy_Coquart.html',
 'Claude_Mandil.html',
 'Claudia_Neidig.html',
 'Clay_Research_Award.html',
 'Clay_Township,_Clark_County,_Missouri.html',
 'Clear_Creek_Township,_Cooper_County,_Missouri.html',
 'Cleveland,_Oklahoma.html',
 'Cleveland_Institution_of_Engineers.html',
 'Cleveland_Play_House.html',
 'Clinton_Engineer_Works.html',
 'Clive_Brown_(footballer).html',
 'Clocking_Out_Is_for_Suckers.html',
 'Clothes_Show_Live.html',
 'Coalition_for_Unity_and_Democracy.html',
 'Coalville_Town_railway_station.html',
 'Coastal_upwelling_of_the_South_Eastern_Arabian_Sea.html',
 'Cobble_Hill,_Brooklyn.html',
 'Coble_hypersurface.html',
 'Code_page_1023.html',
 'Coenaculum_secundum.html',
 'Col_Pearce.html',
 'Colantonio_Incorporated.html',
 'Colchester_Village_Historic_District.html',
 'Cole_Shade_Sule.html',
 'Colleen_Haskell.html',
 'Colors_for_Trombone.html',
 'Colossal_Titan_Strife.html',
 'Colosseum_LiveS_%E2%80%93_The_Reunion_Concerts.html',
 'Columbia_Airport_(Ohio).html',
 'Comedy_Now!.html',
 'Comisi%C3%B3n_Femenil_Mexicana_Nacional.html',
 'Common_Sense_Revolution.html',
 'Communities_of_Tulu_Nadu.html',
 'Companys,_proc%C3%A9s_a_Catalunya.html',
 'Compton%27s_Most_Wanted_discography.html',
 'Computational_Geometry_(journal).html',
 'Congregation_Agudath_Achim.html',
 'Conjugate_depth.html',
 'Connecticut_House_of_Representatives.html',
 'Connell_Mansion.html',
 'Consolidated_Commodore.html',
 'Constance_D%27Arcy_Mackay.html',
 'Constantin_Ro%C8%99u.html',
 'Constitution_of_Kyrgyzstan.html',
 'Continuity_of_Operations.html',
 'Coosa_County_School_District.html',
 'Copamyntis_infusella.html',
 'Copenhagen_Skatepark.html',
 'Copier_family.html',
 'Corey_Lee.html',
 'Cornix.html',
 'Coronium_(gastropod).html',
 'Coronoid_process_of_the_ulna.html',
 'Corozal_Hospital.html',
 'Corporation_(university).html',
 'Corredores_Ferroviarios.html',
 'Cortile_del_Belvedere.html',
 'Cosmopterix_similis.html',
 'Coup_d%27%C3%A9tat.html',
 'Cr%C3%A8me_de_violette.html',
 'Crab-eating_frog.html',
 'Craig_Chester.html',
 'Crawley_Down.html',
 'Crazy_(2000_film).html',
 'Crazy_House_(1928_film).html',
 'Crepidula_atrasolea.html',
 'Cricoid_pressure.html',
 'Criminal_Code_(Canada).html',
 'Crisfield_Municipal_Airport.html',
 'Crispoldus.html',
 'Criss_Cross_(film).html',
 'Cristian_Berdeja.html',
 'Cryptographic_primitive.html',
 'Ctenodes_zonata.html',
 'Cultural_tourism_in_Egypt.html',
 'Cuproxena_hoffmanana.html',
 'Curridge.html',
 'Curtis_F._Marbut.html',
 'Curtis_Jones_(law).html',
 'Curtis_Whitley.html',
 'Curtiss-Wright_Hangar_(Columbia,_South_Carolina).html',
 'Cyclohexane_conformation.html',
 'Cyclone_Gamede.html',
 'Cygany,_Masovian_Voivodeship.html',
 'Dabir_Khan.html',
 'Dachuan_District.html',
 'Dahan-e_Kanak.html',
 'Dailyhunt.html',
 'Dakar_2:_The_World%27s_Ultimate_Rally.html',
 'Dalian_Road_Station.html',
 'Danbury_Ridge_Nature_Reserves.html',
 'Dance_notation.html',
 'Dancing_with_the_Stars_(Greece_season_5).html',
 'Dani%C3%ABl_de_Clercq.html',
 'Daniel_Cerone.html',
 'Daniel_Glazman.html',
 'Daniela_Del_Din.html',
 'Daniella_Abreu.html',
 'Danish_Maritime_Safety_Administration.html',
 'Danny_Gray.html',
 'Darantasia_cuneiplena.html',
 'Daryl_Stanley.html',
 'DataMeet.html',
 'Datang,_Zhuji.html',
 'Dave_Hill_(golfer).html',
 'David_Beasley.html',
 'David_Jesson.html',
 'David_Mandel.html',
 'David_Sands_(psychologist).html',
 'David_Sencer.html',
 'David_Solomona.html',
 'David_Thomson,_3rd_Baron_Thomson_of_Fleet.html',
 'Days_Creek_Formation.html',
 'De_Bruijn_index.html',
 'De_La_Salle_University_%E2%80%93_Dasmari%C3%B1as.html',
 'Dean_Downing.html',
 'Dean_Kukan.html',
 'Deception_(Irish_TV_series).html',
 'Decker_Township,_Richland_County,_Illinois.html',
 'Decoy_receptors.html',
 'Degerfors_IF.html',
 'Delta_Wedding.html',
 'Delvenau.html',
 'Democratic_Forum_of_Germans_in_Romania.html',
 'Demographics_of_American_Samoa.html',
 'Demographics_of_Wallis_and_Futuna.html',
 'Denis_Augustine_Hanley.html',
 'Dennis_Chapman.html',
 'Dennis_Shere.html',
 'Denyse_Sibley.html',
 'Der_Opernball.html',
 'Derek_Acorah.html',
 'Dermatomycosis.html',
 'Derrick_White_(baseball).html',
 'Desert_Rain_(song).html',
 'Deserticossus_murinus.html',
 'Desmiphora_bijuba.html',
 'Destroyer_Squadron_7.html',
 'Deuterocohnia_schreiteri.html',
 'Devarampally.html',
 'Developmental_robotics.html',
 'Devil_on_Horseback.html',
 'Devitt_Insurance.html',
 'Devizes_Town_F.C..html',
 'Dewoitine_D.21.html',
 'Dextran_1.html',
 'Dhanbad_(Vidhan_Sabha_constituency).html',
 'Diablo_Swing_Orchestra.html',
 'Dialogue_for_Hungary.html',
 'Dick_Johnson_(clarinetist).html',
 'Dick_Persson.html',
 'Diego_Galv%C3%A1n.html',
 'DiGiorgio_Corporation.html',
 'Digital_Light_Processing.html',
 'Dik%C4%BCi_parish.html',
 'Dimanche_%C3%A0_Bamako.html',
 'Dimension_of_an_algebraic_variety.html',
 'Diphilus_(physician).html',
 'Diplacus_aurantiacus.html',
 'Discretionary_trust.html',
 'Distance_Education_Centre,_Victoria.html',
 'Divine_Incantations_Scripture.html',
 'DJ-Kicks:_Henrik_Schwarz.html',
 'Dmytrivka,_Shakhtarsk_Raion.html',
 'Dokri_Taluka.html',
 'Domaniowice.html',
 'Domenico_Siniscalco.html',
 'Dominique_Voynet.html',
 'Don_Kindt,_Jr..html',
 'Don_Nelson_Laramore.html',
 'Don_Parsons_(ice_hockey).html',
 'Don_Raye.html',
 'Donal_Moloney.html',
 'Donegal_Township,_Westmoreland_County,_Pennsylvania.html',
 'Double_Wing_Attack.html',
 'Doug_Sahm_and_Band.html',
 'Doughty.html',
 'Douglas_Trojans.html',
 'Doumanaba.html',
 'Dowell_Philip_O%27Reilly.html',
 'Downhill_Domination.html',
 'Dr._Feelgood_(album).html',
 'Dragnet_(franchise).html',
 'Dresden-Plauen_railway_station.html',
 'Drumstruck.html',
 'Dryas_integrifolia.html',
 'Du%C5%A1anovo.html',
 'Du%C5%BEi_Monastery.html',
 'Durham_Women%27s_F.C..html',
 'DWTE-TV.html',
 'DXRA.html',
 'Dysgonia_pudica.html',
 'Dzahadjou_Lamzand%C3%A9.html',
 'DZYM.html',
 'E._E._Evans-Pritchard.html',
 'E._F._McClellan.html',
 'Earl_of_Anglesey.html',
 'Early_medieval_states_in_Kazakhstan.html',
 'Earth_Liberation_Front.html',
 'EarthCheck_Assessed.html',
 'East_Bloomfield_Historic_District.html',
 'East_Down_(Northern_Ireland_Parliament_constituency).html',
 'Eastbrook_Academy.html',
 'Eastern_Finnmark_Police_District.html',
 'Echembrotus.html',
 'Eco-Drive.html',
 'Ed_Jackson_(rugby_player).html',
 'Eddie_Durie.html',
 'Eddie_Eyre.html',
 'Edmonton_municipal_election,_1961.html',
 'EDP_Sarichioi_Wind_Farm.html',
 'Eduardo_De_Filippo.html',
 'Education_and_Training_Board.html',
 'Education_in_Tacloban.html',
 'Edward_Grosvenor.html',
 'Edward_Holmes_Baldock_(dealer).html',
 'Edwin_Bollier.html',
 'Egg_coffee.html',
 'Eggerberg_railway_station.html',
 'Ego_Dominus_Tuus.html',
 'Einstein_(horse).html',
 'Eivind_Hiis_Hauge.html',
 'Ek_Dil_Sau_Afsane.html',
 'El%C5%BCbieta_Dru%C5%BCbacka.html',
 'El_Bordj.html',
 'El_Pas_de_la_Casa.html',
 'Elaine_Fleming.html',
 'ELED.html',
 'Elgin_National_Watch_Company.html',
 'Elio_Calderini.html',
 'Elisa_von_der_Recke.html',
 'Elizabeth_Gray_(fossil_collector).html',
 'Elo%C3%ADna_Miyares_Berm%C3%BAdez.html',
 'Els_Dottermans.html',
 'Elzear_Torreggiani.html',
 'Emarginula_koon.html',
 'Embraer_Unidade_Gavi%C3%A3o_Peixoto_Airport.html',
 'EMD_SD40-2.html',
 'Emily_(1964_song).html',
 'Eminencia.html',
 'Emmanuel_Muhammad.html',
 'Emperor_(novel_series).html',
 'Enamul_Haque_(cricketer,_born_1966).html',
 'Endre_Church.html',
 'ENESSERE.html',
 'English_cricket_team_in_South_Africa_in_1956%E2%80%9357.html',
 'ENMAX_Centrium.html',
 'Enrique_Morales.html',
 'Environmental_impact_of_agriculture.html',
 'Epichorista.html',
 'Epropetes_metallica.html',
 'Equestrian_at_the_1936_Summer_Olympics.html',
 'Erd%C5%91s%E2%80%93Faber%E2%80%93Lov%C3%A1sz_conjecture.html',
 'Eressa_aperiens.html',
 'Eric_Ziebold.html',
 'Erigeron_canaani.html',
 'Erwin_Lutzer.html',
 'Eryngium_planum.html',
 'Esher_Church_of_England_High_School.html',
 'Estadio_Municipal_Pozoblanco.html',
 'Estelle_v._Smith.html',
 'Eternamente_Romanticos.html',
 'Ethan_Van_der_Ryn.html',
 'Ethel_Johns.html',
 'ETS-VIII.html',
 'Eudonia_notozeucta.html',
 'Eugamandus_brunneus.html',
 'Eugenio_Morelli.html',
 'Eupithecia_trancasae.html',
 'Europa_(Roman_province).html',
 'Euxoa_simulata.html',
 'Evanston,_Cincinnati.html',
 'Evene.html',
 'Ewa_Kasprzyk_(athlete).html',
 'Explanation_module.html',
 'Exploratorium_(film).html',
 'Extension_of_the_Wish.html',
 'Eye_of_the_Beholder_III:_Assault_on_Myth_Drannor.html',
 'Eyes_Galaxies.html',
 'F%C3%A9lix_C%C3%A1rdenas.html',
 'F._L._Griggs.html',
 'Faat_Zakirov.html',
 'Face_Drop.html',
 'Faces_(Run%E2%80%93D.M.C._song).html',
 'Facial_cleft.html',
 'Facundo_Gamband%C3%A9.html',
 'Fahy,_County_Mayo.html',
 'Failing_Office_Building.html',
 'Faizullah.html',
 'Falman-County_Acres,_Texas.html',
 'False_pregnancy.html',
 'Faryab,_Dashtestan.html',
 'FC_Bobruisk.html',
 'FC_Khikhani_Khulo.html',
 'Fe%27i_banana.html',
 'Fear_play.html',
 'Feel_No_Fret.html',
 'Feiner_v._New_York.html',
 'Feodosia_Morozova.html',
 'Ferdinand_Arnodin.html',
 'Ferdinand_Mainzer.html',
 'Feria_del_Sol_(M%C3%A9rida).html',
 'Fernanda_Vasconcellos.html',
 'Feuerzangenbowle.html',
 'Fictionwise.html',
 'Fifty_Years_of_Music.html',
 'Filip_Pyrochta.html',
 'Filochy.html',
 'Findwell.html',
 'FinnSec_Security.html',
 'Finnveden.html',
 'Firebaugh,_California.html',
 'Fireworks_EP.html',
 'Firmin%C3%B3polis.html',
 'Fischli.html',
 'Flag_of_Chicago.html',
 'Flag_of_the_Austral_Islands.html',
 'Flashmob_(album).html',
 'Flat_roof.html',
 'Fleetwood,_Oklahoma.html',
 'Flight_Design_Boxtair.html',
 'Flour_Babies.html',
 'Foidolite.html',
 'Foilbacks.html',
 'Follow_(album).html',
 'Football_at_the_National_Games_of_China.html',
 'Football_Foundation.html',
 'Fort_Astoria.html',
 'Fortabat_Art_Collection.html',
 'Forth_and_Bargy_dialect.html',
 'Fortuna_Glacier.html',
 'Forward_Operating_Base_Grizzly.html',
 'Fougangoue.html',
 'Foulonia.html',
 'Fractured_(Everything_I_Said_Was_True).html',
 'France_in_the_Eurovision_Song_Contest_2010.html',
 'Frances_Morris_(actress).html',
 'Frank_C._Archibald_(Vermont_politician).html',
 'Frank_Drum.html',
 'Frank_Gross.html',
 'Frans,_Ain.html',
 'Franz_Georg_Benkert.html',
 'Fraser_Lake_Airport.html',
 'Fred_H._Hildebrandt.html',
 'Fred_Marks.html',
 'Frederick_Leadbetter.html',
 'Freedom_(White_Heart_album).html',
 'Freehold_Township_Schools.html',
 'Friedrich_Albrecht_Anton_Meyer.html',
 'Friedrich_Kirchner.html',
 'Friendship,_Wake_County,_North_Carolina.html',
 'Frisilia_sulcata.html',
 'Frithjof_Schmidt.html',
 'From_All_Sides.html',
 'Frost_Township,_Michigan.html',
 'Fu_Biao.html',
 'Fucibet.html',
 'Functoid.html',
 'Fureai_kippu.html',
 'Furkan_Korkmaz.html',
 'Furto_di_sera_bel_colpo_si_spera.html',
 'Furubira_District,_Hokkaido.html',
 'Fusinus_carvalhoriosi.html',
 'Future_Weather.html',
 'G%C3%B3ra,_Mogilno_County.html',
 'G%C3%B6ncruszka.html',
 'G.O.Y.A._(Gunz_Or_Yay_Available).html',
 'G.S._Lamias_Achilleus.html',
 'Ga%C5%A1parci.html',
 'Gabriele_Poso.html',
 'Gacharageini.html',
 'Gad_(deity).html',
 'Gaetanus_Matthew_Perez.html',
 'Gal%C3%A1pagos,_Guadalajara.html',
 'Galician_Nationalist_Bloc.html',
 'Galloway_and_Upper_Nithsdale_(Scottish_Parliament_constituency).html',
 'Gander_(surname).html',
 'Gandigwad.html',
 'Gang_run_printing.html',
 'Garde_Civique.html',
 'Garden-based_learning.html',
 ...]
'''

len(os.listdir("wiki")) # count of above items

with open("wiki/Cecil_Peak.html") as f:
    print(f.read())


'''
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Cecil Peak - Wikipedia</title>
<script>document.documentElement.className = document.documentElement.className.replace( /(^|\s)client-nojs(\s|$)/, "$1client-js$2" );</script>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Cecil_Peak","wgTitle":"Cecil Peak","wgCurRevisionId":724716112,"wgRevisionId":724716112,"wgArticleId":36574331,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Coordinates on Wikidata","All stub articles","Mountains of Otago","Queenstown-Lakes District","Southern Alps","Otago geography stubs"],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Cecil_Peak","wgRelevantArticleId":36574331,"wgRequestId":"WLhgJApAADkAAI@nTZ4AAACB","wgIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgFlaggedRevsParams":{"tags":{}},"wgStableRevisionId":null,"wgWikiEditorEnabledModules":{"toolbar":true,"dialogs":true,"preview":false,"publish":false},"wgBetaFeaturesFeatures":[],"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsShouldSendModuleToUser":false,"wgPopupsConflictsWithNavPopupGadget":false,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","usePageImages":true,"usePageDescriptions":true},"wgPreferredVariant":"en","wgMFDisplayWikibaseDescriptions":{"search":true,"nearby":true,"watchlist":true,"tagline":true},"wgRelatedArticles":null,"wgRelatedArticlesBetaFeatureEnabled":false,"wgRelatedArticlesUseCirrusSearch":true,"wgRelatedArticlesOnlyUseCirrusSearch":false,"wgULSCurrentAutonym":"English","wgNoticeProject":"wikipedia","wgCentralNoticeCookiesToDelete":[],"wgCentralNoticeCategoriesUsingLegacy":["Fundraising","fundraising"],"wgCategoryTreePageCategoryOptions":"{\"mode\":0,\"hideprefix\":20,\"showcount\":true,\"namespaces\":false}","wgCoordinates":{"lat":-45.108831,"lon":168.628463},"wgWikibaseItemId":"Q5056265","wgCentralAuthMobileDomain":false,"wgVisualEditorToolbarScrollOffset":0,"wgEditSubmitButtonLabelPublish":false});mw.loader.state({"ext.globalCssJs.user.styles":"ready","ext.globalCssJs.site.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","user":"ready","user.options":"loading","user.tokens":"loading","ext.cite.styles":"ready","wikibase.client.init":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","mediawiki.sectionAnchor":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready","ext.globalCssJs.user":"ready","ext.globalCssJs.site":"ready"});mw.loader.implement("user.options@0j3lz3q",function($,jQuery,require,module){mw.user.options.set({"variant":"en"});});mw.loader.implement("user.tokens@1dqfd7l",function ( $, jQuery, require, module ) {
mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});/*@nomin*/;

});mw.loader.load(["ext.cite.a11y","mediawiki.action.view.postEdit","site","mediawiki.page.startup","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","mediawiki.legacy.wikibits","mediawiki.searchSuggest","ext.gadget.teahouse","ext.gadget.ReferenceTooltips","ext.gadget.watchlist-notice","ext.gadget.DRN-wizard","ext.gadget.charinsert","ext.gadget.refToolbar","ext.gadget.extra-toolbar-buttons","ext.gadget.switcher","ext.gadget.featured-articles-links","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging.subscriber","ext.wikimediaEvents","ext.navigationTiming","ext.uls.eventlogger","ext.uls.init","ext.uls.interface","ext.quicksurveys.init","ext.centralNotice.geoIP","ext.centralNotice.startUp","skins.vector.js"]);});</script>
<link rel="stylesheet" href="/w/load.php?debug=false&amp;lang=en&amp;modules=ext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cmediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.sectionAnchor%7Cmediawiki.skinning.interface%7Cskins.vector.styles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"/>
<script async="" src="/w/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/w/load.php?debug=false&amp;lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/>
<meta name="generator" content="MediaWiki 1.29.0-wmf.13"/>
<meta name="referrer" content="origin-when-cross-origin"/>
<link rel="alternate" href="android-app://org.wikipedia/http/en.m.wikipedia.org/wiki/Cecil_Peak"/>
<link rel="alternate" type="application/x-wiki" title="Edit this page" href="/w/index.php?title=Cecil_Peak&amp;action=edit"/>
<link rel="edit" title="Edit this page" href="/w/index.php?title=Cecil_Peak&amp;action=edit"/>
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png"/>
<link rel="shortcut icon" href="/static/favicon/wikipedia.ico"/>
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (en)"/>
<link rel="EditURI" type="application/rsd+xml" href="//en.wikipedia.org/w/api.php?action=rsd"/>
<link rel="copyright" href="//creativecommons.org/licenses/by-sa/3.0/"/>
<link rel="canonical" href="https://en.wikipedia.org/wiki/Cecil_Peak"/>
<link rel="dns-prefetch" href="//login.wikimedia.org"/>
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Cecil_Peak rootpage-Cecil_Peak skin-vector action-view">		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<div id="content" class="mw-body" role="main">
			<a id="top"></a>

							<div id="siteNotice"><!-- CentralNotice --></div>
						<div class="mw-indicators">
</div>
			<h1 id="firstHeading" class="firstHeading" lang="en">Cecil Peak</h1>
									<div id="bodyContent" class="mw-body-content">
									<div id="siteSub">From Wikipedia, the free encyclopedia</div>
								<div id="contentSub"></div>
												<div id="jump-to-nav" class="mw-jump">
					Jump to:					<a href="#mw-head">navigation</a>, 					<a href="#p-search">search</a>
				</div>
				<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><p><b>Cecil Peak</b> is a mountain in the <a href="/wiki/Wakatipu_Basin" title="Wakatipu Basin">Wakatipu Basin</a>, <a href="/wiki/New_Zealand" title="New Zealand">New Zealand</a> and reaches a height of 1,978 metres.<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup> It is on the south side of <a href="/wiki/Lake_Wakatipu" title="Lake Wakatipu">Lake Wakatipu</a>, south south-west of <a href="/wiki/Queenstown,_New_Zealand" title="Queenstown, New Zealand">Queenstown</a> and is highly prominent from around this area. <sup id="cite_ref-2" class="reference"><a href="#cite_note-2">[2]</a></sup></p>
<div class="thumb tright">
<div class="thumbinner" style="width:502px;"><a href="/wiki/File:Cecil-Peak-and-Walter-Peak-with-snow.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/97/Cecil-Peak-and-Walter-Peak-with-snow.jpg/500px-Cecil-Peak-and-Walter-Peak-with-snow.jpg" width="500" height="158" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/97/Cecil-Peak-and-Walter-Peak-with-snow.jpg/750px-Cecil-Peak-and-Walter-Peak-with-snow.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/97/Cecil-Peak-and-Walter-Peak-with-snow.jpg/1000px-Cecil-Peak-and-Walter-Peak-with-snow.jpg 2x" data-file-width="3608" data-file-height="1143" /></a>
<div class="thumbcaption">
<div class="magnify"><a href="/wiki/File:Cecil-Peak-and-Walter-Peak-with-snow.jpg" class="internal" title="Enlarge"></a></div>
View from Fernhill of Cecil Peak (<a href="/wiki/Walter_Peak,_New_Zealand" class="mw-redirect" title="Walter Peak, New Zealand">Walter Peak</a> on right). Kā Kamu-a-Hakitekura is the <a href="/wiki/M%C4%81ori_language" title="Māori language">Māori</a> name for both mountains.</div>
</div>
</div>
<p>Vegetation is mainly grass and tussock (as it is under a pastoral lease<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup>) with trees near the waterline. <a href="/wiki/Hidden_Island,_New_Zealand" class="mw-redirect" title="Hidden Island, New Zealand">Hidden Island</a> is one of four islands in Lake Wakatipu and sits very close to the shoreline of Cecil Peak. On 27 March 2010 a local band performed an outdoor concert in a natural amphitheatre on the peak playing songs from the band <a href="/wiki/Pink_Floyd" title="Pink Floyd">Pink Floyd</a>.<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup></p>
<h2><span class="mw-headline" id="Name">Name</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Cecil_Peak&amp;action=edit&amp;section=1" title="Edit section: Name">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Both Cecil Peak and the nearby mountain of Walter Peak were named after <a href="/wiki/William_Gilbert_Rees" title="William Gilbert Rees">William Rees'</a> eldest sons' first given names by the surveyor <a href="/wiki/James_McKerrow" title="James McKerrow">James McKerrow</a> in 1862.<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup></p>
<h2><span class="mw-headline" id="See_also">See also</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Cecil_Peak&amp;action=edit&amp;section=2" title="Edit section: See also">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul>
<li><a href="/wiki/List_of_mountains_of_New_Zealand_by_height" title="List of mountains of New Zealand by height">List of mountains of New Zealand by height</a></li>
<li><a href="/wiki/Walter_Peak_(New_Zealand)" title="Walter Peak (New Zealand)">Walter Peak</a></li>
</ul>
<h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Cecil_Peak&amp;action=edit&amp;section=3" title="Edit section: References">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><b><a href="#cite_ref-1">^</a></b></span> <span class="reference-text"><cite class="citation web">Malcolm, McKinnon. <a rel="nofollow" class="external text" href="http://www.teara.govt.nz/en/otago-places/17">"Otago places - Wakatipu basin"</a>. Te Ara - the Encyclopedia of New Zealand.</cite><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3ACecil+Peak&amp;rft.aufirst=McKinnon&amp;rft.aulast=Malcolm&amp;rft.btitle=Otago+places+-+Wakatipu+basin&amp;rft.genre=unknown&amp;rft_id=http%3A%2F%2Fwww.teara.govt.nz%2Fen%2Fotago-places%2F17&amp;rft.pub=Te+Ara+-+the+Encyclopedia+of+New+Zealand&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span></li>
<li id="cite_note-2"><span class="mw-cite-backlink"><b><a href="#cite_ref-2">^</a></b></span> <span class="reference-text"><cite class="citation web"><a rel="nofollow" class="external text" href="http://www.tekaraka.co.nz/Issues/TeKaraka44.pdf">"Ngai Tahu Names"</a> <span style="font-size:85%;">(PDF)</span>. <i>Te Karaka Issue 44, pg 13</i>. tekaraka.co.nz<span class="reference-accessdate">. Retrieved <span class="nowrap">18 September</span> 2013</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3ACecil+Peak&amp;rft.atitle=Ngai+Tahu+Names&amp;rft.genre=unknown&amp;rft_id=http%3A%2F%2Fwww.tekaraka.co.nz%2FIssues%2FTeKaraka44.pdf&amp;rft.jtitle=Te+Karaka+Issue+44%2C+pg+13&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal" class="Z3988"><span style="display:none;">&#160;</span></span></span></li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b><a href="#cite_ref-3">^</a></b></span> <span class="reference-text"><cite class="citation web"><a rel="nofollow" class="external text" href="http://www.linz.govt.nz/sites/default/files/docs/crownproperty/high-country-leases/leaselist/cecil-peak-ddr-pt1.pdf">"Crown Pastoral Land Tenure Review"</a> <span style="font-size:85%;">(PDF)</span>. Land Information New Zealand.</cite><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3ACecil+Peak&amp;rft.btitle=Crown+Pastoral+Land+Tenure+Review&amp;rft.genre=unknown&amp;rft_id=http%3A%2F%2Fwww.linz.govt.nz%2Fsites%2Fdefault%2Ffiles%2Fdocs%2Fcrownproperty%2Fhigh-country-leases%2Fleaselist%2Fcecil-peak-ddr-pt1.pdf&amp;rft.pub=Land+Information+New+Zealand&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span></li>
<li id="cite_note-4"><span class="mw-cite-backlink"><b><a href="#cite_ref-4">^</a></b></span> <span class="reference-text"><cite class="citation web"><a rel="nofollow" class="external text" href="http://www.scoop.co.nz/stories/CU1003/S00353.htm">"Rocking it on Cecil Peak"</a>. Scoop Media.</cite><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3ACecil+Peak&amp;rft.btitle=Rocking+it+on+Cecil+Peak&amp;rft.genre=unknown&amp;rft_id=http%3A%2F%2Fwww.scoop.co.nz%2Fstories%2FCU1003%2FS00353.htm&amp;rft.pub=Scoop+Media&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span></li>
<li id="cite_note-5"><span class="mw-cite-backlink"><b><a href="#cite_ref-5">^</a></b></span> <span class="reference-text"><cite class="citation book">Jardine, D.G. (1978). <i>Shadows on the Hill</i>. A.H. &amp; A.W. Reed Ltd. p.&#160;185. <a href="/wiki/International_Standard_Book_Number" title="International Standard Book Number">ISBN</a>&#160;<a href="/wiki/Special:BookSources/0589010093" title="Special:BookSources/0589010093">0589010093</a>.</cite><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3ACecil+Peak&amp;rft.aufirst=D.G.&amp;rft.aulast=Jardine&amp;rft.btitle=Shadows+on+the+Hill&amp;rft.date=1978&amp;rft.genre=book&amp;rft.isbn=0589010093&amp;rft.pages=185&amp;rft.pub=A.H.+%26+A.W.+Reed+Ltd&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span></li>
</ol>
</div>
<p><span style="font-size: small;"><span id="coordinates"><a href="/wiki/Geographic_coordinate_system" title="Geographic coordinate system">Coordinates</a>: <span class="plainlinks nourlexpansion"><a class="external text" href="//tools.wmflabs.org/geohack/geohack.php?pagename=Cecil_Peak&amp;params=-45.108831_N_168.628463_E_"><span class="geo-nondefault"><span class="geo-dms" title="Maps, aerial photos, and other data for this location"><span class="latitude">45°06′32″S</span> <span class="longitude">168°37′42″E</span></span></span><span class="geo-multi-punct">﻿ / ﻿</span><span class="geo-default"><span class="geo-dec" title="Maps, aerial photos, and other data for this location">45.108831°S 168.628463°E</span><span style="display:none">﻿ / <span class="geo">-45.108831; 168.628463</span></span></span></a></span></span></span></p>
<p><br /></p>
<table class="metadata plainlinks stub" role="presentation" style="background:transparent">
<tr>
<td><a href="/wiki/File:Position_of_Otago.png" class="image"><img alt="Stub icon" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Position_of_Otago.png/32px-Position_of_Otago.png" width="32" height="47" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Position_of_Otago.png/48px-Position_of_Otago.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Position_of_Otago.png/64px-Position_of_Otago.png 2x" data-file-width="405" data-file-height="590" /></a></td>
<td><i>This <a href="/wiki/Otago" title="Otago">Otago</a> geography article is a <a href="/wiki/Wikipedia:Stub" title="Wikipedia:Stub">stub</a>. You can help Wikipedia by <a class="external text" href="//en.wikipedia.org/w/index.php?title=Cecil_Peak&amp;action=edit">expanding it</a>.</i>
<div class="plainlinks hlist navbar mini" style="position: absolute; right: 15px; display: none;">
<ul>
<li class="nv-view"><a href="/wiki/Template:Otago-geo-stub" title="Template:Otago-geo-stub"><abbr title="View this template">v</abbr></a></li>
<li class="nv-talk"><a href="/wiki/Template_talk:Otago-geo-stub" title="Template talk:Otago-geo-stub"><abbr title="Discuss this template">t</abbr></a></li>
<li class="nv-edit"><a class="external text" href="//en.wikipedia.org/w/index.php?title=Template:Otago-geo-stub&amp;action=edit"><abbr title="Edit this template">e</abbr></a></li>
</ul>
</div>
</td>
</tr>
</table>


<!-- 
NewPP limit report
Parsed by mw1211
Cached time: 20170210085052
Cache expiry: 2592000
Dynamic content: false
CPU time usage: 0.080 seconds
Real time usage: 0.107 seconds
Preprocessor visited node count: 253/1000000
Preprocessor generated node count: 0/1500000
Post‐expand include size: 10233/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 4/40
Expensive parser function count: 0/500
Lua time usage: 0.043/10.000 seconds
Lua memory usage: 2.57 MB/50 MB
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   89.189      1 -total
 62.17%   55.447      1 Template:Reflist
 48.96%   43.664      4 Template:Cite_web
 24.91%   22.219      1 Template:Coord
 12.74%   11.365      1 Template:Otago-geo-stub
 11.34%   10.113      1 Template:Asbox
  4.71%    4.200      1 Template:Cite_book
-->

<!-- Saved in parser cache with key enwiki:pcache:idhash:36574331-0!*!0!!*!4!* and timestamp 20170210085052 and revision id 724716112
 -->
<noscript><img src="//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" title="" width="1" height="1" style="border: none; position: absolute;" /></noscript></div>					<div class="printfooter">
						Retrieved from "<a dir="ltr" href="https://en.wikipedia.org/w/index.php?title=Cecil_Peak&amp;oldid=724716112">https://en.wikipedia.org/w/index.php?title=Cecil_Peak&amp;oldid=724716112</a>"					</div>
				<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Help:Category" title="Help:Category">Categories</a>: <ul><li><a href="/wiki/Category:Mountains_of_Otago" title="Category:Mountains of Otago">Mountains of Otago</a></li><li><a href="/wiki/Category:Queenstown-Lakes_District" title="Category:Queenstown-Lakes District">Queenstown-Lakes District</a></li><li><a href="/wiki/Category:Southern_Alps" title="Category:Southern Alps">Southern Alps</a></li><li><a href="/wiki/Category:Otago_geography_stubs" title="Category:Otago geography stubs">Otago geography stubs</a></li></ul></div><div id="mw-hidden-catlinks" class="mw-hidden-catlinks mw-hidden-cats-hidden">Hidden categories: <ul><li><a href="/wiki/Category:Coordinates_on_Wikidata" title="Category:Coordinates on Wikidata">Coordinates on Wikidata</a></li><li><a href="/wiki/Category:All_stub_articles" title="Category:All stub articles">All stub articles</a></li></ul></div></div>				<div class="visualClear"></div>
							</div>
		</div>
		<div id="mw-navigation">
			<h2>Navigation menu</h2>

			<div id="mw-head">
									<div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label">
						<h3 id="p-personal-label">Personal tools</h3>
						<ul>
							<li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]" accesskey="n">Talk</a></li><li id="pt-anoncontribs"><a href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]" accesskey="y">Contributions</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=Cecil+Peak" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Cecil+Peak" title="You're encouraged to log in; however, it's not mandatory. [o]" accesskey="o">Log in</a></li>						</ul>
					</div>
									<div id="left-navigation">
										<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
						<h3 id="p-namespaces-label">Namespaces</h3>
						<ul>
															<li  id="ca-nstab-main" class="selected"><span><a href="/wiki/Cecil_Peak"  title="View the content page [c]" accesskey="c">Article</a></span></li>
															<li  id="ca-talk"><span><a href="/wiki/Talk:Cecil_Peak"  title="Discussion about the content page [t]" accesskey="t" rel="discussion">Talk</a></span></li>
													</ul>
					</div>
										<div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label">
												<h3 id="p-variants-label">
							<span>Variants</span><a href="#"></a>
						</h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
									</div>
				<div id="right-navigation">
										<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
						<h3 id="p-views-label">Views</h3>
						<ul>
															<li id="ca-view" class="selected"><span><a href="/wiki/Cecil_Peak" >Read</a></span></li>
															<li id="ca-edit"><span><a href="/w/index.php?title=Cecil_Peak&amp;action=edit"  title="Edit this page [e]" accesskey="e">Edit</a></span></li>
															<li id="ca-history" class="collapsible"><span><a href="/w/index.php?title=Cecil_Peak&amp;action=history"  title="Past revisions of this page [h]" accesskey="h">View history</a></span></li>
													</ul>
					</div>
										<div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label">
						<h3 id="p-cactions-label"><span>More</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
										<div id="p-search" role="search">
						<h3>
							<label for="searchInput">Search</label>
						</h3>

						<form action="/w/index.php" id="searchform">
							<div id="simpleSearch">
							<input type="search" name="search" placeholder="Search Wikipedia" title="Search Wikipedia [f]" accesskey="f" id="searchInput"/><input type="hidden" value="Special:Search" name="title"/><input type="submit" name="fulltext" value="Search" title="Search Wikipedia for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton"/><input type="submit" name="go" value="Go" title="Go to a page with this exact name if it exists" id="searchButton" class="searchButton"/>							</div>
						</form>
					</div>
									</div>
			</div>
			<div id="mw-panel">
				<div id="p-logo" role="banner"><a class="mw-wiki-logo" href="/wiki/Main_Page"  title="Visit the main page"></a></div>
						<div class="portal" role="navigation" id='p-navigation' aria-labelledby='p-navigation-label'>
			<h3 id='p-navigation-label'>Navigation</h3>

			<div class="body">
									<ul>
						<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li><li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li><li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content – the best of Wikipedia">Featured content</a></li><li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li><li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li><li id="n-sitesupport"><a href="https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us">Donate to Wikipedia</a></li><li id="n-shoplink"><a href="//shop.wikimedia.org" title="Visit the Wikipedia store">Wikipedia store</a></li>					</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-interaction' aria-labelledby='p-interaction-label'>
			<h3 id='p-interaction-label'>Interaction</h3>

			<div class="body">
									<ul>
						<li id="n-help"><a href="/wiki/Help:Contents" title="Guidance on how to use and edit Wikipedia">Help</a></li><li id="n-aboutsite"><a href="/wiki/Wikipedia:About" title="Find out about Wikipedia">About Wikipedia</a></li><li id="n-portal"><a href="/wiki/Wikipedia:Community_portal" title="About the project, what you can do, where to find things">Community portal</a></li><li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r">Recent changes</a></li><li id="n-contactpage"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us" title="How to contact Wikipedia">Contact page</a></li>					</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-tb' aria-labelledby='p-tb-label'>
			<h3 id='p-tb-label'>Tools</h3>

			<div class="body">
									<ul>
						<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Cecil_Peak" title="List of all English Wikipedia pages containing links to this page [j]" accesskey="j">What links here</a></li><li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Cecil_Peak" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li><li id="t-upload"><a href="/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]" accesskey="u">Upload file</a></li><li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li><li id="t-permalink"><a href="/w/index.php?title=Cecil_Peak&amp;oldid=724716112" title="Permanent link to this revision of the page">Permanent link</a></li><li id="t-info"><a href="/w/index.php?title=Cecil_Peak&amp;action=info" title="More information about this page">Page information</a></li><li id="t-wikibase"><a href="https://www.wikidata.org/wiki/Q5056265" title="Link to connected data repository item [g]" accesskey="g">Wikidata item</a></li><li id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=Cecil_Peak&amp;id=724716112" title="Information on how to cite this page">Cite this page</a></li>					</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-coll-print_export' aria-labelledby='p-coll-print_export-label'>
			<h3 id='p-coll-print_export-label'>Print/export</h3>

			<div class="body">
									<ul>
						<li id="coll-create_a_book"><a href="/w/index.php?title=Special:Book&amp;bookcmd=book_creator&amp;referer=Cecil+Peak">Create a book</a></li><li id="coll-download-as-rdf2latex"><a href="/w/index.php?title=Special:Book&amp;bookcmd=render_article&amp;arttitle=Cecil+Peak&amp;returnto=Cecil+Peak&amp;oldid=724716112&amp;writer=rdf2latex">Download as PDF</a></li><li id="t-print"><a href="/w/index.php?title=Cecil_Peak&amp;printable=yes" title="Printable version of this page [p]" accesskey="p">Printable version</a></li>					</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-lang' aria-labelledby='p-lang-label'>
			<h3 id='p-lang-label'>Languages</h3>

			<div class="body">
									<ul>
						<li class="interlanguage-link interwiki-ceb"><a href="https://ceb.wikipedia.org/wiki/Cecil_Peak_(tumoy_sa_bukid)" title="Cecil Peak (tumoy sa bukid) – Cebuano" lang="ceb" hreflang="ceb" class="interlanguage-link-target">Cebuano</a></li><li class="interlanguage-link interwiki-cs"><a href="https://cs.wikipedia.org/wiki/Cecil_Peak" title="Cecil Peak – Czech" lang="cs" hreflang="cs" class="interlanguage-link-target">Čeština</a></li><li class="interlanguage-link interwiki-ka"><a href="https://ka.wikipedia.org/wiki/%E1%83%A1%E1%83%94%E1%83%A1%E1%83%98%E1%83%9A%E1%83%98%E1%83%A1_%E1%83%9E%E1%83%98%E1%83%99%E1%83%98" title="სესილის პიკი – Georgian" lang="ka" hreflang="ka" class="interlanguage-link-target">ქართული</a></li><li class="interlanguage-link interwiki-ru"><a href="https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%81%D0%B8%D0%BB-%D0%9F%D0%B8%D0%BA" title="Сесил-Пик – Russian" lang="ru" hreflang="ru" class="interlanguage-link-target">Русский</a></li>					</ul>
				<div class='after-portlet after-portlet-lang'><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Q5056265#sitelinks-wikipedia" title="Edit interlanguage links" class="wbc-editpage">Edit links</a></span></div>			</div>
		</div>
				</div>
		</div>
		<div id="footer" role="contentinfo">
							<ul id="footer-info">
											<li id="footer-info-lastmod"> This page was last modified on 11 June 2016, at 01:06.</li>
											<li id="footer-info-copyright">Text is available under the <a rel="license" href="//en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License">Creative Commons Attribution-ShareAlike License</a><a rel="license" href="//creativecommons.org/licenses/by-sa/3.0/" style="display:none;"></a>;
additional terms may apply.  By using this site, you agree to the <a href="//wikimediafoundation.org/wiki/Terms_of_Use">Terms of Use</a> and <a href="//wikimediafoundation.org/wiki/Privacy_policy">Privacy Policy</a>. Wikipedia® is a registered trademark of the <a href="//www.wikimediafoundation.org/">Wikimedia Foundation, Inc.</a>, a non-profit organization.</li>
									</ul>
							<ul id="footer-places">
											<li id="footer-places-privacy"><a href="https://wikimediafoundation.org/wiki/Privacy_policy" class="extiw" title="wmf:Privacy policy">Privacy policy</a></li>
											<li id="footer-places-about"><a href="/wiki/Wikipedia:About" title="Wikipedia:About">About Wikipedia</a></li>
											<li id="footer-places-disclaimer"><a href="/wiki/Wikipedia:General_disclaimer" title="Wikipedia:General disclaimer">Disclaimers</a></li>
											<li id="footer-places-contact"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us">Contact Wikipedia</a></li>
											<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
											<li id="footer-places-cookiestatement"><a href="https://wikimediafoundation.org/wiki/Cookie_statement">Cookie statement</a></li>
											<li id="footer-places-mobileview"><a href="//en.m.wikipedia.org/w/index.php?title=Cecil_Peak&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Mobile view</a></li>
									</ul>
										<ul id="footer-icons" class="noprint">
											<li id="footer-copyrightico">
							<a href="https://wikimediafoundation.org/"><img src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation"/></a>						</li>
											<li id="footer-poweredbyico">
							<a href="//www.mediawiki.org/"><img src="/static/images/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88" height="31"/></a>						</li>
									</ul>
						<div style="clear:both"></div>
		</div>
		<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.080","walltime":"0.107","ppvisitednodes":{"value":253,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1500000},"postexpandincludesize":{"value":10233,"limit":2097152},"templateargumentsize":{"value":0,"limit":2097152},"expansiondepth":{"value":4,"limit":40},"expensivefunctioncount":{"value":0,"limit":500},"entityaccesscount":{"value":1,"limit":400},"timingprofile":["100.00%   89.189      1 -total"," 62.17%   55.447      1 Template:Reflist"," 48.96%   43.664      4 Template:Cite_web"," 24.91%   22.219      1 Template:Coord"," 12.74%   11.365      1 Template:Otago-geo-stub"," 11.34%   10.113      1 Template:Asbox","  4.71%    4.200      1 Template:Cite_book"]},"scribunto":{"limitreport-timeusage":{"value":"0.043","limit":"10.000"},"limitreport-memusage":{"value":2691141,"limit":52428800}},"cachereport":{"origin":"mw1211","timestamp":"20170210085052","ttl":2592000,"transientcontent":false}}});});</script><script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":71,"wgHostname":"mw1262"});});</script>
	</body>
</html>
'''

# It appears from above that most of the content is within the <div> tag as it common on this type of HTML page

import concurrent.futures # threading 
import time

pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

def read_data(filename):
    with open(filename) as f:
        data = f.read()
    return data

start = time.time()
filenames = ["wiki/{}".format(f) for f in os.listdir("wiki")]
content = pool.map(read_data, filenames)
content = list(content)

end = time.time()
print(end - start)
articles = [f.replace(".html", "").replace("wiki/", "") for f in filenames]

'''
2.952831983566284
It doesn't appear that threading makes a huge difference to performance. 
Perhaps this is due to the task performance of creating new threads.
'''

from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return str(soup.find_all("div", id="content")[0])

start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)
parsed = pool.map(parse_html, content)
parsed = list(parsed)
end = time.time()

print(end - start)

# 139.67757391929626 - very intensive - It looks like using as many processes are there are available processors speeds things up.

'''
Finding common tags to increase performance - Based on our findings, it looks like there are quite a few td, a, li, and span tags. This indicates that articles tend to have lots of links, along with lists and tables.
'''


def count_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = {}
    for tag in soup.find_all():
        if tag.name not in tags:
            tags[tag.name] = 0
        tags[tag.name] += 1
    return tags

start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)
tags = pool.map(count_tags, parsed)
tags = list(tags)

tag_counts = {}
for tag in tags:
    for k,v in tag.items():
        if k not in tag_counts:
            tag_counts[k] = 0
        tag_counts[k] += v
end = time.time()

print(end - start)
# 71.57306599617004


from collections import Counter
import re

def count_words(html):
    soup = BeautifulSoup(html, 'html.parser')
    words = {}
    text = soup.get_text()
    text = re.sub("\W+", " ", text.lower())
    words = text.split(" ")
    words = [w for w in words if len(w) >= 5]
    return Counter(words).most_common(10)

start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=3)
words = pool.map(count_words, parsed)
words = list(words)

word_counts = {}
for wc in words:
    for word, count in wc:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
end = time.time()

print(end - start)
word_counts
# 133.99117708206177
