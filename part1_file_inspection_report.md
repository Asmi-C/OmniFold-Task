# OmniFold File Inspection Report

Generated automatically to support Part 1 (Exploration and Gap Analysis).

## File: `multifold.h5`

- Pandas key: `/df`
- Shape: **418014 rows x 200 columns**

### HDF5 structure

- Group: df
- Dataset: df/axis0
- Dataset: df/axis1
- Dataset: df/block0_items
- Dataset: df/block0_values
- Dataset: df/block1_items
- Dataset: df/block1_values
- Dataset: df/block2_items
- Dataset: df/block2_values

### Column classification

- **observable** (24): pT_ll, pT_l1, pT_l2, eta_l1, eta_l2, phi_l1, phi_l2, y_ll, pT_trackj1, y_trackj1, phi_trackj1, m_trackj1, tau1_trackj1, tau2_trackj1, tau3_trackj1, pT_trackj2, y_trackj2, phi_trackj2, m_trackj2, tau1_trackj2, tau2_trackj2, tau3_trackj2, Ntracks_trackj1, Ntracks_trackj2
- **weight** (175): weight_mc, weights_nominal, weights_ensemble_0, weights_ensemble_1, weights_ensemble_2, weights_ensemble_3, weights_ensemble_4, weights_ensemble_5, weights_ensemble_6, weights_ensemble_7, weights_ensemble_8, weights_ensemble_9, weights_ensemble_10, weights_ensemble_11, weights_ensemble_12, weights_ensemble_13, weights_ensemble_14, weights_ensemble_15, weights_ensemble_16, weights_ensemble_17, weights_ensemble_18, weights_ensemble_19, weights_ensemble_20, weights_ensemble_21, weights_ensemble_22, weights_ensemble_23, weights_ensemble_24, weights_ensemble_25, weights_ensemble_26, weights_ensemble_27, weights_ensemble_28, weights_ensemble_29, weights_ensemble_30, weights_ensemble_31, weights_ensemble_32, weights_ensemble_33, weights_ensemble_34, weights_ensemble_35, weights_ensemble_36, weights_ensemble_37, weights_ensemble_38, weights_ensemble_39, weights_ensemble_40, weights_ensemble_41, weights_ensemble_42, weights_ensemble_43, weights_ensemble_44, weights_ensemble_45, weights_ensemble_46, weights_ensemble_47, weights_ensemble_48, weights_ensemble_49, weights_ensemble_50, weights_ensemble_51, weights_ensemble_52, weights_ensemble_53, weights_ensemble_54, weights_ensemble_55, weights_ensemble_56, weights_ensemble_57, weights_ensemble_58, weights_ensemble_59, weights_ensemble_60, weights_ensemble_61, weights_ensemble_62, weights_ensemble_63, weights_ensemble_64, weights_ensemble_65, weights_ensemble_66, weights_ensemble_67, weights_ensemble_68, weights_ensemble_69, weights_ensemble_70, weights_ensemble_71, weights_ensemble_72, weights_ensemble_73, weights_ensemble_74, weights_ensemble_75, weights_ensemble_76, weights_ensemble_77, weights_ensemble_78, weights_ensemble_79, weights_ensemble_80, weights_ensemble_81, weights_ensemble_82, weights_ensemble_83, weights_ensemble_84, weights_ensemble_85, weights_ensemble_86, weights_ensemble_87, weights_ensemble_88, weights_ensemble_89, weights_ensemble_90, weights_ensemble_91, weights_ensemble_92, weights_ensemble_93, weights_ensemble_94, weights_ensemble_95, weights_ensemble_96, weights_ensemble_97, weights_ensemble_98, weights_ensemble_99, weights_dd, weights_bootstrap_mc_0, weights_bootstrap_mc_1, weights_bootstrap_mc_2, weights_bootstrap_mc_3, weights_bootstrap_mc_4, weights_bootstrap_mc_5, weights_bootstrap_mc_6, weights_bootstrap_mc_7, weights_bootstrap_mc_8, weights_bootstrap_mc_9, weights_bootstrap_mc_10, weights_bootstrap_mc_11, weights_bootstrap_mc_12, weights_bootstrap_mc_13, weights_bootstrap_mc_14, weights_bootstrap_mc_15, weights_bootstrap_mc_16, weights_bootstrap_mc_17, weights_bootstrap_mc_18, weights_bootstrap_mc_19, weights_bootstrap_mc_20, weights_bootstrap_mc_21, weights_bootstrap_mc_22, weights_bootstrap_mc_23, weights_bootstrap_mc_24, weights_bootstrap_data_0, weights_bootstrap_data_1, weights_bootstrap_data_2, weights_bootstrap_data_3, weights_bootstrap_data_4, weights_bootstrap_data_5, weights_bootstrap_data_6, weights_bootstrap_data_7, weights_bootstrap_data_8, weights_bootstrap_data_9, weights_bootstrap_data_10, weights_bootstrap_data_11, weights_bootstrap_data_12, weights_bootstrap_data_13, weights_bootstrap_data_14, weights_bootstrap_data_15, weights_bootstrap_data_16, weights_bootstrap_data_17, weights_bootstrap_data_18, weights_bootstrap_data_19, weights_bootstrap_data_20, weights_bootstrap_data_21, weights_bootstrap_data_22, weights_bootstrap_data_23, weights_bootstrap_data_24, weights_pileup, weights_muEffReco, weights_muEffIso, weights_muEffTrack, weights_muEffTrig, weights_muCalID, weights_muCalMS, weights_muCalResBias, weights_muCalScale, weights_trackEffMain, weights_trackEffJet, weights_trackFake, weights_trackPtScale, weights_theoryPSjet, weights_theoryPSsoft, weights_theoryMPI, weights_theoryPSscale, weights_theoryAlphaS, weights_theoryQCD, weights_theoryPDF, weights_topBackground, weights_lumi
- **metadata** (0): None
- **other** (1): target_dd

### Missing values

- No missing values detected.

### Weight checks

- `weight_mc`: sum=1701.13, min=2.93189e-06, max=0.0192681, negative_count=0, zero_count=0
- `weights_nominal`: sum=1809.46, min=1.79444e-06, max=0.0756672, negative_count=0, zero_count=0
- `weights_ensemble_0`: sum=1812.01, min=1.29161e-06, max=0.102557, negative_count=0, zero_count=0
- `weights_ensemble_1`: sum=1813.26, min=9.35733e-07, max=0.0677593, negative_count=0, zero_count=0
- `weights_ensemble_2`: sum=1811.27, min=1.25059e-06, max=0.0708018, negative_count=0, zero_count=0
- `weights_ensemble_3`: sum=1804.29, min=1.47157e-06, max=0.0962612, negative_count=0, zero_count=0
- `weights_ensemble_4`: sum=1810.51, min=8.60584e-07, max=0.0910675, negative_count=0, zero_count=0
- `weights_ensemble_5`: sum=1812.19, min=2.37352e-06, max=0.101081, negative_count=0, zero_count=0
- `weights_ensemble_6`: sum=1805.44, min=5.45571e-07, max=0.0862184, negative_count=0, zero_count=0
- `weights_ensemble_7`: sum=1812.37, min=1.48382e-06, max=0.0876927, negative_count=0, zero_count=0
- `weights_ensemble_8`: sum=1813.47, min=8.63706e-07, max=0.0800152, negative_count=0, zero_count=0
- `weights_ensemble_9`: sum=1815.19, min=1.33076e-06, max=0.0778453, negative_count=0, zero_count=0
- `weights_ensemble_10`: sum=1818.22, min=8.81889e-07, max=0.0843497, negative_count=0, zero_count=0
- `weights_ensemble_11`: sum=1810.16, min=8.60137e-07, max=0.0903693, negative_count=0, zero_count=0
- `weights_ensemble_12`: sum=1808.03, min=1.53179e-06, max=0.157889, negative_count=0, zero_count=0
- `weights_ensemble_13`: sum=1814, min=3.31116e-07, max=0.0846525, negative_count=0, zero_count=0
- `weights_ensemble_14`: sum=1808.66, min=1.35632e-06, max=0.0835813, negative_count=0, zero_count=0
- `weights_ensemble_15`: sum=1806.17, min=1.07649e-06, max=0.0991908, negative_count=0, zero_count=0
- `weights_ensemble_16`: sum=1805.87, min=7.0262e-07, max=0.099289, negative_count=0, zero_count=0
- `weights_ensemble_17`: sum=1809.71, min=1.21734e-06, max=0.0902122, negative_count=0, zero_count=0
- `weights_ensemble_18`: sum=1811.03, min=1.64431e-06, max=0.114787, negative_count=0, zero_count=0
- `weights_ensemble_19`: sum=1804.48, min=1.1153e-06, max=0.0929338, negative_count=0, zero_count=0
- `weights_ensemble_20`: sum=1813.1, min=1.20811e-06, max=0.103518, negative_count=0, zero_count=0
- `weights_ensemble_21`: sum=1810.67, min=1.26862e-06, max=0.0893474, negative_count=0, zero_count=0
- `weights_ensemble_22`: sum=1810.98, min=1.03331e-06, max=0.1096, negative_count=0, zero_count=0
- `weights_ensemble_23`: sum=1814.09, min=3.50641e-06, max=0.0964651, negative_count=0, zero_count=0
- `weights_ensemble_24`: sum=1801.31, min=7.49312e-07, max=0.0911017, negative_count=0, zero_count=0
- `weights_ensemble_25`: sum=1808.09, min=1.15476e-06, max=0.070573, negative_count=0, zero_count=0
- `weights_ensemble_26`: sum=1815.27, min=2.56272e-06, max=0.0951032, negative_count=0, zero_count=0
- `weights_ensemble_27`: sum=1814.64, min=2.22285e-06, max=0.0604299, negative_count=0, zero_count=0
- `weights_ensemble_28`: sum=1806.6, min=8.20968e-07, max=0.0963703, negative_count=0, zero_count=0
- `weights_ensemble_29`: sum=1809.58, min=2.28255e-06, max=0.0664001, negative_count=0, zero_count=0
- `weights_ensemble_30`: sum=1817.21, min=1.52332e-06, max=0.115892, negative_count=0, zero_count=0
- `weights_ensemble_31`: sum=1808.24, min=2.30561e-06, max=0.0933343, negative_count=0, zero_count=0
- `weights_ensemble_32`: sum=1814.62, min=9.49908e-07, max=0.0821446, negative_count=0, zero_count=0
- `weights_ensemble_33`: sum=1811.23, min=7.17218e-07, max=0.067427, negative_count=0, zero_count=0
- `weights_ensemble_34`: sum=1812.31, min=1.46888e-06, max=0.0634212, negative_count=0, zero_count=0
- `weights_ensemble_35`: sum=1812.84, min=3.73341e-07, max=0.135258, negative_count=0, zero_count=0
- `weights_ensemble_36`: sum=1810.97, min=4.16726e-07, max=0.10484, negative_count=0, zero_count=0
- `weights_ensemble_37`: sum=1805.71, min=6.36114e-07, max=0.0717302, negative_count=0, zero_count=0
- `weights_ensemble_38`: sum=1806.54, min=1.15825e-06, max=0.0761491, negative_count=0, zero_count=0
- `weights_ensemble_39`: sum=1805.6, min=8.21947e-07, max=0.0785462, negative_count=0, zero_count=0
- `weights_ensemble_40`: sum=1810.28, min=5.63422e-07, max=0.0992583, negative_count=0, zero_count=0
- `weights_ensemble_41`: sum=1811.63, min=1.00818e-06, max=0.109218, negative_count=0, zero_count=0
- `weights_ensemble_42`: sum=1811.67, min=7.42458e-07, max=0.0810814, negative_count=0, zero_count=0
- `weights_ensemble_43`: sum=1817.48, min=1.96429e-07, max=0.114949, negative_count=0, zero_count=0
- `weights_ensemble_44`: sum=1806.45, min=7.97593e-07, max=0.0715082, negative_count=0, zero_count=0
- `weights_ensemble_45`: sum=1809.38, min=5.27042e-07, max=0.0911426, negative_count=0, zero_count=0
- `weights_ensemble_46`: sum=1807.08, min=8.32064e-07, max=0.12053, negative_count=0, zero_count=0
- `weights_ensemble_47`: sum=1814.19, min=2.36153e-07, max=0.0962145, negative_count=0, zero_count=0
- `weights_ensemble_48`: sum=1806.62, min=1.53539e-06, max=0.135322, negative_count=0, zero_count=0
- `weights_ensemble_49`: sum=1811.3, min=5.04167e-07, max=0.11239, negative_count=0, zero_count=0
- `weights_ensemble_50`: sum=1812.6, min=1.48482e-06, max=0.0884647, negative_count=0, zero_count=0
- `weights_ensemble_51`: sum=1816.99, min=1.33341e-06, max=0.0845731, negative_count=0, zero_count=0
- `weights_ensemble_52`: sum=1804.07, min=9.76547e-07, max=0.0712151, negative_count=0, zero_count=0
- `weights_ensemble_53`: sum=1805.49, min=2.8624e-07, max=0.106361, negative_count=0, zero_count=0
- `weights_ensemble_54`: sum=1807.82, min=1.51709e-06, max=0.0992582, negative_count=0, zero_count=0
- `weights_ensemble_55`: sum=1817.48, min=2.75948e-06, max=0.07905, negative_count=0, zero_count=0
- `weights_ensemble_56`: sum=1808.49, min=1.25327e-06, max=0.0830956, negative_count=0, zero_count=0
- `weights_ensemble_57`: sum=1803.55, min=8.54055e-07, max=0.0884135, negative_count=0, zero_count=0
- `weights_ensemble_58`: sum=1806.26, min=1.89513e-06, max=0.0861215, negative_count=0, zero_count=0
- `weights_ensemble_59`: sum=1814.09, min=1.36157e-06, max=0.113698, negative_count=0, zero_count=0
- `weights_ensemble_60`: sum=1807.55, min=3.85646e-07, max=0.101644, negative_count=0, zero_count=0
- `weights_ensemble_61`: sum=1808.97, min=6.49281e-07, max=0.094905, negative_count=0, zero_count=0
- `weights_ensemble_62`: sum=1810.43, min=5.85732e-07, max=0.10416, negative_count=0, zero_count=0
- `weights_ensemble_63`: sum=1809.86, min=1.22691e-06, max=0.0977133, negative_count=0, zero_count=0
- `weights_ensemble_64`: sum=1808.17, min=9.21792e-07, max=0.100489, negative_count=0, zero_count=0
- `weights_ensemble_65`: sum=1811.38, min=2.24652e-06, max=0.114816, negative_count=0, zero_count=0
- `weights_ensemble_66`: sum=1807.59, min=2.79795e-07, max=0.0937744, negative_count=0, zero_count=0
- `weights_ensemble_67`: sum=1812.99, min=8.59506e-07, max=0.0830208, negative_count=0, zero_count=0
- `weights_ensemble_68`: sum=1812.52, min=4.30914e-07, max=0.0919193, negative_count=0, zero_count=0
- `weights_ensemble_69`: sum=1813.15, min=1.09922e-06, max=0.0836892, negative_count=0, zero_count=0
- `weights_ensemble_70`: sum=1808.47, min=9.74388e-07, max=0.0910833, negative_count=0, zero_count=0
- `weights_ensemble_71`: sum=1811.65, min=2.4829e-06, max=0.0765481, negative_count=0, zero_count=0
- `weights_ensemble_72`: sum=1807.29, min=1.12994e-06, max=0.0888257, negative_count=0, zero_count=0
- `weights_ensemble_73`: sum=1803.35, min=1.56483e-07, max=0.115012, negative_count=0, zero_count=0
- `weights_ensemble_74`: sum=1808.32, min=6.80776e-07, max=0.113697, negative_count=0, zero_count=0
- `weights_ensemble_75`: sum=1811.77, min=1.55996e-06, max=0.0933287, negative_count=0, zero_count=0
- `weights_ensemble_76`: sum=1811.7, min=1.15358e-06, max=0.06715, negative_count=0, zero_count=0
- `weights_ensemble_77`: sum=1814.96, min=3.40301e-06, max=0.111611, negative_count=0, zero_count=0
- `weights_ensemble_78`: sum=1804.77, min=6.61409e-07, max=0.120803, negative_count=0, zero_count=0
- `weights_ensemble_79`: sum=1813.73, min=1.71147e-06, max=0.0758013, negative_count=0, zero_count=0
- `weights_ensemble_80`: sum=1810.31, min=1.84993e-06, max=0.0943572, negative_count=0, zero_count=0
- `weights_ensemble_81`: sum=1812.9, min=1.0947e-06, max=0.102521, negative_count=0, zero_count=0
- `weights_ensemble_82`: sum=1808.94, min=9.59397e-07, max=0.112665, negative_count=0, zero_count=0
- `weights_ensemble_83`: sum=1809.73, min=5.61884e-07, max=0.0891757, negative_count=0, zero_count=0
- `weights_ensemble_84`: sum=1807.02, min=2.98803e-07, max=0.0845539, negative_count=0, zero_count=0
- `weights_ensemble_85`: sum=1803.04, min=8.07597e-07, max=0.0883474, negative_count=0, zero_count=0
- `weights_ensemble_86`: sum=1810.09, min=1.07402e-06, max=0.072648, negative_count=0, zero_count=0
- `weights_ensemble_87`: sum=1812.12, min=1.37815e-06, max=0.0804758, negative_count=0, zero_count=0
- `weights_ensemble_88`: sum=1815, min=2.75015e-06, max=0.0913596, negative_count=0, zero_count=0
- `weights_ensemble_89`: sum=1804.53, min=1.78143e-07, max=0.108136, negative_count=0, zero_count=0
- `weights_ensemble_90`: sum=1815.44, min=1.91371e-06, max=0.0708945, negative_count=0, zero_count=0
- `weights_ensemble_91`: sum=1813.3, min=3.28268e-06, max=0.130819, negative_count=0, zero_count=0
- `weights_ensemble_92`: sum=1812.21, min=1.16927e-06, max=0.0842412, negative_count=0, zero_count=0
- `weights_ensemble_93`: sum=1816.07, min=8.23744e-07, max=0.108379, negative_count=0, zero_count=0
- `weights_ensemble_94`: sum=1808.23, min=5.60505e-07, max=0.093424, negative_count=0, zero_count=0
- `weights_ensemble_95`: sum=1810.17, min=7.91314e-07, max=0.0924852, negative_count=0, zero_count=0
- `weights_ensemble_96`: sum=1802.3, min=6.72706e-07, max=0.0835172, negative_count=0, zero_count=0
- `weights_ensemble_97`: sum=1806.37, min=4.87924e-07, max=0.0969676, negative_count=0, zero_count=0
- `weights_ensemble_98`: sum=1816.22, min=8.34611e-07, max=0.107708, negative_count=0, zero_count=0
- `weights_ensemble_99`: sum=1811.81, min=2.05963e-06, max=0.112041, negative_count=0, zero_count=0
- `weights_dd`: sum=1801.68, min=1.32998e-06, max=0.0367877, negative_count=0, zero_count=0
- `weights_bootstrap_mc_0`: sum=1808.82, min=1.88131e-06, max=0.0704367, negative_count=0, zero_count=0
- `weights_bootstrap_mc_1`: sum=1814.57, min=1.71525e-06, max=0.0652743, negative_count=0, zero_count=0
- `weights_bootstrap_mc_2`: sum=1806.29, min=2.36803e-06, max=0.0634153, negative_count=0, zero_count=0
- `weights_bootstrap_mc_3`: sum=1811.21, min=2.00576e-06, max=0.0723945, negative_count=0, zero_count=0
- `weights_bootstrap_mc_4`: sum=1808.95, min=1.96032e-06, max=0.0617152, negative_count=0, zero_count=0
- `weights_bootstrap_mc_5`: sum=1810.61, min=2.01101e-06, max=0.0699548, negative_count=0, zero_count=0
- `weights_bootstrap_mc_6`: sum=1809.4, min=2.02084e-06, max=0.0700009, negative_count=0, zero_count=0
- `weights_bootstrap_mc_7`: sum=1813, min=2.09172e-06, max=0.063439, negative_count=0, zero_count=0
- `weights_bootstrap_mc_8`: sum=1809.02, min=2.32534e-06, max=0.0618252, negative_count=0, zero_count=0
- `weights_bootstrap_mc_9`: sum=1809.84, min=2.25486e-06, max=0.0610052, negative_count=0, zero_count=0
- `weights_bootstrap_mc_10`: sum=1809.37, min=1.90758e-06, max=0.0628565, negative_count=0, zero_count=0
- `weights_bootstrap_mc_11`: sum=1812.42, min=1.98463e-06, max=0.0666502, negative_count=0, zero_count=0
- `weights_bootstrap_mc_12`: sum=1808.97, min=2.25285e-06, max=0.0629873, negative_count=0, zero_count=0
- `weights_bootstrap_mc_13`: sum=1807.06, min=2.53066e-06, max=0.0654444, negative_count=0, zero_count=0
- `weights_bootstrap_mc_14`: sum=1809.12, min=2.39356e-06, max=0.0654304, negative_count=0, zero_count=0
- `weights_bootstrap_mc_15`: sum=1809.76, min=2.70347e-06, max=0.0643246, negative_count=0, zero_count=0
- `weights_bootstrap_mc_16`: sum=1810.4, min=2.19087e-06, max=0.0636447, negative_count=0, zero_count=0
- `weights_bootstrap_mc_17`: sum=1809.87, min=2.17079e-06, max=0.0645477, negative_count=0, zero_count=0
- `weights_bootstrap_mc_18`: sum=1806.5, min=2.02064e-06, max=0.0647135, negative_count=0, zero_count=0
- `weights_bootstrap_mc_19`: sum=1809.92, min=1.8679e-06, max=0.0742094, negative_count=0, zero_count=0
- `weights_bootstrap_mc_20`: sum=1812.88, min=2.14827e-06, max=0.0683098, negative_count=0, zero_count=0
- `weights_bootstrap_mc_21`: sum=1810.94, min=2.01159e-06, max=0.0656689, negative_count=0, zero_count=0
- `weights_bootstrap_mc_22`: sum=1810.67, min=2.00136e-06, max=0.0741745, negative_count=0, zero_count=0
- `weights_bootstrap_mc_23`: sum=1811.18, min=2.01162e-06, max=0.0568138, negative_count=0, zero_count=0
- `weights_bootstrap_mc_24`: sum=1810.53, min=2.17323e-06, max=0.0676933, negative_count=0, zero_count=0
- `weights_bootstrap_data_0`: sum=1807.85, min=1.07698e-06, max=0.0785246, negative_count=0, zero_count=0
- `weights_bootstrap_data_1`: sum=1810.5, min=1.7207e-06, max=0.0779938, negative_count=0, zero_count=0
- `weights_bootstrap_data_2`: sum=1803.82, min=1.15943e-06, max=0.0719024, negative_count=0, zero_count=0
- `weights_bootstrap_data_3`: sum=1808.25, min=9.3261e-07, max=0.0796595, negative_count=0, zero_count=0
- `weights_bootstrap_data_4`: sum=1805.45, min=1.22345e-06, max=0.0809693, negative_count=0, zero_count=0
- `weights_bootstrap_data_5`: sum=1816.49, min=9.08922e-07, max=0.0755069, negative_count=0, zero_count=0
- `weights_bootstrap_data_6`: sum=1811.25, min=7.56114e-07, max=0.0719543, negative_count=0, zero_count=0
- `weights_bootstrap_data_7`: sum=1803.17, min=7.89119e-07, max=0.0761768, negative_count=0, zero_count=0
- `weights_bootstrap_data_8`: sum=1807.96, min=8.61489e-07, max=0.0811456, negative_count=0, zero_count=0
- `weights_bootstrap_data_9`: sum=1810.23, min=9.07409e-07, max=0.0773769, negative_count=0, zero_count=0
- `weights_bootstrap_data_10`: sum=1805.29, min=1.2546e-06, max=0.0883408, negative_count=0, zero_count=0
- `weights_bootstrap_data_11`: sum=1803.33, min=1.93656e-06, max=0.082856, negative_count=0, zero_count=0
- `weights_bootstrap_data_12`: sum=1815.47, min=1.06957e-06, max=0.0720794, negative_count=0, zero_count=0
- `weights_bootstrap_data_13`: sum=1807.12, min=6.62998e-07, max=0.0745832, negative_count=0, zero_count=0
- `weights_bootstrap_data_14`: sum=1814.74, min=7.73141e-07, max=0.0843723, negative_count=0, zero_count=0
- `weights_bootstrap_data_15`: sum=1804.8, min=6.64199e-07, max=0.0947441, negative_count=0, zero_count=0
- `weights_bootstrap_data_16`: sum=1809.64, min=1.37313e-06, max=0.07216, negative_count=0, zero_count=0
- `weights_bootstrap_data_17`: sum=1815.09, min=1.18318e-06, max=0.0759133, negative_count=0, zero_count=0
- `weights_bootstrap_data_18`: sum=1804.8, min=1.30275e-06, max=0.0767787, negative_count=0, zero_count=0
- `weights_bootstrap_data_19`: sum=1809, min=1.89592e-06, max=0.0918712, negative_count=0, zero_count=0
- `weights_bootstrap_data_20`: sum=1812.17, min=8.97112e-07, max=0.0892079, negative_count=0, zero_count=0
- `weights_bootstrap_data_21`: sum=1811, min=6.84239e-07, max=0.078384, negative_count=0, zero_count=0
- `weights_bootstrap_data_22`: sum=1809.34, min=4.57385e-07, max=0.0844064, negative_count=0, zero_count=0
- `weights_bootstrap_data_23`: sum=1806.32, min=5.97259e-07, max=0.066239, negative_count=0, zero_count=0
- `weights_bootstrap_data_24`: sum=1807.52, min=1.0222e-06, max=0.0794663, negative_count=0, zero_count=0
- `weights_pileup`: sum=1807.7, min=2.01805e-06, max=0.0762421, negative_count=0, zero_count=0
- `weights_muEffReco`: sum=1819.52, min=1.84185e-06, max=0.0757683, negative_count=0, zero_count=0
- `weights_muEffIso`: sum=1830.4, min=2.14499e-06, max=0.074159, negative_count=0, zero_count=0
- `weights_muEffTrack`: sum=1814.51, min=1.85073e-06, max=0.0743862, negative_count=0, zero_count=0
- `weights_muEffTrig`: sum=1814.59, min=1.66558e-06, max=0.0746517, negative_count=0, zero_count=0
- `weights_muCalID`: sum=1807.5, min=1.87427e-06, max=0.073024, negative_count=0, zero_count=0
- `weights_muCalMS`: sum=1807.98, min=2.13233e-06, max=0.0772432, negative_count=0, zero_count=0
- `weights_muCalResBias`: sum=1809.79, min=2.06024e-06, max=0.0720633, negative_count=0, zero_count=0
- `weights_muCalScale`: sum=1804.62, min=1.83788e-06, max=0.0722171, negative_count=0, zero_count=0
- `weights_trackEffMain`: sum=1808.69, min=2.95697e-06, max=0.0507663, negative_count=0, zero_count=0
- `weights_trackEffJet`: sum=1809.31, min=1.62523e-06, max=0.0733229, negative_count=0, zero_count=0
- `weights_trackFake`: sum=1809.17, min=2.09518e-06, max=0.0637037, negative_count=0, zero_count=0
- `weights_trackPtScale`: sum=1808.89, min=1.68864e-06, max=0.0709099, negative_count=0, zero_count=0
- `weights_theoryPSjet`: sum=1809.4, min=1.99226e-06, max=0.076782, negative_count=0, zero_count=0
- `weights_theoryPSsoft`: sum=1809.44, min=1.82761e-06, max=0.0810458, negative_count=0, zero_count=0
- `weights_theoryMPI`: sum=1809.29, min=1.87792e-06, max=0.0734673, negative_count=0, zero_count=0
- `weights_theoryPSscale`: sum=1807.92, min=1.81182e-06, max=0.0725069, negative_count=0, zero_count=0
- `weights_theoryAlphaS`: sum=1811.76, min=2.01108e-06, max=0.072478, negative_count=0, zero_count=0
- `weights_theoryQCD`: sum=1809.64, min=-0.197845, max=0.143863, negative_count=1673, zero_count=0
- `weights_theoryPDF`: sum=1809.2, min=1.69644e-06, max=0.074964, negative_count=0, zero_count=0
- `weights_topBackground`: sum=1806.05, min=1.962e-06, max=0.0733941, negative_count=0, zero_count=0
- `weights_lumi`: sum=1840.23, min=1.82495e-06, max=0.0769535, negative_count=0, zero_count=0

### Example observable ranges

- `pT_ll`: min=200, max=3233.95, mean=345.469, std=170.876
- `pT_l1`: min=100.36, max=2384.66, mean=259.105, std=143.249
- `pT_l2`: min=25.0002, max=1252.56, mean=93.7249, std=59.9613
- `eta_l1`: min=-2.39994, max=2.39998, mean=0.00198571, std=1.12312
- `eta_l2`: min=-2.39998, max=2.39995, mean=0.00227618, std=1.13862
- `phi_l1`: min=-3.14159, max=3.14159, mean=0.000248655, std=1.81252
- `phi_l2`: min=-3.14158, max=3.14159, mean=0.00136048, std=1.81148
- `y_ll`: min=-2.39626, max=2.39703, mean=0.00198566, std=1.10618
- `pT_trackj1`: min=0.592701, max=3079.32, mean=209.638, std=166.372
- `y_trackj1`: min=-2.49961, max=2.49766, mean=0.00199169, std=1.07337
- `phi_trackj1`: min=-3.14158, max=3.14158, mean=0.00120984, std=1.81568
- `m_trackj1`: min=-0.12765, max=258.809, mean=17.3114, std=13.4307

## File: `multifold_sherpa.h5`

- Pandas key: `/df`
- Shape: **326430 rows x 51 columns**

### HDF5 structure

- Group: df
- Dataset: df/axis0
- Dataset: df/axis1
- Dataset: df/block0_items
- Dataset: df/block0_values
- Dataset: df/block1_items
- Dataset: df/block1_values
- Dataset: df/block2_items
- Dataset: df/block2_values

### Column classification

- **observable** (24): pT_ll, pT_l1, pT_l2, eta_l1, eta_l2, phi_l1, phi_l2, y_ll, pT_trackj1, y_trackj1, phi_trackj1, m_trackj1, tau1_trackj1, tau2_trackj1, tau3_trackj1, pT_trackj2, y_trackj2, phi_trackj2, m_trackj2, tau1_trackj2, tau2_trackj2, tau3_trackj2, Ntracks_trackj1, Ntracks_trackj2
- **weight** (27): weight_mc, weights_nominal, weights_bootstrap_mc_0, weights_bootstrap_mc_1, weights_bootstrap_mc_2, weights_bootstrap_mc_3, weights_bootstrap_mc_4, weights_bootstrap_mc_5, weights_bootstrap_mc_6, weights_bootstrap_mc_7, weights_bootstrap_mc_8, weights_bootstrap_mc_9, weights_bootstrap_mc_10, weights_bootstrap_mc_11, weights_bootstrap_mc_12, weights_bootstrap_mc_13, weights_bootstrap_mc_14, weights_bootstrap_mc_15, weights_bootstrap_mc_16, weights_bootstrap_mc_17, weights_bootstrap_mc_18, weights_bootstrap_mc_19, weights_bootstrap_mc_20, weights_bootstrap_mc_21, weights_bootstrap_mc_22, weights_bootstrap_mc_23, weights_bootstrap_mc_24
- **metadata** (0): None
- **other** (0): None

### Missing values

- No missing values detected.

### Weight checks

- `weight_mc`: sum=1601.73, min=5.09877e-06, max=0.0217872, negative_count=0, zero_count=0
- `weights_nominal`: sum=1816.17, min=4.9389e-06, max=0.0761792, negative_count=0, zero_count=0
- `weights_bootstrap_mc_0`: sum=48157.4, min=0.00010957, max=1.95878, negative_count=0, zero_count=0
- `weights_bootstrap_mc_1`: sum=48324.9, min=9.90579e-05, max=1.7349, negative_count=0, zero_count=0
- `weights_bootstrap_mc_2`: sum=48308.8, min=9.69567e-05, max=1.79814, negative_count=0, zero_count=0
- `weights_bootstrap_mc_3`: sum=48574.2, min=0.000104941, max=1.7962, negative_count=0, zero_count=0
- `weights_bootstrap_mc_4`: sum=47960.7, min=0.000104377, max=1.87485, negative_count=0, zero_count=0
- `weights_bootstrap_mc_5`: sum=47889.4, min=0.00011141, max=1.92387, negative_count=0, zero_count=0
- `weights_bootstrap_mc_6`: sum=48587.1, min=0.00011009, max=1.77543, negative_count=0, zero_count=0
- `weights_bootstrap_mc_7`: sum=48024.7, min=0.000113197, max=1.90694, negative_count=0, zero_count=0
- `weights_bootstrap_mc_8`: sum=47409.5, min=0.000110684, max=1.74503, negative_count=0, zero_count=0
- `weights_bootstrap_mc_9`: sum=48297.2, min=0.000107987, max=1.88911, negative_count=0, zero_count=0
- `weights_bootstrap_mc_10`: sum=47569.5, min=0.000116491, max=1.71506, negative_count=0, zero_count=0
- `weights_bootstrap_mc_11`: sum=48647.6, min=0.000119001, max=1.92121, negative_count=0, zero_count=0
- `weights_bootstrap_mc_12`: sum=48336.5, min=0.000114925, max=1.79462, negative_count=0, zero_count=0
- `weights_bootstrap_mc_13`: sum=47950.5, min=0.000109259, max=1.83722, negative_count=0, zero_count=0
- `weights_bootstrap_mc_14`: sum=48508.2, min=0.000116631, max=1.83545, negative_count=0, zero_count=0
- `weights_bootstrap_mc_15`: sum=48477.6, min=0.00010251, max=1.85363, negative_count=0, zero_count=0
- `weights_bootstrap_mc_16`: sum=47830.8, min=0.000131323, max=1.77112, negative_count=0, zero_count=0
- `weights_bootstrap_mc_17`: sum=48201.1, min=0.000101734, max=1.87745, negative_count=0, zero_count=0
- `weights_bootstrap_mc_18`: sum=47765.8, min=0.000132814, max=1.87983, negative_count=0, zero_count=0
- `weights_bootstrap_mc_19`: sum=48348.2, min=0.000112731, max=1.99601, negative_count=0, zero_count=0
- `weights_bootstrap_mc_20`: sum=48109.4, min=0.000113013, max=1.81753, negative_count=0, zero_count=0
- `weights_bootstrap_mc_21`: sum=48107.7, min=0.000105687, max=1.85801, negative_count=0, zero_count=0
- `weights_bootstrap_mc_22`: sum=47546.4, min=0.000103782, max=1.96353, negative_count=0, zero_count=0
- `weights_bootstrap_mc_23`: sum=47946.9, min=0.000107727, max=1.85716, negative_count=0, zero_count=0
- `weights_bootstrap_mc_24`: sum=47777.6, min=0.000110445, max=1.85396, negative_count=0, zero_count=0

### Example observable ranges

- `pT_ll`: min=200, max=2865.18, mean=316.651, std=145.095
- `pT_l1`: min=100.985, max=2117.39, mean=236.125, std=120.201
- `pT_l2`: min=25.0005, max=1088.65, mean=88.2646, std=55.0121
- `eta_l1`: min=-2.39989, max=2.39989, mean=0.00293245, std=1.14757
- `eta_l2`: min=-2.39999, max=2.39998, mean=0.00349134, std=1.16149
- `phi_l1`: min=-3.14159, max=3.14159, mean=0.0171954, std=1.8169
- `phi_l2`: min=-3.14159, max=3.14158, mean=0.0201974, std=1.81737
- `y_ll`: min=-2.39823, max=2.39703, mean=0.00316236, std=1.12857
- `pT_trackj1`: min=0.673399, max=2578.85, mean=211.564, std=152.535
- `y_trackj1`: min=-2.49973, max=2.49781, mean=0.00228727, std=1.10712
- `phi_trackj1`: min=-3.14158, max=3.14155, mean=-0.0182387, std=1.81115
- `m_trackj1`: min=-0.0221465, max=272.849, mean=16.0342, std=13.2414

## File: `multifold_nonDY.h5`

- Pandas key: `/df`
- Shape: **433397 rows x 26 columns**

### HDF5 structure

- Group: df
- Dataset: df/axis0
- Dataset: df/axis1
- Dataset: df/block0_items
- Dataset: df/block0_values
- Dataset: df/block1_items
- Dataset: df/block1_values

### Column classification

- **observable** (24): pT_ll, pT_l1, pT_l2, eta_l1, eta_l2, phi_l1, phi_l2, y_ll, pT_trackj1, y_trackj1, phi_trackj1, m_trackj1, tau1_trackj1, tau2_trackj1, tau3_trackj1, pT_trackj2, y_trackj2, phi_trackj2, m_trackj2, tau1_trackj2, tau2_trackj2, tau3_trackj2, Ntracks_trackj1, Ntracks_trackj2
- **weight** (2): weight_mc, weights_nominal
- **metadata** (0): None
- **other** (0): None

### Missing values

- No missing values detected.

### Weight checks

- `weight_mc`: sum=1780.72, min=2.93189e-06, max=0.052995, negative_count=0, zero_count=0
- `weights_nominal`: sum=1810.59, min=1.15961e-06, max=0.0765444, negative_count=0, zero_count=0

### Example observable ranges

- `pT_ll`: min=200, max=3233.95, mean=345.562, std=170.738
- `pT_l1`: min=100.36, max=2384.66, mean=258.997, std=142.945
- `pT_l2`: min=25.0002, max=1252.56, mean=93.9313, std=60.1495
- `eta_l1`: min=-2.39994, max=2.39998, mean=0.00189796, std=1.12092
- `eta_l2`: min=-2.39998, max=2.39995, mean=0.00222623, std=1.13675
- `phi_l1`: min=-3.14159, max=3.14159, mean=0.000375758, std=1.81263
- `phi_l2`: min=-3.14158, max=3.14159, mean=0.00115353, std=1.81178
- `y_ll`: min=-2.39626, max=2.39703, mean=0.00190169, std=1.10406
- `pT_trackj1`: min=0.592701, max=3079.32, mean=210.583, std=167.155
- `y_trackj1`: min=-2.49961, max=2.49766, mean=0.00238848, std=1.07822
- `phi_trackj1`: min=-3.14158, max=3.14158, mean=0.00138205, std=1.81535
- `m_trackj1`: min=-0.394935, max=258.809, mean=17.3044, std=13.5061

## Cross-file comparison

- Common columns across all files (26):

  - `Ntracks_trackj1`
  - `Ntracks_trackj2`
  - `eta_l1`
  - `eta_l2`
  - `m_trackj1`
  - `m_trackj2`
  - `pT_l1`
  - `pT_l2`
  - `pT_ll`
  - `pT_trackj1`
  - `pT_trackj2`
  - `phi_l1`
  - `phi_l2`
  - `phi_trackj1`
  - `phi_trackj2`
  - `tau1_trackj1`
  - `tau1_trackj2`
  - `tau2_trackj1`
  - `tau2_trackj2`
  - `tau3_trackj1`
  - `tau3_trackj2`
  - `weight_mc`
  - `weights_nominal`
  - `y_ll`
  - `y_trackj1`
  - `y_trackj2`

### File-specific columns

- `multifold.h5` (174 unique columns):
  - `target_dd`
  - `weights_bootstrap_data_0`
  - `weights_bootstrap_data_1`
  - `weights_bootstrap_data_10`
  - `weights_bootstrap_data_11`
  - `weights_bootstrap_data_12`
  - `weights_bootstrap_data_13`
  - `weights_bootstrap_data_14`
  - `weights_bootstrap_data_15`
  - `weights_bootstrap_data_16`
  - `weights_bootstrap_data_17`
  - `weights_bootstrap_data_18`
  - `weights_bootstrap_data_19`
  - `weights_bootstrap_data_2`
  - `weights_bootstrap_data_20`
  - `weights_bootstrap_data_21`
  - `weights_bootstrap_data_22`
  - `weights_bootstrap_data_23`
  - `weights_bootstrap_data_24`
  - `weights_bootstrap_data_3`
  - `weights_bootstrap_data_4`
  - `weights_bootstrap_data_5`
  - `weights_bootstrap_data_6`
  - `weights_bootstrap_data_7`
  - `weights_bootstrap_data_8`
  - `weights_bootstrap_data_9`
  - `weights_bootstrap_mc_0`
  - `weights_bootstrap_mc_1`
  - `weights_bootstrap_mc_10`
  - `weights_bootstrap_mc_11`
  - `weights_bootstrap_mc_12`
  - `weights_bootstrap_mc_13`
  - `weights_bootstrap_mc_14`
  - `weights_bootstrap_mc_15`
  - `weights_bootstrap_mc_16`
  - `weights_bootstrap_mc_17`
  - `weights_bootstrap_mc_18`
  - `weights_bootstrap_mc_19`
  - `weights_bootstrap_mc_2`
  - `weights_bootstrap_mc_20`
  - `weights_bootstrap_mc_21`
  - `weights_bootstrap_mc_22`
  - `weights_bootstrap_mc_23`
  - `weights_bootstrap_mc_24`
  - `weights_bootstrap_mc_3`
  - `weights_bootstrap_mc_4`
  - `weights_bootstrap_mc_5`
  - `weights_bootstrap_mc_6`
  - `weights_bootstrap_mc_7`
  - `weights_bootstrap_mc_8`
  - `weights_bootstrap_mc_9`
  - `weights_dd`
  - `weights_ensemble_0`
  - `weights_ensemble_1`
  - `weights_ensemble_10`
  - `weights_ensemble_11`
  - `weights_ensemble_12`
  - `weights_ensemble_13`
  - `weights_ensemble_14`
  - `weights_ensemble_15`
  - `weights_ensemble_16`
  - `weights_ensemble_17`
  - `weights_ensemble_18`
  - `weights_ensemble_19`
  - `weights_ensemble_2`
  - `weights_ensemble_20`
  - `weights_ensemble_21`
  - `weights_ensemble_22`
  - `weights_ensemble_23`
  - `weights_ensemble_24`
  - `weights_ensemble_25`
  - `weights_ensemble_26`
  - `weights_ensemble_27`
  - `weights_ensemble_28`
  - `weights_ensemble_29`
  - `weights_ensemble_3`
  - `weights_ensemble_30`
  - `weights_ensemble_31`
  - `weights_ensemble_32`
  - `weights_ensemble_33`
  - `weights_ensemble_34`
  - `weights_ensemble_35`
  - `weights_ensemble_36`
  - `weights_ensemble_37`
  - `weights_ensemble_38`
  - `weights_ensemble_39`
  - `weights_ensemble_4`
  - `weights_ensemble_40`
  - `weights_ensemble_41`
  - `weights_ensemble_42`
  - `weights_ensemble_43`
  - `weights_ensemble_44`
  - `weights_ensemble_45`
  - `weights_ensemble_46`
  - `weights_ensemble_47`
  - `weights_ensemble_48`
  - `weights_ensemble_49`
  - `weights_ensemble_5`
  - `weights_ensemble_50`
  - `weights_ensemble_51`
  - `weights_ensemble_52`
  - `weights_ensemble_53`
  - `weights_ensemble_54`
  - `weights_ensemble_55`
  - `weights_ensemble_56`
  - `weights_ensemble_57`
  - `weights_ensemble_58`
  - `weights_ensemble_59`
  - `weights_ensemble_6`
  - `weights_ensemble_60`
  - `weights_ensemble_61`
  - `weights_ensemble_62`
  - `weights_ensemble_63`
  - `weights_ensemble_64`
  - `weights_ensemble_65`
  - `weights_ensemble_66`
  - `weights_ensemble_67`
  - `weights_ensemble_68`
  - `weights_ensemble_69`
  - `weights_ensemble_7`
  - `weights_ensemble_70`
  - `weights_ensemble_71`
  - `weights_ensemble_72`
  - `weights_ensemble_73`
  - `weights_ensemble_74`
  - `weights_ensemble_75`
  - `weights_ensemble_76`
  - `weights_ensemble_77`
  - `weights_ensemble_78`
  - `weights_ensemble_79`
  - `weights_ensemble_8`
  - `weights_ensemble_80`
  - `weights_ensemble_81`
  - `weights_ensemble_82`
  - `weights_ensemble_83`
  - `weights_ensemble_84`
  - `weights_ensemble_85`
  - `weights_ensemble_86`
  - `weights_ensemble_87`
  - `weights_ensemble_88`
  - `weights_ensemble_89`
  - `weights_ensemble_9`
  - `weights_ensemble_90`
  - `weights_ensemble_91`
  - `weights_ensemble_92`
  - `weights_ensemble_93`
  - `weights_ensemble_94`
  - `weights_ensemble_95`
  - `weights_ensemble_96`
  - `weights_ensemble_97`
  - `weights_ensemble_98`
  - `weights_ensemble_99`
  - `weights_lumi`
  - `weights_muCalID`
  - `weights_muCalMS`
  - `weights_muCalResBias`
  - `weights_muCalScale`
  - `weights_muEffIso`
  - `weights_muEffReco`
  - `weights_muEffTrack`
  - `weights_muEffTrig`
  - `weights_pileup`
  - `weights_theoryAlphaS`
  - `weights_theoryMPI`
  - `weights_theoryPDF`
  - `weights_theoryPSjet`
  - `weights_theoryPSscale`
  - `weights_theoryPSsoft`
  - `weights_theoryQCD`
  - `weights_topBackground`
  - `weights_trackEffJet`
  - `weights_trackEffMain`
  - `weights_trackFake`
  - `weights_trackPtScale`
- `multifold_sherpa.h5` (25 unique columns):
  - `weights_bootstrap_mc_0`
  - `weights_bootstrap_mc_1`
  - `weights_bootstrap_mc_10`
  - `weights_bootstrap_mc_11`
  - `weights_bootstrap_mc_12`
  - `weights_bootstrap_mc_13`
  - `weights_bootstrap_mc_14`
  - `weights_bootstrap_mc_15`
  - `weights_bootstrap_mc_16`
  - `weights_bootstrap_mc_17`
  - `weights_bootstrap_mc_18`
  - `weights_bootstrap_mc_19`
  - `weights_bootstrap_mc_2`
  - `weights_bootstrap_mc_20`
  - `weights_bootstrap_mc_21`
  - `weights_bootstrap_mc_22`
  - `weights_bootstrap_mc_23`
  - `weights_bootstrap_mc_24`
  - `weights_bootstrap_mc_3`
  - `weights_bootstrap_mc_4`
  - `weights_bootstrap_mc_5`
  - `weights_bootstrap_mc_6`
  - `weights_bootstrap_mc_7`
  - `weights_bootstrap_mc_8`
  - `weights_bootstrap_mc_9`
- `multifold_nonDY.h5` (0 unique columns):
  - None
