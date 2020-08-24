# default directories
import time_module as tm
en_path ='/scratch/local/shzhu/EN_BOND/TEST/global_ensemble_run_v2/'
run_path='/scratch/local/shzhu/EN_BOND/TEST/merra2_2x25_tagCH4/'
temp_path = en_path+ 'temp/'
met_path = '/scratch/local/shzhu/GC_DATA/ctm/GEOS_2x2.5/MERRA2'  #HEMCO_Config.rc
data_path = '/scratch/local/shzhu/GC_DATA/ctm' # input.geos
emis_path ='/exports/csce/datastore/geos/users/s2008420/EMIS/' #path of emission datas 
res_path = en_path+ 'Restart_files/'
config_path = en_path+'Config_files/'
diagn_path = en_path+'Diagn_files'
mask_file = '/exports/csce/datastore/geos/users/s2008420/global_mask_20.nc'

out_path='./enkf_output/' # the model output
#obs_path=run_path+'/oco_obs/'            # observations
#inv_path=run_path+'/oco_inv/'
#def_input_file=run_path+'/input.geos' # GEOS-CHEM model input file
#oco_orbit_path=run_path+'/oco_orbit/' # OCO orbit 
#oco_ak_path=run_path+'/oco_ak/'       # OCO averaging kernel
##c/starting time for geos chem simulation

#st_yyyy, st_mm, st_dd=2008,11,1
#st_yyyy, st_mm, st_dd = 2015,1,1
#st_doy = tm.day_of_year(st_yyyy, st_mm, st_dd)

##c/time resultion in day

temp_res='mon' # it can be fixed or flexible(should modified main code)
inv_lag_window=3
nstep=24
nstep_start=0

cfg_pb_file='./ens_ch4_cfg.2015-2016'

##c/force the system to re-initialize to be a fixed value if True
new_restart= False
fixed_init_val=1.0e-8
restart_file = './GEOSChem.Restart.20160701_0000z.nc4'
rerun_now=True

rerun_date='20130101'
ntracers = 40 
sub_sous = False
n_sous_loop  = 2
sub_tracers = False
n_tracer_loop = 1
#tracer_start = [1,11] #[1, maxtracer+1]
#tracer_end =[11,21] #[1, maxtracer+1]
#tracer_num = [10,10] 
tracer_start = [14]
tracer_end =[21]
tracer_num = [7]

##c selected run
select_runs=list(range(18,21))
#select_sous=

#def_tracerinfo_file=run_path+"/tracerinfo.dat"
#def_diaginfo_file=run_path+"/diaginfo.dat"


# added by rainbow
n_regs = 20
n_sous = 2
sous_name = ['CH4_TAG_AN','CH4_TAG_NA']
## for HEMCO_Config.RC
emis_file_name = ['CH4_EMIS_2015.nc','CH4_EMIS_2015.nc']
emis_var_name = ['CH4_AN' , 'CH4_NA']
emis_time = ['2015-2016/1-12/1/0','2015-2016/1-12/1/0']
emis_unit = 'kg/m2/s'
emis_rank = 'xy'
