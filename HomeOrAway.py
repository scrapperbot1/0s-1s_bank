# -*- coding: latin-1 -*-
import re,httplib2,datetime,requests,traceback
import requests

def freshWoundsForces(mixed_score):
    fails_accumu=0
    fails_accumu_array=[]
    mixed_score_len=len(mixed_score)
    for msrn,msr in enumerate(mixed_score):
        msrn_human=msrn+1
        t_goal_diff=msr[0]-msr[1]
        t_goal_diff_abs=abs(t_goal_diff)
        if t_goal_diff==0:
            t_goal_diff_abs=1
        if t_goal_diff<=0:
            fails_accumu+=t_goal_diff_abs
        if t_goal_diff>0 or msrn_human==mixed_score_len:
            fails_accumu_array+=[fails_accumu]
            fails_accumu=0
    return sum(fails_accumu_array[:2])

def googleSearchResults(url_arg):
    request_headers = {
                      'user-agent': random_ua
                      }
    response = requests.get(url_arg, headers= request_headers)
    response_text=response.text
    return response_text
local_date=datetime.datetime.now()
CURRENT_TIME_HOUR_HUNT=local_date.hour
CURRENT_TIME_MIN_HUNT=local_date.minute
CURRENT_YEAR_RAW=local_date.year
CURRENT_MONTH=local_date.month
CURRENT_DAY=local_date.day
todays_date=[CURRENT_DAY,CURRENT_MONTH,CURRENT_YEAR_RAW]
TODAYS_DATE_STRING=f'{int(CURRENT_DAY)}{int(CURRENT_MONTH)}{int(CURRENT_YEAR_RAW)}'
CURRENT_YEAR=CURRENT_YEAR_RAW
yea_r = str(CURRENT_YEAR_RAW)
USED_MONTH=12
if CURRENT_MONTH>USED_MONTH:
    USED_MONTH=CURRENT_MONTH
MOTNH_LIMIT=USED_MONTH
YEAR_RETRACER=5
CONTEST_URL=''
OLD_ALL_SCORES_DRITY_SEEKER=5
def error_printer(defined_error):
  #print(f'CONTEST_URL: {CONTEST_URL}\n{traceback.format_exc()}')
  #print(defined_error)
  pass
contenthttp_counter=0
def c_abs(nom):
    nom_returned=nom
    if nom_returned<0:
        nom_returned=-1*nom_returned
    return nom_returned
def quickCentCalc(data_array):
    home_data=c_abs(data_array[0])
    away_data=c_abs(data_array[1])
    team_data_max=max([home_data,away_data])
    team_data_max_len=len(str(team_data_max))
    tens_maker=int('1'+'0'*team_data_max_len)
    if data_array[0]<0 or data_array[1]<0:
        home_data=data_array[0]+tens_maker
        away_data=data_array[1]+tens_maker
        team_data_max=max([home_data,away_data])
    if team_data_max<10:
       home_data=home_data+10
       away_data=away_data+10
    data_sum=home_data+away_data
    home_cent_counts=0
    away_cent_counts=0
    try:
        home_cent_counts=round((home_data/data_sum)*100)
    except ZeroDivisionError:
        pass
    try:
        away_cent_counts=round((away_data/data_sum)*100)
    except ZeroDivisionError:
        pass
    return [home_cent_counts,away_cent_counts]
def quickCentCalcUnique(data_array,decimal_place=1):
    home_data=c_abs(data_array[0])
    away_data=c_abs(data_array[1])
    team_data_max=max([home_data,away_data])
    team_data_max_len=len(str(team_data_max))
    tens_maker=int('1'+'0'*team_data_max_len)
    if data_array[0]<0 or data_array[1]<0:
        home_data=data_array[0]+tens_maker
        away_data=data_array[1]+tens_maker
        team_data_max=max([home_data,away_data])
    if team_data_max<10:
       home_data=home_data+10
       away_data=away_data+10
    data_sum=home_data+away_data
    home_cent_counts=0
    away_cent_counts=0
    try:
        home_cent_counts=round((home_data/data_sum)*100,decimal_place)
    except ZeroDivisionError:
        pass
    try:
        away_cent_counts=round((away_data/data_sum)*100,decimal_place)
    except ZeroDivisionError:
        pass
    return [home_cent_counts,away_cent_counts]

def aTeamQualitiesGreaterThanB(qualities_array,MAX_DIFF=20):
    VOUCHING_FOR_HOME=True
    VOUCHING_FOR_AWAY=True
    VOUCHING_FOR_HOME_CENTS_SUM=0
    VOUCHING_FOR_AWAY_CENTS_SUM=0
    MEGA_DIFFS_QUALITIES_HOME_LOGIC=False
    MEGA_DIFFS_QUALITIES_AWAY_LOGIC=False
    for qtis in qualities_array:
        qtis_h=qtis[0]
        VOUCHING_FOR_HOME_CENTS_SUM+=qtis_h
        qtis_a=qtis[1]
        VOUCHING_FOR_AWAY_CENTS_SUM+=qtis_a
        qtis_abs_diff=abs(qtis_h-qtis_a)
        if qtis_h<qtis_a:
            VOUCHING_FOR_HOME=False
        if qtis_a<qtis_h:
            VOUCHING_FOR_AWAY=False
        if qtis_h>=qtis_a:
            pass
        else:
            if qtis_abs_diff>=MAX_DIFF:
                MEGA_DIFFS_QUALITIES_AWAY_LOGIC=True
        if qtis_a>=qtis_h:
            pass
        else:
            if qtis_abs_diff>=MAX_DIFF:
                MEGA_DIFFS_QUALITIES_HOME_LOGIC=True
    MEGA_QUALITIES_CENT=quickCentCalcUnique([VOUCHING_FOR_HOME_CENTS_SUM,VOUCHING_FOR_AWAY_CENTS_SUM])
    if not VOUCHING_FOR_HOME and not VOUCHING_FOR_AWAY:
        if MEGA_DIFFS_QUALITIES_HOME_LOGIC and MEGA_QUALITIES_CENT[0]>MEGA_QUALITIES_CENT[1]:
            VOUCHING_FOR_HOME=True
        if MEGA_DIFFS_QUALITIES_AWAY_LOGIC and MEGA_QUALITIES_CENT[1]>MEGA_QUALITIES_CENT[0]:
            VOUCHING_FOR_AWAY=True
    return [VOUCHING_FOR_HOME,VOUCHING_FOR_AWAY,MEGA_QUALITIES_CENT]

def oldFormDeci(old_form_arr):
    BIGGER_COEFFICIENT=[]
    for ofe in old_form_arr:
        coe_effi_array=[]
        for ofec in ofe:
            ofe_num=".".join(re.findall(r'\d',str(round(ofec))))
            ofe_num_round=round(eval(ofe_num))
            coe_effi_array+=[ofe_num_round]
            BIGGER_COEFFICIENT+=[ofe_num_round]
    return BIGGER_COEFFICIENT
def hiddenLosses(scores_array_all):
    fist_h_scr=scores_array_all[0][0]
    fist_a_scr=scores_array_all[0][1]
    hidden_losses_count=0
    hidden_losses_count_purely=0
    LOSSES_PATTERN_TRIGGERED=False
    if fist_h_scr>=fist_a_scr:
        for hl in scores_array_all[1:]:
            hl_h=hl[0]
            hl_a=hl[1]
            hlsdff=abs(hl_h-hl_a)
            if hl_h<hl_a:
                hidden_losses_count+=(1+hlsdff)
                hidden_losses_count_purely+=1
            else:
                break
    if fist_h_scr==fist_a_scr and hidden_losses_count_purely>=1:
        LOSSES_PATTERN_TRIGGERED=True
    return [hidden_losses_count,LOSSES_PATTERN_TRIGGERED]
def h2hScoresLeveler(h2hScorsArray):
    h2hScorsArray_clean=scoresCleaner(h2hScorsArray)
    home_wins_count=0
    away_wins_count=0
    for hths in h2hScorsArray_clean:
        hths_h=hths[0]
        hths_a=hths[1]
        scabsdff=abs(hths_h-hths_a)
        if scabsdff<=1:
            home_wins_count+=1
            away_wins_count+=1
        if hths_h>hths_a and hths_h>=2:
            home_wins_count+=1
        if hths_a>hths_h and hths_a>=2:
            away_wins_count+=1
    COUNTS_MAX=max([home_wins_count,away_wins_count])
    if COUNTS_MAX==0:
       home_wins_count=1
       away_wins_count=1
    return quickCentCalcUnique([home_wins_count,away_wins_count])
def latestWounds(latest_scores_array):
    home_losses=0
    away_losses=0
    for lscrs in latest_scores_array:
        lscrs_h=lscrs[0]
        lscrs_a=lscrs[1]
        sdiff=abs(lscrs_h-lscrs_a)
        if sdiff==0:
            sdiff=1
        if lscrs_h<=lscrs_a:
            home_losses+=sdiff
        if lscrs_a<=lscrs_h:
            away_losses+=sdiff
    return home_losses
def dynamicForm(h2h_rough,THE_TRIPPLETS_CENT_ARG,striker_wounts_cent,striker_defence_cent,defence_cent):
    h2h_rough_h=h2h_rough[0]
    h2h_rough_a=h2h_rough[1]
    striker_wounts_cent_h=striker_wounts_cent[0]
    striker_wounts_cent_a=striker_wounts_cent[1]
    striker_defence_cent_h=striker_defence_cent[0]
    striker_defence_cent_a=striker_defence_cent[1]
    defence_cent_h=defence_cent[0]
    defence_cent_a=defence_cent[1]
    FINAL_FRM=THE_TRIPPLETS_CENT_ARG
    if striker_wounts_cent_h<striker_wounts_cent_a and striker_defence_cent_h>striker_defence_cent_a:
        if defence_cent_h<40 and defence_cent_a<40:
            FINAL_FRM=quickCentCalc([striker_wounts_cent_h+h2h_rough_h,striker_wounts_cent_a+h2h_rough_a])
    if striker_wounts_cent_a<striker_wounts_cent_h and striker_defence_cent_a>striker_defence_cent_h:
        if defence_cent_a<40 and defence_cent_h<40:
            FINAL_FRM=quickCentCalc([striker_wounts_cent_h+h2h_rough_h,striker_wounts_cent_a+h2h_rough_a])
    return FINAL_FRM
def megaQualitiesCount(megaQualitiesCount_arr):
    home_wins_count_num=0
    home_wins_count_cent=0
    away_wins_count_num=0
    away_wins_count_cent=0
    HOME_COUNTER_QUALITIES=0
    AWAY_COUNTER_QUALITIES=0
    for mqc in megaQualitiesCount_arr:
        mqc_home=mqc[0]
        mqc_away=mqc[1]
        home_wins_count_cent+=mqc_home
        away_wins_count_cent+=mqc_away
        mega_deff=c_abs(mqc_home-mqc_away)
        if mqc_home>=mqc_away:
            home_wins_count_num+=1
        else:
            AWAY_COUNTER_QUALITIES+=mega_deff
        if mqc_away>=mqc_home:
            away_wins_count_num+=1
        else:
            HOME_COUNTER_QUALITIES+=mega_deff
    MEGA_WINS_CENT=quickCentCalcUnique([home_wins_count_cent,away_wins_count_cent])
    MEGA_WINS_CENT_COUNTER=quickCentCalc([HOME_COUNTER_QUALITIES,AWAY_COUNTER_QUALITIES])
    return [home_wins_count_num,away_wins_count_num,MEGA_WINS_CENT,MEGA_WINS_CENT_COUNTER]
def qualitiesCountMagn(q_array,num_lim=1):
    COUNT_PASSED_HOME=True
    COUNT_PASSED_AWAY=True
    for qa in q_array:
        hq=qa[0]
        aq=qa[1]
        if (hq>=aq and aq>num_lim) or hq<=aq:
            COUNT_PASSED_HOME=False
        if (aq>=hq and hq>num_lim) or aq<=hq:
            COUNT_PASSED_AWAY=False
    return [COUNT_PASSED_HOME,COUNT_PASSED_AWAY]
def formLossesIndividually(forms_arr,freshWounds):
    freshWounds_h=freshWounds[0]
    freshWounds_a=freshWounds[1]
    home_leads_count=0
    away_leads_count=0
    home_leads_cent=0
    away_leads_cent=0
    for hum in forms_arr:
        hum_h=hum[0]+freshWounds_h
        hum_a=hum[1]+freshWounds_a
        home_leads_cent+=hum_h
        away_leads_cent+=hum_a
        if hum_h>=hum_a:
            home_leads_count+=1
        if hum_a>=hum_h:
            away_leads_count+=1
    CENTS_LOSSES_FORM=quickCentCalcUnique([home_leads_cent,away_leads_cent])
    return [home_leads_count,away_leads_count,CENTS_LOSSES_FORM]
API_SWITCH=1
def scraperApi(target_url):
    target_url_used=target_url
    payload = { 'api_key': '5a2a8b8222167badcc2576b670f2c43c', 'url':target_url_used}
    response = requests.get('https://api.scraperapi.com/', params=payload)
    content_f=response.text
    content_str_expo=content_f.replace('\n','').lower()
    return content_str_expo
def h2hModalDiffCent(h2h_scores):
    home_diffs_array=[]
    away_diffs_array=[]
    for h2hs in h2h_scores:
        h2hs_home=h2hs[0]
        h2hs_away=h2hs[1]
        h2hs_home_diff=h2hs_home-h2hs_away
        h2hs_away_diff=h2hs_away-h2hs_home
        if h2hs_home_diff>=0:
            home_diffs_array+=[h2hs_home_diff]
        if h2hs_away_diff>=0:
            away_diffs_array+=[h2hs_away_diff]
    if len(home_diffs_array)==0:
        home_diffs_array=[0]
    if len(away_diffs_array)==0:
        away_diffs_array=[0]
    home_diffs_array_mode=modalVal(home_diffs_array)
    away_diffs_array_mode=modalVal(away_diffs_array)
    MODAL_CENT=quickCentCalc([home_diffs_array_mode,away_diffs_array_mode])
    return MODAL_CENT
def pos_wc_counter_cent(pos,wins_count,counter,wounds_force,h2h_rough):
    home_opt=pos[1]+wins_count[0]
    away_opt=pos[0]+wins_count[1]
    tim_quick_cent=quickCentCalc([home_opt,away_opt])
    tim_form_cent=formCent(h2h_rough,tim_quick_cent)
    home_opt=tim_form_cent[0]+wounds_force[0]+counter[0]
    away_opt=tim_form_cent[1]+wounds_force[1]+counter[1]
    final_quick_cent=quickCentCalc([home_opt,away_opt])
    return final_quick_cent
def otherMotivator(tims_pos_arr,tims_wins_count_arr):
    tims_pos_arr_home=tims_pos_arr[0]
    tims_pos_arr_away=tims_pos_arr[1]
    tims_wins_count_arr_home=tims_wins_count_arr[0]
    tims_wins_count_arr_away=tims_wins_count_arr[1]
    pos_cent=quickCentCalc([tims_pos_arr_away,tims_pos_arr_home])
    wins_count_cent=quickCentCalc(tims_wins_count_arr)
    returned_cent=wins_count_cent
    if tims_wins_count_arr_home==tims_wins_count_arr_away:
        returned_cent=pos_cent
    return returned_cent
def firstTwoConsistencyCent(home_consistency,away_consistency):
    home_consistency_count=0
    away_consistency_count=0
    for cshn,cshe in enumerate(home_consistency):
        if cshn<=1:
            home_consistency_count+=cshe
        else:
            break
    for csan,csae in enumerate(away_consistency):
        if csan<=1:
            away_consistency_count+=csae
        else:
            break
    return [home_consistency_count,away_consistency_count]
def lossTruely(h2h_cent_ar,loss_arr):
    h2h_cent_ar_h=h2h_cent_ar[0]
    h2h_cent_ar_a=h2h_cent_ar[1]
    loss_arr_h=loss_arr[0]
    loss_arr_a=loss_arr[1]
    h2h_cent_ar_h_val=0
    h2h_cent_ar_a_val=0
    cents_sum=h2h_cent_ar_h+h2h_cent_ar_a
    try:
        h2h_cent_ar_h_val=round(loss_arr_h*round(h2h_cent_ar_h/cents_sum,2),2)
    except ZeroDivisionError:
        pass
    try:
        h2h_cent_ar_a_val=round(loss_arr_a*round(h2h_cent_ar_a/cents_sum,2),2)
    except ZeroDivisionError:
        pass
    return [h2h_cent_ar_h_val,h2h_cent_ar_a_val]
def overshadowedPlusFormPlusWounds(h2h_cents_arr,final_form,losses,h2h_stats_len_arg):
    home_buried_diff=0
    away_buried_diff=0
    hff=final_form[0]
    aff=final_form[1]
    hlss=losses[0]
    alss=losses[1]
    home_h2h_leads_count=0
    away_h2h_leads_count=0
    for h2hca in h2h_cents_arr:
        h2h_h=h2hca[0]
        h2h_a=h2hca[1]
        ovdf=c_abs(h2h_h-h2h_a)
        if h2h_h>=h2h_a:
            home_buried_diff+=ovdf
            home_h2h_leads_count+=1
        if h2h_a>=h2h_h:
            away_buried_diff+=ovdf
            away_h2h_leads_count+=1
    if hff>aff and away_buried_diff>0 and h2h_stats_len_arg<5:
        aff=aff+away_buried_diff+alss
    if aff>hff and home_buried_diff>0 and h2h_stats_len_arg<5:
        hff=hff+home_buried_diff+hlss
    if home_h2h_leads_count==0:
        home_h2h_leads_count=1
    if away_h2h_leads_count==0:
        away_h2h_leads_count=1
    return [quickCentCalc([hff,aff]),[home_h2h_leads_count,away_h2h_leads_count]]
def arrayEleAbsDiff(arry_ele):
    returned_arr=arry_ele
    if len(arry_ele)>1:
        returned_arr=[]
        for ens,elea in enumerate(arry_ele):
            hens=ens+1
            try:
               next_ele=c_abs(arry_ele[hens]-elea)
               returned_arr+=[next_ele]
            except IndexError:
                pass
    return returned_arr
def chains_losses_func(scores_arr):
    len_scores_arr=len(scores_arr)
    if len_scores_arr==0:
        scores_arr=[(-1,-1)]
    CHAINES_BLEEDING_COUNT=0
    loses_chains_check_count=0
    sdff_child=scores_arr[0][0]-scores_arr[0][1]
    df2=0
    for ts0 in scores_arr:
        hts0=ts0[0]
        ats0=ts0[1]
        df2=c_abs(hts0-ats0)
        if hts0<=ats0 and hts0>-1:
           loses_chains_check_count+=(df2+1)
           if hts0<ats0:
              CHAINES_BLEEDING_COUNT+=1
        else:
            break
    if loses_chains_check_count==1 and sdff_child==-1:
        loses_chains_check_count=0
    if loses_chains_check_count==1 and sdff_child<=-2 and scores_arr_u[0][0]>-1:
        loses_chains_check_count=loses_chains_check_count-1
    return [loses_chains_check_count,CHAINES_BLEEDING_COUNT]
def consistencyChecker(TeamScoress_omtc,h2h_scores):
    consistency_count_arr=[]
    CHAINES_BLEEDING_H2H=0
    CHAINES_BLEEDING_OTM=0
    consis_count=0
    consi_num_arr=[]
    scors_acc=0
    first_addr=0
    def quickScrAddr(hsc_arg,asc_arg):
        if hsc_arg==asc_arg:
           addr=1
        elif hsc_arg>asc_arg:
           addr=1
        else:
          addr=1
        return addr
    chains_losses_func_OMT_HUB=chains_losses_func(TeamScoress_omtc)
    loses_chains_check_count_other_m=chains_losses_func_OMT_HUB[0]
    CHAINES_BLEEDING_OTM=chains_losses_func_OMT_HUB[1]
    loses_chains_check_count_h2h_OMT_HUB=chains_losses_func(h2h_scores)
    loses_chains_check_count_h2h=loses_chains_check_count_h2h_OMT_HUB[0]
    CHAINES_BLEEDING_H2H=loses_chains_check_count_h2h_OMT_HUB[1]
    loses_chains_check_count_total=loses_chains_check_count_other_m+loses_chains_check_count_h2h
    for tsn,ts in enumerate(TeamScoress_omtc):
        hts=ts[0]
        ats=ts[1]
        sdiff=c_abs(hts-ats)
        if hts>=ats or sdiff==1:
            consi_num_arr+=[(tsn+1,ts)]
    for csn, cse in enumerate(consi_num_arr):
        con_num=cse[0]
        con_nxt_num=len(consi_num_arr)
        try:
            con_nxt_num=consi_num_arr[csn+1][0]
        except IndexError:
            pass
        con_scores=cse[1]
        hsc=con_scores[0]
        asc=con_scores[1]
        df=con_nxt_num-con_num
        if df==1:
          addr_l=quickScrAddr(hsc,asc)
          consis_count+=1
          scors_acc+=addr_l
        else:
           if consis_count>0:
              first_addr=quickScrAddr(hsc,asc)
              consistency_count_arr+=[scors_acc+first_addr]
           consis_count=0
           scors_acc=0
    CB_H2H='0-H2H-NO'
    CH_OMT='0-OMT-NO'
    if CHAINES_BLEEDING_H2H>1:
        CB_H2H=f'{CHAINES_BLEEDING_H2H}-H2H-YES'
    if CHAINES_BLEEDING_OTM>1:
        CH_OMT=f'{CHAINES_BLEEDING_OTM}-OMT-YES'
    return [consistency_count_arr,loses_chains_check_count_total,[CB_H2H,CH_OMT]]
def lastScoresLostTrigger(h2h_lscr,otherMLscr):
    home_scores_diff_sum=0
    away_scores_diff_sum=0
    homeh2h=h2h_lscr[0]
    awayh2h=h2h_lscr[1]
    homeOthM=otherMLscr[0]
    awayOthM=otherMLscr[1]
    if homeh2h<awayh2h:
        home_scores_diff_sum+=(c_abs(homeh2h-awayh2h))
    if awayh2h<homeh2h:
        away_scores_diff_sum+=(c_abs(awayh2h-homeh2h))
    if homeOthM<awayOthM:
        home_scores_diff_sum+=(c_abs(homeOthM-awayOthM))
    if awayOthM<homeOthM:
        away_scores_diff_sum+=(c_abs(awayOthM-homeOthM))
    return home_scores_diff_sum
def dec_form(elemtn):
  elemtn_str=str(elemtn)
  elemtn_str_len=len(elemtn_str)-1
  elemtn_str=re.findall(r'\d',elemtn_str)
  elemtn_str.insert(elemtn_str_len,'.')
  elemtn_str=eval(''.join(elemtn_str))
  return elemtn_str
def formCent(team_forms,team_element):
    _1=team_forms[0]
    _2=team_forms[1]
    _3=team_element[0]
    _4=team_element[1]
    if _3==0:
        _3=1
    if _4==0:
        _4=1
    team_forms_sum=sum(team_forms)
    _5=0
    _6=0
    try:
        _5=round((_1/team_forms_sum)*_3)
    except ZeroDivisionError:
        pass
    try:
        _6=round((_2/team_forms_sum)*_4)
    except ZeroDivisionError:
        pass
    _7=quickCentCalcUnique([_5,_6])
    return _7
def h2h_lastXLostPoints(h2h_sarr):
    hlsc=0
    alsc=0
    for hs in h2h_sarr:
        hls=hs[0]
        als=hs[1]
        h2h_abs=c_abs(hls-als)
        if hls>als:
            alsc+=h2h_abs
        if als>hls:
            hlsc+=h2h_abs
    return [hlsc,alsc]
def qualitiesCount(home_qualities_array,away_qualities_array):
    hacnt=0
    awyacnt=0
    hc_nt=0
    ac_nt=0
    for qlts_num, qlts_h in enumerate(home_qualities_array):
        qlts_a=away_qualities_array[qlts_num]
        hc_nt+=qlts_h
        ac_nt+=qlts_a
        if qlts_h>=qlts_a:
            hacnt+=1
        if qlts_a>=qlts_h:
            awyacnt+=1
    return [hacnt,awyacnt,quickCentCalc([hc_nt,ac_nt])]
def teamsStructuralLogic(STRUCTURAL_ARRAY,TEAM_STRUCTURE_ARRAY_ARG):
    HOME_STRC=STRUCTURAL_ARRAY[0]
    HOME_STRC_SUM=TEAM_STRUCTURE_ARRAY_ARG[0]
    HOME_STRC_LEN=len(HOME_STRC)
    AWAY_STRC=STRUCTURAL_ARRAY[1]
    AWAY_STRC_SUM=TEAM_STRUCTURE_ARRAY_ARG[1]
    HOME_LEADS_OR_DRAWS_ALL=False
    AWAY_LEADS_OR_DRAWS_ALL=False
    HLODACNT=0
    ALODACNT=0
    for strn,hstre in enumerate(HOME_STRC):
        astre=AWAY_STRC[strn]
        if hstre>=astre:
            HLODACNT+=1
        if astre>=hstre:
            ALODACNT+=1
    EXTRA_HOME_FORCE=HOME_STRC[3]<=50 and HOME_STRC[2]>=AWAY_STRC[2]
    EXTRA_AWAY_FORCE=AWAY_STRC[3]<=50 and AWAY_STRC[2]>=HOME_STRC[2]
    if HLODACNT==HOME_STRC_LEN and (HOME_STRC[3]>=45 or HOME_STRC[1]>=50) and HOME_STRC_SUM>AWAY_STRC_SUM:
        HOME_LEADS_OR_DRAWS_ALL=True
    if ALODACNT==HOME_STRC_LEN and (AWAY_STRC[3]>=45 or AWAY_STRC[1]>=50) and HOME_STRC_SUM<AWAY_STRC_SUM:
        AWAY_LEADS_OR_DRAWS_ALL=True
    if HOME_STRC[1]>=AWAY_STRC[1] and HOME_STRC[3]>=45 and HOME_STRC[2]>0 and HOME_STRC_SUM>AWAY_STRC_SUM:
        HOME_LEADS_OR_DRAWS_ALL=True
    if AWAY_STRC[1]>=HOME_STRC[1] and AWAY_STRC[3]>=45 and AWAY_STRC[2]>0 and HOME_STRC_SUM<AWAY_STRC_SUM:
        AWAY_LEADS_OR_DRAWS_ALL=True
    if HOME_STRC[3]<=50 and not EXTRA_HOME_FORCE:
         HOME_LEADS_OR_DRAWS_ALL=False
    if AWAY_STRC[3]<=50 and not EXTRA_AWAY_FORCE:
         AWAY_LEADS_OR_DRAWS_ALL=False
    return [HOME_LEADS_OR_DRAWS_ALL,AWAY_LEADS_OR_DRAWS_ALL]
def pointsLostInLastThreeGames(last_three_games_scores_array):
    home_points_lost_total=0
    count_down=3
    draws_in_chains=0
    loses_in_chains=0
    for ltgs in last_three_games_scores_array:
        h_ltgs=ltgs[0]
        a_ltgs=ltgs[1]
        goals_diff=c_abs(h_ltgs-a_ltgs)
        if h_ltgs==a_ltgs:
            home_points_lost_total+=(goals_diff+2+count_down)
            draws_in_chains+=2
            if draws_in_chains>2 and count_down==2:
                home_points_lost_total+=draws_in_chains
        else:
            draws_in_chains=0
        if h_ltgs<a_ltgs:
            home_points_lost_total+=(goals_diff+3+count_down)
            loses_in_chains+=3
            if loses_in_chains>3 and count_down==2:
                home_points_lost_total+=loses_in_chains
        else:
            loses_in_chains=0
        count_down-=1
    return home_points_lost_total
def h2hWinsCountCent(h2h_category_array):
    home_wins_cnt=0
    away_wins_cnt=0
    for h2hc in h2h_category_array:
        for dh2hc in h2hc:
            hscrs=dh2hc[0]
            ascrs=dh2hc[1]
            if hscrs>=ascrs:
                home_wins_cnt+=1
            if ascrs>=hscrs:
                away_wins_cnt+=1
    qui_calc=quickCentCalc([home_wins_cnt,away_wins_cnt])
    return qui_calc
def teamsPosMarginDeterminer(TotalTeams,TeamsPosArr):
    HTP=TeamsPosArr[0]
    ATM=TeamsPosArr[1]
    def quickRange(tPos):
        TeamPosMargin=[]
        tcount=0
        tcount_r=0
        for tn in range(1,TotalTeams+1):
            tcount+=1
            if tn==tPos:
                TeamPosMargin+=[tcount]
                break
        for tnr in reversed(range(1,TotalTeams+1)):
            tcount_r+=1
            if tnr==tPos:
                TeamPosMargin+=[tcount_r]
                break
        _5_PLUS=False
        try:
            _5_PLUS=min(TeamPosMargin)>=5
        except ValueError:
            pass
        return _5_PLUS
    HomeOperation=quickRange(HTP)
    AwayOperation=quickRange(ATM)
    return HomeOperation and AwayOperation
def contenthttp(c_url):
    global contenthttp_counter
    try:
        responsey, contentsey=httplib2.Http().request(c_url)
        contentsey=contentsey.decode("utf-8", 'ignore').replace('\n','').lower()
        #print(contentsey)
        return contentsey
    except Exception:
          #pass
          if contenthttp_counter<=1:
             contenthttp_counter+=1
             contenthttp(c_url)
google_recursion_count=0
def teamDrivePurposeBasedOnPointsAndPos(ALL_TEAMS_POINT_ARG_ARR,TEAM_POINTS,TEAMS_POS):
    home_team_pos=TEAMS_POS[0]
    away_team_pos=TEAMS_POS[1]
    home_team_point=TEAM_POINTS[0]
    away_team_point=TEAM_POINTS[1]
    def pointsCutUpAndDown(pos_point_array):
        actual_pos=pos_point_array[0]
        point=pos_point_array[1]
        point_plus_3=point+3
        teams_passed_count_forward=0
        teams_below_count=0
        sliced_point_array_top=list(reversed(ALL_TEAMS_POINT_ARG_ARR[:actual_pos-1]))
        sliced_point_array_bottom=ALL_TEAMS_POINT_ARG_ARR[actual_pos:]
        for pts in sliced_point_array_top:
            if point_plus_3>pts:
               teams_passed_count_forward+=1
            else:
                break
        for ptsbd in sliced_point_array_bottom:
            ptsbd_plus_3=ptsbd+3
            if ptsbd_plus_3>point:
               teams_below_count+=1
            else:
                break
        return [teams_passed_count_forward,teams_below_count]
    HOME_ENGINE_N=pointsCutUpAndDown([home_team_pos,home_team_point])
    AWAY_ENGINE_N=pointsCutUpAndDown([away_team_pos,away_team_point])
    return [HOME_ENGINE_N,AWAY_ENGINE_N]
def teamPlus1DrawsCent(ALL_HOME_SCORES,ALL_AWAY_SCORES):
    def scoresHanhler(scrs_arr):
        defense_count=0
        D_CENT=0
        for sar in scrs_arr:
            hsar=sar[0]
            asar=sar[1]
            if hsar==asar and hsar>0:
               defense_count+=1
        try:
            D_CENT=round((defense_count/len(scrs_arr))*100)
        except ZeroDivisionError:
            pass
        return D_CENT
    return [scoresHanhler(ALL_HOME_SCORES),scoresHanhler(ALL_AWAY_SCORES)]
def miniFormCalc(chunk_forms_array):
    home_wins_counts=0
    away_wins_counts=0
    for box in chunk_forms_array:
        hcent=box[0]
        acent=box[1]
        home_wins_counts+=hcent
        away_wins_counts+=acent
    QUICK_CENT1=quickCentCalc([home_wins_counts,away_wins_counts])
    home_wins_counts=QUICK_CENT1[0]
    away_wins_counts=QUICK_CENT1[1]
    return [home_wins_counts,away_wins_counts]
def deci_creater(num_cent_arr):
    coefficient_array=[]
    for nc in num_cent_arr:
        num_cent_str=str(nc)
        num_cent_str_split=re.findall(r'\d',num_cent_str)
        num_cent_str_split_len=len(num_cent_str_split)
        if num_cent_str_split_len==1:
           num_cent_str='1'
        eval_num=eval(num_cent_str)
        if num_cent_str_split_len>1:
           eval_num=round(eval(f'{num_cent_str_split[0]}.{num_cent_str_split[1]}'))
        if eval_num==0:
           eval_num=1
        coefficient_array+=[eval_num]
    return coefficient_array
def centsWellArranger(cent_arranged,monthlyCentFused=[]):
    WELL_ARRANGED_ARRAY=[]
    prev_cent=cent_arranged[0]
    home_cent_prev=prev_cent[0]
    away_cent_prev=prev_cent[1]
    count=0
    for arr in cent_arranged:
        home_cent=arr[0]
        away_cent=arr[1]
        WELL_ARRANGED_ARRAY+=[arr]
        WELL_ARRANGED_ARRAY_LEN=len(WELL_ARRANGED_ARRAY)-1
        count+=1
        if home_cent_prev==home_cent and away_cent_prev==away_cent and count>1:
            WELL_ARRANGED_ARRAY=WELL_ARRANGED_ARRAY[:WELL_ARRANGED_ARRAY_LEN]
        if home_cent==0 and away_cent==0:
           WELL_ARRANGED_ARRAY=WELL_ARRANGED_ARRAY[:WELL_ARRANGED_ARRAY_LEN]
        home_cent_prev=arr[0]
        away_cent_prev=arr[1]
    small_box=[]
    for mn,me in enumerate(monthlyCentFused):
        mnh=mn+1
        small_box+=[me]
        if mnh>1 and mnh%2==0:
           WELL_ARRANGED_ARRAY+=[small_box]
           small_box=[]
    return WELL_ARRANGED_ARRAY
def tripplePredict(HOME_WINS_DRAWS_CENT_LOCAL0,
                   AWAY_WINS_DRAWS_CENT_LOCAL0,
                   home_resilience_level,
                   away_resilience_level,
                   home_striking_power,
                   away_striking_power,
                   home_structure,
                   away_structure):
    TEAMS_WINS_DRAWS_CENT_MIN=min([HOME_WINS_DRAWS_CENT_LOCAL0,AWAY_WINS_DRAWS_CENT_LOCAL0])
    TEAMS_WINS_DRAWS_CENT_DIFF=c_abs(HOME_WINS_DRAWS_CENT_LOCAL0-AWAY_WINS_DRAWS_CENT_LOCAL0)
    TEAM_STRIKING_POWER_DIFF=c_abs(home_striking_power-away_striking_power)
    structure_dff=c_abs(home_structure-away_structure)
    TEAM_STRIKING_POWER_MIN=min([home_striking_power,away_striking_power])
    GG_POSSIBLE=TEAMS_WINS_DRAWS_CENT_MIN>=55 and TEAM_STRIKING_POWER_MIN>=55 and structure_dff<=14
    HOME_WINS_POSIBLE=home_striking_power>=away_striking_power and home_structure>=away_structure
    if HOME_WINS_POSIBLE and home_striking_power>=away_striking_power and TEAMS_WINS_DRAWS_CENT_DIFF>=16 and TEAM_STRIKING_POWER_DIFF<=10 and HOME_WINS_DRAWS_CENT_LOCAL0<AWAY_WINS_DRAWS_CENT_LOCAL0:
       HOME_WINS_POSIBLE=False
    AWAY_WINS_POSIBLE=away_striking_power>=home_striking_power and away_structure>=home_structure
    if AWAY_WINS_POSIBLE and away_striking_power>=home_striking_power and TEAMS_WINS_DRAWS_CENT_DIFF>=16 and TEAM_STRIKING_POWER_DIFF<=10 and HOME_WINS_DRAWS_CENT_LOCAL0>AWAY_WINS_DRAWS_CENT_LOCAL0:
       AWAY_WINS_POSIBLE=False
    UNDER_3P5=True
    return [GG_POSSIBLE,HOME_WINS_POSIBLE,AWAY_WINS_POSIBLE,UNDER_3P5]
def teamsQualitiesMax(rough_h2h_cents,strikers_cents,defenders_cents):
    h_h2h=rough_h2h_cents[0]
    a_h2h=rough_h2h_cents[1]
    if h_h2h<53:
       h_h2h=0
    if a_h2h<53:
       a_h2h=0
    HOME_GRAND_Max=max([h_h2h,strikers_cents[0],defenders_cents[0]])
    AWAY_GRAND_Max=max([a_h2h,strikers_cents[1],defenders_cents[1]])
    home_max_type=f'{h_h2h}h'
    away_max_type=f'{a_h2h}h'
    if HOME_GRAND_Max==strikers_cents[0]:
        home_max_type=f'{HOME_GRAND_Max}s'
    if HOME_GRAND_Max==defenders_cents[0]:
        home_max_type=f'{HOME_GRAND_Max}d'
    if AWAY_GRAND_Max==strikers_cents[1]:
        away_max_type=f'{AWAY_GRAND_Max}s'
    if AWAY_GRAND_Max==defenders_cents[1]:
        away_max_type=f'{AWAY_GRAND_Max}d'
    return [HOME_GRAND_Max,AWAY_GRAND_Max,[home_max_type,away_max_type]]
def h2hModalScoresSum(h2h_scores_tuple):
    over3_count=0
    for scrsh in h2h_scores_tuple:
        scrsh_sum=sum(scrsh)
        if scrsh_sum>=3:
            over3_count+=1
    return over3_count
def handicapFact(teamsMegaSumsArray):
    teamsMegaSumsArray_H=teamsMegaSumsArray[0]
    teamsMegaSumsArray_A=teamsMegaSumsArray[1]
    HOME_QOUTEINT=0
    AWAY_QOUTEINT=0
    try:
        HOME_QOUTEINT=round(0.1+(teamsMegaSumsArray_H/teamsMegaSumsArray_A))
    except ZeroDivisionError:
        pass
    try:
        AWAY_QOUTEINT=round(0.1+(teamsMegaSumsArray_A/teamsMegaSumsArray_H))
    except ZeroDivisionError:
        pass
    return [HOME_QOUTEINT,AWAY_QOUTEINT]
def multiMarketPredictor(HOME_TEAM,
                         AWAY_TEAM,
                         H2H_SCORES_SUM_MODE_ARG,
                         FORM_CENT_QUICK_ARG,
                         final_form_diff,
                         HOME_AWAY_LOST_POINTS_CENT_ARG,
                         RECENT_LOSES_ARRAY,
                         currentLosesCent_diff,
                         H2H_ROUGH_MIXED_ARG,
                         STRIKERS_POWER,
                         TEAM_DEFEN,
                         INCRE_DECRE_ARG,
                         C_DRIVEN_FORCE_ARG,
                         QUALITIES_COUNT_ARG,
                         FINAL_PLUS_C_DRIVEN,
                         CDF_DIV_ARG,
                         CDF_LAST_GAMES_DIV_ARG,
                         HOME_AWAY_STRUCTURE,
                         TEAMS_LAST_SCORES_WOUNDS,
                         CENTS_ARRAY_ARG,
                         STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG,
                         HOME_ONLY_AWAY_ONLY_CENT_ARRAY,
                         UNI_COEFFICIENT_ARG,
                         TEAM_WINS_ALL_H2H_LOGIC,
                         OTHER_SITES_PREDICTION_ARG,
                         H2H_LAST_SCORE_CENT_BOX,
                         POSITION_BOX,
                         POSITION_TOP_DOWN_BOX,
                         WINS_DRAWS_CENT_ARG,
                         H2H_NO_DISCRE_ARRAY,
                         H2H_FINAL_FORM_ARG,
                         H2H_DISCRET_FORM_LOCAL_ARG,
                         CDF_DIV_ABS_DFF_ARG,
                         LOST_POINTS_TOTAL_PLUS_OMTC_FORM_CENT_ARG,
                         OLD_AND_NEW_LOST_POINTS_SUM_ARG,
                         LAST_LOST_POINTS_CENT_ARG,
                         ALL_TIMES_H2H_ARG_CENT2,
                         LAST_SCORES_ONLY_T_DIFF,
                         LAST_WOUNDS_SQUAD_ARG,
                         LEAGUE_STAGE_FINALS_ARG,
                         ATT_WND_HUB_ARG,
                         FINAL_FORM_AND_ATTACKS_PLUS_SOT_ARG,
                         ATT_AND_SOT_ARG,
                         OVER_SHADOWED_CENTS_ARG,
                         FINAL_FORM_AND_OS_CENTS_ARG,
                         OVER_SHADOWED_CENTS_COUNTER_ARG,
                         TEAMS_1st2_CONSISTENCY_CENT_ARG,
                         ROUGH_FINAL_TEAMS_FORM_ARG,
                         POINTS_LEFT_HUNGER_ARG,
                         POS_COUNTER_WOUNDS_CENT_ARG,
                         ROUGH_FF_POS_CENT_ARG,
                         STRIKE_DEFENCE_CENT_ARG,
                         CONCRETE_FORM_ARG,
                         QUICK_QUALITIES_ARG,
                         QUICK_QUALITIES2_ARG,
                         TEAMS_GRAND_MAX_HUB_ARG,
                         FORM_WOUND_AND_TRANS_ARG,
                         MIN_SUB_VERY_OLD_OR_NO_H2H_ARG,
                         TEAMS_VETERAN_STATUS_ARG,
                         EXPERIMENTAL_FINAL_FORM_ARG,
                         TEAMS_AVERAGE_LOGIC_BOX_ARG,
                         TEAMS_TRIO_DIFF_MIN_VAL_ARG,
                         TITANIC_FORM_ARG,
                         H2H_SAME_MTCHS_CENTS_RAW_ARG,
                         TEAM_TRANSITION_SUM_ARG,
                         DANGEROUS_TEAM_LOGIC_ARG,
                         STRIKERS_AND_WOUNDS_CENT_ARG,
                         VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG,
                         DYNAMIC_WOUNDS_ARRAY_ARG,
                         CONSISTENCY_HUB_ARG,
                         THE_THREE_QUALITIES_ARG,
                         FINAL_PROTOTYPE_FORM_HUB,
                         TEAM_GREEN_LIGHT_CENT_ARG,
                         TEAMS_FAILS_PATTERN_FORCE_ARG,
                         MEGA_QUALITIES_SERIES_CENT_ARG,
                         TEAM_QUALITIES_COUNT_VERY_STRONG_ARG,
                         PRO_TEAM_STATUS_ARG):
    PREDICTION_MADE=False
    PRO_TEAM_STATUS_ARG_H=PRO_TEAM_STATUS_ARG[0]
    PRO_TEAM_STATUS_ARG_A=PRO_TEAM_STATUS_ARG[1]
    TEAM_QUALITIES_COUNT_VERY_STRONG_ARG_H=TEAM_QUALITIES_COUNT_VERY_STRONG_ARG[0]
    TEAM_QUALITIES_COUNT_VERY_STRONG_ARG_A=TEAM_QUALITIES_COUNT_VERY_STRONG_ARG[1]
    MEGA_QUALITIES_SERIES_CENT_ARG_H=MEGA_QUALITIES_SERIES_CENT_ARG[0]
    MEGA_QUALITIES_SERIES_CENT_ARG_A=MEGA_QUALITIES_SERIES_CENT_ARG[1]
    TEAM_GREEN_LIGHT_CENT_ARG_H=TEAM_GREEN_LIGHT_CENT_ARG[0]
    TEAM_GREEN_LIGHT_CENT_ARG_A=TEAM_GREEN_LIGHT_CENT_ARG[1]
    TEAMS_FAILS_PATTERN_FORCE_ARG_H=TEAMS_FAILS_PATTERN_FORCE_ARG[0]
    TEAMS_FAILS_PATTERN_FORCE_ARG_A=TEAMS_FAILS_PATTERN_FORCE_ARG[1]
    TEAM_GREEN_LIGHT_CENT_ARG_ABS_DIFF=abs(TEAM_GREEN_LIGHT_CENT_ARG[0]-TEAM_GREEN_LIGHT_CENT_ARG[1])
    CUSTOM_POSITION_H=FINAL_PROTOTYPE_FORM_HUB[0][0]
    CUSTOM_POSITION_A=FINAL_PROTOTYPE_FORM_HUB[0][1]
    FINAL_PROTOTYPE_FORM_COUNT_H=FINAL_PROTOTYPE_FORM_HUB[1][0]
    FINAL_PROTOTYPE_FORM_COUNT_A=FINAL_PROTOTYPE_FORM_HUB[1][1]
    FINAL_PROTOTYPE_FORM_H=FINAL_PROTOTYPE_FORM_HUB[1][2][0]
    FINAL_PROTOTYPE_FORM_A=FINAL_PROTOTYPE_FORM_HUB[1][2][1]
    FINAL_PROTOTYPE_FORM_ABS_DIFF=abs(FINAL_PROTOTYPE_FORM_H-FINAL_PROTOTYPE_FORM_A)
    VARIABLE_QUALITIES_DIFF_LOCAL=THE_THREE_QUALITIES_ARG[0]
    VARIABLES_CHANGE_LOGIC_HOME_LOCAL=THE_THREE_QUALITIES_ARG[1]
    VARIABLES_CHANGE_LOGIC_AWAY_LOCAL=THE_THREE_QUALITIES_ARG[2]
    HOME_CONSISTENCY_LOCAL=CONSISTENCY_HUB_ARG[0]+[0]
    HOME_CONSISTENCY_LOCAL_FIRST_1s2Max=max(HOME_CONSISTENCY_LOCAL[:2])
    AWAY_CONSISTENCY_LOCAL=CONSISTENCY_HUB_ARG[1]+[0]
    AWAY_CONSISTENCY_LOCAL_FIRST_1s2Max=max(AWAY_CONSISTENCY_LOCAL[:2])
    DYNAMIC_WOUNDS_ARRAY_ARG_H=DYNAMIC_WOUNDS_ARRAY_ARG[0]
    DYNAMIC_WOUNDS_ARRAY_ARG_A=DYNAMIC_WOUNDS_ARRAY_ARG[1]
    DYNAMIC_WOUNDS_ARRAY_ARG_ABS_DIFF=abs(DYNAMIC_WOUNDS_ARRAY_ARG_H-DYNAMIC_WOUNDS_ARRAY_ARG_A)
    VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_H=VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG[0]
    VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_A=VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG[1]
    VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_abs=abs(VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_H-VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_A)
    STRIKERS_AND_WOUNDS_CENT_ARG_H=STRIKERS_AND_WOUNDS_CENT_ARG[0]
    STRIKERS_AND_WOUNDS_CENT_ARG_A=STRIKERS_AND_WOUNDS_CENT_ARG[1]
    DANGEROUS_TEAM_LOGIC_ARG_H=DANGEROUS_TEAM_LOGIC_ARG[0]
    DANGEROUS_TEAM_LOGIC_ARG_A=DANGEROUS_TEAM_LOGIC_ARG[1]
    TEAM_TRANSITION_SUM_ARG_H=TEAM_TRANSITION_SUM_ARG[0]
    TEAM_TRANSITION_SUM_ARG_A=TEAM_TRANSITION_SUM_ARG[1]
    TRANS_ABS_DIFF=abs(TEAM_TRANSITION_SUM_ARG_H-TEAM_TRANSITION_SUM_ARG_A)
    HOME_TRANS_LOGIC=TEAM_TRANSITION_SUM_ARG_H>=TEAM_TRANSITION_SUM_ARG_A or TRANS_ABS_DIFF<=7
    AWAY_TRANS_LOGIC=TEAM_TRANSITION_SUM_ARG_A>=TEAM_TRANSITION_SUM_ARG_H or TRANS_ABS_DIFF<=7
    H2H_SAME_MTCHS_CENTS_RAW_ARG_H=H2H_SAME_MTCHS_CENTS_RAW_ARG[0]
    H2H_SAME_MTCHS_CENTS_RAW_ARG_A=H2H_SAME_MTCHS_CENTS_RAW_ARG[1]
    TITANIC_FORM_ARG_COUNT_H=TITANIC_FORM_ARG[0]
    TITANIC_FORM_ARG_COUNT_A=TITANIC_FORM_ARG[1]
    HOME_TRIO_DIFF_MIN_VAL_LOCAL=TEAMS_TRIO_DIFF_MIN_VAL_ARG[0]
    AWAY_TRIO_DIFF_MIN_VAL_LOCAL=TEAMS_TRIO_DIFF_MIN_VAL_ARG[1]
    TEAM_AVERAGE_H_LOCAL=TEAMS_AVERAGE_LOGIC_BOX_ARG[0]
    TEAM_AVERAGE_A_LOCAL=TEAMS_AVERAGE_LOGIC_BOX_ARG[1]
    EXPERIMENTAL_FINAL_FORM_ARG_H=EXPERIMENTAL_FINAL_FORM_ARG[0]
    EXPERIMENTAL_FINAL_FORM_ARG_A=EXPERIMENTAL_FINAL_FORM_ARG[1]
    EXPERIMENTAL_FINAL_FORM_ARG_ABS_DIFF=abs(EXPERIMENTAL_FINAL_FORM_ARG_H-EXPERIMENTAL_FINAL_FORM_ARG_A)
    TEAMS_VETERAN_STATUS_ARG_H=TEAMS_VETERAN_STATUS_ARG[0]
    TEAMS_VETERAN_STATUS_ARG_A=TEAMS_VETERAN_STATUS_ARG[1]
    MIN_SUB_LOCAL=MIN_SUB_VERY_OLD_OR_NO_H2H_ARG[0]
    VERY_OLD_OR_NO_H2H=MIN_SUB_VERY_OLD_OR_NO_H2H_ARG[1]
    FORM_WOUND_AND_TRANS_ARG_H=FORM_WOUND_AND_TRANS_ARG[0]
    FORM_WOUND_AND_TRANS_ARG_A=FORM_WOUND_AND_TRANS_ARG[1]
    TEAMS_GRAND_MAX_D=[TEAMS_GRAND_MAX_HUB_ARG[0],TEAMS_GRAND_MAX_HUB_ARG[1]]
    TEAMS_GRAND_MAX_D_COMMENT=TEAMS_GRAND_MAX_HUB_ARG[2]
    TEAMS_GRAND_MAX_D_COMMENT_H=TEAMS_GRAND_MAX_D_COMMENT[0]
    TEAMS_GRAND_MAX_D_COMMENT_A=TEAMS_GRAND_MAX_D_COMMENT[1]
    TEAMS_GRAND_MAX_ARG_H=TEAMS_GRAND_MAX_D[0]
    TEAMS_GRAND_MAX_ARG_A=TEAMS_GRAND_MAX_D[1]
    TEAMS_GRAND_MAX_ARG_ABS_DIFF=c_abs(TEAMS_GRAND_MAX_ARG_H-TEAMS_GRAND_MAX_ARG_A)
    CONCRETE_FORM_ARG_H=CONCRETE_FORM_ARG[0]
    CONCRETE_FORM_ARG_A=CONCRETE_FORM_ARG[1]
    CONCRETE_FORM_ARG_ABS_DIFF=c_abs(CONCRETE_FORM_ARG_H-CONCRETE_FORM_ARG_A)
    OVER_SHADOWED_CENTS_ARG_H=OVER_SHADOWED_CENTS_ARG[0]
    OVER_SHADOWED_CENTS_ARG_A=OVER_SHADOWED_CENTS_ARG[1]
    OVER_SHADOWED_CENTS_ARG_ABS_DIFF=c_abs(OVER_SHADOWED_CENTS_ARG_H-OVER_SHADOWED_CENTS_ARG_A)
    QUICK_QUALITIES_ARG_COUNT_H=QUICK_QUALITIES_ARG[0]
    QUICK_QUALITIES_ARG_COUNT_A=QUICK_QUALITIES_ARG[1]
    QUICK_QUALITIES_ARG_H=QUICK_QUALITIES_ARG[2][0]
    QUICK_QUALITIES_ARG_A=QUICK_QUALITIES_ARG[2][1]
    QUICK_QUALITIES_ARG2_COUNT_H=QUICK_QUALITIES2_ARG[0]
    QUICK_QUALITIES_ARG2_COUNT_A=QUICK_QUALITIES2_ARG[1]
    QUICK_QUALITIES_ARG2_H=QUICK_QUALITIES2_ARG[2][0]
    QUICK_QUALITIES_ARG2_A=QUICK_QUALITIES2_ARG[2][1]
    STRIKE_DEFENCE_CENT_ARG_H=STRIKE_DEFENCE_CENT_ARG[0]
    STRIKE_DEFENCE_CENT_ARG_A=STRIKE_DEFENCE_CENT_ARG[1]
    STRIKE_DEFENCE_CENT_ARG_ABS_DIFF=c_abs(STRIKE_DEFENCE_CENT_ARG_H-STRIKE_DEFENCE_CENT_ARG_A)
    ROUGH_FF_POS_CENT_ARG_H=ROUGH_FF_POS_CENT_ARG[0]
    ROUGH_FF_POS_CENT_ARG_A=ROUGH_FF_POS_CENT_ARG[1]
    ROUGH_FF_POS_CENT_ARG_ABS_DIFF=c_abs(ROUGH_FF_POS_CENT_ARG_H-ROUGH_FF_POS_CENT_ARG_A)
    POS_COUNTER_WOUNDS_CENT_ARG_H=POS_COUNTER_WOUNDS_CENT_ARG[0]
    POS_COUNTER_WOUNDS_CENT_ARG_A=POS_COUNTER_WOUNDS_CENT_ARG[1]
    POS_COUNTER_WOUNDS_CENT_ARG_ABS_DIFF=c_abs(POS_COUNTER_WOUNDS_CENT_ARG_H-POS_COUNTER_WOUNDS_CENT_ARG_A)
    POINTS_LEFT_HUNGER_ARG_H=POINTS_LEFT_HUNGER_ARG[0]
    POINTS_LEFT_HUNGER_ARG_A=POINTS_LEFT_HUNGER_ARG[1]
    ROUGH_FINAL_TEAMS_FORM_ARG_H=ROUGH_FINAL_TEAMS_FORM_ARG[0]
    ROUGH_FINAL_TEAMS_FORM_ARG_A=ROUGH_FINAL_TEAMS_FORM_ARG[1]
    ROUGH_FINAL_TEAMS_FORM_ARG_ABS_DIFF=c_abs(ROUGH_FINAL_TEAMS_FORM_ARG_H-ROUGH_FINAL_TEAMS_FORM_ARG_A)
    QUALITIES_COUNT_ARG_H=QUALITIES_COUNT_ARG[2][0]
    QUALITIES_COUNT_ARG_A=QUALITIES_COUNT_ARG[2][1]
    QUALITIES_COUNT_ARG_ABS_DIFF=c_abs(QUALITIES_COUNT_ARG_H-QUALITIES_COUNT_ARG_A)
    T1ST2_CONSIS_CENT_HOME=TEAMS_1st2_CONSISTENCY_CENT_ARG[0]
    T1ST2_CONSIS_CENT_AWAY=TEAMS_1st2_CONSISTENCY_CENT_ARG[1]
    CDF_HOME=C_DRIVEN_FORCE_ARG[0]
    CDF_AWAY=C_DRIVEN_FORCE_ARG[1]
    FINAL_FORM_AND_OS_CENTS_HOME=FINAL_FORM_AND_OS_CENTS_ARG[0]
    FINAL_FORM_AND_OS_CENTS_AWAY=FINAL_FORM_AND_OS_CENTS_ARG[1]
    OVER_SHADOWED_CENTS_COUNTER_H=OVER_SHADOWED_CENTS_COUNTER_ARG[0]
    OVER_SHADOWED_CENTS_COUNTER_A=OVER_SHADOWED_CENTS_COUNTER_ARG[1]
    OVER_SHADOWED_CENTS_COUNTER_ABS_DFF=c_abs(OVER_SHADOWED_CENTS_COUNTER_H-OVER_SHADOWED_CENTS_COUNTER_A)
    FINAL_FORM_AND_OS_CENTS_ABS_DIFF=c_abs(FINAL_FORM_AND_OS_CENTS_HOME-FINAL_FORM_AND_OS_CENTS_AWAY)
    ATT_AND_SOT_ARG_HOME=ATT_AND_SOT_ARG[0]
    ATT_AND_SOT_ARG_AWAY=ATT_AND_SOT_ARG[1]
    ATT_AND_SOT_ARG_ABS_DIFF=c_abs(ATT_AND_SOT_ARG_HOME-ATT_AND_SOT_ARG_AWAY)
    FINAL_FORM_AND_ATTACKS_PLUS_SOT_H=FINAL_FORM_AND_ATTACKS_PLUS_SOT_ARG[0]
    FINAL_FORM_AND_ATTACKS_PLUS_SOT_A=FINAL_FORM_AND_ATTACKS_PLUS_SOT_ARG[1]
    FINAL_FORM_AND_ATTACKS_PLUS_SOT_ABS_DIFF=c_abs(FINAL_FORM_AND_ATTACKS_PLUS_SOT_H-FINAL_FORM_AND_ATTACKS_PLUS_SOT_A)
    HOME_ATTACKS_PLUS_WOUNDS_CH=ATT_WND_HUB_ARG[0]
    AWAY_ATTACKS_PLUS_WOUNDS_CH=ATT_WND_HUB_ARG[1]
    TEAMS_ATTACKS_PLUS_WOUNDS_CH_ABS_DIFF=c_abs(HOME_ATTACKS_PLUS_WOUNDS_CH-AWAY_ATTACKS_PLUS_WOUNDS_CH)
    LSW_HOME=LAST_WOUNDS_SQUAD_ARG[0]
    LSW_AWAY=LAST_WOUNDS_SQUAD_ARG[1]
    LSW_HOME_PATTERN=LAST_WOUNDS_SQUAD_ARG[2]
    LSW_AWAY_PATTERN=LAST_WOUNDS_SQUAD_ARG[3]
    CHAIN_LOSS_ABS_DIFF=c_abs(LSW_HOME_PATTERN-LSW_AWAY_PATTERN)
    LAST_MTC_SCR_MAX=max([LSW_HOME_PATTERN,LSW_AWAY_PATTERN])
    LAST_MTC_SCR_MIN=min([LSW_HOME_PATTERN,LSW_AWAY_PATTERN])
    H2H_LAST_SCORE_CENT_BOX_H=H2H_LAST_SCORE_CENT_BOX[0]
    H2H_LAST_SCORE_CENT_BOX_A=H2H_LAST_SCORE_CENT_BOX[1]
    ONLY_HOME_SCORES_LAST_SC_DIFF_ARG=LAST_SCORES_ONLY_T_DIFF[0]
    ONLY_AWAY_SCORES_LAST_SC_DIFF_ARG=LAST_SCORES_ONLY_T_DIFF[1]
    FORM_CENT_QUICK_HOME=FORM_CENT_QUICK_ARG[0]
    FORM_CENT_QUICK_AWAY=FORM_CENT_QUICK_ARG[1]
    OVER_SHADOWED_CENTS_COUNTER_H_LOGIC=OVER_SHADOWED_CENTS_COUNTER_H>OVER_SHADOWED_CENTS_COUNTER_A and POS_COUNTER_WOUNDS_CENT_ARG_H>POS_COUNTER_WOUNDS_CENT_ARG_A and ROUGH_FINAL_TEAMS_FORM_ARG_H>ROUGH_FINAL_TEAMS_FORM_ARG_A and POINTS_LEFT_HUNGER_ARG_H>=POINTS_LEFT_HUNGER_ARG_A and OVER_SHADOWED_CENTS_COUNTER_ABS_DFF>=3
    OVER_SHADOWED_CENTS_COUNTER_A_LOGIC=OVER_SHADOWED_CENTS_COUNTER_A>OVER_SHADOWED_CENTS_COUNTER_H and POS_COUNTER_WOUNDS_CENT_ARG_A>POS_COUNTER_WOUNDS_CENT_ARG_H and ROUGH_FINAL_TEAMS_FORM_ARG_A>ROUGH_FINAL_TEAMS_FORM_ARG_H and POINTS_LEFT_HUNGER_ARG_A>=POINTS_LEFT_HUNGER_ARG_H and OVER_SHADOWED_CENTS_COUNTER_ABS_DFF>=3
    H2H_ROUGH_MIXED_ARG_H=H2H_ROUGH_MIXED_ARG[0]
    H2H_ROUGH_MIXED_ARG_A=H2H_ROUGH_MIXED_ARG[1]
    H2H_ROUG_DIFF=c_abs(H2H_ROUGH_MIXED_ARG_H-H2H_ROUGH_MIXED_ARG_A)
    CDF_DIV_ARG_HOME=round(CDF_DIV_ARG[0])
    CDF_DIV_ARG_AWAY=round(CDF_DIV_ARG[1])
    CDF_DIV_ARG_ABS_DIFF=c_abs(CDF_DIV_ARG_HOME-CDF_DIV_ARG_AWAY)
    HURTS_LOGIC_HOME=(LSW_HOME>LSW_AWAY) or (LSW_HOME_PATTERN>LSW_AWAY_PATTERN)
    HURTS_LOGIC_AWAY=(LSW_AWAY>LSW_HOME) or (LSW_AWAY_PATTERN>LSW_HOME_PATTERN)
    LSW_TIM_ABS_DIFF=c_abs(LSW_HOME-LSW_AWAY)
    LSW_TIM_PATTERN_ABS_DIFF=c_abs(LSW_HOME_PATTERN-LSW_AWAY_PATTERN)
    CDF_LAST_GAMES_DIV_ARG_H=round(CDF_LAST_GAMES_DIV_ARG[0])
    CDF_LAST_GAMES_DIV_ARG_A=round(CDF_LAST_GAMES_DIV_ARG[1])
    TEAM_DEFEN_HOME=TEAM_DEFEN[0]
    TEAM_DEFEN_AWAY=TEAM_DEFEN[1]
    TEAM_DEFEN_MAX=max(TEAM_DEFEN)
    STRIKERS_POWER_MIN=min(STRIKERS_POWER)
    STRIKERS_POWER_MAX=max(STRIKERS_POWER)
    HOME_STRIKERS_POWER=STRIKERS_POWER[0]
    AWAY_STRIKERS_POWER=STRIKERS_POWER[1]
    C_DRIVEN_FORCE_DIFF_ARG=c_abs(CDF_HOME-CDF_AWAY)
    HOME_ATH2H=ALL_TIMES_H2H_ARG_CENT2[0]
    AWAY_ATH2H=ALL_TIMES_H2H_ARG_CENT2[1]
    FPCD_HOME=FINAL_PLUS_C_DRIVEN[0]
    FPCD_AWAY=FINAL_PLUS_C_DRIVEN[1]
    FPCD_ABS_DIFF=c_abs(FPCD_HOME-FPCD_AWAY)
    _3LSPOLST_HOME=LAST_LOST_POINTS_CENT_ARG[0]
    _3LSPOLST_AWAY=LAST_LOST_POINTS_CENT_ARG[1]
    _3LSPOLST_ABS_DIFF=c_abs(_3LSPOLST_HOME-_3LSPOLST_AWAY)
    ONPLOST_HOME=OLD_AND_NEW_LOST_POINTS_SUM_ARG[0]
    ONPLOST_AWAY=OLD_AND_NEW_LOST_POINTS_SUM_ARG[1]
    ONPL_ABS_DIFF=c_abs(ONPLOST_HOME-ONPLOST_AWAY)
    H2H_NO_DISCRE_ARRAY_HOME=H2H_NO_DISCRE_ARRAY[0]
    H2H_NO_DISCRE_ARRAY_AWAY=H2H_NO_DISCRE_ARRAY[1]
    HOME_TL_OMTCENT=LOST_POINTS_TOTAL_PLUS_OMTC_FORM_CENT_ARG[0]
    AWAY_TL_OMTCENT=LOST_POINTS_TOTAL_PLUS_OMTC_FORM_CENT_ARG[1]
    LOST_PS_OMT_ABS_DIFF=c_abs(HOME_TL_OMTCENT-AWAY_TL_OMTCENT)
    H2H_D_FORM_ABS_DFF=c_abs(H2H_DISCRET_FORM_LOCAL_ARG[0]-H2H_DISCRET_FORM_LOCAL_ARG[1])
    H2H_FINAL_FORM_HOME=H2H_FINAL_FORM_ARG[0]
    H2H_FINAL_FORM_AWAY=H2H_FINAL_FORM_ARG[1]
    HOME_WINS_DRAWS_CENT_LOCAL=WINS_DRAWS_CENT_ARG[0]
    AWAY_WINS_DRAWS_CENT_LOCAL=WINS_DRAWS_CENT_ARG[1]
    WINS_DRAWS_CENT_ARG_MAX=max(WINS_DRAWS_CENT_ARG)
    WINS_DRAWS_CENT_ARG_MIN=min(WINS_DRAWS_CENT_ARG)
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG_H=STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG[0]
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG_A=STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG[1]
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG_ABS_DIFF=abs(STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG_H-STRIKE_DEFENCE_LOSSES_CENT_COMBINED_ARG_A)
    HOME_POSITION=POSITION_BOX[0]
    AWAY_POSITION=POSITION_BOX[1]
    HOME_WOUNDS_LOGIC=(DYNAMIC_WOUNDS_ARRAY_ARG_H>=3 or DYNAMIC_WOUNDS_ARRAY_ARG_H>=DYNAMIC_WOUNDS_ARRAY_ARG_A or (DYNAMIC_WOUNDS_ARRAY_ARG_ABS_DIFF<=2 and DYNAMIC_WOUNDS_ARRAY_ARG_H>0)) and CUSTOM_POSITION_H<CUSTOM_POSITION_A
    AWAY_WOUNDS_LOGIC=(DYNAMIC_WOUNDS_ARRAY_ARG_A>=3 or DYNAMIC_WOUNDS_ARRAY_ARG_A>=DYNAMIC_WOUNDS_ARRAY_ARG_H or (DYNAMIC_WOUNDS_ARRAY_ARG_ABS_DIFF<=2 and DYNAMIC_WOUNDS_ARRAY_ARG_A>0)) and CUSTOM_POSITION_A<CUSTOM_POSITION_H
    TEAM_POSITION_DIFF=c_abs(HOME_POSITION-AWAY_POSITION)
    HOME_PTDB=POSITION_TOP_DOWN_BOX[0]
    AWAY_PTDB=POSITION_TOP_DOWN_BOX[1]
    HOME_PTDB_TOP=HOME_PTDB[0]
    AWAY_PTDB_TOP=AWAY_PTDB[0]
    PTDB_TOP_MAX=max([HOME_PTDB_TOP,AWAY_PTDB_TOP])
    HOME_PTDB_BOTTOM=HOME_PTDB[1]
    AWAY_PTDB_BOTTOM=AWAY_PTDB[1]
    PTDB_BOTTOM_MAX=max([HOME_PTDB_BOTTOM,AWAY_PTDB_BOTTOM])
    DRIVEN_ENGIN_INSTIGATION_LOGIC=PTDB_TOP_MAX>=2 or PTDB_BOTTOM_MAX>=3
    SPORTYBET_HA_ODDS=OTHER_SITES_PREDICTION_ARG[0]
    HOME_ODDZ=SPORTYBET_HA_ODDS[0]
    AWAY_ODDZ=SPORTYBET_HA_ODDS[1]
    ODDZ_DIFF=c_abs(HOME_ODDZ-AWAY_ODDZ)
    odds_min=min(SPORTYBET_HA_ODDS)
    FOREBET_PREDICTION_LOCAL=OTHER_SITES_PREDICTION_ARG[1]
    FOREBET_PREDICTION_LOCAL_SUM=sum(FOREBET_PREDICTION_LOCAL)
    FOREBET_PREDICTION_LOCAL_MIN=min(FOREBET_PREDICTION_LOCAL)
    FOREBET_PREDICTION_LOCAL_MAX=max(FOREBET_PREDICTION_LOCAL)
    HOME_SCR=FOREBET_PREDICTION_LOCAL[0]
    AWAY_SCR=FOREBET_PREDICTION_LOCAL[1]
    HOME_WINS_OTHER_SITES=HOME_ODDZ<=AWAY_ODDZ and HOME_SCR>=AWAY_SCR
    AWAY_WINS_OTHER_SITES=AWAY_ODDZ<=HOME_ODDZ and AWAY_SCR>=HOME_SCR
    FOREBET_PREDICTION_SCORES_DIFF=c_abs(HOME_SCR-AWAY_SCR)
    HOME_ONLY_AWAY_ONLY_CENT_ARRAY_MIN=min(HOME_ONLY_AWAY_ONLY_CENT_ARRAY)
    HOME_DIDNT_WIN_LAST2_H2H_GAMES=TEAM_WINS_ALL_H2H_LOGIC[0]
    AWAY_DIDNT_WIN_LAST2_H2H_GAMES=TEAM_WINS_ALL_H2H_LOGIC[1]
    HOME_KILLER=not HOME_DIDNT_WIN_LAST2_H2H_GAMES and C_DRIVEN_FORCE_DIFF_ARG>2 and CDF_HOME<CDF_AWAY
    AWAY_KILLER=not AWAY_DIDNT_WIN_LAST2_H2H_GAMES and C_DRIVEN_FORCE_DIFF_ARG>2 and CDF_AWAY<CDF_HOME
    UNI_COEFFI_HOME=UNI_COEFFICIENT_ARG[0]
    UNI_COEFFI_AWAY=UNI_COEFFICIENT_ARG[1]
    HOME_POTENTIAL=CENTS_ARRAY_ARG[0]
    AWAY_POTENTIAL=CENTS_ARRAY_ARG[1]
    DRAWS_POTENTIAL=CENTS_ARRAY_ARG[2]
    TEAMS_POTENTIAL_DIFF=c_abs(HOME_POTENTIAL-AWAY_POTENTIAL)
    DP_GREATER_THAN_ALL=TEAMS_POTENTIAL_DIFF<=15 or DRAWS_POTENTIAL>HOME_POTENTIAL and DRAWS_POTENTIAL>AWAY_POTENTIAL
    WINS_COUNT_OVERALL=CENTS_ARRAY_ARG[3]
    WINS_FORM_OVERALL=CENTS_ARRAY_ARG[4]
    HOME_WINS_FORM=WINS_FORM_OVERALL[0]
    AWAY_WINS_FORM=WINS_FORM_OVERALL[1]
    HOME_WINS_COUNT=WINS_COUNT_OVERALL[0]
    AWAY_WINS_COUNT=WINS_COUNT_OVERALL[1]
    TEAM_WINS_COUNT_ABS_DIFF=c_abs(HOME_WINS_COUNT-AWAY_WINS_COUNT)
    TOTAL_FORMS_DIFF=c_abs(HOME_WINS_FORM-AWAY_WINS_FORM)
    HOME_L_WOUNDS=TEAMS_LAST_SCORES_WOUNDS[0]
    AWAY_L_WOUNDS=TEAMS_LAST_SCORES_WOUNDS[1]
    H_STRUCTURE=HOME_AWAY_STRUCTURE[0]
    A_STRUCTURE=HOME_AWAY_STRUCTURE[1]
    HOME_STRIKING_POWER=H_STRUCTURE-HOME_WINS_DRAWS_CENT_LOCAL
    AWAY_STRIKING_POWER=A_STRUCTURE-AWAY_WINS_DRAWS_CENT_LOCAL
    HOME_WINS_LOGIC0=HOME_WINS_DRAWS_CENT_LOCAL>AWAY_WINS_DRAWS_CENT_LOCAL and HOME_STRIKING_POWER>AWAY_STRIKING_POWER
    AWAY_WINS_LOGIC0=AWAY_WINS_DRAWS_CENT_LOCAL>HOME_WINS_DRAWS_CENT_LOCAL and AWAY_STRIKING_POWER>HOME_STRIKING_POWER
    TRIPPLE_PREDICTION_LOGIG=tripplePredict(HOME_WINS_DRAWS_CENT_LOCAL,AWAY_WINS_DRAWS_CENT_LOCAL,
                                            H_STRUCTURE-HOME_WINS_DRAWS_CENT_LOCAL,A_STRUCTURE-AWAY_WINS_DRAWS_CENT_LOCAL,
                                            HOME_STRIKING_POWER,AWAY_STRIKING_POWER,
                                            H_STRUCTURE,A_STRUCTURE)
    print(f'TRIPPLE_PREDICTION_LOGIG ---> {TRIPPLE_PREDICTION_LOGIG}')
    GG_WINS_LOGIC=TRIPPLE_PREDICTION_LOGIG[0]
    HOME_WINS_LOGIC=TRIPPLE_PREDICTION_LOGIG[1]
    AWAY_WINS_LOGIC=TRIPPLE_PREDICTION_LOGIG[2]
    UNDER_3P5_WINS_LOGIC=TRIPPLE_PREDICTION_LOGIG[3]
    TEAM_STRIKING_POWER_MIN=min([HOME_STRIKING_POWER,AWAY_STRIKING_POWER])
    TEAM_STRIKING_POWER_MAX=max([HOME_STRIKING_POWER,AWAY_STRIKING_POWER])
    STRUCTURE_DIFF=c_abs(H_STRUCTURE-A_STRUCTURE)
    H2H_DFFSS=c_abs(H2H_FINAL_FORM_HOME-H2H_FINAL_FORM_AWAY)
    i1=INCRE_DECRE_ARG[0][0]
    i2=INCRE_DECRE_ARG[0][1]
    d1=INCRE_DECRE_ARG[1][0]
    d2=INCRE_DECRE_ARG[1][1]
    home_mult_decre=1
    away_mult_decre=1
    if H2H_DFFSS>=21:
       if H2H_FINAL_FORM_HOME>H2H_FINAL_FORM_AWAY:
          away_mult_decre=-1
       else:
          home_mult_decre=-1
    HOME_DECRE_CENT=d1*home_mult_decre
    AWAY_DECRE_CENT=d2*away_mult_decre
    HOME_NET_INCRE=i1-d1
    AWAY_NET_INCRE=i2-d2
    NET_INCRE=[HOME_NET_INCRE,AWAY_NET_INCRE]
    NET_INCRE_SUM=sum(NET_INCRE)
    NET_INCRE_MIN=min(NET_INCRE)
    NET_INCRE_MAX=0
    try:
        NET_INCRE_MAX=max(NET_INCRE)
    except Exception:
        pass
    DECRE_CENT_ARRAY=[HOME_DECRE_CENT,AWAY_DECRE_CENT]
    DECRE_CENT_ARRAY_MIN=min(DECRE_CENT_ARRAY)
    print(f'NET_INCRE ---> {NET_INCRE}{NET_INCRE_SUM}')
    RECENT_LOSES_ARRAY_MIN=min(RECENT_LOSES_ARRAY)
    RECENT_LOSES_ARRAY_MAX=max(RECENT_LOSES_ARRAY)
    HOME_FORM_FINAL=FORM_CENT_QUICK_ARG[0]
    AWAY_FORM_FINAL=FORM_CENT_QUICK_ARG[1]
    INNER_QUICK=quickCentCalc([HOME_FORM_FINAL+HOME_WINS_COUNT,AWAY_FORM_FINAL+AWAY_WINS_COUNT])
    HOME_FORM_FINAL_PLUS_COUNT=INNER_QUICK[0]
    AWAY_FORM_FINAL_PLUS_COUNT=INNER_QUICK[1]
    FORM_COUNT_DIFF=c_abs(HOME_FORM_FINAL_PLUS_COUNT-AWAY_FORM_FINAL_PLUS_COUNT)
    HOME_AWAY_FINAL_FORM_MIN=min(FORM_CENT_QUICK_ARG)
    HOME_ALL_SCORES_LOSES=HOME_AWAY_LOST_POINTS_CENT_ARG[0]
    AWAY_ALL_SCORES_LOSES=HOME_AWAY_LOST_POINTS_CENT_ARG[1]
    HRL=RECENT_LOSES_ARRAY[0]
    ARL=RECENT_LOSES_ARRAY[1]
    HOME_CURRENT_DRIVE=HRL+sum(HOME_PTDB)
    AWAY_CURRENT_DRIVE=ARL+sum(AWAY_PTDB)
    TOTAL_LOST_POINTS_HOME=HOME_ALL_SCORES_LOSES+HRL
    TOTAL_LOST_POINTS_AWAY=AWAY_ALL_SCORES_LOSES+ARL
    TOTAL_LOSES_CENT=quickCentCalc([TOTAL_LOST_POINTS_HOME,TOTAL_LOST_POINTS_AWAY])
    TOTAL_LOST_POINTS_HOME_GRAND=TOTAL_LOSES_CENT[0]
    TOTAL_LOST_POINTS_AWAY_GRAND=TOTAL_LOSES_CENT[1]
    TEAMS_CURRENT_DRIVE_FORCES=quickCentCalc([HOME_CURRENT_DRIVE,AWAY_CURRENT_DRIVE])
    TEAMS_CURRENT_DRIVE_FORCES=quickCentCalc([TOTAL_LOST_POINTS_HOME_GRAND+TEAMS_CURRENT_DRIVE_FORCES[0],TOTAL_LOST_POINTS_AWAY_GRAND+TEAMS_CURRENT_DRIVE_FORCES[1]])
    print(f'TEAMS_CURRENT_DRIVE_FORCES ---> {TEAMS_CURRENT_DRIVE_FORCES}')
    print(f'TOTAL_LOSES_CENT ---> {[TOTAL_LOST_POINTS_HOME,TOTAL_LOST_POINTS_AWAY]}')
    HOME_DRIVEN_FORCE=TEAMS_CURRENT_DRIVE_FORCES[0]
    AWAY_DRIVEN_FORCE=TEAMS_CURRENT_DRIVE_FORCES[1]
    TEAMS_CURRENT_DRIVE_FORCES_ABS_DIFF=c_abs(HOME_DRIVEN_FORCE-AWAY_DRIVEN_FORCE)
    total_losses_diff=c_abs(TOTAL_LOST_POINTS_HOME-TOTAL_LOST_POINTS_AWAY)
    TEAMS_CURRENT_DRIVE_FORCES_MIN=min(TEAMS_CURRENT_DRIVE_FORCES)
    RECENT_LOSES_DIFF=c_abs(HRL-ARL)
    HOME_NET_FORM=HOME_FORM_FINAL+HOME_DECRE_CENT
    AWAY_NET_FORM=AWAY_FORM_FINAL+AWAY_DECRE_CENT
    NET_FORM_DIFF=c_abs(HOME_NET_FORM-AWAY_NET_FORM)
    NET_FORM_MIN=min([c_abs(HOME_NET_FORM),c_abs(AWAY_NET_FORM)])
    NET_FORM_MAX=max([c_abs(HOME_NET_FORM),c_abs(AWAY_NET_FORM)])
    print(f'NET_FORM_MIN ---> {NET_FORM_MIN}')
    NET_FORM_ARRAY=[HOME_NET_FORM,AWAY_NET_FORM]
    print(f'HOME_AWAY_DECRE_CENT ---> {DECRE_CENT_ARRAY}')
    print(f'HOME_AWAY_NET_FORMS ---> {NET_FORM_ARRAY}')
    #HOME OR DRAW AND AWAY OR DRAW ZONE
    HOME_SWAP_ALERT=final_form_diff<=6 and HRL<ARL and HOME_DRIVEN_FORCE<=AWAY_DRIVEN_FORCE and TEAMS_CURRENT_DRIVE_FORCES_ABS_DIFF>=10
    AWAY_SWAP_ALERT=final_form_diff<=6 and ARL<HRL and AWAY_DRIVEN_FORCE<=HOME_DRIVEN_FORCE and TEAMS_CURRENT_DRIVE_FORCES_ABS_DIFF>=10
    HOME_DRAW_FORM=HOME_NET_FORM+HRL+HOME_NET_INCRE
    AWAY_DRAW_FORM=AWAY_NET_FORM+ARL+AWAY_NET_INCRE
    def woundPlusMinusChanger(mult_operator):
        TOTAL_LOST_POINTS_HOME=TEAMS_CURRENT_DRIVE_FORCES[0]
        TOTAL_LOST_POINTS_AWAY=TEAMS_CURRENT_DRIVE_FORCES[1]
        HOME_WOUNDS_DIFF_FORM=mult_operator*TOTAL_LOST_POINTS_HOME
        AWAY_WOUNDS_DIFF_FORM=mult_operator*TOTAL_LOST_POINTS_AWAY
        HOME_NET_STRENGTH=HOME_FORM_FINAL+HOME_WOUNDS_DIFF_FORM
        AWAY_NET_STRENGTH=AWAY_FORM_FINAL+AWAY_WOUNDS_DIFF_FORM
        WOUND_DIV_CENT=quickCentCalc([HOME_NET_STRENGTH,AWAY_NET_STRENGTH])
        wounds_div_home=WOUND_DIV_CENT[0]
        wounds_div_away=WOUND_DIV_CENT[1]
        return [wounds_div_home,wounds_div_away]
    WOUND_MINUS=woundPlusMinusChanger(-1)
    wounds_div_home_MINUS=WOUND_MINUS[0]
    wounds_div_away_MINUS=WOUND_MINUS[1]
    WOUND_PLUS=woundPlusMinusChanger(1)
    wounds_div_home_PLUS=WOUND_PLUS[0]
    wounds_div_away_PLUS=WOUND_PLUS[1]
    OVER_ALL_FORM_PLUS=miniFormCalc([[wounds_div_home_PLUS,wounds_div_away_PLUS],HOME_ONLY_AWAY_ONLY_CENT_ARRAY])
    OVER_ALL_FORM=miniFormCalc([[wounds_div_home_MINUS,wounds_div_away_MINUS],HOME_ONLY_AWAY_ONLY_CENT_ARRAY])
    OVER_ALL_FORM_PLUS_HOME=OVER_ALL_FORM_PLUS[0]
    OVER_ALL_FORM_PLUS_AWAY=OVER_ALL_FORM_PLUS[1]
    OVER_ALL_FORM_PLUS_DIFF=c_abs(OVER_ALL_FORM_PLUS_HOME-OVER_ALL_FORM_PLUS_AWAY)
    HOME_OVER_ALL=OVER_ALL_FORM[0]
    AWAY_OVER_ALL=OVER_ALL_FORM[1]
    OVER_ALL_FORM_DIFF=c_abs(HOME_OVER_ALL-AWAY_OVER_ALL)
    FORMS_MIN=min([OVER_ALL_FORM_PLUS_DIFF,OVER_ALL_FORM_DIFF])
    HOME_ALL_FORM=OVER_ALL_FORM_PLUS[0]+HOME_OVER_ALL
    AWAY_ALL_FORM=OVER_ALL_FORM_PLUS[1]+AWAY_OVER_ALL
    GRAND_TEAM_FORM=quickCentCalc([HOME_ALL_FORM,AWAY_ALL_FORM])
    GRAND_TEAM_FORM_HOME=GRAND_TEAM_FORM[0]
    GRAND_TEAM_FORM_AWAY=GRAND_TEAM_FORM[1]
    GRAND_TEAM_FORM_ABS_DIFF=c_abs(GRAND_TEAM_FORM_HOME-GRAND_TEAM_FORM_AWAY)
    #EXPERIMENT WITH FORMS ZONE
    DANGEROUS_TEAM_LOGIC_ARG_H_LOGIC=(DANGEROUS_TEAM_LOGIC_ARG_H and not DANGEROUS_TEAM_LOGIC_ARG_A) or (not DANGEROUS_TEAM_LOGIC_ARG_H and not DANGEROUS_TEAM_LOGIC_ARG_A)
    DANGEROUS_TEAM_LOGIC_ARG_A_LOGIC=(DANGEROUS_TEAM_LOGIC_ARG_A and not DANGEROUS_TEAM_LOGIC_ARG_H) or (not DANGEROUS_TEAM_LOGIC_ARG_A and not DANGEROUS_TEAM_LOGIC_ARG_H)
    EXPERIMENTAL_HOME_LOGIC=VARIABLES_CHANGE_LOGIC_HOME_LOCAL and HOME_WOUNDS_LOGIC#(HOME_CONSISTENCY_LOCAL_FIRST_1s2Max>=10 and VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_H>VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_A) or (DYNAMIC_WOUNDS_ARRAY_ARG_H>DYNAMIC_WOUNDS_ARRAY_ARG_A and DYNAMIC_WOUNDS_ARRAY_ARG_ABS_DIFF>=5 and HOME_CONSISTENCY_LOCAL_FIRST_1s2Max<10 and VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_H>VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_A)# and HOME_POSITION<AWAY_POSITION and VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_abs>=12#STRIKERS_AND_WOUNDS_CENT_ARG_H>=STRIKERS_AND_WOUNDS_CENT_ARG_A and not TEAM_AVERAGE_H_LOCAL and HOME_POSITION<AWAY_POSITION and H2H_SAME_MTCHS_CENTS_RAW_ARG_H>H2H_SAME_MTCHS_CENTS_RAW_ARG_A and DANGEROUS_TEAM_LOGIC_ARG_H_LOGIC# and QUICK_QUALITIES_ARG_H>QUICK_QUALITIES_ARG_A and QUICK_QUALITIES_ARG2_H>QUICK_QUALITIES_ARG2_A and (QUICK_QUALITIES_ARG_A<25 and QUICK_QUALITIES_ARG2_A<25)
    EXPERIMENTAL_AWAY_LOGIC=VARIABLES_CHANGE_LOGIC_AWAY_LOCAL and AWAY_WOUNDS_LOGIC#(AWAY_CONSISTENCY_LOCAL_FIRST_1s2Max>=10 and VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_A>VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_H) or (DYNAMIC_WOUNDS_ARRAY_ARG_A>DYNAMIC_WOUNDS_ARRAY_ARG_H and DYNAMIC_WOUNDS_ARRAY_ARG_ABS_DIFF>=5 and AWAY_CONSISTENCY_LOCAL_FIRST_1s2Max<10 and VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_A>VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_H)# and AWAY_POSITION<HOME_POSITION and VARIABLE_FINAL_FORM_H2H_INFLUENCED_ARG_abs>=12#STRIKERS_AND_WOUNDS_CENT_ARG_A>=STRIKERS_AND_WOUNDS_CENT_ARG_H and not TEAM_AVERAGE_A_LOCAL and AWAY_POSITION<HOME_POSITION and H2H_SAME_MTCHS_CENTS_RAW_ARG_A>H2H_SAME_MTCHS_CENTS_RAW_ARG_H and DANGEROUS_TEAM_LOGIC_ARG_A_LOGIC# and QUICK_QUALITIES_ARG_A>QUICK_QUALITIES_ARG_H and QUICK_QUALITIES_ARG2_A>QUICK_QUALITIES_ARG2_H and (QUICK_QUALITIES_ARG_H<25 and QUICK_QUALITIES_ARG2_H<25)
    HOME_STRAIGH_WIN_LOGIC=(TEAM_DEFEN_HOME>TEAM_DEFEN_AWAY and TEAM_DEFEN_HOME>=55) or ((HOME_STRIKERS_POWER>AWAY_STRIKERS_POWER and HOME_STRIKERS_POWER>=55) or (not VERY_OLD_OR_NO_H2H and H2H_ROUGH_MIXED_ARG_H>H2H_ROUGH_MIXED_ARG_A and H2H_ROUGH_MIXED_ARG_H>=55))
    AWAY_STRAIGH_WIN_LOGIC=(TEAM_DEFEN_AWAY>TEAM_DEFEN_HOME and TEAM_DEFEN_AWAY>=55) or ((AWAY_STRIKERS_POWER>HOME_STRIKERS_POWER and AWAY_STRIKERS_POWER>=55) or (not VERY_OLD_OR_NO_H2H and H2H_ROUGH_MIXED_ARG_A>H2H_ROUGH_MIXED_ARG_H and H2H_ROUGH_MIXED_ARG_A>=53))
    HOME_STRAIGH_WIN_LOGIC2=MIN_SUB_LOCAL>=12 and ((HOME_STRIKERS_POWER>AWAY_STRIKERS_POWER and HOME_STRIKERS_POWER>=40 and TEAM_DEFEN_HOME>=50) or (HOME_STRIKERS_POWER>AWAY_STRIKERS_POWER and HOME_STRIKERS_POWER>=50 and TEAM_DEFEN_HOME>=40) or (not VERY_OLD_OR_NO_H2H and H2H_ROUGH_MIXED_ARG_H>H2H_ROUGH_MIXED_ARG_A and H2H_ROUGH_MIXED_ARG_H>=53 and TEAM_DEFEN_HOME>=40))
    AWAY_STRAIGH_WIN_LOGIC2=MIN_SUB_LOCAL>=12 and ((AWAY_STRIKERS_POWER>HOME_STRIKERS_POWER and AWAY_STRIKERS_POWER>=40 and TEAM_DEFEN_AWAY>=50) or (AWAY_STRIKERS_POWER>HOME_STRIKERS_POWER and AWAY_STRIKERS_POWER>=50 and TEAM_DEFEN_AWAY>=40) or (not VERY_OLD_OR_NO_H2H and H2H_ROUGH_MIXED_ARG_A>H2H_ROUGH_MIXED_ARG_H and H2H_ROUGH_MIXED_ARG_A>=53 and TEAM_DEFEN_AWAY>=40))
    HSW='NO'
    ASW='NO'
    if VARIABLE_QUALITIES_DIFF_LOCAL>=8:#not TEAM_AVERAGE_H_LOCAL and TEAM_AVERAGE_A_LOCAL and HOME_POSITION<=AWAY_POSITION and HOME_TRIO_DIFF_MIN_VAL_LOCAL>=-10 and TITANIC_FORM_ARG_COUNT_H>=5:#(HOME_STRAIGH_WIN_LOGIC or HOME_STRAIGH_WIN_LOGIC2) and HOME_POSITION<=AWAY_POSITION and STRIKE_DEFENCE_CENT_ARG_H>STRIKE_DEFENCE_CENT_ARG_A and STRIKE_DEFENCE_CENT_ARG_ABS_DIFF>=10:
       HSW='YES'
    if VARIABLE_QUALITIES_DIFF_LOCAL>=8:#not TEAM_AVERAGE_A_LOCAL and TEAM_AVERAGE_H_LOCAL and AWAY_POSITION<=HOME_POSITION and AWAY_TRIO_DIFF_MIN_VAL_LOCAL>=-10 and TITANIC_FORM_ARG_COUNT_A>=5:#(AWAY_STRAIGH_WIN_LOGIC or AWAY_STRAIGH_WIN_LOGIC2) and AWAY_POSITION<=HOME_POSITION and STRIKE_DEFENCE_CENT_ARG_A>STRIKE_DEFENCE_CENT_ARG_H and STRIKE_DEFENCE_CENT_ARG_ABS_DIFF>=10:
       ASW='YES'
    if TEAM_GREEN_LIGHT_CENT_ARG_ABS_DIFF<=4:
        #print(f'-------------------------------> GG FT HOME TEAM ---> {HOME_TEAM}\n')
        #PREDICTION_MADE=True
        pass 
    if not PREDICTION_MADE and PRO_TEAM_STATUS_ARG_H:# and MEGA_QUALITIES_SERIES_CENT_ARG_A<=2 and TEAM_GREEN_LIGHT_CENT_ARG_H>TEAM_GREEN_LIGHT_CENT_ARG_A and TEAMS_FAILS_PATTERN_FORCE_ARG_H>=TEAMS_FAILS_PATTERN_FORCE_ARG_A:# and HOME_TRANS_LOGIC:
        print(f'-------------------------------> HOME OR DRAW FT HOME TEAM({HSW}) ---> {HOME_TEAM}\n')
        PREDICTION_MADE=True
        pass
    if not PREDICTION_MADE and PRO_TEAM_STATUS_ARG_A:# and MEGA_QUALITIES_SERIES_CENT_ARG_H<=2 and TEAM_GREEN_LIGHT_CENT_ARG_A>TEAM_GREEN_LIGHT_CENT_ARG_H and TEAMS_FAILS_PATTERN_FORCE_ARG_A>=TEAMS_FAILS_PATTERN_FORCE_ARG_H:# and AWAY_TRANS_LOGIC:
        print(f'-------------------------------> AWAY OR DRAW FT AWAY TEAM({ASW}) ---> {AWAY_TEAM}\n')
        PREDICTION_MADE=True
        pass

    if not PREDICTION_MADE and HOME_WOUNDS_LOGIC and FINAL_PROTOTYPE_FORM_COUNT_H>FINAL_PROTOTYPE_FORM_COUNT_A and FINAL_PROTOTYPE_FORM_H>FINAL_PROTOTYPE_FORM_A:
        #print(f'-------------------------------> HOME OR DRAW FT HOME TEAM({HSW}*k) ---> {HOME_TEAM}\n')
        #PREDICTION_MADE=True
        pass
    if not PREDICTION_MADE and AWAY_WOUNDS_LOGIC and FINAL_PROTOTYPE_FORM_COUNT_A>FINAL_PROTOTYPE_FORM_COUNT_H and FINAL_PROTOTYPE_FORM_A>FINAL_PROTOTYPE_FORM_H:
        #print(f'-------------------------------> AWAY OR DRAW FT AWAY TEAM({ASW}*k) ---> {AWAY_TEAM}\n')
        #PREDICTION_MADE=True
        
        pass
    return PREDICTION_MADE
def currentLosesCent(home_last_two_scores_array,away_last_two_scores_array):
    def scores_runner(scores_array,TEAMname,teamCoeffie,GRAND_DIV_COEFFIE):
        lost_count=0
        CHAINS_LOST_ALERT=False
        CHAINS_LOST_TENSION=0
        CHAINS_LOST_COUNT=0
        _plus_2_lost_count=0
        _plus_2_lost_tension=0
        for sarn,sar in enumerate(scores_array):
            chains_lost_count=0
            lost_diff_array=[]
            for srn,sarc in enumerate(sar):
                hsls=sarc[0]
                asls=sarc[1]
                scrdff=c_abs(hsls-asls)
                adv_diff=scrdff
                if hsls<asls:
                    if srn==0:
                      adv_diff=scrdff*teamCoeffie
                    PLUS_TWO_LOST=False
                    if scrdff>=2 and srn==0 and sarn!=3:
                          _plus_2_lost_count+=1
                          _plus_2_lost_tension+=(scrdff*teamCoeffie)
                          PLUS_TWO_LOST=True
                    if not PLUS_TWO_LOST and sarn!=3:
                         lost_count+=adv_diff
                    chains_lost_count+=1
                    lost_diff_array+=[scrdff*teamCoeffie]
            if chains_lost_count>1:
               for ldf in lost_diff_array:
                   CHAINS_LOST_TENSION+=(ldf*GRAND_DIV_COEFFIE)
               CHAINS_LOST_ALERT=True
               CHAINS_LOST_COUNT+=1
        BRUISES_ARRAY=[lost_count,_plus_2_lost_count,_plus_2_lost_tension,CHAINS_LOST_ALERT,CHAINS_LOST_COUNT,CHAINS_LOST_TENSION]
        print(f'BRUISES_ARRAY({TEAMname}) ---> {BRUISES_ARRAY}')
        return BRUISES_ARRAY
    print(f'BRUISES_ARRAY_CODE ---> [LC,+2LC,+2LCT,CHLA,CHLC,CHLCT]')
    def discreteLosesChecker(loses_rec):
        loses_10CentCount=0
        NONE_SCORES_ARR=[1,3,4]
        for lcn,lc in enumerate(loses_rec):
            try:
                if lcn not in NONE_SCORES_ARR:
                    loses_10CentCount+=lc
            except Exception:
                pass
        return loses_10CentCount
    home_total_scores_lost=scores_runner(home_last_two_scores_array,'HOME',1,1)
    home_total_scores_lost=discreteLosesChecker(home_total_scores_lost)
    away_total_scores_lost=scores_runner(away_last_two_scores_array,'AWAY',1,1)
    away_total_scores_lost=discreteLosesChecker(away_total_scores_lost)
    return [round(home_total_scores_lost),round(away_total_scores_lost)]
def lastScoresInfluence(home_last_scores,home_discrete_form_array,away_last_scores,away_discrete_form_array):
    home_last_scores_reversed=list(reversed(home_last_scores))
    away_last_scores_reversed=list(reversed(away_last_scores))
    d_data_home=0
    d_data_away=0
    def innerCentCalc(data_rr):
        h_data=data_rr[0]
        a_data=data_rr[1]
        QUICK_CENT3=quickCentCalc([h_data,a_data])
        h_cent=QUICK_CENT3[0]
        a_cent=QUICK_CENT3[1]
        return [h_cent,a_cent]
    #['ADW','AWD','WL','LW','CONSE','AFTER_CONSE_DRAW']
    for scssn,scssh in enumerate(home_last_scores_reversed):
        scssa=away_last_scores_reversed[scssn]
        hm_scr0_prev=scssh[0][0]
        aw_scr0_prev=scssh[0][1]
        hm_scr1_prev=scssa[0][0]
        aw_scr1_prev=scssa[0][1]
        for issn,issnh in enumerate(scssh):
            issna=scssa[issn]
            hm_scr0=issnh[0]
            aw_scr0=issnh[1]
            hm_scr1=issna[0]
            aw_scr1=issna[1]
            if issn>0:
               if hm_scr0_prev>aw_scr0_prev and hm_scr0>aw_scr0:
                  d_data_home+=home_discrete_form_array[4]
               else:
                    if hm_scr0_prev>aw_scr0_prev:
                       d_data_home+=home_discrete_form_array[2]
                    if hm_scr0_prev<aw_scr0_prev:
                       d_data_home+=home_discrete_form_array[3]
                    if hm_scr0_prev==aw_scr0_prev:
                       d_data_home+=home_discrete_form_array[0]
            if issn>0:
               if hm_scr1_prev>aw_scr1_prev and hm_scr1>aw_scr1:
                  d_data_away+=away_discrete_form_array[4]
               else:
                    if hm_scr1_prev>aw_scr1_prev:
                       d_data_away+=away_discrete_form_array[2]
                    if hm_scr1_prev<aw_scr1_prev:
                       d_data_away+=away_discrete_form_array[3]
                    if hm_scr1_prev==aw_scr1_prev:
                       d_data_away+=away_discrete_form_array[0]
            hm_scr0_prev=hm_scr0
            aw_scr0_prev=aw_scr0
            hm_scr1_prev=hm_scr1
            aw_scr1_prev=aw_scr1
    CURENT_CENT=innerCentCalc([d_data_home,d_data_away])
    return CURENT_CENT
def h2hAnalyers(h2h_scores_array):
    h2h_scores_array_reversed=list(reversed(h2h_scores_array))
    if len(h2h_scores_array_reversed)==0:
        h2h_scores_array_reversed=[(-1,-1)]
    def h2h_form(fused_data):
        prevh2h=fused_data[0]
        home_wins_count=0
        away_wins_count=0
        for fdn,fd in enumerate(fused_data):
            fdn_h=fdn+1
            if fdn_h>1 and fdn_h%2==0:
                if prevh2h>fd:
                   home_wins_count+=1
                if fd>prevh2h:
                   away_wins_count+=1
                if prevh2h==fd:
                    home_wins_count+=1
                    away_wins_count+=1
            prevh2h=fd
        QUICK_CENT4=quickCentCalc([home_wins_count,away_wins_count])
        h2h_discrete_form_home=QUICK_CENT4[0]
        h2h_discrete_form_away=QUICK_CENT4[1]
        return [h2h_discrete_form_home,h2h_discrete_form_away]
    def h2h_cent_inner(home_data_array,away_data_array):
        FUSED_DATA=[]
        for hcn, hce in enumerate(home_data_array):
            ace=away_data_array[hcn]
            hcent=0
            acent=0
            try:
                hcent=hce*10
                acent=ace*10
            except ZeroDivisionError:
                pass
            FUSED_DATA+=[hcent]
            FUSED_DATA+=[acent]
        return FUSED_DATA
    home_sc_prev=0
    away_sc_prev=0
    after_win_draws_count_home=0
    after_win_draws_count_away=0
    win_lost_count_home=0
    win_lost_count_away=0
    lost_win_count_home=0
    lost_win_count_away=0
    consecutive_wins_count_home=0
    consecutive_wins_count_away=0
    consecutive_count_home_prev=h2h_scores_array_reversed[0][0]
    consecutive_count_away_prev=h2h_scores_array_reversed[0][1]
    consecutive_count_home=0
    consecutive_count_away=0
    after_consecutive_wins_draws_count_home=0
    after_consecutive_wins_draws_count_away=0
    after_draw_score_home=0
    after_draw_score_away=0
    for cnn,criti in enumerate(h2h_scores_array_reversed):
        home_sc_cur=criti[0]
        away_sc_cur=criti[1]
        if home_sc_prev==away_sc_prev:
           if home_sc_cur>away_sc_cur:
              after_draw_score_home+=1
           if away_sc_cur>home_sc_cur:
              after_draw_score_away+=1
        if home_sc_cur==away_sc_cur:
            if home_sc_prev>away_sc_prev:
               after_win_draws_count_home+=1
            if away_sc_prev>home_sc_prev:
               after_win_draws_count_away+=1
        if home_sc_prev>away_sc_prev and away_sc_cur>home_sc_cur:
            win_lost_count_home+=1
        if away_sc_prev>home_sc_prev and home_sc_cur>away_sc_cur:
            win_lost_count_away+=1
        if home_sc_prev<away_sc_prev and home_sc_cur>away_sc_cur:
            lost_win_count_home+=1
        if away_sc_prev<home_sc_prev and away_sc_cur>home_sc_cur:
            lost_win_count_away+=1
        if home_sc_prev>away_sc_prev and home_sc_cur>away_sc_cur:
            consecutive_wins_count_home+=1
            consecutive_count_home+=1
        if away_sc_prev>home_sc_prev and away_sc_cur>home_sc_cur:
            consecutive_wins_count_away+=1
            consecutive_count_away+=1
        if consecutive_count_home>1 and consecutive_count_home_prev==consecutive_count_home:
           after_consecutive_wins_draws_count_home+=1
           consecutive_count_home_prev=0
           consecutive_count_home=0
        if consecutive_count_away>1 and consecutive_count_away_prev==consecutive_count_away:
           after_consecutive_wins_draws_count_away+=1
           consecutive_count_away=0
           consecutive_count_away_prev=0
        consecutive_count_home_prev=consecutive_count_home
        consecutive_count_away_prev=consecutive_count_away
        home_sc_prev=home_sc_cur
        away_sc_prev=away_sc_cur
    HOME_DATA_FOR_D_RECORD=[after_draw_score_home,after_win_draws_count_home,win_lost_count_home,lost_win_count_home,consecutive_wins_count_home,after_consecutive_wins_draws_count_home]
    AWAY_DATA_FOR_D_RECORD=[after_draw_score_away,after_win_draws_count_away,win_lost_count_away,lost_win_count_away,consecutive_wins_count_away,after_consecutive_wins_draws_count_away]
    H2HCENT_FUSE_DATA=h2h_cent_inner(HOME_DATA_FOR_D_RECORD,AWAY_DATA_FOR_D_RECORD)
    H2H_DISCRET_FORM=h2h_form(H2HCENT_FUSE_DATA)
    return [HOME_DATA_FOR_D_RECORD,AWAY_DATA_FOR_D_RECORD,H2HCENT_FUSE_DATA,['ADW','AWD','WL','LW','CONSE','AFTER_CONSE_DRAW'],H2H_DISCRET_FORM]
def GG_predictor(purelyH2H_Scores,scores_cent_arr_h2h,onlyHome_only_away_cent,HOME_WOUNDSS,AWAY_WOUNDSS,grand_form_array):
    purelyH2H_Scores_3_cut=purelyH2H_Scores[:2]
    homeall_lost=0
    homeall_lost_logic=False
    awayall_lost=0
    awayall_lost_logic=False
    HOME_G_FORM=grand_form_array[0]
    AWAY_G_FORM=grand_form_array[1]
    DRAW_G_FORM=grand_form_array[2]
    diffs=HOME_G_FORM-AWAY_G_FORM
    if diffs<0:
        diffs=-1*diffs
    form_av=min([HOME_G_FORM,AWAY_G_FORM])
    DRAW_AMBRE=(DRAW_G_FORM>=HOME_G_FORM and DRAW_G_FORM>=AWAY_G_FORM) or form_av<=0 or diffs<=10
    for s in purelyH2H_Scores_3_cut:
        hs=s[0]
        ass=s[1]
        if (hs-ass)<0:
            homeall_lost+=1
        if (ass-hs)<0:
            awayall_lost+=1
        if homeall_lost==2:
           homeall_lost_logic=True
        if awayall_lost==2:
           awayall_lost_logic=True
    purelyH2H_Scores_lascdf=0
    h2h_homeCent=scores_cent_arr_h2h[0]
    h2h_awayCent=scores_cent_arr_h2h[1]
    onlyHA_homeCent=onlyHome_only_away_cent[0]
    onlyHA_awayCent=onlyHome_only_away_cent[1]
    M1_H2H=min([h2h_homeCent,h2h_awayCent])
    M1_OHA=min([onlyHA_homeCent,onlyHA_awayCent])
    purelyH2H_Scores_len=len(purelyH2H_Scores)
    if purelyH2H_Scores_len>0:
       purelyH2H_Scores_lascdf=purelyH2H_Scores[0]
       purelyH2H_Scores_lascdf=purelyH2H_Scores_lascdf[0]-purelyH2H_Scores_lascdf[1]
    GG_CLOCKED=False
    if M1_H2H>=40 and M1_OHA>=40 and not DRAW_AMBRE:
        GG_CLOCKED=((purelyH2H_Scores_lascdf<0 or homeall_lost_logic) and HOME_WOUNDSS) or ((purelyH2H_Scores_lascdf>0 or awayall_lost_logic) and AWAY_WOUNDSS)
        if purelyH2H_Scores_lascdf==0:
           GG_CLOCKED=(AWAY_WOUNDSS and HOME_WOUNDSS and M1_H2H>=50 and M1_OHA>=50)
        if (homeall_lost_logic or awayall_lost_logic) and M1_H2H>=50 and M1_OHA>=50:
            GG_CLOCKED=True
    return GG_CLOCKED
def incrementOrDecrease(home_forms_array,away_forms_array):
    home_incre_count=0
    home_decre_count=0
    away_incre_count=0
    away_decre_count=0
    home_prev_form=home_forms_array[0]
    away_prev_form=away_forms_array[0]
    for hawn,haw in enumerate(home_forms_array):
        haw_h=hawn+1
        haw_away=away_forms_array[hawn]
        if haw_h>1 and haw_h%2==0:
            if haw>home_prev_form:
                hidf=c_abs(haw-home_prev_form)
                home_incre_count+=hidf
            if haw<home_prev_form:
                hddf=c_abs(haw-home_prev_form)
                home_decre_count+=hddf
            if haw_away>away_prev_form:
                aidf=c_abs(haw_away-away_prev_form)
                away_incre_count+=aidf
            if haw_away<away_prev_form:
                addf=c_abs(haw_away-away_prev_form)
                away_decre_count+=addf
        home_prev_form=haw
        away_prev_form=haw_away
    return [[home_incre_count,away_incre_count],[home_decre_count,away_decre_count]]
def lossCentCalc(scores_array_n):
    home_losses_count=0
    away_losses_count=0
    for scn in scores_array_n:
        h_scn=scn[0]
        a_scn=scn[1]
        sc_dff=h_scn-a_scn
        if sc_dff<0:
            sc_dff=-1*sc_dff
        if h_scn==a_scn:
           home_losses_count+=2
           away_losses_count+=2
        if h_scn<a_scn:
            home_losses_count+=sc_dff
        if a_scn<h_scn:
            away_losses_count+=sc_dff
    QUICK_CENT5=quickCentCalc([home_losses_count,away_losses_count])
    home_loss_cent=QUICK_CENT5[0]
    away_loss_cent=QUICK_CENT5[1]
    return [home_loss_cent,away_loss_cent]
def scoresCleaner(scores_colle,cutNum=0):
    SCORES_LOCAL=scores_colle
    SCORES_LOCAL_LEN=len(scores_colle)
    COMPROMISED_SCORES=[]
    indece_box_home=[]
    big_scrs_count_home=0
    indece_box_away=[]
    big_scrs_count_away=0
    for scn,sc in enumerate(scores_colle):
        hsc_scr=sc[0]
        asc_scr=sc[1]
        hsc_scr_asc_scr_dff=c_abs(hsc_scr-asc_scr)
        add_scores=sc
        if hsc_scr_asc_scr_dff>1:
           if hsc_scr>asc_scr:
               big_scrs_count_home+=1
               add_scores=(1+dec_form(hsc_scr),0)
           else:
               big_scrs_count_away+=1
               add_scores=(0,1+dec_form(asc_scr))
        COMPROMISED_SCORES+=[add_scores]
    big_scors_count_max=max([big_scrs_count_home,big_scrs_count_away])
    if big_scors_count_max>2:
       SCORES_LOCAL=scores_colle
    else:
        SCORES_LOCAL=COMPROMISED_SCORES
    if cutNum>0:
       SCORES_LOCAL=SCORES_LOCAL[:cutNum]
    return SCORES_LOCAL
def drawProjectorCent(WELL_ARRANGED_ARRAY_ARG):
    ARRAY_WAREHOUSE=WELL_ARRANGED_ARRAY_ARG
    ARRAY_WAREHOUSE_len=len(WELL_ARRANGED_ARRAY_ARG)
    less_than_10_count=0
    less_than_10_is_draw_cent=0
    home_win_cent=0
    away_win_cent=0
    home_wins_count=0
    away_wins_count=0
    home_grt_count=0
    away_grt_count=0
    ELE_TOTAL=0
    HOME_TOTAL_GRAND_FORM=0
    AWAY_TOTAL_GRAND_FORM=0
    HOME_DRAW_CATE_WINS_CENTS_SUM=0
    Home_draw_cate_wins_count=0
    AWAY_DRAW_CATE_WINS_CENTS_SUM=0
    Away_draw_cate_wins_count=0
    for awh in ARRAY_WAREHOUSE:
        try:
            eprev=awh[0]
            for ecn, ece in enumerate(awh):
                ecn_h=ecn+1
                if ecn_h>1 and ecn_h%2==0:
                    ele_1=eprev
                    ele_2=ece
                    ele_diff=c_abs(ele_1-ele_2)
                    ele_1_compro=dec_form(ele_1)
                    ele_2_compro=dec_form(ele_2)
                    ele_diff_compro=dec_form(ele_diff)
                    if ele_diff>20:
                       ele_1=ele_1_compro
                       ele_2=ele_2_compro
                       ele_diff=ele_diff_compro
                    HOME_TOTAL_GRAND_FORM+=ele_1
                    AWAY_TOTAL_GRAND_FORM+=ele_2
                    if ele_1>=ele_2:
                       home_grt_count+=1
                    if ele_2>=ele_1:
                       away_grt_count+=1
                    if ele_diff<15:
                        less_than_10_count+=1
                        if ele_1>=ele_2:
                           HOME_DRAW_CATE_WINS_CENTS_SUM+=ele_diff
                           Home_draw_cate_wins_count+=1
                        if ele_2>=ele_1:
                           AWAY_DRAW_CATE_WINS_CENTS_SUM+=ele_diff
                           Away_draw_cate_wins_count+=1
                    else:
                        if ele_1>=ele_2:
                            home_wins_count+=ele_diff
                        if ele_2>=ele_1:
                            away_wins_count+=ele_diff
                eprev=ece
        except IndexError:
            pass
    try:
        count_cent=[home_grt_count,away_grt_count]
        home_wins_count=home_wins_count+count_cent[0]
        away_wins_count=away_wins_count+count_cent[1]
        GRAND_CENT_2=quickCentCalc([home_wins_count,away_wins_count])
        home_win_cent=GRAND_CENT_2[0]
        away_win_cent=GRAND_CENT_2[1]
    except ZeroDivisionError:
        pass

    try:
        less_than_10_is_draw_cent=round((less_than_10_count/ARRAY_WAREHOUSE_len)*100)
    except ZeroDivisionError:
        pass
    DRAND_FORM_SUM=quickCentCalc([HOME_TOTAL_GRAND_FORM,AWAY_TOTAL_GRAND_FORM])
    HOME_TOTAL_GRAND_FORM=DRAND_FORM_SUM[0]
    AWAY_TOTAL_GRAND_FORM=DRAND_FORM_SUM[1]
    HOME_DRAW_CATE_WINS_CENTS_SUM=round(HOME_DRAW_CATE_WINS_CENTS_SUM)
    AWAY_DRAW_CATE_WINS_CENTS_SUM=round(AWAY_DRAW_CATE_WINS_CENTS_SUM)
    return [home_win_cent,away_win_cent,less_than_10_is_draw_cent,[home_grt_count,away_grt_count],[HOME_TOTAL_GRAND_FORM,AWAY_TOTAL_GRAND_FORM],[HOME_DRAW_CATE_WINS_CENTS_SUM,Home_draw_cate_wins_count],[AWAY_DRAW_CATE_WINS_CENTS_SUM,Away_draw_cate_wins_count]]
def TeamWinsTruly(home_away_cent_array,
                  home_away_cent_array_5_cut,
                  h2h_older_array,
                  h2h_newer_array,
                  home_away_lost_games_array,
                  home_away_last_games_score_array,
                  only_home_only_away_last_scores_array,
                  HOME_AWAY_GRAND_DIFF_ARRAY,
                  HOME_TEAM_TRANSITION_arg,
                  AWAY_TEAM_TRANSITION_arg,
                  same_teams_cent_array_ARG,
                  CENTS_ARRAY_ARG,
                  home_away_dnt_wins_all_logic_array,
                  all_scores_home_away_cnet_array):
    def formSize(cent_arr,h2h_home_away_cent,same_teams_cent_array):
        same_teams_cent_HOME=same_teams_cent_array[0]
        same_teams_cent_AWAY=same_teams_cent_array[1]
        home_cent_HA=h2h_home_away_cent[0]
        away_cent_HA=h2h_home_away_cent[1]
        home_cent=cent_arr[0]+home_cent_HA+same_teams_cent_HOME
        away_cent=cent_arr[1]+away_cent_HA+same_teams_cent_AWAY
        deci_home=-1
        deci_away=-1
        deci_home_HA=-1
        deci_away_HA=-1
        try:
            deci_home=round((home_cent/away_cent),2)
        except ZeroDivisionError:
            pass
        try:
            deci_away=round((away_cent/home_cent),2)
        except ZeroDivisionError:
            pass
        return [deci_home,deci_away]
    home_dnt_wins_all_logic_arg_local=home_away_dnt_wins_all_logic_array[0]
    away_dnt_wins_all_logic_arg_local=home_away_dnt_wins_all_logic_array[1]
    home_all_scs_cent=all_scores_home_away_cnet_array[0]
    away_all_scs_cent=all_scores_home_away_cnet_array[1]
    home_away_all_scores_cent_diff=home_all_scs_cent-away_all_scs_cent
    if home_away_all_scores_cent_diff<0:
        home_away_all_scores_cent_diff=-1*home_away_all_scores_cent_diff
    HOME_FORM=CENTS_ARRAY_ARG[0]
    AWAY_FORM=CENTS_ARRAY_ARG[1]
    DRAW_FORM=CENTS_ARRAY_ARG[2]
    HOME_FORM_AWAY_FORM_DIFF=HOME_FORM-AWAY_FORM
    if HOME_FORM_AWAY_FORM_DIFF<0:
        HOME_FORM_AWAY_FORM_DIFF=-1*HOME_FORM_AWAY_FORM_DIFF
    only_home_last_scrs=only_home_only_away_last_scores_array[0]
    only_home_last_scrs_diff=only_home_last_scrs[0]-only_home_last_scrs[1]
    only_away_last_scrs=only_home_only_away_last_scores_array[1]
    only_away_last_scrs_diff=only_away_last_scrs[0]-only_away_last_scrs[1]
    home_tran_h2h=HOME_TEAM_TRANSITION_arg[0]
    home_tran_omtc=HOME_TEAM_TRANSITION_arg[1]
    away_tran_h2h=AWAY_TEAM_TRANSITION_arg[0]
    away_tran_omtc=AWAY_TEAM_TRANSITION_arg[1]
    BIG_DECI=formSize(home_away_cent_array,h2h_older_array,same_teams_cent_array_ARG)
    BIG_DECI_HOME=BIG_DECI[0]
    BIG_DECI_AWAY=BIG_DECI[1]
    BIG_DECI_DIFF=round(BIG_DECI_HOME-BIG_DECI_AWAY)
    if BIG_DECI_DIFF<0:
        BIG_DECI_DIFF=-1*BIG_DECI_DIFF
    HOME_GRAND_DIFF_MIN=HOME_AWAY_GRAND_DIFF_ARRAY[0]
    AWAY_GRAND_DIFF_MIN=HOME_AWAY_GRAND_DIFF_ARRAY[1]
    only_home_old_form=home_away_cent_array[0]
    only_away_old_form=home_away_cent_array[1]
    only_home_away_old_form_diff=only_home_old_form-only_away_old_form
    if only_home_away_old_form_diff<0:
        only_home_away_old_form_diff=-1*only_home_away_old_form_diff
    only_home_new_form=home_away_cent_array_5_cut[0]
    only_away_new_form=home_away_cent_array_5_cut[1]
    only_home_away_new_form_diff=only_home_new_form-only_away_new_form
    if only_home_away_new_form_diff<0:
        only_home_away_new_form_diff=-1*only_home_away_new_form_diff
    home_h2h_old_form=h2h_older_array[0]
    away_h2h_old_form=h2h_older_array[1]
    home_away_h2h_old_form_diff=home_h2h_old_form-away_h2h_old_form
    if home_away_h2h_old_form_diff<0:
        home_away_h2h_old_form_diff=-1*home_away_h2h_old_form_diff
    DRAW_STRIKED=home_away_all_scores_cent_diff<=15 or only_home_away_old_form_diff<=15 or BIG_DECI_DIFF<=1 or home_away_h2h_old_form_diff<=15 or HOME_FORM_AWAY_FORM_DIFF<=15 or (DRAW_FORM>=HOME_FORM and DRAW_FORM>=AWAY_FORM)

    home_h2h_new_form=h2h_newer_array[0]
    away_h2h_new_form=h2h_newer_array[1]
    away_h2h_new_form_diff=home_h2h_new_form-away_h2h_new_form

    home_games_lost=home_away_lost_games_array[0]
    away_games_lost=home_away_lost_games_array[1]
    DANGEROUS_HOME=only_home_new_form>only_home_old_form and only_home_away_new_form_diff<=15 and home_games_lost>away_games_lost
    DANGEROUS_AWAY=only_away_new_form>only_away_old_form and only_home_away_new_form_diff<=15 and away_games_lost>home_games_lost
    print(f'[DANGEROUS_HOME,DANGEROUS_AWAY] ---> {[DANGEROUS_HOME,DANGEROUS_AWAY]}')
    home_away_games_lost_diff=home_games_lost-away_games_lost

    home_last_game_score_diff=home_away_last_games_score_array[0]
    home_last_game_score_diff=home_last_game_score_diff[0]-home_last_game_score_diff[1]
    home_last_games_lost_diff_min=min([only_home_last_scrs_diff,home_last_game_score_diff])

    away_last_game_score_diff=home_away_last_games_score_array[1]
    away_last_game_score_diff=away_last_game_score_diff[0]-away_last_game_score_diff[1]
    away_last_games_lost_diff_min=min([only_away_last_scrs_diff,away_last_game_score_diff])
    HOME_DEFEAT_NOT_PREDICTABLE=DRAW_STRIKED and (away_last_games_lost_diff_min<=-2 or home_away_games_lost_diff<=-3 or home_tran_omtc>away_tran_omtc)
    AWAY_DEFEAT_NOT_PREDICTABLE=DRAW_STRIKED and (home_last_games_lost_diff_min<=-2 or home_away_games_lost_diff>=3 or away_tran_omtc>home_tran_omtc)

    HOME_WINS_RECORD=not DANGEROUS_AWAY and home_h2h_old_form>=away_h2h_old_form and HOME_FORM>AWAY_FORM and HOME_FORM>DRAW_FORM and home_tran_h2h>=away_tran_h2h and away_tran_omtc<20 and BIG_DECI_HOME>BIG_DECI_AWAY and only_home_old_form>only_away_old_form and only_home_new_form>only_away_new_form 
    AWAY_WINS_RECORD=not DANGEROUS_HOME and away_h2h_old_form>=home_h2h_old_form and AWAY_FORM>HOME_FORM and AWAY_FORM>DRAW_FORM and away_tran_h2h>=home_tran_h2h and home_tran_omtc<20 and BIG_DECI_AWAY>BIG_DECI_HOME and only_away_old_form>only_home_old_form and only_away_new_form>only_home_new_form 
    HOME_WINS_TRULY=False
    AWAY_WINS_TRULY=False
    if HOME_WINS_RECORD and only_home_old_form>=40 and only_home_new_form>=40:
        if not HOME_DEFEAT_NOT_PREDICTABLE and home_dnt_wins_all_logic_arg_local:
            HOME_WINS_TRULY=True
    if AWAY_WINS_RECORD and only_away_old_form>=40 and only_away_new_form>=40:
        if not AWAY_DEFEAT_NOT_PREDICTABLE and away_dnt_wins_all_logic_arg_local:
            AWAY_WINS_TRULY=True
    return [HOME_WINS_TRULY,AWAY_WINS_TRULY,BIG_DECI,DRAW_STRIKED,HOME_DEFEAT_NOT_PREDICTABLE,AWAY_DEFEAT_NOT_PREDICTABLE]
def forebetHomePageUrlHunter(homePageDOM):
    matches_div=re.findall(r'tnmscn.+?</a>',homePageDOM)
    clean_url_array=[]
    for d in matches_div:
        match_url=re.findall(r'href.+?\>',d)
        date_bah=re.findall(r'date_bah.+?</time>',d)
        formed_date=[]
        for dt in date_bah:
          clean_dt=re.findall(r'\d+',dt)
          for cd in clean_dt:
            formed_date+=[cd]
        try:
            www_forebet="https://www.forebet.com/en/"
            found_url=match_url[0]
            found_url=re.findall(r'football/matches/.+',found_url)
            found_url=found_url[0]
            for drt in ['">',"'>"]:
                found_url=found_url.replace(drt,'').strip()
            match_url_clean=f'{www_forebet}{found_url}'#match_url[0].strip().replace('href="',www_forebet)
            CURRENT_DAY_FOREBET=int(formed_date[0])
            CURRENT_MONTH_FOREBET=int(formed_date[1])
            CURRENT_YEAR_RAW_FOREBET=int(formed_date[2])
            TODAYS_DATE_STRING_FOREBET=f'{CURRENT_DAY_FOREBET}{CURRENT_MONTH_FOREBET}{CURRENT_YEAR_RAW_FOREBET}'
            MATCH_MIN_INT=int(formed_date[4])
            MATCH_HOUR_INT=int(formed_date[3])
            HOUR_INTERVAL=(MATCH_HOUR_INT-CURRENT_TIME_HOUR_HUNT)*60
            MATCH_START_TIME_INTERVAL=(MATCH_MIN_INT-CURRENT_TIME_MIN_HUNT)+HOUR_INTERVAL
            MATCH_START_TIME_INTERVAL_FLAG=MATCH_START_TIME_INTERVAL>=30
            TIME_UPDATE=1
            if TIME_UPDATE==1 and TODAYS_DATE_STRING_FOREBET==TODAYS_DATE_STRING:
                if ((MATCH_HOUR_INT>=CURRENT_TIME_HOUR_HUNT and MATCH_MIN_INT>=CURRENT_TIME_MIN_HUNT) or MATCH_HOUR_INT>CURRENT_TIME_HOUR_HUNT) and MATCH_START_TIME_INTERVAL_FLAG:
                    clean_url_array+=[[match_url_clean,formed_date]]
            elif TODAYS_DATE_STRING_FOREBET==TODAYS_DATE_STRING:
                clean_url_array+=[[match_url_clean,formed_date]]
        except IndexError:
            pass
    return clean_url_array
def forebetMatchesUrls():
  curl=[]
  with open('forebetHTML.html','r', encoding="utf8") as fbthtml:
    fbthtml_bytes=fbthtml.read().replace('\n','')
    curl=forebetHomePageUrlHunter(fbthtml_bytes)
    fbthtml.close()
  return curl
def googleHrefFetcher(url,TITTLE_ARRAY):
    global google_recursion_count
    HOME_NAME=TITTLE_ARRAY[0]
    AWAY_NAME=TITTLE_ARRAY[1]
    used_url=FOREBET_HOME_PAGE_URL
    try:
      element=''
      content_c = ''
      if API_SWITCH==0:
         #element=requests.get(url)
         content_c=googleSearchResults(url)
      else:
        content_c=scraperApi(used_url)
      _url=''
      KEY=r'href=".+?"'
      #print(f'content_c ---> {content_c}')
      #print()
      try:
        keyfound=re.findall(KEY,content_c)
        keyfound_len=len(keyfound)
        try:
          for kn in range(keyfound_len):
            k=keyfound[kn]
            dynamic_hit=re.findall(r'https.+www.+forebet.+com.+en.+football.+matches.+?&',k)
            dynamic_hit_len=len(dynamic_hit)
            if dynamic_hit_len>0:
                _url=dynamic_hit[0].replace("&",'')
                dynamic_hit_split=_url.split('https')
                dynamic_hit_split_len=len(dynamic_hit_split)-1
                _url=dynamic_hit_split[dynamic_hit_split_len].strip()
                _url=f'https{_url}'
                break
        except IndexError as er:
            error_printer(f"er ----> {er}",content_c)
        return _url
      except IndexError as er1:
          error_printer(f"er1 ----> {er1}",content_c)
    except Exception as connection_timeout:
           error_printer(f"ERROR_CONNECTION_TIMEOUT--->{connection_timeout}",content_c)
           if google_recursion_count<=1:
            google_recursion_count+=1
            googleHrefFetcher(url,TITTLE_ARRAY)
def win_loss_cent(team_scrs_array,cutNum0=0,cent_indentity=0):
    global OLD_ALL_SCORES_DRITY_SEEKER
    team_scrs_array_local=scoresCleaner(team_scrs_array,cutNum0)
    LATEST_DEFENCE_CENT=0
    LATEST_STRIKE_CENT=0
    home_wins_draws_all_len_count=0
    home_wins_draws_all_len_count_num=0
    home_wins_draws_cut_len_count=0
    home_wins_draws_cut_len_count_num=0
    team_scrs_len=len(team_scrs_array_local)
    team_scrs_len_lost_by_1_old=team_scrs_len
    team_scrs_len_0_6=round(0.6*team_scrs_len)
    seeker_len_abs_diff=abs(team_scrs_len-OLD_ALL_SCORES_DRITY_SEEKER)
    seeker_len_abs_diff_old=abs(team_scrs_len-team_scrs_len_0_6)
    arget_team_centhome=0
    target_team_centAway=0
    winnings_count_target_team=0
    winnings_count_opo_team=0
    home_sum_w=0
    away_sum_w=0
    draws_count=0
    home_lost_by_1_count=0
    home_lost_by_1_count_old=0
    for srn,sr in enumerate(team_scrs_array_local):
      srn_human=srn+1
      home_raw_score=team_scrs_array[srn][0]
      away_raw_score=team_scrs_array[srn][1]
      draws_count_incre=1
      home_lost_by_1_count_incre=1
      hm=sr[0]
      home_sum_w+=hm
      aw=sr[1]
      away_sum_w+=aw
      dfw=hm-aw
      raw_scores_diff=c_abs(home_raw_score-away_raw_score)
      df_abs=c_abs(hm-aw)
      if cent_indentity>0 and srn_human<=OLD_ALL_SCORES_DRITY_SEEKER and team_scrs_len>OLD_ALL_SCORES_DRITY_SEEKER and seeker_len_abs_diff>=5:
        draws_count_incre=0
        hm=0
        aw=0
        df_abs=0
      _0_0= hm==0 and aw==0
      if _0_0 or dfw==-1 or dfw==1:
         draws_count+=draws_count_incre
      if hm==aw:
        winnings_count_target_team+=hm
      if hm>aw:
        winnings_count_target_team+=df_abs
      if aw==hm:
        winnings_count_opo_team+=aw
      if aw>hm:
        winnings_count_opo_team+=df_abs
      if home_raw_score>=away_raw_score:
         home_wins_draws_all_len_count+=1
      if cent_indentity>0 and srn_human<=team_scrs_len_0_6 and team_scrs_len>OLD_ALL_SCORES_DRITY_SEEKER and seeker_len_abs_diff_old>=5:
         home_lost_by_1_count_incre=0
         team_scrs_len_lost_by_1_old=team_scrs_len-team_scrs_len_0_6
      if raw_scores_diff<=1 and home_raw_score<=1:
         home_lost_by_1_count+=1
         home_lost_by_1_count_old+=home_lost_by_1_count_incre
      if srn_human<=team_scrs_len_0_6:
        if home_raw_score>=2:
            LATEST_STRIKE_CENT+=1
        if raw_scores_diff<=1 and home_raw_score<=1:
            LATEST_DEFENCE_CENT+=1
        if home_raw_score>=away_raw_score:
            home_wins_draws_cut_len_count+=1
    winnings_count_target_team=winnings_count_target_team+round((draws_count/2))
    winnings_count_opo_team=winnings_count_opo_team+round((draws_count/2))
    GRAND_CENT=quickCentCalc([winnings_count_target_team,winnings_count_opo_team])
    LBOCCNT=0
    LBOCCNT_OLD=0
    try:
        LBOCCNT=round((home_lost_by_1_count/team_scrs_len)*100)
    except ZeroDivisionError:
        pass
    try:
        LBOCCNT_OLD=round((home_lost_by_1_count_old/team_scrs_len_lost_by_1_old)*100)
    except ZeroDivisionError:
        pass
    try:
        LATEST_STRIKE_CENT=round((LATEST_STRIKE_CENT/team_scrs_len_0_6)*100)
    except ZeroDivisionError:
        pass
    try:
        LATEST_DEFENCE_CENT=round((LATEST_DEFENCE_CENT/team_scrs_len_0_6)*100)
    except ZeroDivisionError:
        pass
    home_wins_draws_all_len_count_num=home_wins_draws_all_len_count
    home_wins_draws_cut_len_count_num=home_wins_draws_cut_len_count
    try:
        home_wins_draws_all_len_count=round((home_wins_draws_all_len_count/team_scrs_len)*100)
    except ZeroDivisionError:
        pass
    try:
        home_wins_draws_cut_len_count=round((home_wins_draws_cut_len_count/team_scrs_len_0_6)*100)
    except ZeroDivisionError:
        pass
    arget_team_centhome=GRAND_CENT[0]
    target_team_centAway=GRAND_CENT[1]
    trans_truly=-1*(home_wins_draws_all_len_count-home_wins_draws_cut_len_count)
    GEN_RETURN_VAL=[arget_team_centhome,target_team_centAway,LBOCCNT,[LATEST_STRIKE_CENT,LATEST_DEFENCE_CENT],[home_wins_draws_all_len_count,home_wins_draws_cut_len_count,[home_wins_draws_all_len_count_num,home_wins_draws_cut_len_count_num],trans_truly],LBOCCNT_OLD]
    return GEN_RETURN_VAL
def monthsChopper(months_arg):
    month='month'
    age=''
    if months_arg==12:
       age=f'1yr'
    if months_arg>12:
       op1=int(f'{months_arg/12}'.split('.')[0])
       op2=12*op1
       op3=months_arg-op2
       if op1==1:
          if op3>1:
             month='months'
          age=f'{op1}yr {op3}{month}'
       if op1>1:
          if op3>1:
             month='months'
          if op3==0:
             month=''
          age=f'{op1}yrs {op3}{month}'
    if months_arg<12:
         if months_arg>1:
              month='months'
         age=f'{months_arg}{month}'
    return age
def datePatternCorrector(raw_date):
    returned_date=raw_date
    day=raw_date[1]
    month=raw_date[0]
    year=raw_date[2]
    if month>12:
       returned_date=[day,month,year]
    return returned_date
def h2hage(h2h_dates_arr,home_dates_arr,away_dates_arr,HOME_or_AWAY):
        H2H_OLDER_0=False
        h2h_day=h2h_dates_arr[1]
        h2h_month=h2h_dates_arr[0]
        h2h_yr=h2h_dates_arr[2]

        home_match_day=home_dates_arr[1]
        home_match_month=home_dates_arr[0]
        home_match_yr=home_dates_arr[2]

        away_match_day=away_dates_arr[1]
        away_match_month=away_dates_arr[0]
        away_match_yr=away_dates_arr[2]

        homeH2HDayDiff=h2h_day-home_match_day
        homeH2HmonthDiff=h2h_month-home_match_month
        homeH2HyearDiff=h2h_yr-home_match_yr

        awayH2HDayDiff=h2h_day-away_match_day
        awayH2HmonthDiff=h2h_month-away_match_month
        awayH2HyearDiff=h2h_yr-away_match_yr
        def innerAge(day_diff,month_diff,yr_diff,team_match_month,cyr,team='HOME'):
            age_comment=''
            def accurateMonths(incre=1):
                  curent_yr=cyr
                  month_total=h2h_month
                  team_match_month_arg=team_match_month
                  h2h_yr_local=h2h_yr
                  if incre!=1:
                     curent_yr=h2h_yr
                     month_total=team_match_month
                     team_match_month_arg=h2h_month
                     h2h_yr_local=cyr
                  month_interval=0
                  while h2h_yr_local!=curent_yr:
                       month_total+=1
                       month_interval+=1
                       if month_total==13:
                          h2h_yr_local+=1
                          month_total=0
                          month_interval-=1
                  month_interval=month_interval+team_match_month_arg
                  return month_interval

            if yr_diff==0:
               if month_diff==0:
                  if day_diff==0:
                      age_comment=f'{team} h2h match SAME DAY[{day_diff}day(s)]'
                  if day_diff<0:
                     days_old=-1*day_diff
                     age_comment=f'{team} h2h match OLDER[{days_old}day(s)]'
                     H2H_OLDER_0=True
                  if day_diff>0:
                     age_comment=f'{team} h2h match YOUNGER[{day_diff}day(s)]'
               if month_diff<0:
                  month_old=-1*month_diff
                  age_comment=f'{team} h2h match OLDER[{month_old}month(s)]'
                  H2H_OLDER_0=True
               if month_diff>0:
                  age_comment=f'{team} h2h match YOUNGER[{month_diff}month(s)]'
            if yr_diff<0:
               yr_old=monthsChopper(accurateMonths())
               age_comment=f'{team} h2h match OLDER[{yr_old}]'
               H2H_OLDER_0=True
            if yr_diff>0:
               yr_old2=monthsChopper(accurateMonths(0))
               age_comment=f'{team} h2h match YOUNGER[{yr_old2}]'
            return age_comment
        homeTm=f'HOME'
        awayTm=f'AWAY'
        HomeMatchAge=innerAge(homeH2HDayDiff,homeH2HmonthDiff,homeH2HyearDiff,
                              home_match_month,home_match_yr,homeTm)
        AwayMatchAge=innerAge(awayH2HDayDiff,awayH2HmonthDiff,awayH2HyearDiff,
                              away_match_month,away_match_yr,awayTm)
        return [HomeMatchAge,AwayMatchAge,H2H_OLDER_0]
def matchesDatesHandler(dates_arr,HOME_TEAM,AWAY_TEAM):
   h2h_date=dates_arr[0]
   h2h_date_day=h2h_date[0]
   h2h_date_month=h2h_date[1]
   h2h_date_year=h2h_date[2] 

   HomeMatchesDates=dates_arr[1]
   HomeMatchesDates_day=HomeMatchesDates[0]
   HomeMatchesDates_month=HomeMatchesDates[1]
   HomeMatchesDates_year=HomeMatchesDates[2]

   AwayMatchesDates=dates_arr[2]
   AwayMatchesDates_day=AwayMatchesDates[0]
   AwayMatchesDates_month=AwayMatchesDates[1]
   AwayMatchesDates_year=AwayMatchesDates[2]

   awayH2H_OTHER_M_AGE=''
   H2H_OLDER=False
   h2h_last_date=[h2h_date_day,h2h_date_month,h2h_date_year]
   otherMts_Last_dateHome=[HomeMatchesDates_day,HomeMatchesDates_month,HomeMatchesDates_year]
   otherMts_Last_dateAway=[AwayMatchesDates_day,AwayMatchesDates_month,AwayMatchesDates_year]
   H_A=[HOME_TEAM,AWAY_TEAM]
   GRAND_AGE_DATA=h2hage(datePatternCorrector(h2h_last_date),datePatternCorrector(otherMts_Last_dateHome),datePatternCorrector(otherMts_Last_dateAway),H_A)
   homeH2H_OTHER_M_AGE=GRAND_AGE_DATA[0]
   awayH2H_OTHER_M_AGE=GRAND_AGE_DATA[1]
   H2H_OLDER=GRAND_AGE_DATA[2]
   return [homeH2H_OTHER_M_AGE,H2H_OLDER,awayH2H_OTHER_M_AGE]
def modalVal(array):
    array_max=max(array)+1
    goals_list=[]
    modal_value=[]
    for rm in range(array_max):
        goals_list+=[rm]
        ele_count=array.count(rm)
        modal_value+=[ele_count]
    max_modal_value=max(modal_value)
    max_mv_index=modal_value.index(max_modal_value)
    modal_goal=goals_list[max_mv_index]
    return modal_goal
def drawKong(arr):
        ALL_PO_ARR=[]
        arr_str=f'{arr}'
        nums=re.findall(r'\d+|-\d+',arr_str)
        nums_int=[int(ni) for ni in nums]
        nums_int_posi=[]
        for p in nums_int:
              inptp=p
              if p<0:
                 inptp=-1*p
              nums_int_posi+=[inptp]
        RECENT_FORMS=[nums_int_posi[1],nums_int_posi[3],nums_int_posi[5],nums_int_posi[7]]
        RECENT_FORMS_max_min=min(RECENT_FORMS)
        RECENT_FORMS_max=max(RECENT_FORMS)
        for r in nums_int:
            r_used=r
            if r<0:
               r_used=-1*r
            ALL_PO_ARR+=[r_used]
        pos_min=min(ALL_PO_ARR)
        pos_max=max(ALL_PO_ARR)
        pos_min_max_diff=pos_max-pos_min
        return [RECENT_FORMS_max_min,RECENT_FORMS_max,pos_min_max_diff]

def subAnalyser(GRAND_HOME_DIFF_arg,
                GRAND_AWAY_DIFF_arg,
                wins_loss_cont,
                PlayersSatsHome,
                PlayersSatsAway,
                Susp_Injured_Players_Home,
                Susp_Injured_Players_Away,
                home_last_scoresDiff,
                away_last_scoresDiff,
                HOME_or_AWAY):
    HOME_TEAM=HOME_or_AWAY[0]
    AWAY_TEAM=HOME_or_AWAY[1]
    def min_last_scores(rr):
        total_min_score=0
        for ms in rr:
            if ms<0:
               total_min_score+=ms
        return total_min_score
    home_last_scoresDiffMIN=min_last_scores(home_last_scoresDiff)
    away_last_scoresDiffMIN=min_last_scores(away_last_scoresDiff)
    lasth2hHome=home_last_scoresDiff[0]
    lasth2hAway=away_last_scoresDiff[0]
    mins=min([lasth2hHome,lasth2hAway])
    home_old_form=GRAND_HOME_DIFF_arg[1]
    home_new_form=GRAND_HOME_DIFF_arg[3]
    away_old_form=GRAND_AWAY_DIFF_arg[1]
    away_new_form=GRAND_AWAY_DIFF_arg[3]
    home_wins0=wins_loss_cont[0]
    away_wins0=wins_loss_cont[1]
    home_total_goals=PlayersSatsHome[0]
    away_total_goals=PlayersSatsAway[0]
    Homestrickers_out_goals=0
    Awaystrickers_out_goals=0
    HomeNonstrickers_plus5games_out=0
    AwayNonstrickers_plus5games_out=0
    def quickie(HAStrikers,flg='strikers'):
          total_goals_nonStrikers=0
          NON_STRIKERS=[]
          STRIKERS_OUT=[]
          for r in HAStrikers:
            g_t=re.findall(r'\d+',r)
            g_t_int=[int(gti) for gti in g_t]
            NON_STRIKERS=g_t_int
            try:
                sout=g_t_int[0]
                total_goals_nonStrikers+=sout
                STRIKERS_OUT+=[sout]
            except IndexError:
                pass
          if flg!='strikers':
            total_goals_nonStrikers=0
            for nst in NON_STRIKERS:
                if nst>=5:
                    total_goals_nonStrikers+=1
          return [total_goals_nonStrikers,STRIKERS_OUT]
    noNewLineHome=Susp_Injured_Players_Home.replace('\n','')
    noNewLineAway=Susp_Injured_Players_Away.replace('\n','')
    Homestrickers_out=re.findall(r'\(\d+,\d+.+?\)',noNewLineHome)
    Awaystrickers_out=re.findall(r'\(\d+,\d+.+?\)',noNewLineAway)
    Homestrickers_out_goals=quickie(Homestrickers_out)
    Awaystrickers_out_goals=quickie(Awaystrickers_out)
    Homestrickers_out_goals_array=Homestrickers_out_goals[1]
    Awaystrickers_out_goals_array=Awaystrickers_out_goals[1]
    Homestrickers_out_goals=Homestrickers_out_goals[0]
    Awaystrickers_out_goals=Awaystrickers_out_goals[0]
    HomeNonstrickers_out=re.findall(r'\(\W\).+?\d+',noNewLineHome)
    AwayNonstrickers_out=re.findall(r'\(\W\).+?\d+',noNewLineAway)
    HomeNonstrickers_plus5games_out=quickie(HomeNonstrickers_out,0)[0]
    AwayNonstrickers_plus5games_out=quickie(AwayNonstrickers_out,0)[0]
    MyPrediction='Unpredictable'
    def netGoalsCent(total_goals_arr,missingStrikers_total_goals_arr):
        print(total_goals_arr,missingStrikers_total_goals_arr)
        HomenetGoal=total_goals_arr[0]-missingStrikers_total_goals_arr[0]
        AwaynetGoal=total_goals_arr[1]-missingStrikers_total_goals_arr[1]
        grandGoals=HomenetGoal+AwaynetGoal
        print([HomenetGoal,AwaynetGoal,grandGoals])
        QUICK_CENT6=quickCentCalc([HomenetGoal,AwaynetGoal])
        home_cent=QUICK_CENT6[0]
        away_cent=QUICK_CENT6[1]
        return [home_cent,away_cent,HomenetGoal,AwaynetGoal]
    HA_CENT=netGoalsCent([home_total_goals,away_total_goals],[Homestrickers_out_goals,Awaystrickers_out_goals])
    guage2=40
    HomeNetGoalCent=HA_CENT[0]
    HomeNetGoal=HA_CENT[2]
    AwayNetGoalCent=HA_CENT[1]
    AwayNetGoal=HA_CENT[3]
    return [MyPrediction,
            HomeNonstrickers_plus5games_out,
            AwayNonstrickers_plus5games_out,
            HomeNetGoalCent,
            AwayNetGoalCent,HomeNetGoal,AwayNetGoal,
            Homestrickers_out_goals_array,
            Awaystrickers_out_goals_array]

def homeOrAwayPredictor(r1_arg,r2_arg,next_matches,
                        home_or_away_box,
                        last_scores_array,
                        team_points_arr,GRAND_HOME_STATS_LOCAL_arg,
                        GRAND_AWAY_STATS_LOCAL_arg,returned):
        min_scrs_home=min(last_scores_array[0])
        min_scrs_away=min(last_scores_array[1])
        home_point_diff=team_points_arr[0]-team_points_arr[1]
        away_point_diff=-1*home_point_diff
        next_matches_min=min(next_matches)
        homeTeamName=home_or_away_box[0]
        awayTeamName=home_or_away_box[1]
        HOME_AWAY_WINS_DIC={'TrueH':[],'TrueA':[]}
        def wins_filler(status,h_or_a):
              try:
                status_key=f'{status}{h_or_a}'
                HOME_AWAY_WINS_DIC_VAL=HOME_AWAY_WINS_DIC[status_key]
                HOME_AWAY_WINS_DIC_VAL+=[h_or_a]
              except KeyError:
                     pass
        Hh2h_old=r1_arg[0][0]
        Ah2h_old=r2_arg[0][0]
        HOME_WON=Hh2h_old>Ah2h_old
        wins_filler(HOME_WON,'H')
        AWAY_WON=Ah2h_old>Hh2h_old
        wins_filler(AWAY_WON,'A')
        HOME_WON=Hh2h_old==Ah2h_old
        wins_filler(HOME_WON,'H')
        AWAY_WON=Ah2h_old==Hh2h_old
        wins_filler(AWAY_WON,'A')
        OldH2HDiffHome=Hh2h_old-Ah2h_old
        OldH2HDiffAway=-1*OldH2HDiffHome
        HOmtchs_old=r1_arg[0][1]
        AOmtchs_old=r2_arg[0][1]
        HOME_WON=HOmtchs_old>AOmtchs_old
        wins_filler(HOME_WON,'H')
        AWAY_WON=AOmtchs_old>HOmtchs_old
        wins_filler(AWAY_WON,'A')
        HOME_WON=HOmtchs_old==AOmtchs_old
        wins_filler(HOME_WON,'H')
        AWAY_WON=AOmtchs_old==HOmtchs_old
        wins_filler(AWAY_WON,'A')
        OldOtherMatchesDiffHome=HOmtchs_old-AOmtchs_old
        OldOtherMatchesDiffAway=-1*OldOtherMatchesDiffHome

        #end of old performance records
        #start of new performance records
        Hh2h_new=r1_arg[1][0]
        Ah2h_new=r2_arg[1][0]
        HOME_WON=Hh2h_new>Ah2h_new
        wins_filler(HOME_WON,'H')
        AWAY_WON=Ah2h_new>Hh2h_new
        wins_filler(AWAY_WON,'A')
        HOME_WON=Hh2h_new==Ah2h_new
        wins_filler(HOME_WON,'H')
        AWAY_WON=Ah2h_new==Hh2h_new
        wins_filler(AWAY_WON,'A')
        NewH2HDiffHome=Hh2h_new-Ah2h_new
        NewH2HDiffAway=-1*NewH2HDiffHome

        HOmtchs_new=r1_arg[1][1]
        AOmtchs_new=r2_arg[1][1]
        HOME_WON=HOmtchs_new>AOmtchs_new
        wins_filler(HOME_WON,'H')
        AWAY_WON=AOmtchs_new>HOmtchs_new
        wins_filler(AWAY_WON,'A')
        HOME_WON=HOmtchs_new==AOmtchs_new
        wins_filler(HOME_WON,'H')
        AWAY_WON=AOmtchs_new==HOmtchs_new
        wins_filler(AWAY_WON,'A')
        NewOtherMatchesDiffHome=HOmtchs_new-AOmtchs_new
        NewOtherMatchesDiffAway=-1*NewOtherMatchesDiffHome

        GRAND_HOME_DIFF=[OldH2HDiffHome,OldOtherMatchesDiffHome,NewH2HDiffHome,NewOtherMatchesDiffHome]
        GRAND_HOME_DIFF_MIN=min(GRAND_HOME_DIFF)
        GRAND_HOME_DIFF_LAST=GRAND_HOME_DIFF[3]
        GRAND_HOME_DIFF_LAST_but2=GRAND_HOME_DIFF[1]

        GRAND_AWAY_DIFF=[OldH2HDiffAway,OldOtherMatchesDiffAway,NewH2HDiffAway,NewOtherMatchesDiffAway]
        GRAND_AWAY_DIFF_MIN=min(GRAND_AWAY_DIFF)
        GRAND_AWAY_DIFF_LAST=GRAND_AWAY_DIFF[3]
        GRAND_AWAY_DIFF_LAST_but2=GRAND_AWAY_DIFF[1]
        HOME_H2H_HEADS=min([GRAND_HOME_DIFF[0],GRAND_HOME_DIFF[2]])
        AWAY_H2H_HEADS=min([GRAND_AWAY_DIFF[0],GRAND_AWAY_DIFF[2]])
        Prediction='Unpredictable'
        print(f'GRAND_HOME_DIFF ---> {GRAND_HOME_DIFF,HOME_H2H_HEADS}')
        print(f'GRAND_AWAY_DIFF ---> {GRAND_AWAY_DIFF,AWAY_H2H_HEADS}')
        PotentialDVal=drawKong([GRAND_HOME_DIFF,GRAND_AWAY_DIFF])
        home_wins=HOME_AWAY_WINS_DIC['TrueH'].count('H')
        away_wins=HOME_AWAY_WINS_DIC['TrueA'].count('A')
        HOME_OR_AWAY_WINS=[home_wins,away_wins]
        print(f'DRAW POINT------------------------------------{PotentialDVal}------------------------------------DRAW POINT')
        print(f'HOME----------------------------{HOME_OR_AWAY_WINS}----------------------------AWAY')
        Prediction=[['Unpredictable ---> player stats empty',0,0,0,0],[0,0,0],[0,0,0]]
        try:
                home_last_scoresDiff=last_scores_array[0]
                away_last_scoresDiff=last_scores_array[1]
                Susp_Injured_Players_HomeAway=re.findall(r'Injured Players Home.+PlayersSatsAway|Injured Players Away.+\]',returned.replace('\n',''))
                Susp_Injured_Players_Home=Susp_Injured_Players_HomeAway[0]
                Susp_Injured_Players_Away=Susp_Injured_Players_HomeAway[1]
                ANALYSED_OUTCOME=subAnalyser(GRAND_HOME_DIFF,GRAND_AWAY_DIFF,[home_wins,away_wins],
                                               GRAND_HOME_STATS_LOCAL_arg,GRAND_AWAY_STATS_LOCAL_arg,Susp_Injured_Players_Home,
                                               Susp_Injured_Players_Away,home_last_scoresDiff,
                                               away_last_scoresDiff,home_or_away_box)
                Prediction=[ANALYSED_OUTCOME,PotentialDVal,HOME_OR_AWAY_WINS,[GRAND_HOME_DIFF,GRAND_AWAY_DIFF]]
        except IndexError as dd:
                 error_printer(dd)
        return Prediction
        #end of new performance records
def topLeaguesOnlineHunter():
    h_top_L = httplib2.Http()
    resp_f_top_L, content_f_top_L=h_top_L.request('https://www.teamform.com/en/league-ranking/world')
    content_str_top_L=content_f_top_L.decode("utf-8", 'ignore').replace('\n','').lower()
    team_meta__info=re.findall(r'team-meta.+?\d+\.\d+',content_str_top_L)
    TOP_50_WORLD_LEAGUES=[]
    for tmi in team_meta__info:
        tmi_no_tab=tmi.replace('\t','')
        team_name_and_country=re.findall(r'team-meta__info.+?</div>',tmi_no_tab)
        team_name_and_country_len=len(team_name_and_country)
        name_arr=[]
        if team_name_and_country_len==2:
            for tn in team_name_and_country:
                clean_league_name=tn.replace('team-meta__info">','').replace('</div>','').strip()
                written_name=clean_league_name.replace('la liga','laliga')
                written_name=written_name.replace('turkey','turkiye')
                name_arr+=[written_name]
            LEAGUE=f'{name_arr[1]} {name_arr[0]}'.upper()
            TOP_50_WORLD_LEAGUES+=[LEAGUE]
    return TOP_50_WORLD_LEAGUES
LEAGUES_ARR_FROM_ONLINE=topLeaguesOnlineHunter()
def topLeaguesHunter(sportyBetLeagueTitle):
    LEAGUES_ARR=LEAGUES_ARR_FROM_ONLINE#['PREMIER LEAGUE', 'UEFA CHAMPIONS LEAGUE', 'SERIE A', 'SUPER LIG', 'BRASILEIRO SERIE A', 'SUPERLIGA', 'LIGUE 1', 'DFB POKAL', 'UEFA EUROPA LEAGUE', 'COPPA ITALIA', 'EREDIVISIE', 'LIGA PORTUGAL', 'PREMIERSHIP', 'LALIGA', 'ALLSVENSKAN', 'MLS', 'BUNDESLIGA', 'UEFA EUROPA CONFERENCE LEAGUE', 'LIGA MX, APERTURA', 'COPA DEL REY', 'COUPE DE FRANCE', 'SAUDI PRO LEAGUE']
    sportyBetLeagueTitle_local=sportyBetLeagueTitle.upper()
    LEAGUE_STATUS='LOWER LEAGUE'
    try:
        sportyBetLeagueTitle_local=sportyBetLeagueTitle_local.split('(')[0].strip()
    except Exception:
        pass
    if sportyBetLeagueTitle_local in LEAGUES_ARR:
       LEAGUE_INDEX=LEAGUES_ARR.index(sportyBetLeagueTitle_local)
       LEAGUE_STATUS=f'TOP LEAGUE({LEAGUE_INDEX+1})'
    return LEAGUE_STATUS
def h2hAnalysis(h_2_h):
    home_wins_arr=[]
    team_draws=0
    away_wins_arr=[]
    for t in h_2_h:
        home_scr=t[0]
        away_scr=t[1]
        if home_scr==away_scr:
             team_draws+=1
        if home_scr>away_scr or home_scr==away_scr:
           home_wins_arr+=['1']
        if away_scr>home_scr or away_scr==home_scr:
           away_wins_arr+=['1']
    return [[home_wins_arr.count('1'),away_wins_arr.count('1')],team_draws]
writes='e'
if writes=='w':
    with open('playerStats.html',writes) as wa_out:
        wa_out.write('')
        wa_out.close()
def playerStatsFileHandler(bytess):
    with open('playerStats.html','a') as wa:
        wa.write(bytess)
        wa.close()
picked_match_count=0
total_odds=1
def painForce(scors):
    scors_5_cut=scors[:5]
    home_losses=0
    away_losses=0
    grand_losses=1
    for scp in scors_5_cut:
        hsp=scp[0]
        asp=scp[1]
        goaldiffhm=hsp-asp
        goaldiffawy=-1*goaldiffhm
        if goaldiffhm<0:
           goaldiffhm=-1*goaldiffhm
        if goaldiffawy<0:
           goaldiffawy=-1*goaldiffawy
        if hsp<asp:
           home_losses+=goaldiffhm
        if asp<hsp:
           away_losses+=goaldiffawy
    QUICK_CENT7=quickCentCalc([home_losses,away_losses])
    painForcesHome=QUICK_CENT7[0]
    painForcesAway=QUICK_CENT7[1]
    return [painForcesHome,painForcesAway]
def lastThreeGamesAnalyst(scores):
    _3_cut=scores[:3]
    diff_count=0
    last_wound=_3_cut[0][0]-_3_cut[0][1]
    for s in _3_cut:
        df=s[0]-s[1]
        if df<0:
           diff_count+=1
    if last_wound<0 and diff_count<=1:
       diff_count=3
    return diff_count>1
def scoresCutter(scores_arr):
      home_scores_len=len(scores_arr[0])
      away_scores_len=len(scores_arr[1])
      min_len=min([home_scores_len,away_scores_len])
      cut_home=scores_arr[0][:home_scores_len]
      cut_away=scores_arr[1][:away_scores_len]
      if min_len<=2:
         cut_home=scores_arr[0]
         cut_away=scores_arr[1]
      return [cut_home,cut_away]
def monthlyCent(monthly_score,mCutNum):
    monthly_score_local=scoresCleaner(monthly_score,mCutNum)
    monthly_score_len=len(monthly_score_local)
    homeTotalScr=0
    home_sum=0
    awayTotalScr=0
    away_sum=0
    draws_count0=0
    home_chains_count=0
    hcc=0
    away_chains_count=0
    acc=0
    for srn,sc in enumerate(monthly_score_local):
        hmscr=sc[0]
        home_sum+=hmscr
        awyscr=sc[1]
        away_sum+=awyscr
        dfw0=hmscr-awyscr
        _0_0_= hmscr==0 and awyscr==0
        if _0_0_ or dfw0==-1 or dfw0==1:
            draws_count0+=1
        if hmscr==awyscr:
           homeTotalScr+=hmscr
        if hmscr>awyscr:
           homeTotalScr+=(hmscr-awyscr)
           hcc+=1
           if srn>0 and hcc>1:
            home_chains_count+=1
        else:
            hcc=0
        if awyscr==hmscr:
           awayTotalScr+=awyscr
        if awyscr>hmscr:
            awayTotalScr+=(awyscr-hmscr)
            acc+=1
            if srn>0 and acc>1:
                away_chains_count+=1
        else:
            acc=0
    home_cent=0
    away_cent=0
    homeTotalScr=homeTotalScr+round((draws_count0/2))
    awayTotalScr=awayTotalScr+round((draws_count0/2))
    QUICK_CENT8=quickCentCalc([homeTotalScr,awayTotalScr])
    home_cent=QUICK_CENT8[0]
    away_cent=QUICK_CENT8[1]
    return [home_cent,away_cent]
def diffAnalyist(monthly_cent_array):
    diff_arr=[]
    try:
        prev_dif=monthly_cent_array[1]-monthly_cent_array[0]
        for men,mee in enumerate(monthly_cent_array):
            hmen=men+1
            dff=monthly_cent_array[hmen]-mee
            diff_arr+=[dff]
    except IndexError:
        pass
    return diff_arr
def teamWinsDrawsCent(scores_arr):
    scores_arr_len=len(scores_arr)
    lboc=0
    for lbo in scores_arr:
        hs=lbo[0]
        aas=lbo[1]
        if hs>=aas:
            lboc+=1
    try:
        lboc=round((lboc/scores_arr_len)*100)
    except ZeroDivisionError:
        pass
    return lboc
def teamStrikersPotential(teamScores,cent_indentity_strike=0):
    global OLD_ALL_SCORES_DRITY_SEEKER
    teamScores_len=len(teamScores)
    teamScores_len_cut06=round(0.6*teamScores_len)
    seeker_len_abs_diff_strike=abs(teamScores_len-teamScores_len_cut06)
    team_strike_scores_len_old=teamScores_len
    home_stroke_count=0
    away_stroke_count=0
    home_stroke_count_old=0
    for scrrTn,scrrT in enumerate(teamScores):
        scrr_home=scrrT[0]
        scrr_away=scrrT[1]
        scrrTn_human=scrrTn+1
        team_strike_incre=1
        if cent_indentity_strike>0 and scrrTn_human<=teamScores_len_cut06 and teamScores_len>OLD_ALL_SCORES_DRITY_SEEKER and seeker_len_abs_diff_strike>=5:
           team_strike_scores_len_old=teamScores_len-teamScores_len_cut06
           team_strike_incre=0
        if scrr_home>=2:
           home_stroke_count+=1
           home_stroke_count_old+=team_strike_incre
        if scrr_away>=2:
           away_stroke_count+=1
    home_stroke_count_cent=0
    away_stroke_count_cent=0
    home_stroke_count_cent_old=0
    try:
        home_stroke_count_cent=round((home_stroke_count/teamScores_len)*100)
    except ZeroDivisionError:
        pass
    try:
        away_stroke_count_cent=round((away_stroke_count/teamScores_len)*100)
    except ZeroDivisionError:
        pass
    try:
        home_stroke_count_cent_old=round((home_stroke_count_old/team_strike_scores_len_old)*100)
    except ZeroDivisionError:
        pass
    return [home_stroke_count_cent,home_stroke_count,[home_stroke_count_cent_old,home_stroke_count_old]]
totalSelectedGames=0
def reshuffler(scores):
    away_scores_only=[]
    for scr_ in scores:
        away_scores_only+=[(scr_[1],scr_[0])]
    return away_scores_only
def monthlyScoresCentDiffer(home_monthly_scores,away_monthly_scores):
    diff_aer=[]
    try:
        for nmh, hms in enumerate(home_monthly_scores):
            ams=away_monthly_scores[nmh]
            diff_aer+=[hms-ams]
    except IndexError:
        pass
    return diff_aer
def ggCent(ALL_SCORES):
    ALL_SCORES_LEN=len(ALL_SCORES)
    gg_count=0
    gg_cent=0
    draws_count=0
    draws_cent=0
    over_1_count=0
    over_1_cent=0
    _1_goal_diff_count=0
    for scrss in ALL_SCORES:
        min_score=min(scrss)
        hts=scrss[0]
        ats=scrss[1]
        scr_sum=hts+ats
        if hts==ats:
           draws_count+=1
        gdff=c_abs(hts-ats)
        if gdff==1:
           _1_goal_diff_count+=1
        if scr_sum>=2:
           over_1_count+=1
        if min_score>=1:
            gg_count+=1
    try:
        gg_cent=round((gg_count/ALL_SCORES_LEN)*100)
    except ZeroDivisionError:
        pass
    try:
        over_1_cent=round((over_1_count/ALL_SCORES_LEN)*100)
    except ZeroDivisionError:
        pass
    try:
        dc=draws_count+_1_goal_diff_count
        draws_cent=round((dc/ALL_SCORES_LEN)*100)
    except ZeroDivisionError:
        pass
    return [gg_cent,over_1_cent,draws_cent]
def lostRecentGames(scores_array):
    lost_points_count=0
    for p in scores_array:
        hp=p[0]
        ap=p[1]
        if hp<ap:
           lost_points_count+=1
    return lost_points_count
def pillarCents(pillar_array):
    plr_home=pillar_array[0]
    plr_away=pillar_array[1]
    QUICK_CENT9=quickCentCalc([plr_home,plr_away])
    pillar_array_cent=[QUICK_CENT9[0],QUICK_CENT9[1]]
    return pillar_array_cent

def monthlyPointsCent(home_monthly_p_cent_array,away_monthly_p_cent_array):
    min_len=min([len(home_monthly_p_cent_array),len(away_monthly_p_cent_array)])
    home_monthly_p_cent_array_same_len=home_monthly_p_cent_array[:min_len]
    away_monthly_p_cent_array_same_len=away_monthly_p_cent_array[:min_len]
    for mn in range(min_len):
        away_cent=away_monthly_p_cent_array_same_len[mn]
        incre=mn+1
        mn_hu=mn+incre
        home_monthly_p_cent_array_same_len.insert(mn_hu,away_cent)
    return home_monthly_p_cent_array_same_len
def quickDivider(h2h_old_cent,otherM_cent_old,otherM_cent_new,only_home_cnt_old,only_home_cnt_new):
        def zerodiv(h,a):
            RESULT=-1
            try:
                RESULT=round((h/a),1)
            except ZeroDivisionError:
                pass
            return RESULT
        h2h_old_centH=h2h_old_cent[0]
        h2h_old_centA=h2h_old_cent[1]
        HDV_1=zerodiv(h2h_old_centH,h2h_old_centA)
        ADV_1=zerodiv(h2h_old_centA,h2h_old_centH)

        otherM_cent_oldH=otherM_cent_old[0]
        otherM_cent_oldA=otherM_cent_old[1]
        HDV_2=zerodiv(otherM_cent_oldH,otherM_cent_oldA)
        ADV_2=zerodiv(otherM_cent_oldA,otherM_cent_oldH)

        otherM_cent_newH=otherM_cent_new[0]
        otherM_cent_newA=otherM_cent_new[1]
        HDV_3=zerodiv(otherM_cent_newH,otherM_cent_newA)
        ADV_3=zerodiv(otherM_cent_newA,otherM_cent_newH)

        only_home_cnt_oldH=only_home_cnt_old[0]
        only_home_cnt_oldA=only_home_cnt_old[1]
        HDV_4=zerodiv(only_home_cnt_oldH,only_home_cnt_oldA)
        ADV_4=zerodiv(only_home_cnt_oldA,only_home_cnt_oldH)

        only_home_cnt_newH=only_home_cnt_new[0]
        only_home_cnt_newA=only_home_cnt_new[1]
        HDV_5=zerodiv(only_home_cnt_newH,only_home_cnt_newA)
        ADV_5=zerodiv(only_home_cnt_newA,only_home_cnt_newH)

        HOME_GRAND_DIVS=[HDV_1,HDV_2,HDV_3,HDV_4,HDV_5]
        AWAY_GRAND_DIVS=[ADV_1,ADV_2,ADV_3,ADV_4,ADV_5]
        return [HOME_GRAND_DIVS,AWAY_GRAND_DIVS,[round(sum(HOME_GRAND_DIVS),1),round(sum(AWAY_GRAND_DIVS),1)]]
def teamDidntWinAllTwoGames(h2h_two_games,all_scores_last_game):
    customized_games=[h2h_two_games[0],all_scores_last_game]
    hg=h2h_two_games[0][0]
    ag=h2h_two_games[0][1]
    hg_other_m=all_scores_last_game[0]
    ag_other_m=all_scores_last_game[1]
    def won_all_func(two_games):
        won_all_count=0
        for hth in two_games:
            home_score=hth[0]
            away_score=hth[1]
            if home_score>away_score:
                won_all_count+=1
        return won_all_count<2
    h2h_logic=won_all_func(h2h_two_games)
    customized_logic=hg>ag and ag_other_m>hg_other_m
    if customized_logic:
        h2h_logic=False
    return h2h_logic
def sub_predictor(FBT_H_A_ARR,meta_data,league_title_arg2,OTHER_MATCHES_ARG,CORRECTIONS_local,match_odds_arg2,TEAMS_ATTACK_CENT_ARG,TEAMS_SHOTS_ON_TARGET_CENTS_ARG):
    global picked_match_count,total_odds,totalSelectedGames
    match_odds_arg2_cut_3=match_odds_arg2
    if len(match_odds_arg2_cut_3[0])<4:
        match_odds_arg2_cut_3=match_odds_arg2[1:]
    match_odds_arg2_cut_3=match_odds_arg2_cut_3[:3]
    HOME_ODD=eval(match_odds_arg2_cut_3[0])
    AWAY_ODD=eval(match_odds_arg2_cut_3[2])
    ODDS_MIN=min([HOME_ODD,AWAY_ODD])
    HOME_ODD_DIFF=HOME_ODD-AWAY_ODD
    AWAY_ODD_DIFF=AWAY_ODD-HOME_ODD
    odds_diff=c_abs(HOME_ODD_DIFF)
    LeagueStatus=topLeaguesHunter(league_title_arg2)
    SUSPENDED_PLAYERS_RECORDS_LOCAL=OTHER_MATCHES_ARG[7]
    GRAND_HOME_STATS_LOCAL=SUSPENDED_PLAYERS_RECORDS_LOCAL[0]
    HOME_SUS_PLAYERS_RECORDS_LOCAL=SUSPENDED_PLAYERS_RECORDS_LOCAL[1]
    GRAND_AWAY_STATS_LOCAL=SUSPENDED_PLAYERS_RECORDS_LOCAL[2]
    AWAY_SUS_PLAYERS_RECORDS_LOCAL=SUSPENDED_PLAYERS_RECORDS_LOCAL[3]
    HOME_STRIKERS_GOALS_TOTAL_LOCAL=SUSPENDED_PLAYERS_RECORDS_LOCAL[4]
    AWAY_STRIKERS_GOALS_TOTAL_LOCAL=SUSPENDED_PLAYERS_RECORDS_LOCAL[5]
    H2H_DIC_LOCAL_GRAND=OTHER_MATCHES_ARG[0]
    PURELY_HOME_AWAY_H2H_SCORES_ARG=H2H_DIC_LOCAL_GRAND[1]
    ALL_TIMES_H2H_ARG=H2H_DIC_LOCAL_GRAND[2]
    ALL_TIMES_H2H_ARG_FS=ALL_TIMES_H2H_ARG[0]
    ALL_TIMES_H2H_VERY_OLD_ARG=H2H_DIC_LOCAL_GRAND[3]
    ALL_TIMES_H2H_VERY_OLD_ARG_CENT=win_loss_cent(ALL_TIMES_H2H_VERY_OLD_ARG)[:2]
    ALL_TIMES_H2H_ARG_CENT=win_loss_cent(ALL_TIMES_H2H_ARG)[:2]
    PURELY_HOME_AWAY_H2H_SCORES_ARG_LEN=len(PURELY_HOME_AWAY_H2H_SCORES_ARG)
    if PURELY_HOME_AWAY_H2H_SCORES_ARG_LEN==0:
        PURELY_HOME_AWAY_H2H_SCORES_ARG=[(-1,-1)]
    PURELY_HOME_AWAY_H2H_SCORES_ARG_FS=PURELY_HOME_AWAY_H2H_SCORES_ARG[0]
    PURELY_H_A_LAST_SCR_DIFF=0
    try:
        PURELY_H_A_LAST_SCR_DIFF=PURELY_HOME_AWAY_H2H_SCORES_ARG[0]
        PURELY_H_A_LAST_SCR_DIFF=PURELY_H_A_LAST_SCR_DIFF[0]-PURELY_H_A_LAST_SCR_DIFF[1]
    except IndexError:
        pass
    H2H_DIC_LOCAL=H2H_DIC_LOCAL_GRAND[0]
    SBT_DIC_LOCAL_DIC=OTHER_MATCHES_ARG[1]
    home_T=FBT_H_A_ARR[0]
    home_T_Point=-1
    HometeamPosition=-1
    away_T=FBT_H_A_ARR[1]
    away_T_Point=-1
    AwayteamPosition=-1
    try:
        home_T_Point=SBT_DIC_LOCAL_DIC[home_T][0]
        HometeamPosition=SBT_DIC_LOCAL_DIC[home_T][1]
        away_T_Point=SBT_DIC_LOCAL_DIC[away_T][0]
        AwayteamPosition=SBT_DIC_LOCAL_DIC[away_T][1]
    except TypeError:
        pass
    PointDiff=home_T_Point-away_T_Point
    H2H_AWAY=H2H_DIC_LOCAL[away_T]
    H2H_HOME=H2H_DIC_LOCAL[home_T]
    H2H_SCR_LEN=len(H2H_HOME)
    H2H_TUPLE=[]
    gg_count=0
    for h2hn, h2he in enumerate(H2H_HOME):
        awscr=H2H_AWAY[h2hn]
        tpl=(h2he,awscr)
        tpl_sum=h2he+awscr
        if h2he>0 and awscr>0:
            gg_count+=1
        H2H_TUPLE+=[tpl]
    #[H2H_DIC,SBT_DIC,HOME_OR_AWAY_DIC,FOREBET_PREDICTION,H_A_NEXT_MATCHES,HOM,AOM,SUSPENDED_PLAYERS_RECORDS,ALL_TEAMS_LEN_LOCAL2,[home_same_team_cent,away_same_team_cent],[HOME_SAME_TEAM_AGAINST_LEN,AWAY_SAME_TEAM_AGAINST_LEN],STANDINGS_OF_BOTH_TEAMS_TABLE_LOCAL,notfinaldic_local,SAME_HOME_AWAY_SCORES,ALL_TEAMS_POINTS_ARRAY_LOCAL]
    ALL_TEAMS_LEN_LOCAL=OTHER_MATCHES_ARG[8]
    ALL_TEAMS_LEN_LOCAL_HALF=round(ALL_TEAMS_LEN_LOCAL/2)
    SAME_TEAMS_AGAINST=OTHER_MATCHES_ARG[9]
    SAME_TEAMS_AGAINST_LEN=OTHER_MATCHES_ARG[10]
    STANDINGS_OF_BOTH_TEAMS_TABLE_LOCAL2=OTHER_MATCHES_ARG[11]
    notfinaldic_local2=OTHER_MATCHES_ARG[12]
    SAME_HOME_AWAY_SCORES_LOCAL=OTHER_MATCHES_ARG[13]
    ALL_TEAMS_POINTS_ARRAY_LOCAL_HERE=OTHER_MATCHES_ARG[14]
    both_teams_in_group2_impo=OTHER_MATCHES_ARG[15]
    HOME_OBSTACLE_POINTS_IMPO=OTHER_MATCHES_ARG[16]
    AWAY_OBSTACLE_POINTS_IMPO=OTHER_MATCHES_ARG[17]
    STANDINGS_OF_BOTH_TEAMS_LEN_IMPORTED=OTHER_MATCHES_ARG[18]
    ONLY_SAME_TEAMS_HOME=(-1,-1)
    ONLY_SAME_TEAMS_AWAY=(-1,-1)
    try:
        ONLY_SAME_TEAMS_HOME=SAME_HOME_AWAY_SCORES_LOCAL[0]
    except IndexError as indeerr:
             error_printer(indeerr)
    try:
        ONLY_SAME_TEAMS_AWAY=SAME_HOME_AWAY_SCORES_LOCAL[1]
    except IndexError as indeerr1:
             error_printer(indeerr1)
    ONLY_SAME_TEAMS_HOME_RECENT_CENT=win_loss_cent(ONLY_SAME_TEAMS_HOME,5)[0]
    home_same_team_cent_recent_local=ONLY_SAME_TEAMS_HOME_RECENT_CENT
    home_same_team_cent_recent_local_used=home_same_team_cent_recent_local
    ONLY_SAME_TEAMS_AWAY_RECENT_CENT=win_loss_cent(ONLY_SAME_TEAMS_AWAY,5)[0]
    away_same_team_cent_recent_local=ONLY_SAME_TEAMS_AWAY_RECENT_CENT
    away_same_team_cent_recent_local_used=away_same_team_cent_recent_local
    home_same_team_cent_local_len=SAME_TEAMS_AGAINST_LEN[0]
    away_same_team_cent_local_len=SAME_TEAMS_AGAINST_LEN[1]
    SAME_TEAMS_PLAYED_LEN_MAX=max([home_same_team_cent_local_len,away_same_team_cent_local_len])
    home_same_team_cent_local=SAME_TEAMS_AGAINST[0]
    away_same_team_cent_local=SAME_TEAMS_AGAINST[1]
    SAME_TEAMS_TRANS_H=ONLY_SAME_TEAMS_HOME_RECENT_CENT-home_same_team_cent_local
    SAME_TEAMS_TRANS_A=ONLY_SAME_TEAMS_AWAY_RECENT_CENT-away_same_team_cent_local
    H_A_NEXT_MATCHES_LOCAL=OTHER_MATCHES_ARG[4]
    H2H_DATE=[17, 9, 1995]
    try:
        H2H_DATE=H2H_DIC_LOCAL['H2H_DATE'][0]
    except IndexError:
        pass
    HOMh_n_a=OTHER_MATCHES_ARG[5]
    BelowTeamPosGamesCentHome=HOMh_n_a[7]
    ONLY_HOME_SCORES=[(-1,-1)]
    try:
        ONLY_HOME_SCORES=HOMh_n_a[6]
    except IndexError as only_home_scores_error:
        error_printer(only_home_scores_error)
    TEAMS_GTOP_GUYS_POSHOME=HOMh_n_a[3]
    ALL_SCORES_DIRTY_HOME=HOMh_n_a[4]
    HOME_FAILS_PATTERN=freshWoundsForces(ALL_SCORES_DIRTY_HOME)
    HometopGuysCent=TEAMS_GTOP_GUYS_POSHOME[0]
    HometeamPosition=TEAMS_GTOP_GUYS_POSHOME[1]
    MONTHLY_SCORES_GRAND_LOCAL_HOME=HOMh_n_a[2]
    HOMh_n_a_Date=HOMh_n_a[0][0]
    HOME_OTHER_M_HOMEandAWAY=HOMh_n_a[1]
    AOMh_n_a=OTHER_MATCHES_ARG[6]
    BelowTeamPosGamesCentAway=AOMh_n_a[7]
    ONLY_AWAY_SCORES=[(-1,-1)]
    try:
        ONLY_AWAY_SCORES=AOMh_n_a[6]
    except IndexError as only_away_scores_error:
        error_printer(only_away_scores_error)
    min_len=min([len(ONLY_HOME_SCORES),len(ONLY_AWAY_SCORES)])
    ONLY_SCORES_MAX_LEN=max([len(ONLY_HOME_SCORES),len(ONLY_AWAY_SCORES)])
    ONLY_AWAY_SCORES_REARRANGED=reshuffler(ONLY_AWAY_SCORES)
    OP1=ONLY_HOME_SCORES
    OP2=ONLY_AWAY_SCORES_REARRANGED
    only_home_score_cent=win_loss_cent(OP1,0,1)[0]
    only_away_score_cent=win_loss_cent(OP2,0,1)[0]
    only_home_score_cent_used=only_home_score_cent
    only_away_score_cent_used=only_away_score_cent
    only_home_or_away_arr=[only_home_score_cent,only_away_score_cent]
    ONLY_HOME_OR_AWAY_CENT_MIN=min(only_home_or_away_arr)
    ONLY_H_A_DIFF=only_home_score_cent-only_away_score_cent
    ONLY_HOME_GREATER=only_home_score_cent>=only_away_score_cent
    ONLY_AWAY_GREATER=only_away_score_cent>=only_home_score_cent
    if ONLY_H_A_DIFF<0:
        ONLY_H_A_DIFF=-1*ONLY_H_A_DIFF
    CUT_5=5
    SCORES_LEN_MIN=min([len(ONLY_HOME_SCORES),len(ONLY_AWAY_SCORES_REARRANGED)])
    if SCORES_LEN_MIN<CUT_5:
        CUT_5=SCORES_LEN_MIN
    only_home_cent_5_cut=win_loss_cent(ONLY_HOME_SCORES,CUT_5)[0]
    only_home_cent_5_cut_sample=only_home_cent_5_cut
    only_away_cent_5_cut=win_loss_cent(ONLY_AWAY_SCORES_REARRANGED,CUT_5)[0]
    only_away_cent_5_cut_sample=only_away_cent_5_cut
    ONLY_TEAM_TRANS_H=only_home_cent_5_cut-only_home_score_cent
    ONLY_TEAM_TRANS_A=only_away_cent_5_cut-only_away_score_cent
    print(f'PURELY_HOME_AWAY_H2H_SCORES({PURELY_HOME_AWAY_H2H_SCORES_ARG_LEN}) ---> {PURELY_HOME_AWAY_H2H_SCORES_ARG}\n')
    print(f'only_home_cent_5_cut ---> {only_home_cent_5_cut}\nonly_away_cent_5_cut ---> {only_away_cent_5_cut}\n')
    print(f'ONLY_HOME_SCORES ---> {ONLY_HOME_SCORES}\nONLY_AWAY_SCORES ---> {ONLY_AWAY_SCORES}\n')
    print(f'ONLY_HOME_SCORES_CENT: {only_home_score_cent}\nONLY_AWAY_SCORES_CENT: {only_away_score_cent}\n')
    ONLY_HOME_SCORES_LEN=len(ONLY_HOME_SCORES)
    ONLY_AWAY_SCORES_REARRANGED_LEN=len(ONLY_AWAY_SCORES_REARRANGED)
    ONLY_HOME_AWAY_LEN_MIN=min([ONLY_HOME_SCORES_LEN,ONLY_AWAY_SCORES_REARRANGED_LEN])
    #ONLY_HOME_AWAY_OVER_2GLS_MIN=min([ONLY_HOME_SCORES_OVER_2GLS_CENT,ONLY_AWAY_SCORES_OVER_2GLS_CENT])
    #ONLY_HOME_AWAY_OVER_2GLS_MAX=max([ONLY_HOME_SCORES_OVER_2GLS_CENT,ONLY_AWAY_SCORES_OVER_2GLS_CENT])
    #O_HM_AWY_O2GLS_DIFF=ONLY_HOME_SCORES_OVER_2GLS_CENT-ONLY_AWAY_SCORES_OVER_2GLS_CENT
    #if O_HM_AWY_O2GLS_DIFF<0:
        #O_HM_AWY_O2GLS_DIFF=-1*O_HM_AWY_O2GLS_DIFF
    #print(f'ONLY_HOME_SCORES_OVER_2GLS_CENT({ONLY_HOME_SCORES_LEN}): {ONLY_HOME_SCORES_OVER_2GLS_CENT}\nONLY_AWAY_SCORES_OVER_2GLS_CENT({ONLY_AWAY_SCORES_REARRANGED_LEN}): {ONLY_AWAY_SCORES_OVER_2GLS_CENT}\n')

    TEAMS_GTOP_GUYS_POSAWAY=AOMh_n_a[3]
    ALL_SCORES_DIRTY_AWAY=AOMh_n_a[4]
    AWAY_FAILS_PATTERN=freshWoundsForces(ALL_SCORES_DIRTY_AWAY)
    scores_len_arr=[len(ALL_SCORES_DIRTY_HOME),len(ALL_SCORES_DIRTY_AWAY)]
    ALL_SCORES_DIRTY_LEN_MIN=min(scores_len_arr)
    ALL_SCORES_DIRTY_MAX_LEN=max(scores_len_arr)
    CUT_5_OTHER_M=5
    if ALL_SCORES_DIRTY_LEN_MIN<CUT_5_OTHER_M:
        CUT_5_OTHER_M=ALL_SCORES_DIRTY_LEN_MIN
    HOME_CONSISTENCY=consistencyChecker(ALL_SCORES_DIRTY_HOME,H2H_TUPLE)
    HOME_WOUND_PATTERNS=HOME_CONSISTENCY[1]
    CHAINS_LOSSES_COMMENT_H=HOME_CONSISTENCY[2]
    CHAINS_LOSSES_COMMENT_H_NUMBERS=f'{CHAINS_LOSSES_COMMENT_H}'
    CHAINS_LOSSES_COMMENT_H_NUMBERS=re.findall(r'\d+',CHAINS_LOSSES_COMMENT_H_NUMBERS)
    CHAINS_LOSSES_COMMENT_H_NUMBERS_INT=0
    for lint in CHAINS_LOSSES_COMMENT_H_NUMBERS:
        CHAINS_LOSSES_COMMENT_H_NUMBERS_INT+=int(lint)
    HOME_WOUND_PATTERNS_USED=HOME_WOUND_PATTERNS
    HOME_CONSISTENCY=HOME_CONSISTENCY[0]
    AWAY_CONSISTENCY=consistencyChecker(ALL_SCORES_DIRTY_AWAY,reshuffler(H2H_TUPLE))
    HIDDEN_LOSSES_HOME_HUB=hiddenLosses(ALL_SCORES_DIRTY_HOME)
    HIDDEN_LOSSES_HOME=HIDDEN_LOSSES_HOME_HUB[0]
    LOSSES_PATTERN_TRIGGERED_HOME=HIDDEN_LOSSES_HOME_HUB[1]
    HIDDEN_LOSSES_AWAY_HUB=hiddenLosses(ALL_SCORES_DIRTY_AWAY)
    HIDDEN_LOSSES_AWAY=HIDDEN_LOSSES_AWAY_HUB[0]
    LOSSES_PATTERN_TRIGGERED_AWAY=HIDDEN_LOSSES_AWAY_HUB[1]
    AWAY_WOUND_PATTERNS=AWAY_CONSISTENCY[1]
    CHAINS_LOSSES_COMMENT_A=AWAY_CONSISTENCY[2]
    CHAINS_LOSSES_COMMENT_A_NUMBERS=f'{CHAINS_LOSSES_COMMENT_A}'
    CHAINS_LOSSES_COMMENT_A_NUMBERS=re.findall(r'\d+',CHAINS_LOSSES_COMMENT_A_NUMBERS)
    CHAINS_LOSSES_COMMENT_A_NUMBERS_INT=0
    for lint_a in CHAINS_LOSSES_COMMENT_A_NUMBERS:
        CHAINS_LOSSES_COMMENT_A_NUMBERS_INT+=int(lint_a)
    AWAY_WOUND_PATTERNS_USED=AWAY_WOUND_PATTERNS
    AWAY_CONSISTENCY=AWAY_CONSISTENCY[0]
    TEAMS_1st2_CONSISTENCY_CENT=firstTwoConsistencyCent(HOME_CONSISTENCY,AWAY_CONSISTENCY)
    LAST_3_GAMES_LOST_POINTS_HOME=pointsLostInLastThreeGames(ALL_SCORES_DIRTY_HOME[:3])
    LAST_3_GAMES_LOST_POINTS_AWAY=pointsLostInLastThreeGames(ALL_SCORES_DIRTY_AWAY[:3])
    LAST_LOST_POINTS_CENT=[LAST_3_GAMES_LOST_POINTS_HOME,LAST_3_GAMES_LOST_POINTS_AWAY]
    ONLY_HOME_SCORES_OVER_2GLS_CENT=teamStrikersPotential(ALL_SCORES_DIRTY_HOME)[0]
    ONLY_AWAY_SCORES_OVER_2GLS_CENT=teamStrikersPotential(ALL_SCORES_DIRTY_AWAY)[0]
    HOME_WINS_DRAWS_CENT=teamWinsDrawsCent(ALL_SCORES_DIRTY_HOME)
    AWAY_WINS_DRAWS_CENT=teamWinsDrawsCent(ALL_SCORES_DIRTY_AWAY)
    home_points_lost=lostRecentGames(ALL_SCORES_DIRTY_HOME[:5])
    away_points_lost=lostRecentGames(ALL_SCORES_DIRTY_AWAY[:5])
    lost_games_cent_array=[home_points_lost,away_points_lost]
    print(f'home_away_lost_games_in_last_five_games ---> {lost_games_cent_array}')
    AwaytopGuysCent=TEAMS_GTOP_GUYS_POSAWAY[0]
    AwayteamPosition=TEAMS_GTOP_GUYS_POSAWAY[1]
    TEAMS_DRIVEN_ENGINE_X=teamDrivePurposeBasedOnPointsAndPos(ALL_TEAMS_POINTS_ARRAY_LOCAL_HERE,[home_T_Point,away_T_Point],[HometeamPosition,AwayteamPosition])
    TEAMS_DRIVEN_ENGINE_X_H_SUM=sum(TEAMS_DRIVEN_ENGINE_X[0])
    TEAMS_DRIVEN_ENGINE_X_A_SUM=sum(TEAMS_DRIVEN_ENGINE_X[1])
    BELOW_TEAMS_POS_GAME_CENTS=[[BelowTeamPosGamesCentHome,BelowTeamPosGamesCentAway],[HometeamPosition,AwayteamPosition]]
    ABOVE_POST_DRIVEN_CENT=quickCentCalc([TEAMS_DRIVEN_ENGINE_X[0][0],TEAMS_DRIVEN_ENGINE_X[1][0]])
    print(f'ABOVE_POST_DRIVEN_CENT ---> {ABOVE_POST_DRIVEN_CENT}')
    MONTHLY_SCORES_GRAND_LOCAL_AWAY=AOMh_n_a[2]
    MONTHLY_SCORES_DIFF=monthlyScoresCentDiffer(MONTHLY_SCORES_GRAND_LOCAL_HOME,MONTHLY_SCORES_GRAND_LOCAL_AWAY)
    AOMh_n_a_Date=AOMh_n_a[0][0]
    dateInterOfMatches=matchesDatesHandler([H2H_DATE,HOMh_n_a_Date,AOMh_n_a_Date],home_T,away_T)
    CURRENT_AGE=matchesDatesHandler([todays_date,HOMh_n_a_Date,AOMh_n_a_Date],home_T,away_T)
    home_last_game_current_age=int(re.findall(r'\d+',CURRENT_AGE[0])[1])
    HOME_LAST_GAME_FORGOTEN=home_last_game_current_age>=5
    away_last_game_current_age=int(re.findall(r'\d+',CURRENT_AGE[2])[1])
    AWAY_LAST_GAME_FORGOTEN=away_last_game_current_age>=5
    AWAY_OTHER_M_HOMEandAWAY=AOMh_n_a[1]
    NMH=H_A_NEXT_MATCHES_LOCAL[0]
    NMA=H_A_NEXT_MATCHES_LOCAL[1]
    total_next_match_min=min([NMH,NMA])
    OP_DIC={'0':1,'1':0}
    home_away=re.findall(r'MATCH\(sportybet\).+? --->',meta_data)[0].replace('MATCH(sportybet): ','')
    home_away=home_away.replace(' --->','').split(' vs ')
    same_score_len=scoresCutter([ALL_SCORES_DIRTY_HOME,ALL_SCORES_DIRTY_AWAY])
    MatchNumber=re.findall(r'MATCH NUMBER.+?\d+',meta_data)
    MatchCount=0
    for mn in MatchNumber:
        mnn=re.findall(r'\d+',mn)
        MatchCount=int(mnn[0])
    otherMlastScoreHomeSameLen=same_score_len[0]
    otherMlastScoreAwaySameLen=same_score_len[1]
    HTIM_ORGANIC_POINT_CENT=win_loss_cent(otherMlastScoreHomeSameLen,0,1)
    ATIM_ORGANIC_POINT_CENT=win_loss_cent(otherMlastScoreAwaySameLen,0,1)
    HOME_LOST_BY_ONE=HTIM_ORGANIC_POINT_CENT[2]
    AWAY_LOST_BY_ONE=ATIM_ORGANIC_POINT_CENT[2]
    TEAM_DEFENCE_ABS_DIFF=abs(HOME_LOST_BY_ONE-AWAY_LOST_BY_ONE)
    HOME_LOST_BY_ONE_USED=HOME_LOST_BY_ONE
    AWAY_LOST_BY_ONE_USED=AWAY_LOST_BY_ONE
    MICRO_STRIKE_DEFENCE_HOME=HTIM_ORGANIC_POINT_CENT[3]
    MICRO_STRIKE_DEFENCE_AWAY=ATIM_ORGANIC_POINT_CENT[3]
    HOME_TRANS_HUNT_QUALITIES=HTIM_ORGANIC_POINT_CENT[4]
    AWAY_TRANS_HUNT_QUALITIES=ATIM_ORGANIC_POINT_CENT[4]
    LBOCCNT_OLD_LOCAL_HOME=HTIM_ORGANIC_POINT_CENT[5]
    LBOCCNT_OLD_LOCAL_AWAY=ATIM_ORGANIC_POINT_CENT[5]
    PURE_OLD_TEAMS_DEFENCE=[LBOCCNT_OLD_LOCAL_HOME,LBOCCNT_OLD_LOCAL_AWAY]
    if ALL_SCORES_DIRTY_MAX_LEN<5:
        HOME_LOST_BY_ONE_USED=0
        AWAY_LOST_BY_ONE_USED=0
    HTIM_ORGANIC_POINT_CENT=HTIM_ORGANIC_POINT_CENT[0]
    ATIM_ORGANIC_POINT_CENT=ATIM_ORGANIC_POINT_CENT[0]
    MAX_ARR=[HTIM_ORGANIC_POINT_CENT,ATIM_ORGANIC_POINT_CENT]
    centMax=max(MAX_ARR)
    max_dex=MAX_ARR.index(centMax)
    T_TO_WIN=FBT_H_A_ARR[max_dex]
    opdex=OP_DIC[f'{max_dex}']
    _3POINT5_WINS=0
    GG_CENT=0
    H2H_TUPLE_used=H2H_TUPLE
    if len(H2H_TUPLE)==0:
        H2H_TUPLE_used=[(-1,-1)]
    HOME_FAILS_PATTERN_H2H_HOME=freshWoundsForces(H2H_TUPLE_used)
    HOME_FAILS_PATTERN_H2H_AWAY=freshWoundsForces(reshuffler(H2H_TUPLE_used))
    H2H_CENT_TRULY=h2hScoresLeveler(H2H_TUPLE_used)
    HOME_LATEST_WOUNDS=latestWounds([H2H_TUPLE_used[0]]+ALL_SCORES_DIRTY_HOME[:5])
    AWAY_LATEST_WOUNDS=latestWounds([(H2H_TUPLE_used[0][1],H2H_TUPLE_used[0][0])]+ALL_SCORES_DIRTY_AWAY[:5])
    HOME_WOUND_PATTERNS=max([HOME_WOUND_PATTERNS,HOME_LATEST_WOUNDS])
    AWAY_WOUND_PATTERNS=max([AWAY_WOUND_PATTERNS,AWAY_LATEST_WOUNDS])
    H2H_SCORES_SUM_MODE=h2hModalScoresSum(H2H_TUPLE)
    H2H_DIFF_MODAL_CENT=h2hModalDiffCent(H2H_TUPLE)
    H2H_TUPLE_FS=H2H_TUPLE[0]
    H2H_TUPLE_LEN=len(H2H_TUPLE)
    GG_CENT=round((gg_count/H2H_TUPLE_LEN)*100)
    print(f'GG_CENT ---> {GG_CENT}')
    H2H_TUPLE_SUM=sum(H2H_TUPLE[0])
    H2HPainForce=painForce(H2H_TUPLE)
    HomeH2HPainForce=H2HPainForce[0]
    AwayH2HPainForce=H2HPainForce[1]
    H2H_TUPLE_LAST_SCR=H2H_TUPLE[0]
    h2hlstdiff=H2H_TUPLE_LAST_SCR[1]-H2H_TUPLE_LAST_SCR[0]
    h2h_wins=h2hAnalysis(H2H_TUPLE)[0]
    HOME_H2H_WINS=h2h_wins[0]
    AWAY_H2H_WINS=h2h_wins[1]
    if HOME_H2H_WINS==0:
        HOME_H2H_WINS=1
    if AWAY_H2H_WINS==0:
        AWAY_H2H_WINS=1
    H2H_WINS_COUNT_CENT=quickCentCalc([HOME_H2H_WINS,AWAY_H2H_WINS])
    GRAND_H2H_CENT=win_loss_cent(H2H_TUPLE,0,1)
    OP3=PURELY_HOME_AWAY_H2H_SCORES_ARG[:10]
    OP3_USED=OP3
    if OP3[0][0]==-1:
        OP3_USED=H2H_TUPLE
    QUICK_H2H_WINS_CENT=h2hWinsCountCent([OP3_USED])
    print(f'QUICK_H2H_WINS_CENT ---> {QUICK_H2H_WINS_CENT}')
    GRAND_PURELY_H2H_CENT=win_loss_cent(OP3)
    HOP1=GRAND_PURELY_H2H_CENT[0]
    HOP2=GRAND_PURELY_H2H_CENT[1]
    if H2H_TUPLE_LEN>0 and H2H_TUPLE[0][0]!=-1:
        GRAND_PURELY_H2H_CENT=GRAND_H2H_CENT
    PURELY_HOME_H2H_CENT=GRAND_PURELY_H2H_CENT[0]
    PURELY_AWAY_H2H_CENT=GRAND_PURELY_H2H_CENT[1]
    H2H_HOME_CENT=GRAND_H2H_CENT[0]
    H2H_AWAY_CENT=GRAND_H2H_CENT[1]
    H2H_OTHER_MATCHES_CENT_HOME=[H2H_HOME_CENT,HTIM_ORGANIC_POINT_CENT]
    H2H_OTHER_MATCHES_CENT_AWAY=[H2H_AWAY_CENT,ATIM_ORGANIC_POINT_CENT]
    omcent_diff=HTIM_ORGANIC_POINT_CENT-ATIM_ORGANIC_POINT_CENT
    if omcent_diff<0:
        omcent_diff=-1*omcent_diff
    h2h_cent_diff=H2H_HOME_CENT-H2H_AWAY_CENT
    if h2h_cent_diff<0:
       h2h_cent_diff=-1*h2h_cent_diff
    H2H_CENT_ARR=[H2H_HOME_CENT,H2H_AWAY_CENT]
    h2h_cent_min=min(H2H_CENT_ARR)
    FOREBETpredictions=OTHER_MATCHES_ARG[3]
    max_scr=max(FOREBETpredictions)
    FOREBETpredictions_min=min(FOREBETpredictions)
    max_scr_index=FOREBETpredictions.index(max_scr)
    team=home_away[max_scr_index]
    FOREBETpredictions_sum=sum(FOREBETpredictions)
    OTHER_SITES_PREDICTION=[[HOME_ODD,AWAY_ODD],FOREBETpredictions]
    dashes='-'*(len(league_title_arg2+LeagueStatus)+2)
    under_picked='unpredictable'
    _5_cutH2H=H2H_TUPLE[:5]
    _2h2h_cut=H2H_TUPLE[:2]
    home_dnt_wins_all_logic=teamDidntWinAllTwoGames(_2h2h_cut,ALL_SCORES_DIRTY_AWAY[0])
    away_dnt_wins_all_logic=teamDidntWinAllTwoGames(reshuffler(_2h2h_cut),ALL_SCORES_DIRTY_HOME[0])
    print(f'[home_dnt_wins_all_logic,away_dnt_wins_all_logic] ---> {[home_dnt_wins_all_logic,away_dnt_wins_all_logic]}')
    _5_cutH2H_grand=win_loss_cent(H2H_TUPLE,len(_5_cutH2H))
    last5_matches_h2h_cent_home=_5_cutH2H_grand[0]
    last5_matches_h2h_cent_away=_5_cutH2H_grand[1]
    h2h_min_main=min([last5_matches_h2h_cent_home,last5_matches_h2h_cent_away])
    current_home_h2h_greater=last5_matches_h2h_cent_home>last5_matches_h2h_cent_away
    current_away_h2h_greater=last5_matches_h2h_cent_away>last5_matches_h2h_cent_home
    _5_cut_Other_Matches_Home=ALL_SCORES_DIRTY_HOME[:5]
    homeTeamDraws=h2hAnalysis(ALL_SCORES_DIRTY_HOME)[1]
    HOME_WOUNDS=lastThreeGamesAnalyst(ALL_SCORES_DIRTY_HOME)
    AWAY_WOUNDS=lastThreeGamesAnalyst(ALL_SCORES_DIRTY_AWAY)
    ALL_SCORES_DIRTY_HOME_LAST=ALL_SCORES_DIRTY_HOME[0]
    HomeOtherMlastScrDiff=ALL_SCORES_DIRTY_HOME_LAST[0]-ALL_SCORES_DIRTY_HOME_LAST[1]
    ALL_SCORES_DIRTY_AWAY_LAST=ALL_SCORES_DIRTY_AWAY[0]
    AwayOtherMlastScrDiff=ALL_SCORES_DIRTY_AWAY_LAST[0]-ALL_SCORES_DIRTY_AWAY_LAST[1]
    BOTH_TEAMS_LOST_ON_OTHER_MTC=HomeOtherMlastScrDiff<=-1 and AwayOtherMlastScrDiff<=-1
    _5_cut_Other_Matches_Away=ALL_SCORES_DIRTY_AWAY[:5]
    awayTeamDraws=h2hAnalysis(ALL_SCORES_DIRTY_AWAY)[1]
    lost_games_cent=pillarCents(lost_games_cent_array)
    draws_cent=pillarCents([homeTeamDraws,awayTeamDraws])
    homeTeamDrawsGreater=homeTeamDraws>awayTeamDraws
    awayTeamDrawsGreater=awayTeamDraws>homeTeamDraws
    HomeOtherMatchesPainForce=painForce(ALL_SCORES_DIRTY_HOME)[0]
    AwayOtherMatchesPainForce=painForce(ALL_SCORES_DIRTY_AWAY)[0]
    last5_matches_otherMatches_cent_home=win_loss_cent(ALL_SCORES_DIRTY_HOME,CUT_5_OTHER_M)[0]
    last5_matches_otherMatches_cent_away=win_loss_cent(ALL_SCORES_DIRTY_AWAY,CUT_5_OTHER_M)[0]
    ThisRelatedToUpVariableHome=[last5_matches_h2h_cent_home,last5_matches_otherMatches_cent_home]
    ThisRelatedToUpVariableAway=[last5_matches_h2h_cent_away,last5_matches_otherMatches_cent_away]
    lastScrh2hHomeDiff=_5_cutH2H[0][0]-_5_cutH2H[0][1]
    lastScrOtherMsHomeDiff=_5_cut_Other_Matches_Home[0][0]-_5_cut_Other_Matches_Home[0][1]
    DIFFS_ARR_HOME=[lastScrh2hHomeDiff,lastScrOtherMsHomeDiff]
    lastScrh2hAwayDiff=_5_cutH2H[0][1]-_5_cutH2H[0][0]
    lastScrOtherMsAwayDiff=_5_cut_Other_Matches_Away[0][0]-_5_cut_Other_Matches_Away[0][1]
    DIFFS_ARR_AWAY=[lastScrh2hAwayDiff,lastScrOtherMsAwayDiff]

    HomeNewPerfoVsOldPerfoH2HvsOtherM=ThisRelatedToUpVariableHome[0]-H2H_OTHER_MATCHES_CENT_HOME[0]
    HomeNewPerfoVsOldPerfoH2HvsOtherM2=ThisRelatedToUpVariableHome[1]-H2H_OTHER_MATCHES_CENT_HOME[1]
    HOME_TEAM_TRANSITION=[HomeNewPerfoVsOldPerfoH2HvsOtherM,HomeNewPerfoVsOldPerfoH2HvsOtherM2]

    AwayNewPerfoVsOldPerfoH2HvsOtherM=ThisRelatedToUpVariableAway[0]-H2H_OTHER_MATCHES_CENT_AWAY[0]
    AwayNewPerfoVsOldPerfoH2HvsOtherM2=ThisRelatedToUpVariableAway[1]-H2H_OTHER_MATCHES_CENT_AWAY[1]
    AWAY_TEAM_TRANSITION=[AwayNewPerfoVsOldPerfoH2HvsOtherM,AwayNewPerfoVsOldPerfoH2HvsOtherM2]
    ARR_HOME=[H2H_OTHER_MATCHES_CENT_HOME,ThisRelatedToUpVariableHome]
    ARR_AWAY=[H2H_OTHER_MATCHES_CENT_AWAY,ThisRelatedToUpVariableAway]
    RECENT_SCORES_DIFF=[DIFFS_ARR_HOME,DIFFS_ARR_AWAY]
    TEAM_POINTS_ARR=[home_T_Point,away_T_Point]
    vss=f'{home_T} vs {away_T}'
    meta_add_on0=f'PlayersSatsHome ---> {GRAND_HOME_STATS_LOCAL}\nSusp/Injured Players Home ---> {HOME_SUS_PLAYERS_RECORDS_LOCAL}\n\nPlayersSatsAway ---> {GRAND_AWAY_STATS_LOCAL}\nSusp/Injured Players Away ---> {AWAY_SUS_PLAYERS_RECORDS_LOCAL}'
    meta_addon3=f'Home Strikers Total Goals ---> {HOME_STRIKERS_GOALS_TOTAL_LOCAL}\nAway Strikers Total Goals ---> {AWAY_STRIKERS_GOALS_TOTAL_LOCAL}'
    bytes_=f'{vss}\n{meta_addon3}\n{meta_add_on0}\nEND OF UP DATA\n'.replace('\n\n','\n')
    MY_PREDICTION=homeOrAwayPredictor(ARR_HOME,ARR_AWAY,H_A_NEXT_MATCHES_LOCAL,
                                      [home_T,away_T],
                                      RECENT_SCORES_DIFF,
                                      TEAM_POINTS_ARR,GRAND_HOME_STATS_LOCAL,
                                      GRAND_AWAY_STATS_LOCAL,bytes_)
    MY_PREDICTION_ACTUAL=MY_PREDICTION[0]
    HOME_OR_AWAY_WINS_LOCAL=MY_PREDICTION[2]
    GRAND_HOME_AWAY_DIFF=MY_PREDICTION[3]
    GRAND_HOME_DIFF_MIN_LOCAL=min(GRAND_HOME_AWAY_DIFF[0])
    GRAND_AWAY_DIFF_MIN_LOCAL=min(GRAND_HOME_AWAY_DIFF[1])
    HW=HOME_OR_AWAY_WINS_LOCAL[0]
    AW=HOME_OR_AWAY_WINS_LOCAL[1]
    HOME_OR_AWAY_WINS_LOCAL_MIN=min(HOME_OR_AWAY_WINS_LOCAL)
    HOME_OR_AWAY_WINS_LOCAL_DIFF=HW-AW
    if HOME_OR_AWAY_WINS_LOCAL_DIFF<0:
        HOME_OR_AWAY_WINS_LOCAL_DIFF=-1*HOME_OR_AWAY_WINS_LOCAL_DIFF
    HomeNetGoal_local=MY_PREDICTION_ACTUAL[5]
    AwayNetGoal_local=MY_PREDICTION_ACTUAL[6]
    Homestrickers_out_goals_array_local=MY_PREDICTION_ACTUAL[7]
    Awaystrickers_out_goals_array_local=MY_PREDICTION_ACTUAL[8]
    def netStrikersArr(strikers_arr,strikersAot_arr):
        STRIKERS_OUT_RUNNING_BEAKER=strikers_arr
        for saot in strikersAot_arr:
            try:
                saot_dex=STRIKERS_OUT_RUNNING_BEAKER.index(saot)
                saot_dex_plus=saot_dex+1
                STRIKERS_OUT_RUNNING_BEAKER=STRIKERS_OUT_RUNNING_BEAKER[:saot_dex]+STRIKERS_OUT_RUNNING_BEAKER[saot_dex_plus:]
            except ValueError:
                pass
        return STRIKERS_OUT_RUNNING_BEAKER
    HomeNetStrikersArr=netStrikersArr(HOME_STRIKERS_GOALS_TOTAL_LOCAL,Homestrickers_out_goals_array_local)
    AwayNetStrikersArr=netStrikersArr(AWAY_STRIKERS_GOALS_TOTAL_LOCAL,Awaystrickers_out_goals_array_local)
    goals_net_min=min([HomeNetGoal_local,AwayNetGoal_local])
    goals_net_diff=HomeNetGoal_local-AwayNetGoal_local
    if goals_net_diff<0:
        goals_net_diff=-1*goals_net_diff
    homeStrikersLeading=HomeNetGoal_local>AwayNetGoal_local
    awayStrikersLeading=AwayNetGoal_local>HomeNetGoal_local
    DRAW_POINT=MY_PREDICTION[1]
    HomeLossForces=[HomeH2HPainForce,HomeOtherMatchesPainForce]
    HomeLossForces_sum=sum(HomeLossForces)
    AwayLossForces=[AwayH2HPainForce,AwayOtherMatchesPainForce]
    AwayLossForces_sum=sum(AwayLossForces)
    LossForcesDiffHome=HomeLossForces_sum-AwayLossForces_sum
    LossForcesDiffAway=-1*LossForcesDiffHome
    if LossForcesDiffHome<0:
       LossForcesDiffHome=0
    if LossForcesDiffAway<0:
       LossForcesDiffAway=0
    MY_PREDICTION='Unpredictable'
    TOTAL_LEAGUE_MATCHES=(ALL_TEAMS_LEN_LOCAL*2)-2
    TOTAL_LEAGUE_MATCHES_23rd=round(TOTAL_LEAGUE_MATCHES*(3/4))
    TPM_HOME=len(ALL_SCORES_DIRTY_HOME)
    TPM_AWAY=len(ALL_SCORES_DIRTY_AWAY)
    wall=3
    HOME_STRIKERS_GOALS_TOTAL_LOCAL_3_CUT=HomeNetStrikersArr[:wall]
    AWAY_STRIKERS_GOALS_TOTAL_LOCAL_3_CUT=AwayNetStrikersArr[:wall]
    HOME_STRIKERS_TRULY_CENT=[]
    AWAY_STRIKERS_TRULY_CENT=[]
    if len(HOME_STRIKERS_GOALS_TOTAL_LOCAL_3_CUT)==wall and len(AWAY_STRIKERS_GOALS_TOTAL_LOCAL_3_CUT)==wall:
        for s in range(wall):
            s_home=HOME_STRIKERS_GOALS_TOTAL_LOCAL_3_CUT[s]
            s_home_cent=int((s_home/TPM_HOME)*100)
            HOME_STRIKERS_TRULY_CENT+=[s_home_cent]
            s_away=AWAY_STRIKERS_GOALS_TOTAL_LOCAL_3_CUT[s]
            s_away_cent=int((s_away/TPM_AWAY)*100)
            AWAY_STRIKERS_TRULY_CENT+=[s_away_cent]
    HOME_STRIKERS_TRULY=False
    AWAY_STRIKERS_TRULY=False
    TRUE_STRIKERS_INFO=''
    HOME_STRIKERS_TRULY_MIN=0
    AWAY_STRIKERS_TRULY_MIN=0
    try:
        HOME_STRIKERS_TRULY_MIN=min(HOME_STRIKERS_TRULY_CENT)
        AWAY_STRIKERS_TRULY_MIN=min(AWAY_STRIKERS_TRULY_CENT)
        HOME_STRIKERS_TRULY=HOME_STRIKERS_TRULY_MIN>=30
        AWAY_STRIKERS_TRULY=AWAY_STRIKERS_TRULY_MIN>=30
        TRUE_STRIKERS_INFO=[HOME_STRIKERS_TRULY_CENT,HOME_STRIKERS_TRULY_MIN,HOME_STRIKERS_TRULY,AWAY_STRIKERS_TRULY_CENT,AWAY_STRIKERS_TRULY_MIN,AWAY_STRIKERS_TRULY]
    except ValueError:
        pass
    pure_same_match_diff=home_same_team_cent_local-away_same_team_cent_local
    pure_same_match_min=min([home_same_team_cent_local,away_same_team_cent_local])
    if pure_same_match_diff<0:
       pure_same_match_diff=-1*pure_same_match_diff
    HOME_TEAM=home_away[0]
    AWAY_TEAM=home_away[1].split(" ---> ")[0]
    TEAMS_POINT_ARR=[home_T_Point,away_T_Point]
    home_away_monthly_cents_mixed_array=monthlyPointsCent(MONTHLY_SCORES_GRAND_LOCAL_HOME,MONTHLY_SCORES_GRAND_LOCAL_AWAY)
    CENTS_ARRAY_H2H=h2hAnalyers(PURELY_HOME_AWAY_H2H_SCORES_ARG)
    HOME_COUNT_REC=CENTS_ARRAY_H2H[0]
    AWAY_COUNT_REC=CENTS_ARRAY_H2H[1]
    H2H_CENT_FUSED_DATA=CENTS_ARRAY_H2H[2]
    H2H_COUNT_DATA_CODE=CENTS_ARRAY_H2H[3]
    #[0,1,2,3,4,5,6,7,8,9,10,11]
    FD=H2H_CENT_FUSED_DATA
    FD_HOME=[FD[0],FD[2],FD[4],FD[6],FD[8],FD[10]]
    FD_AWAY=[FD[1],FD[3],FD[5],FD[7],FD[9],FD[11]]
    ash=PURELY_HOME_AWAY_H2H_SCORES_ARG
    asa=PURELY_HOME_AWAY_H2H_SCORES_ARG
    if PURELY_HOME_AWAY_H2H_SCORES_ARG_LEN<=1:
        ash=[(0,0),(0,0)]
        asa=[(0,0),(0,0)]
    LAST_SCORES_INFLUENCE=lastScoresInfluence([[ash[0],ash[1]]],FD_HOME,[[asa[0],asa[1]]],FD_AWAY)
    LSIH=LAST_SCORES_INFLUENCE[0]
    LSIA=LAST_SCORES_INFLUENCE[1]
    LAST_SCORES_INFLUENCE=[LSIH,LSIA]
    DYNAMIC_H2H_USAGE=H2H_TUPLE
    if H2H_TUPLE_LEN<2 and PURELY_HOME_AWAY_H2H_SCORES_ARG_LEN>1:
        DYNAMIC_H2H_USAGE=PURELY_HOME_AWAY_H2H_SCORES_ARG
    if H2H_TUPLE_LEN==1 and PURELY_HOME_AWAY_H2H_SCORES_ARG_LEN==1:
        if PURELY_HOME_AWAY_H2H_SCORES_ARG[0][0]>-1:
            DYNAMIC_H2H_USAGE=PURELY_HOME_AWAY_H2H_SCORES_ARG
        if H2H_TUPLE[0][0]>-1:
            DYNAMIC_H2H_USAGE=H2H_TUPLE
    H2H_DIRTY_SCORES_ARR_HOME=[DYNAMIC_H2H_USAGE[0],ALL_SCORES_DIRTY_HOME[0]]
    HOME_LAST_TWO_SCORES_ARRAY=[DYNAMIC_H2H_USAGE[:2],
                                ALL_SCORES_DIRTY_HOME[:2],
                                H2H_DIRTY_SCORES_ARR_HOME]
    H2H_DIRTY_SCORES_ARR_AWAY=[DYNAMIC_H2H_USAGE[0],ONLY_AWAY_SCORES_REARRANGED[0]]
    AWAY_LAST_TWO_SCORES_ARRAY=[reshuffler(DYNAMIC_H2H_USAGE)[:2],
                                ALL_SCORES_DIRTY_AWAY[:2],
                                H2H_DIRTY_SCORES_ARR_AWAY]
    H2H_DISCRET_FORM_LOCAL=win_loss_cent(PURELY_HOME_AWAY_H2H_SCORES_ARG)[:2]
    H2H_D_FORM_HOME=H2H_DISCRET_FORM_LOCAL[0]
    H2H_D_FORM_AWAY=H2H_DISCRET_FORM_LOCAL[1]
    VERY_OLD_H2H_REC_TRIGGERED=False
    if H2H_TUPLE_FS[0]==-1 and ALL_TIMES_H2H_ARG_FS[0]==-1:
        ATH2HVOLDCENT_H=50#only_home_cent_5_cut#ALL_TIMES_H2H_VERY_OLD_ARG_CENT[0]
        ATH2HVOLDCENT_A=50#only_away_cent_5_cut#ALL_TIMES_H2H_VERY_OLD_ARG_CENT[1]
        H2H_D_FORM_HOME=50
        H2H_D_FORM_AWAY=50
        ALL_TIMES_H2H_ARG_CENT=[50,50]#ALL_TIMES_H2H_VERY_OLD_ARG_CENT
        PURELY_HOME_H2H_CENT=ATH2HVOLDCENT_H
        PURELY_AWAY_H2H_CENT=ATH2HVOLDCENT_A
        VERY_OLD_H2H_REC_TRIGGERED=True
    H2H_D_FORM_DIFF=H2H_D_FORM_HOME-H2H_D_FORM_AWAY
    if H2H_D_FORM_DIFF<0:
        H2H_D_FORM_DIFF=-1*H2H_D_FORM_DIFF
    if len(ONLY_HOME_SCORES)<10 or len(ONLY_AWAY_SCORES_REARRANGED)<10:
       only_home_cent_5_cut_sample=0
       only_away_cent_5_cut_sample=0
    if home_same_team_cent_local_len<10 or away_same_team_cent_local_len<10:
       home_same_team_cent_recent_local=0
       away_same_team_cent_recent_local=0
    all_scores_cent_cut_5_home=ThisRelatedToUpVariableHome[1]
    all_scores_cent_cut_5_away=ThisRelatedToUpVariableAway[1]
    if ALL_SCORES_DIRTY_MAX_LEN<10:
       home_same_team_cent_recent_local=0
       away_same_team_cent_recent_local=0
    WELL_ARRANGED_ARRAY=centsWellArranger([[only_home_score_cent,only_away_score_cent],
                          [only_home_cent_5_cut_sample,only_away_cent_5_cut_sample],
                          [home_same_team_cent_local,away_same_team_cent_local],
                          [home_same_team_cent_recent_local,away_same_team_cent_recent_local],
                          [H2H_OTHER_MATCHES_CENT_HOME[1],H2H_OTHER_MATCHES_CENT_AWAY[1]],
                          [all_scores_cent_cut_5_home,all_scores_cent_cut_5_away]],home_away_monthly_cents_mixed_array)
    POS_CENT=quickCentCalc([AwayteamPosition,HometeamPosition])
    CENTS_ARRAY = drawProjectorCent(WELL_ARRANGED_ARRAY)
    GRAND_DIV=quickDivider([H2H_HOME_CENT,H2H_AWAY_CENT],
                            [H2H_OTHER_MATCHES_CENT_HOME[1],H2H_OTHER_MATCHES_CENT_AWAY[1]],
                            [ThisRelatedToUpVariableHome[1],ThisRelatedToUpVariableAway[1]],
                            [only_home_score_cent,only_away_score_cent],
                            [only_home_cent_5_cut_sample,only_away_cent_5_cut_sample])
    HOME_POINT_LOST_CENT=lossCentCalc(ALL_SCORES_DIRTY_HOME)[0]
    AWAY_POINT_LOST_CENT=lossCentCalc(ALL_SCORES_DIRTY_AWAY)[0]
    GRAND_LOSES_ARRAY=currentLosesCent(HOME_LAST_TWO_SCORES_ARRAY,AWAY_LAST_TWO_SCORES_ARRAY)
    HOME_RECENT_LOSES_CENT=GRAND_LOSES_ARRAY[0]
    AWAY_RECENT_LOSES_CENT=GRAND_LOSES_ARRAY[1]
    OLD_AND_NEW_LOST_POINTS_SUM=quickCentCalc([LAST_LOST_POINTS_CENT[0],LAST_LOST_POINTS_CENT[1]])
    GG_RECENT_INSTI1=c_abs(HOME_RECENT_LOSES_CENT-AWAY_RECENT_LOSES_CENT)
    GG_RECENT_INSTI2=c_abs(LAST_LOST_POINTS_CENT[0]-LAST_LOST_POINTS_CENT[1])
    GG_SURE=GG_RECENT_INSTI1<=4 and min(GRAND_LOSES_ARRAY)>0 and GG_RECENT_INSTI2<=4 and min(LAST_LOST_POINTS_CENT)>0
    INCRE_DECRE=incrementOrDecrease([only_home_cent_5_cut_sample,only_away_cent_5_cut_sample,
                                     home_same_team_cent_local,ONLY_SAME_TEAMS_HOME_RECENT_CENT,
                                     H2H_OTHER_MATCHES_CENT_HOME[0],ThisRelatedToUpVariableHome[0],
                                     H2H_OTHER_MATCHES_CENT_HOME[1],ThisRelatedToUpVariableHome[1]],[only_away_score_cent,only_away_cent_5_cut,
                                       away_same_team_cent_local,ONLY_SAME_TEAMS_AWAY_RECENT_CENT,
                                       H2H_OTHER_MATCHES_CENT_AWAY[0],ThisRelatedToUpVariableAway[0],
                                       H2H_OTHER_MATCHES_CENT_AWAY[1],ThisRelatedToUpVariableAway[1]])
    # GG_STRIKED=GG_predictor(PURELY_HOME_AWAY_H2H_SCORES_ARG,
    #                             [PURELY_HOME_H2H_CENT,PURELY_AWAY_H2H_CENT],
    #                        [only_home_score_cent,only_away_score_cent],
    #                        HOME_WOUNDS,AWAY_WOUNDS,
    #                        CENTS_ARRAY)
    print(f'LAST_SCORES_INFLUENCE ---> {LAST_SCORES_INFLUENCE}')
    print(f'INCRE_DECRE ---> {INCRE_DECRE}\n')
    print(f'H2H_DISCRET_FORM_LOCAL ---> {H2H_DISCRET_FORM_LOCAL}\n')
    print(f'{H2H_COUNT_DATA_CODE}\n{HOME_COUNT_REC}\n{AWAY_COUNT_REC}\n')
    HOME_INCRE=INCRE_DECRE[0][0]
    AWAY_INCRE=INCRE_DECRE[0][1]
    HOME_DECRE=INCRE_DECRE[1][0]
    AWAY_DECRE=INCRE_DECRE[1][1]
    lost_points_diff=HOME_POINT_LOST_CENT-AWAY_POINT_LOST_CENT
    if lost_points_diff<0:
        lost_points_diff=-1*lost_points_diff
    GRAND_DIV_SUM_HOME=GRAND_DIV[2][0]
    GRAND_DIV_SUM_AWAY=GRAND_DIV[2][1]
    G_DIFF=GRAND_DIV_SUM_HOME-GRAND_DIV_SUM_AWAY
    if G_DIFF<0:
        G_DIFF=-1*G_DIFF
    print(f'GRAND_DIV ---> {GRAND_DIV}\n')
    HOME_WINS_OVERALL=CENTS_ARRAY[0]
    AWAY_WINS_OVERALL=CENTS_ARRAY[1]
    DRAW_WINS_OVERALL=CENTS_ARRAY[2]
    GRAND_COUNT=CENTS_ARRAY[3]
    CUSTOM_POSITION_ARRAY=[HometeamPosition,AwayteamPosition]
    if HometeamPosition==AwayteamPosition:
        CUSTOM_POSITION_ARRAY=[GRAND_COUNT[1],GRAND_COUNT[0]]
    GRAND_COUNT_HOME=GRAND_COUNT[0]
    GRAND_COUNT_AWAY=GRAND_COUNT[1]
    GRAND_COUNT_CENT=quickCentCalc([GRAND_COUNT_HOME,GRAND_COUNT_AWAY])
    HOME_DRAWS_DISCRETE_CENT=CENTS_ARRAY[5][0]
    AWAY_DRAWS_DISCRETE_CENT=CENTS_ARRAY[6][0]
    OVERALL_FDFF=HOME_WINS_OVERALL-AWAY_WINS_OVERALL
    if OVERALL_FDFF<0:
       OVERALL_FDFF=-1*OVERALL_FDFF
    TEAMS_PLUS1_DRAWS_CENT=teamPlus1DrawsCent(ALL_SCORES_DIRTY_HOME,ALL_SCORES_DIRTY_AWAY)
    HOME_RESILIENCE_LEVEL=TEAMS_PLUS1_DRAWS_CENT[0]
    AWAY_RESILIENCE_LEVEL=TEAMS_PLUS1_DRAWS_CENT[1]
    HOME_STRU=HOME_RESILIENCE_LEVEL+HOME_LOST_BY_ONE_USED+HOME_WINS_DRAWS_CENT+ONLY_HOME_SCORES_OVER_2GLS_CENT
    AWAY_STRU=AWAY_RESILIENCE_LEVEL+AWAY_LOST_BY_ONE_USED+AWAY_WINS_DRAWS_CENT+ONLY_AWAY_SCORES_OVER_2GLS_CENT
    TEAM_STRUCTURE_ARRAY=quickCentCalc([HOME_STRU,AWAY_STRU])
    OTHER_MATCHES_FORM_HOME=CENTS_ARRAY[4][0]#+AwayteamPosition
    OTHER_MATCHES_FORM_AWAY=CENTS_ARRAY[4][1]#+HometeamPosition
    TOTAL_LOSES_INSTIGATION=quickCentCalc([HOME_RECENT_LOSES_CENT+OLD_AND_NEW_LOST_POINTS_SUM[0],AWAY_RECENT_LOSES_CENT+OLD_AND_NEW_LOST_POINTS_SUM[1]])
    HTIM_ORGANIC_POINT_CENT_USED=HTIM_ORGANIC_POINT_CENT
    ATIM_ORGANIC_POINT_CENT_USED=ATIM_ORGANIC_POINT_CENT
    H2H_COEFFIE=deci_creater(H2H_DISCRET_FORM_LOCAL)
    PosAvgGtrThanOrEquals5=teamsPosMarginDeterminer(ALL_TEAMS_LEN_LOCAL,[HometeamPosition,AwayteamPosition])
    if PosAvgGtrThanOrEquals5:
        HTIM_ORGANIC_POINT_CENT_USED=BELOW_TEAMS_POS_GAME_CENTS[0][0]+HometopGuysCent
        ATIM_ORGANIC_POINT_CENT_USED=BELOW_TEAMS_POS_GAME_CENTS[0][1]+AwaytopGuysCent
    TEAMS_ORE_SCORES_AVERAGE=quickCentCalc([HTIM_ORGANIC_POINT_CENT_USED,ATIM_ORGANIC_POINT_CENT_USED])
    LAST_H2H_SCORE_CENT=quickCentCalc([H2H_TUPLE[0][0],H2H_TUPLE[0][1]])
    OP_H2H_HOME=PURELY_HOME_H2H_CENT+LAST_H2H_SCORE_CENT[0]
    OP_H2H_AWAY=PURELY_AWAY_H2H_CENT+LAST_H2H_SCORE_CENT[1]
    DYNAMIC_H2H_DIFF=c_abs(PURELY_HOME_H2H_CENT-PURELY_AWAY_H2H_CENT)
    FINAl_H2H_ACCURATE=True
    if DYNAMIC_H2H_DIFF<10 and H2H_TUPLE_LEN<3:
        OP_H2H_HOME=OP_H2H_HOME+ALL_TIMES_H2H_ARG_CENT[0]+H2H_D_FORM_HOME
        OP_H2H_AWAY=OP_H2H_AWAY+ALL_TIMES_H2H_ARG_CENT[1]+H2H_D_FORM_AWAY
        FINAl_H2H_ACCURATE=False
    QUICK_CENT13=quickCentCalc([OP_H2H_HOME,OP_H2H_AWAY])
    H2H_ROUGH_MIXED_HOME=ALL_TIMES_H2H_ARG_CENT[0]+PURELY_HOME_H2H_CENT+LAST_H2H_SCORE_CENT[0]
    H2H_ROUGH_MIXED_AWAY=ALL_TIMES_H2H_ARG_CENT[1]+PURELY_AWAY_H2H_CENT+LAST_H2H_SCORE_CENT[1]
    H2H_ROUGH_MIXED=quickCentCalc([H2H_ROUGH_MIXED_HOME,H2H_ROUGH_MIXED_AWAY])
    HOME_H2H_FINAL_FORM=QUICK_CENT13[0]
    AWAY_H2H_FINAL_FORM=QUICK_CENT13[1]
    H2H_ROUGH_MIXED=quickCentCalc([H2H_ROUGH_MIXED[0]+HOME_H2H_FINAL_FORM,H2H_ROUGH_MIXED[1]+AWAY_H2H_FINAL_FORM])
    if FINAl_H2H_ACCURATE:
        H2H_ROUGH_MIXED=QUICK_CENT13
    TEAMS_VETERAN_STATUS=[H2H_ROUGH_MIXED[0]>=H2H_ROUGH_MIXED[1],H2H_ROUGH_MIXED[1]>=H2H_ROUGH_MIXED[0]]
    HOME_ALL_SCORES_STRIKE_HUB=teamStrikersPotential(ALL_SCORES_DIRTY_HOME,1)
    HOME_ALL_SCORES_STRIKE=HOME_ALL_SCORES_STRIKE_HUB[:2]
    HOME_ALL_SCORES_STRIKE_OLD=HOME_ALL_SCORES_STRIKE_HUB[2]
    HOME_ALL_SCORES_STRIKE_CENT=HOME_ALL_SCORES_STRIKE[0]
    AWAY_ALL_SCORES_STRIKE_HUB=teamStrikersPotential(ALL_SCORES_DIRTY_AWAY,1)
    AWAY_ALL_SCORES_STRIKE=AWAY_ALL_SCORES_STRIKE_HUB[:2]
    AWAY_ALL_SCORES_STRIKE_OLD=AWAY_ALL_SCORES_STRIKE_HUB[2]
    AWAY_ALL_SCORES_STRIKE_CENT=AWAY_ALL_SCORES_STRIKE[0]
    STRIKER_CENT_ABS_DIFF=abs(HOME_ALL_SCORES_STRIKE_CENT-AWAY_ALL_SCORES_STRIKE_CENT)
    H2H_X_LOST_P_CENT=h2h_lastXLostPoints(H2H_TUPLE[:1])
    HOME_LAST_SCORES_LOSS=lastScoresLostTrigger(H2H_TUPLE[0],ALL_SCORES_DIRTY_HOME[0])
    AWAY_LAST_SCORES_LOSS=lastScoresLostTrigger(reshuffler(H2H_TUPLE)[0],ALL_SCORES_DIRTY_AWAY[0])
    HIDDEN_LOSSES_USED_HOME=HIDDEN_LOSSES_HOME
    HIDDEN_LOSSES_USED_AWAY=HIDDEN_LOSSES_AWAY
    if LOSSES_PATTERN_TRIGGERED_HOME:
       HIDDEN_LOSSES_USED_HOME=0
    if LOSSES_PATTERN_TRIGGERED_AWAY:
       HIDDEN_LOSSES_USED_AWAY=0
    FRESH_WOUNDS=[HIDDEN_LOSSES_USED_HOME+HOME_LAST_SCORES_LOSS+max([HOME_LAST_SCORES_LOSS,HOME_WOUND_PATTERNS_USED]),HIDDEN_LOSSES_USED_AWAY+AWAY_LAST_SCORES_LOSS+max([AWAY_LAST_SCORES_LOSS,AWAY_WOUND_PATTERNS_USED])]
    if FRESH_WOUNDS[0]==FRESH_WOUNDS[1]:
        FRESH_WOUNDS=[HOME_WOUND_PATTERNS,AWAY_WOUND_PATTERNS]
    DYNAMIC_WOUNDS_ARRAY=FRESH_WOUNDS
    DYNAMIC_WOUNDS_ARRAY_ORIGINAL=DYNAMIC_WOUNDS_ARRAY
    COMPROMISED_WOUNS_1=formCent([CUSTOM_POSITION_ARRAY[1],CUSTOM_POSITION_ARRAY[0]],DYNAMIC_WOUNDS_ARRAY)
    COMPROMISED_WOUNS=oldFormDeci([COMPROMISED_WOUNS_1])
    DYNAMIC_WOUNDS_ARRAY=COMPROMISED_WOUNS
    C_DRIVEN_FORCE=DYNAMIC_WOUNDS_ARRAY
    TEAMS_ORE_SCORES_AVERAGE=quickCentCalc([HTIM_ORGANIC_POINT_CENT_USED,ATIM_ORGANIC_POINT_CENT_USED])
    HOME_ALL_SCORES_STRIKE_USED=HOME_ALL_SCORES_STRIKE_CENT
    AWAY_ALL_SCORES_STRIKE_USED=AWAY_ALL_SCORES_STRIKE_CENT
    STRIKERS_COUNT_MAX=max([HOME_ALL_SCORES_STRIKE[1],AWAY_ALL_SCORES_STRIKE[1]])
    STRIKERS_CENT_MAX=max([HOME_ALL_SCORES_STRIKE_USED,AWAY_ALL_SCORES_STRIKE_USED])
    if STRIKERS_COUNT_MAX<=4 and STRIKERS_CENT_MAX<=50:
        HOME_ALL_SCORES_STRIKE_USED=HOME_ALL_SCORES_STRIKE[1]
        AWAY_ALL_SCORES_STRIKE_USED=AWAY_ALL_SCORES_STRIKE[1]
    if ONLY_SCORES_MAX_LEN<5:
        only_home_score_cent_used=0
        only_away_score_cent_used=0
    DISCRE_SPECIAL_SUM_HOME=HOME_LOST_BY_ONE+CENTS_ARRAY[3][0]+HOME_ALL_SCORES_STRIKE_USED+OTHER_MATCHES_FORM_HOME
    DISCRE_SPECIAL_SUM_AWAY=AWAY_LOST_BY_ONE+CENTS_ARRAY[3][1]+AWAY_ALL_SCORES_STRIKE_USED+OTHER_MATCHES_FORM_AWAY
    ATTACKS_PLUS_SHOTS_ON_TARGET_CENT_H=TEAMS_ATTACK_CENT_ARG[0]+TEAMS_SHOTS_ON_TARGET_CENTS_ARG[0]
    ATTACKS_PLUS_SHOTS_ON_TARGET_CENT_A=TEAMS_ATTACK_CENT_ARG[1]+TEAMS_SHOTS_ON_TARGET_CENTS_ARG[1]
    HOME_ATTACKS_PLUS_WOUNDS=ATTACKS_PLUS_SHOTS_ON_TARGET_CENT_H+HOME_WOUND_PATTERNS
    AWAY_ATTACKS_PLUS_WOUNDS=ATTACKS_PLUS_SHOTS_ON_TARGET_CENT_A+AWAY_WOUND_PATTERNS
    ATT_AND_SOT=quickCentCalc([ATTACKS_PLUS_SHOTS_ON_TARGET_CENT_H,ATTACKS_PLUS_SHOTS_ON_TARGET_CENT_A])
    ATT_WND_HUB=quickCentCalc([HOME_ATTACKS_PLUS_WOUNDS,AWAY_ATTACKS_PLUS_WOUNDS])
    QUICK_CENT11=quickCentCalc([DISCRE_SPECIAL_SUM_HOME,DISCRE_SPECIAL_SUM_AWAY])
    OTHER_MATCHES_FF_HOME=QUICK_CENT11[0]
    OTHER_MATCHES_FF_AWAY=QUICK_CENT11[1]
    FORM_CENT_QUICK=formCent([1,1],QUICK_CENT11)
    HOME_FINAL_FORM=FORM_CENT_QUICK[0]
    AWAY_FINAL_FORM=FORM_CENT_QUICK[1]
    FINAL_FORM_AND_ATTACKS_PLUS_SOT=quickCentCalc([ATT_AND_SOT[0]+HOME_FINAL_FORM,ATT_AND_SOT[1]+AWAY_FINAL_FORM])
    OVER_SHADOWED_CENTS_HUB=overshadowedPlusFormPlusWounds([[PURELY_HOME_H2H_CENT,PURELY_AWAY_H2H_CENT],LAST_H2H_SCORE_CENT,ALL_TIMES_H2H_ARG_CENT],
                                                            FORM_CENT_QUICK,
                                                            [HOME_WOUND_PATTERNS,AWAY_WOUND_PATTERNS],H2H_TUPLE_LEN)
    OVER_SHADOWED_CENTS=OVER_SHADOWED_CENTS_HUB[0]
    H2H_LDS_COUNT=OVER_SHADOWED_CENTS_HUB[1]
    H2H_LDS_COUNT_CENT=quickCentCalc(H2H_LDS_COUNT)
    HOME_SENSITIVE_CENT_REC=OLD_AND_NEW_LOST_POINTS_SUM[0]+OTHER_MATCHES_FORM_HOME
    AWAY_SENSITIVE_CENT_REC=OLD_AND_NEW_LOST_POINTS_SUM[1]+OTHER_MATCHES_FORM_AWAY
    LOST_POINTS_TOTAL_PLUS_OMTC_FORM_CENT=quickCentCalc([HOME_SENSITIVE_CENT_REC,AWAY_SENSITIVE_CENT_REC])
    HOME_FINAL_FORM_PLUS_WOUNDS=HOME_FINAL_FORM+C_DRIVEN_FORCE[0]+HOME_ALL_SCORES_STRIKE_CENT#+HOME_POINT_LOST_CENT
    AWAY_FINAL_FORM_PLUS_WOUNDS=AWAY_FINAL_FORM+C_DRIVEN_FORCE[1]+AWAY_ALL_SCORES_STRIKE_CENT#+AWAY_POINT_LOST_CENT
    QUICK_CENT14=quickCentCalc([HOME_FINAL_FORM_PLUS_WOUNDS,AWAY_FINAL_FORM_PLUS_WOUNDS])
    UNI_COEFFICIENT=deci_creater([HOME_H2H_FINAL_FORM,AWAY_H2H_FINAL_FORM])
    HOME_COEFFI=UNI_COEFFICIENT[0]
    AWAY_COEFFI=UNI_COEFFICIENT[1]
    UNI_OTMCS_COEFFICIENT=deci_creater([OTHER_MATCHES_FORM_HOME,OTHER_MATCHES_FORM_AWAY])
    FINAL_FORM_DIFF=c_abs(HOME_FINAL_FORM-AWAY_FINAL_FORM)
    #home_T_Point
    #HometeamPosition
    #away_T_Point
    #AwayteamPosition
    home_trans_diff=HOME_TEAM_TRANSITION[1]-AWAY_TEAM_TRANSITION[1]
    away_trans_diff=AWAY_TEAM_TRANSITION[1]-HOME_TEAM_TRANSITION[1]
    GG_OVER_1_CENT=ggCent(PURELY_HOME_AWAY_H2H_SCORES_ARG[:15])
    GLDFF=c_abs(HOME_RECENT_LOSES_CENT-AWAY_RECENT_LOSES_CENT)
    FF_DFF=c_abs(HOME_FINAL_FORM-AWAY_FINAL_FORM)
    HOME_AWAY_LOST_POINTS_CENT=[HOME_POINT_LOST_CENT,AWAY_POINT_LOST_CENT]
    DRAW_STRIKES=DRAW_WINS_OVERALL>=HOME_WINS_OVERALL and DRAW_WINS_OVERALL>=AWAY_WINS_OVERALL
    DRAW_STRIKES=DRAW_STRIKES or OVERALL_FDFF<=15 or FF_DFF<=15
    MatchStageArray=['PLAY-OFF','SEMI-FINALS','FINALS','PLAYOFFS']
    LEAGUE_STAGE_FINALS=False
    for ms in MatchStageArray:
        if ms in league_title_arg2:
            LEAGUE_STAGE_FINALS=True
    PREDICTIONS_MADE=False
    HOME_STRU_ARR=[HOME_LOST_BY_ONE_USED,HOME_WINS_DRAWS_CENT,HOME_RESILIENCE_LEVEL,ONLY_HOME_SCORES_OVER_2GLS_CENT]
    AWAY_STRU_ARR=[AWAY_LOST_BY_ONE_USED,AWAY_WINS_DRAWS_CENT,AWAY_RESILIENCE_LEVEL,ONLY_AWAY_SCORES_OVER_2GLS_CENT]
    TEAM_STRUCT_LOGIC=teamsStructuralLogic([HOME_STRU_ARR,AWAY_STRU_ARR],TEAM_STRUCTURE_ARRAY)
    CDF_HOME=C_DRIVEN_FORCE[0]
    CDF_AWAY=C_DRIVEN_FORCE[1]
    CDF_HOME_DIV=CDF_HOME
    CDF_AWAY_DIV=CDF_AWAY
    def quickLossesDiv(losses_driven):
        C_DRIVEN_FORCE_ELE=[]
        for cde in losses_driven:
            adde=cde
            if adde==0:
               adde=1
            C_DRIVEN_FORCE_ELE+=[adde]
        CDF_HOME2=C_DRIVEN_FORCE_ELE[0]
        CDF_AWAY2=C_DRIVEN_FORCE_ELE[1]
        try:
           CDF_HOME_DIV=round((CDF_AWAY2/CDF_HOME2),2)
        except ZeroDivisionError:
           pass
        try:
           CDF_AWAY_DIV=round((CDF_HOME2/CDF_AWAY2),2)
        except ZeroDivisionError:
           pass
        return [CDF_HOME_DIV,CDF_AWAY_DIV]
    DRIVEN_FORCES_COMBI=[C_DRIVEN_FORCE[0]+HOME_LAST_SCORES_LOSS,C_DRIVEN_FORCE[1]+AWAY_LAST_SCORES_LOSS]
    CDF_DIV=quickLossesDiv(DRIVEN_FORCES_COMBI)
    CDF_DIV_ABS_DFF=round(c_abs(CDF_DIV[0]-CDF_DIV[1]),2)
    CDF_LAST_GAMES_DIV=quickLossesDiv([HOME_LAST_SCORES_LOSS,AWAY_LAST_SCORES_LOSS])
    CDF_HOME=C_DRIVEN_FORCE[0]
    CDF_AWAY=C_DRIVEN_FORCE[1]
    C_DRIVEN_FORCE_DIFF_ABS=c_abs(CDF_HOME-CDF_AWAY)
    HOME_KILLER=not home_dnt_wins_all_logic and C_DRIVEN_FORCE_DIFF_ABS>2 and CDF_HOME<CDF_AWAY
    AWAY_KILLER=not away_dnt_wins_all_logic and C_DRIVEN_FORCE_DIFF_ABS>2 and CDF_AWAY<CDF_HOME
    ONLY_HOME_SCORES_LAST_SC_DIFF=ONLY_HOME_SCORES[0][0]-ONLY_HOME_SCORES[0][1]
    ONLY_AWAY_SCORES_LAST_SC_DIFF=ONLY_AWAY_SCORES[0][1]-ONLY_AWAY_SCORES[0][0]
    LAST_WOUNDS_SQUAD=[HOME_LAST_SCORES_LOSS,AWAY_LAST_SCORES_LOSS,HOME_WOUND_PATTERNS,AWAY_WOUND_PATTERNS]
    loss_decimal=lossTruely(H2H_ROUGH_MIXED,C_DRIVEN_FORCE)
    C_DRIVEN_FORCE_PLUS_POS_HOME=loss_decimal[0]
    C_DRIVEN_FORCE_PLUS_POS_AWAY=loss_decimal[1]
    Oth_M_Truly=formCent(H2H_ROUGH_MIXED,[ThisRelatedToUpVariableHome[1],ThisRelatedToUpVariableAway[1]])
    OVER_SHADOWED_CENTS=quickCentCalc([OVER_SHADOWED_CENTS[0]+Oth_M_Truly[0],OVER_SHADOWED_CENTS[1]+Oth_M_Truly[1]])
    FINAL_FORM_AND_OVER_SHADOWED_CENTS=quickCentCalc([HOME_FINAL_FORM+OVER_SHADOWED_CENTS[0],AWAY_FINAL_FORM+OVER_SHADOWED_CENTS[1]])
    HOME_TEAM_TRANSITION_sum=sum(HOME_TEAM_TRANSITION)
    AWAY_TEAM_TRANSITION_sum=sum(AWAY_TEAM_TRANSITION)
    FINAL_FORM_AND_OVER_SHADOWED_CENTS=quickCentCalc([HOME_TEAM_TRANSITION_sum+FINAL_FORM_AND_OVER_SHADOWED_CENTS[0],AWAY_TEAM_TRANSITION_sum+FINAL_FORM_AND_OVER_SHADOWED_CENTS[1]])
    PURELY_HOME_H2H_CENT_USD=PURELY_HOME_H2H_CENT
    PURELY_AWAY_H2H_CENT_USD=PURELY_AWAY_H2H_CENT
    if H2H_TUPLE_LEN<2:
       PURELY_HOME_H2H_CENT_USD=H2H_ROUGH_MIXED[0]
       PURELY_AWAY_H2H_CENT_USD=H2H_ROUGH_MIXED[1]
    BLEEDING_UPPER_H2H_HOME=PURELY_HOME_H2H_CENT_USD>PURELY_AWAY_H2H_CENT_USD and CDF_HOME>=CDF_AWAY
    BLEEDING_UPPER_H2H_AWAY=PURELY_AWAY_H2H_CENT_USD>PURELY_HOME_H2H_CENT_USD and CDF_AWAY>=CDF_HOME
    HOME_QUALITIES_ARR=[TEAMS_1st2_CONSISTENCY_CENT[0],HOME_FINAL_FORM,OVER_SHADOWED_CENTS[0],FINAL_FORM_AND_OVER_SHADOWED_CENTS[0],only_home_cent_5_cut]
    AWAY_QUALITIES_ARR=[TEAMS_1st2_CONSISTENCY_CENT[1],AWAY_FINAL_FORM,OVER_SHADOWED_CENTS[1],FINAL_FORM_AND_OVER_SHADOWED_CENTS[1],only_away_cent_5_cut]
    QUALITIES_COUNT=qualitiesCount(HOME_QUALITIES_ARR,AWAY_QUALITIES_ARR)
    QUALITIES_COUNT_COUNTS=[QUALITIES_COUNT[0],QUALITIES_COUNT[1]]
    QUALITIES_COUNT=formCent(H2H_ROUGH_MIXED,QUALITIES_COUNT[2])
    QUALITIES_COUNT_COUNTS=[QUALITIES_COUNT[0],QUALITIES_COUNT[1]]
    QUALITIES_COUNT=[QUALITIES_COUNT_COUNTS[0],QUALITIES_COUNT_COUNTS[1],QUALITIES_COUNT]
    HOME_QUALITIES_ELE=QUALITIES_COUNT[2][0]
    AWAY_QUALITIES_ELE=QUALITIES_COUNT[2][1]
    QUALITY_COUNT_NUMS=[QUALITIES_COUNT[0],QUALITIES_COUNT[1]]
    QUALITIES_COUNTER=formCent(QUALITY_COUNT_NUMS,QUALITIES_COUNT[2])
    if (HOME_QUALITIES_ELE>AWAY_QUALITIES_ELE and QUALITIES_COUNT[0]<QUALITIES_COUNT[1]) or (AWAY_QUALITIES_ELE>HOME_QUALITIES_ELE and QUALITIES_COUNT[1]<QUALITIES_COUNT[0]):
        QUALITIES_COUNT=[QUALITY_COUNT_NUMS[0],QUALITY_COUNT_NUMS[1],QUALITIES_COUNTER]
    HOME_QUALITIES=QUALITIES_COUNT[2][0]
    AWAY_QUALITIES=QUALITIES_COUNT[2][1]
    if VERY_OLD_H2H_REC_TRIGGERED:
       PURELY_HOME_H2H_CENT_USD=only_home_cent_5_cut
       PURELY_AWAY_H2H_CENT_USD=only_away_cent_5_cut
    OVER_SHADOWED_CENTS_COUNTER=[C_DRIVEN_FORCE[0]+PURELY_HOME_H2H_CENT_USD,C_DRIVEN_FORCE[1]+PURELY_AWAY_H2H_CENT_USD]
    OVER_SHADOWED_CENTS_COUNTER_ABS_DIFF_H=OVER_SHADOWED_CENTS_COUNTER[0]-OVER_SHADOWED_CENTS_COUNTER[1]
    OVER_SHADOWED_CENTS_COUNTER_ABS_DIFF_A=OVER_SHADOWED_CENTS_COUNTER[1]-OVER_SHADOWED_CENTS_COUNTER[0]
    H2H_ABS_DIFF=c_abs(PURELY_HOME_H2H_CENT_USD-PURELY_AWAY_H2H_CENT_USD)
    if H2H_ABS_DIFF>10 and not VERY_OLD_H2H_REC_TRIGGERED:
        PURELY_HOME_H2H_CENT_USD=H2H_DIFF_MODAL_CENT[0]
        PURELY_AWAY_H2H_CENT_USD=H2H_DIFF_MODAL_CENT[1]
    if not BLEEDING_UPPER_H2H_HOME and not BLEEDING_UPPER_H2H_AWAY:
        OVER_SHADOWED_CENTS_COUNTER=[C_DRIVEN_FORCE[0]+PURELY_HOME_H2H_CENT_USD,C_DRIVEN_FORCE[1]+PURELY_AWAY_H2H_CENT_USD]
    if not BLEEDING_UPPER_H2H_AWAY and not BLEEDING_UPPER_H2H_HOME:
        OVER_SHADOWED_CENTS_COUNTER=[C_DRIVEN_FORCE[0]+PURELY_HOME_H2H_CENT_USD,C_DRIVEN_FORCE[1]+PURELY_AWAY_H2H_CENT_USD]
    QUALITIES_COUNT_abs_diff=c_abs(HOME_QUALITIES-AWAY_QUALITIES)
    ROUGH_FINAL_TEAMS_FORM=formCent(OVER_SHADOWED_CENTS_COUNTER,QUALITIES_COUNT[2])
    ROUGH_FINAL_TEAMS_FORM=formCent(H2H_DIFF_MODAL_CENT,ROUGH_FINAL_TEAMS_FORM)
    POS_COUNTER_WOUNDS_CENT=pos_wc_counter_cent([HometeamPosition,AwayteamPosition],[CENTS_ARRAY[3][0],CENTS_ARRAY[3][1]],[0,0],C_DRIVEN_FORCE,H2H_ROUGH_MIXED)
    C_DRIVEN_FORCE_CENT=DYNAMIC_WOUNDS_ARRAY
    QUALITIES_LOSSES_SLICE=formCent(C_DRIVEN_FORCE_CENT,QUALITIES_COUNT[2])
    #QUALITIES_LOSSES_SLICE=formCent(H2H_ROUGH_MIXED,QUALITIES_LOSSES_SLICE)
    ROUGH_FF_POS_CENT=quickCentCalc([ROUGH_FINAL_TEAMS_FORM[0]+POS_COUNTER_WOUNDS_CENT[0],ROUGH_FINAL_TEAMS_FORM[1]+POS_COUNTER_WOUNDS_CENT[1]])
    #ROUGH_FF_POS_CENT=quickCentCalc([QUALITIES_LOSSES_SLICE[0]+ROUGH_FF_POS_CENT[0],QUALITIES_LOSSES_SLICE[1]+ROUGH_FF_POS_CENT[1]])
    HOME_POINTS_LEFT_TO_QUALIFY=sum(HOME_OBSTACLE_POINTS_IMPO)-home_T_Point
    HOME_POINTS_LEFT_TO_QUALIFY_used=HOME_POINTS_LEFT_TO_QUALIFY
    AWAY_POINTS_LEFT_TO_QUALIFY=sum(AWAY_OBSTACLE_POINTS_IMPO)-away_T_Point
    AWAY_POINTS_LEFT_TO_QUALIFY_used=AWAY_POINTS_LEFT_TO_QUALIFY
    if HOME_POINTS_LEFT_TO_QUALIFY_used<0:
       HOME_POINTS_LEFT_TO_QUALIFY_used=0
    if AWAY_POINTS_LEFT_TO_QUALIFY_used<0:
       AWAY_POINTS_LEFT_TO_QUALIFY_used=0
    POINTS_LEFT_HUNGER=formCent(H2H_ROUGH_MIXED,[HOME_POINTS_LEFT_TO_QUALIFY_used,AWAY_POINTS_LEFT_TO_QUALIFY_used])
    STRIKE_DEFENCE_CENT=quickCentCalcUnique([HOME_ALL_SCORES_STRIKE_CENT+HOME_LOST_BY_ONE,AWAY_ALL_SCORES_STRIKE_CENT+AWAY_LOST_BY_ONE])
    STRIKE_DEFENCE_CENT_PURE_OLD=quickCentCalcUnique([HOME_ALL_SCORES_STRIKE_OLD[0]+PURE_OLD_TEAMS_DEFENCE[0],AWAY_ALL_SCORES_STRIKE_OLD[0]+PURE_OLD_TEAMS_DEFENCE[1]])
    STRIKE_DEFENCE_CENT_USED=STRIKE_DEFENCE_CENT
    STRIKE_DEFENCE_CENT_FREE_H2H=STRIKE_DEFENCE_CENT
    STRIKE_DEFENCE_CENT=formCent(H2H_ROUGH_MIXED,STRIKE_DEFENCE_CENT)
    STRIKE_DEFENCE_CENT_ABS_DIFF=abs(STRIKE_DEFENCE_CENT[0]-STRIKE_DEFENCE_CENT[1])
    STRIKE_DEFENCE_CENT_NEW=quickCentCalcUnique([sum(MICRO_STRIKE_DEFENCE_HOME),sum(MICRO_STRIKE_DEFENCE_AWAY)])
    STRIKE_DEFENCE_CENT_NEW_USED=STRIKE_DEFENCE_CENT_NEW
    STRIKE_DEFENCE_CENT_NEW=formCent(H2H_ROUGH_MIXED,STRIKE_DEFENCE_CENT_NEW)
    STRIKE_DEFENCE_CENT_DYNAMIC=quickCentCalcUnique([H2H_ROUGH_MIXED[0]+sum(MICRO_STRIKE_DEFENCE_HOME)+HOME_ALL_SCORES_STRIKE_CENT+HOME_LOST_BY_ONE,H2H_ROUGH_MIXED[1]+sum(MICRO_STRIKE_DEFENCE_AWAY)+AWAY_ALL_SCORES_STRIKE_CENT+AWAY_LOST_BY_ONE])
    STRIKE_DEFENCE_LOSSES_CENT=quickCentCalc([STRIKE_DEFENCE_CENT[0]+C_DRIVEN_FORCE_CENT[0],STRIKE_DEFENCE_CENT[1]+C_DRIVEN_FORCE_CENT[1]])
    STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT=quickCentCalcUnique([STRIKE_DEFENCE_CENT_DYNAMIC[0]+C_DRIVEN_FORCE_CENT[0],STRIKE_DEFENCE_CENT_DYNAMIC[1]+C_DRIVEN_FORCE_CENT[1]])
    STRIKE_DEFENCE_LOSSES_CENT_NEW=quickCentCalc([STRIKE_DEFENCE_CENT_NEW[0]+C_DRIVEN_FORCE_CENT[0],STRIKE_DEFENCE_CENT_NEW[1]+C_DRIVEN_FORCE_CENT[1]])
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED=quickCentCalc([STRIKE_DEFENCE_LOSSES_CENT_NEW[0]+STRIKE_DEFENCE_LOSSES_CENT[0],STRIKE_DEFENCE_LOSSES_CENT_NEW[1]+STRIKE_DEFENCE_LOSSES_CENT[1]])
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED_USED=STRIKE_DEFENCE_LOSSES_CENT_COMBINED
    TEAMS_MEGA_CENTS_ARRAY=[ATT_AND_SOT,TEAMS_1st2_CONSISTENCY_CENT,POINTS_LEFT_HUNGER,POS_COUNTER_WOUNDS_CENT,STRIKE_DEFENCE_CENT,ROUGH_FF_POS_CENT,ROUGH_FINAL_TEAMS_FORM,OVER_SHADOWED_CENTS_COUNTER,QUALITIES_COUNT[2],FINAL_FORM_AND_OVER_SHADOWED_CENTS,OVER_SHADOWED_CENTS,QUICK_CENT11,QUICK_CENT13,H2H_ROUGH_MIXED,H2H_LDS_COUNT_CENT]
    TEAMS_MEGA_CENTS=megaQualitiesCount(TEAMS_MEGA_CENTS_ARRAY)[:3]
    QUALITIES_LOSSES_SLICE=formCent(H2H_ROUGH_MIXED,QUALITIES_LOSSES_SLICE)
    MEGA_QUALITIES_AND_MEGA_WOUNDS=quickCentCalc([QUALITIES_LOSSES_SLICE[0]+TEAMS_MEGA_CENTS[2][0],QUALITIES_LOSSES_SLICE[1]+TEAMS_MEGA_CENTS[2][1]])
    CONCRETE_FORM=quickCentCalc([STRIKE_DEFENCE_CENT[0]+STRIKE_DEFENCE_LOSSES_CENT[0],STRIKE_DEFENCE_LOSSES_CENT[1]+STRIKE_DEFENCE_CENT[1]])
    TEAMS_GRAND_MAX_HUB=teamsQualitiesMax(H2H_ROUGH_MIXED,[HOME_ALL_SCORES_STRIKE_CENT,AWAY_ALL_SCORES_STRIKE_CENT],[HOME_LOST_BY_ONE,AWAY_LOST_BY_ONE])
    TEAMS_GRAND_MAX_D=[TEAMS_GRAND_MAX_HUB[0],TEAMS_GRAND_MAX_HUB[1]]
    TEAMS_GRAND_MAX_D_COMMENT=TEAMS_GRAND_MAX_HUB[2]
    FORM_WOUND_AND_TRANS=quickCentCalc([STRIKE_DEFENCE_CENT[0]+CDF_HOME+sum(HOME_TEAM_TRANSITION),STRIKE_DEFENCE_CENT[1]+CDF_AWAY+sum(AWAY_TEAM_TRANSITION)])
    FORM_WOUND_AND_TRANS=formCent(H2H_ROUGH_MIXED,FORM_WOUND_AND_TRANS)
    THE_TRIPPLETS_CENT=quickCentCalc([STRIKE_DEFENCE_CENT[0]+CONCRETE_FORM[0]+FORM_WOUND_AND_TRANS[0],STRIKE_DEFENCE_CENT[1]+CONCRETE_FORM[1]+FORM_WOUND_AND_TRANS[1]])
    THE_TRIPPLETS_CENT_DIVS=[round(THE_TRIPPLETS_CENT[0]/THE_TRIPPLETS_CENT[1],1),round(THE_TRIPPLETS_CENT[1]/THE_TRIPPLETS_CENT[0],1)]
    MIN_SUB=round(min([STRIKE_DEFENCE_CENT[0]-STRIKE_DEFENCE_CENT[1],CONCRETE_FORM[0]-CONCRETE_FORM[1],FORM_WOUND_AND_TRANS[0]-FORM_WOUND_AND_TRANS[1]]),1)
    STRIKERS_AND_WOUNDS_CENT=quickCentCalc([HOME_ALL_SCORES_STRIKE_CENT+HOME_WOUND_PATTERNS,AWAY_ALL_SCORES_STRIKE_CENT+AWAY_WOUND_PATTERNS])
    EXPERIMENTAL_FINAL_FORM_LATEST=quickCentCalc([ThisRelatedToUpVariableHome[1]+HOME_WOUND_PATTERNS,ThisRelatedToUpVariableAway[1]+AWAY_WOUND_PATTERNS])
    LATEST_H2H=[ThisRelatedToUpVariableHome[0],ThisRelatedToUpVariableAway[0]]
    EXPERIMENTAL_FINAL_FORM_LATEST=quickCentCalc([LATEST_H2H[0]+EXPERIMENTAL_FINAL_FORM_LATEST[0],LATEST_H2H[1]+EXPERIMENTAL_FINAL_FORM_LATEST[1]])
    EXPERIMENTAL_FINAL_FORM=quickCentCalcUnique([STRIKE_DEFENCE_CENT[0]+EXPERIMENTAL_FINAL_FORM_LATEST[0],STRIKE_DEFENCE_CENT[1]+EXPERIMENTAL_FINAL_FORM_LATEST[1]])#dynamicForm(H2H_ROUGH_MIXED,THE_TRIPPLETS_CENT,STRIKERS_AND_WOUNDS_CENT,STRIKE_DEFENCE_CENT,[HOME_LOST_BY_ONE,AWAY_LOST_BY_ONE])
    STRIKER_DEFENCE_DIFF_MIN=min([STRIKER_CENT_ABS_DIFF,TEAM_DEFENCE_ABS_DIFF])
    TEAMS_NO_H2H=True
    DYNAMIC_WOUNDS_ARRAY_H2H_INFLUENCED=formCent(H2H_ROUGH_MIXED,DYNAMIC_WOUNDS_ARRAY)
    H2H_DIFF_MODAL_CENT_WOUNDS=quickCentCalcUnique([H2H_DIFF_MODAL_CENT[0]+DYNAMIC_WOUNDS_ARRAY[0],H2H_DIFF_MODAL_CENT[1]+DYNAMIC_WOUNDS_ARRAY[1]])
    if VERY_OLD_H2H_REC_TRIGGERED:
        TEAMS_NO_H2H=STRIKER_DEFENCE_DIFF_MIN>=12 and STRIKE_DEFENCE_CENT_ABS_DIFF>=15
        H2H_DIFF_MODAL_CENT_WOUNDS=quickCentCalcUnique([home_same_team_cent_recent_local_used+DYNAMIC_WOUNDS_ARRAY[0],away_same_team_cent_recent_local_used+DYNAMIC_WOUNDS_ARRAY[1]])
        if SAME_TEAMS_PLAYED_LEN_MAX==0:
           H2H_DIFF_MODAL_CENT_WOUNDS=STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT
        #EXPERIMENTAL_FINAL_FORM=STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT
    EXPERIMENTAL_FINAL_FORM_NEW=quickCentCalcUnique([STRIKE_DEFENCE_CENT_DYNAMIC[0]+EXPERIMENTAL_FINAL_FORM_LATEST[0],STRIKE_DEFENCE_CENT_DYNAMIC[1]+EXPERIMENTAL_FINAL_FORM_LATEST[1]])
    EXPERIMENTAL_FINAL_FORM_COMBINED=quickCentCalc([EXPERIMENTAL_FINAL_FORM_LATEST[0]+sum(MICRO_STRIKE_DEFENCE_HOME),EXPERIMENTAL_FINAL_FORM_LATEST[1]+sum(MICRO_STRIKE_DEFENCE_AWAY)])
    POS_TOUCH=[AwayteamPosition+GRAND_COUNT_HOME,HometeamPosition+GRAND_COUNT_AWAY]
    EXPERIMENTAL_FINAL_FORM_COMBINED=formCent(POS_TOUCH,EXPERIMENTAL_FINAL_FORM_COMBINED)
    EXPERIMENTAL_FINAL_FORM_COMBINED=formCent(EXPERIMENTAL_FINAL_FORM_NEW,EXPERIMENTAL_FINAL_FORM_COMBINED)
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED =formCent(STRIKE_DEFENCE_CENT,STRIKERS_AND_WOUNDS_CENT)
    STRIKE_DEFENCE_LOSSES_CENT_COMBINED=quickCentCalc([STRIKE_DEFENCE_LOSSES_CENT_COMBINED[0]+HOME_TEAM_TRANSITION_sum,STRIKE_DEFENCE_LOSSES_CENT_COMBINED[1]+AWAY_TEAM_TRANSITION_sum])
    EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED=quickCentCalcUnique([EXPERIMENTAL_FINAL_FORM_NEW[0]+STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT[0],EXPERIMENTAL_FINAL_FORM_NEW[1]+STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT[1]])
    QUICK_QUALITIES=megaQualitiesCount([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED,EXPERIMENTAL_FINAL_FORM,EXPERIMENTAL_FINAL_FORM_NEW])[:3]
    EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS=quickCentCalcUnique([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED[0]+DYNAMIC_WOUNDS_ARRAY[0],EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED[1]+DYNAMIC_WOUNDS_ARRAY[1]])
    #OLD_NEW_FORCES_LAST_WOUNDS_TRANS=quickCentCalcUnique([STRIKE_DEFENCE_LOSSES_CENT[0]+STRIKE_DEFENCE_LOSSES_CENT_NEW[0],STRIKE_DEFENCE_LOSSES_CENT[1]+STRIKE_DEFENCE_LOSSES_CENT_NEW[1]])
    OLD_NEW_FORCES_LAST_WOUNDS_TRANS=quickCentCalcUnique([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[0]+HOME_TEAM_TRANSITION_sum,EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[1]+AWAY_TEAM_TRANSITION_sum])
    if H2H_TUPLE_LEN>=3 and max(H2H_ROUGH_MIXED)>=55:
       EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS=quickCentCalcUnique([PURELY_HOME_H2H_CENT+DYNAMIC_WOUNDS_ARRAY[0],PURELY_AWAY_H2H_CENT+DYNAMIC_WOUNDS_ARRAY[1]])
       OLD_NEW_FORCES_LAST_WOUNDS_TRANS=quickCentCalcUnique([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[0]+HOME_TEAM_TRANSITION_sum,EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[1]+AWAY_TEAM_TRANSITION_sum])
       STRIKERS_AND_WOUNDS_CENT=formCent(H2H_ROUGH_MIXED,STRIKERS_AND_WOUNDS_CENT)
    QUICK_QUALITIES2=megaQualitiesCount([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS,OLD_NEW_FORCES_LAST_WOUNDS_TRANS,STRIKERS_AND_WOUNDS_CENT])[:3]
    TEAM_AVERAGE_H=HOME_LOST_BY_ONE<55 and HOME_ALL_SCORES_STRIKE_CENT<55 and H2H_ROUGH_MIXED[0]<55
    TEAM_AVERAGE_A=AWAY_LOST_BY_ONE<55 and AWAY_ALL_SCORES_STRIKE_CENT<55 and H2H_ROUGH_MIXED[1]<55
    PRO_HOME_TEAM=not TEAM_AVERAGE_H and STRIKERS_AND_WOUNDS_CENT[0]>=STRIKERS_AND_WOUNDS_CENT[1]
    PRO_AWAY_TEAM=not TEAM_AVERAGE_A and STRIKERS_AND_WOUNDS_CENT[1]>=STRIKERS_AND_WOUNDS_CENT[0]
    HOME_TRIO_DIFF_MIN_VAL=min([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[0]-EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[1],OLD_NEW_FORCES_LAST_WOUNDS_TRANS[0]-OLD_NEW_FORCES_LAST_WOUNDS_TRANS[1],STRIKERS_AND_WOUNDS_CENT[0]-STRIKERS_AND_WOUNDS_CENT[1]])
    AWAY_TRIO_DIFF_MIN_VAL=min([EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[1]-EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS[0],OLD_NEW_FORCES_LAST_WOUNDS_TRANS[1]-OLD_NEW_FORCES_LAST_WOUNDS_TRANS[0],STRIKERS_AND_WOUNDS_CENT[1]-STRIKERS_AND_WOUNDS_CENT[0]])
    QUICK_QUALITIES_SUM=quickCentCalcUnique([QUICK_QUALITIES[2][0]+QUICK_QUALITIES2[2][0],QUICK_QUALITIES[2][1]+QUICK_QUALITIES2[2][1]])
    TITANIC_FORM_HUB=megaQualitiesCount([[AwayteamPosition,HometeamPosition],H2H_DIFF_MODAL_CENT_WOUNDS,STRIKERS_AND_WOUNDS_CENT,CONCRETE_FORM,FORM_WOUND_AND_TRANS,STRIKE_DEFENCE_CENT,STRIKE_DEFENCE_CENT_NEW,STRIKE_DEFENCE_CENT_DYNAMIC,STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT,STRIKE_DEFENCE_LOSSES_CENT,STRIKE_DEFENCE_LOSSES_CENT_NEW,THE_TRIPPLETS_CENT,EXPERIMENTAL_FINAL_FORM,EXPERIMENTAL_FINAL_FORM_NEW,EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED,EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS])
    TITANIC_FORM=TITANIC_FORM_HUB[:3]
    TITANIC_FORM_COUNT_CENT=quickCentCalcUnique([TITANIC_FORM[0],TITANIC_FORM[1]])
    TITANIC_ESTIMATED_FORM=quickCentCalcUnique([TITANIC_FORM_COUNT_CENT[0]+TITANIC_FORM[2][0],TITANIC_FORM_COUNT_CENT[1]+TITANIC_FORM[2][1]])
    H2H_DIFF_MODAL_CENT_WOUNDS_PLUS_MIN_VALS=[round((H2H_DIFF_MODAL_CENT_WOUNDS[0]+HOME_TRIO_DIFF_MIN_VAL),1),round((H2H_DIFF_MODAL_CENT_WOUNDS[1]+AWAY_TRIO_DIFF_MIN_VAL),1)]
    H2H_SAME_MTCHS_CENTS_RAW=quickCentCalcUnique([H2H_ROUGH_MIXED[0]+home_same_team_cent_recent_local_used+TITANIC_FORM[0]+AwayteamPosition,H2H_ROUGH_MIXED[1]+away_same_team_cent_recent_local_used+TITANIC_FORM[1]+HometeamPosition])
    H2H_SAME_MTCHS_CENTS_LOSS_ELEVATED=formCent([HOME_LAST_SCORES_LOSS,AWAY_LAST_SCORES_LOSS],H2H_SAME_MTCHS_CENTS_RAW)
    HOME_H2H_LEADS=PURELY_HOME_H2H_CENT>PURELY_AWAY_H2H_CENT or H2H_ROUGH_MIXED[0]>H2H_ROUGH_MIXED[1]
    AWAY_H2H_LEADS=PURELY_AWAY_H2H_CENT>PURELY_HOME_H2H_CENT or H2H_ROUGH_MIXED[1]>H2H_ROUGH_MIXED[0]
    HOME_DANGEROUS=(HOME_H2H_LEADS and HOME_LAST_SCORES_LOSS>AWAY_LAST_SCORES_LOSS) or (HometeamPosition<AwayteamPosition and HOME_LAST_SCORES_LOSS>AWAY_LAST_SCORES_LOSS) or ((HOME_H2H_LEADS or HometeamPosition<AwayteamPosition) and HOME_LAST_SCORES_LOSS>0)
    AWAY_DANGEROUS=(AWAY_H2H_LEADS and AWAY_LAST_SCORES_LOSS>HOME_LAST_SCORES_LOSS) or (AwayteamPosition<HometeamPosition and AWAY_LAST_SCORES_LOSS>HOME_LAST_SCORES_LOSS) or ((AWAY_H2H_LEADS or AwayteamPosition<HometeamPosition) and AWAY_LAST_SCORES_LOSS>0)
    POINTS_LEFT_PLUS_DYNAMIC_WOUNDS_ARRAY=quickCentCalcUnique([DYNAMIC_WOUNDS_ARRAY[0]+AWAY_POINTS_LEFT_TO_QUALIFY,DYNAMIC_WOUNDS_ARRAY[1]+HOME_POINTS_LEFT_TO_QUALIFY])
    TEAM_AVERAGE_H_USED=0
    TEAM_AVERAGE_A_USED=0
    PRO_HOME_TEAM_USED=0
    PRO_AWAY_TEAM_USED=0
    HOME_DANGEROUS_USED=0
    AWAY_DANGEROUS_USED=0
    HometeamPosition_used=0
    AwayteamPosition_used=0
    if not TEAM_AVERAGE_H:
       TEAM_AVERAGE_H_USED=1
    if not TEAM_AVERAGE_A:
       TEAM_AVERAGE_A_USED=1
    if PRO_HOME_TEAM:
       PRO_HOME_TEAM_USED=1
    if PRO_AWAY_TEAM:
       PRO_AWAY_TEAM_USED=1
    if HOME_DANGEROUS:
       HOME_DANGEROUS_USED=1
    if AWAY_DANGEROUS:
       AWAY_DANGEROUS_USED=1
    if HometeamPosition<AwayteamPosition:
       HometeamPosition_used=1
    if AwayteamPosition<HometeamPosition:
       AwayteamPosition_used=1
    AVERAGE_TEAM_LOGIC=[TEAM_AVERAGE_H_USED,TEAM_AVERAGE_A_USED]
    PRO_TEAM_LOGIC=[PRO_HOME_TEAM_USED,PRO_AWAY_TEAM_USED]
    DANGEROUS_TEAM_LOGIC=[HOME_DANGEROUS_USED,AWAY_DANGEROUS_USED]
    POSITION_GREATER=[HometeamPosition_used,AwayteamPosition_used]
    MIN_HAUL_ARRAY=[POSITION_GREATER,DANGEROUS_TEAM_LOGIC,AVERAGE_TEAM_LOGIC,PRO_TEAM_LOGIC,[TITANIC_FORM[0],TITANIC_FORM[1]],H2H_SAME_MTCHS_CENTS_RAW,POINTS_LEFT_PLUS_DYNAMIC_WOUNDS_ARRAY]
    MIN_HAUL_CENT=megaQualitiesCount(MIN_HAUL_ARRAY)[:3]
    TEAMS_DRIVEN_ENGINE_X_H_SUM_USED=TEAMS_DRIVEN_ENGINE_X_H_SUM
    TEAMS_DRIVEN_ENGINE_X_A_SUM_USED=TEAMS_DRIVEN_ENGINE_X_A_SUM
    TEAMS_DRIVEN_ENGINE_X_H_F=TEAMS_DRIVEN_ENGINE_X[0][0]
    TEAMS_DRIVEN_ENGINE_X_A_F=TEAMS_DRIVEN_ENGINE_X[1][0]
    TEAMS_DRIVEN_ENGINE_X_H_B=TEAMS_DRIVEN_ENGINE_X[0][1]
    TEAMS_DRIVEN_ENGINE_X_A_B=TEAMS_DRIVEN_ENGINE_X[1][1]
    ACCUMULATED_POINTS=[MIN_HAUL_CENT[0]+TEAMS_DRIVEN_ENGINE_X_H_SUM,MIN_HAUL_CENT[1]+TEAMS_DRIVEN_ENGINE_X_A_SUM]
    ACCUMULATED_POINTS_CENT=quickCentCalcUnique(ACCUMULATED_POINTS)
    GRAND_FORMS_ARRAY_OLD=[STRIKE_DEFENCE_CENT_PURE_OLD,[HTIM_ORGANIC_POINT_CENT,ATIM_ORGANIC_POINT_CENT],[only_home_score_cent,only_away_score_cent],[home_same_team_cent_local,away_same_team_cent_local]]
    GRAND_FORMS_ARRAY_NEW=[[last5_matches_otherMatches_cent_home,last5_matches_otherMatches_cent_away],[home_same_team_cent_recent_local_used,away_same_team_cent_recent_local_used],STRIKE_DEFENCE_CENT_NEW_USED,[only_home_cent_5_cut,only_away_cent_5_cut]]
    GRAND_FORMS_ARRAY_NEW2=[[last5_matches_otherMatches_cent_home,last5_matches_otherMatches_cent_away],[home_same_team_cent_recent_local_used,away_same_team_cent_recent_local_used],[only_home_cent_5_cut,only_away_cent_5_cut]]
    GRAND_FORMS_RAW_QUALITIES_OLD=megaQualitiesCount(GRAND_FORMS_ARRAY_OLD)[:3]
    GRAND_FORMS_RAW_QUALITIES_NEW=megaQualitiesCount(GRAND_FORMS_ARRAY_NEW)[:3]
    GRAND_FORMS_RAW_QUALITIES_NEW2=megaQualitiesCount(GRAND_FORMS_ARRAY_NEW2)[:3][2]
    GRAND_FORMS_RAW_QUALITIES_NEW_CENT=[GRAND_FORMS_RAW_QUALITIES_NEW[2][0],GRAND_FORMS_RAW_QUALITIES_NEW[2][1]]
    GRAND_FORMS_RAW_QUALITIES_AVERAGE=quickCentCalcUnique([GRAND_FORMS_RAW_QUALITIES_OLD[2][0]+GRAND_FORMS_RAW_QUALITIES_NEW[2][0],GRAND_FORMS_RAW_QUALITIES_OLD[2][1]+GRAND_FORMS_RAW_QUALITIES_NEW[2][1]])
    GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H=formCent(H2H_ROUGH_MIXED,GRAND_FORMS_RAW_QUALITIES_AVERAGE)
    GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT=quickCentCalcUnique([GRAND_FORMS_RAW_QUALITIES_AVERAGE[0]+ONLY_SAME_TEAMS_HOME_RECENT_CENT,GRAND_FORMS_RAW_QUALITIES_AVERAGE[1]+ONLY_SAME_TEAMS_AWAY_RECENT_CENT])
    GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES=quickCentCalcUnique([GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT[0]+DYNAMIC_WOUNDS_ARRAY[0],GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT[1]+DYNAMIC_WOUNDS_ARRAY[1]])
    FORM_QUALITIES_CHANGE_H=round((GRAND_FORMS_RAW_QUALITIES_NEW[2][0]-GRAND_FORMS_RAW_QUALITIES_OLD[2][0]),1)
    FORM_QUALITIES_CHANGE_A=round((GRAND_FORMS_RAW_QUALITIES_NEW[2][1]-GRAND_FORMS_RAW_QUALITIES_OLD[2][1]),1)
    FORM_CENT_LOSSES_INDIVIDUALLY=formLossesIndividually(GRAND_FORMS_ARRAY_OLD,DYNAMIC_WOUNDS_ARRAY)
    FORM_CENT_LOSSES_INDIVIDUALLY_TRANS=quickCentCalcUnique([FORM_CENT_LOSSES_INDIVIDUALLY[2][0]+HOME_TEAM_TRANSITION_sum,FORM_CENT_LOSSES_INDIVIDUALLY[2][1]+AWAY_TEAM_TRANSITION_sum])
    GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS=quickCentCalcUnique([all_scores_cent_cut_5_home+GRAND_FORMS_RAW_QUALITIES_AVERAGE[0],GRAND_FORMS_RAW_QUALITIES_AVERAGE[1]+all_scores_cent_cut_5_away])
    GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES=[GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS[0]+DYNAMIC_WOUNDS_ARRAY[0],GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS[1]+DYNAMIC_WOUNDS_ARRAY[1]]
    print(f'GRAND_FORMS_H2H_INFLUENCED_H2H_ROUGH_MIXED ---> {H2H_ROUGH_MIXED}')
    GRAND_FORMS_H2H_INFLUENCED=quickCentCalcUnique([H2H_ROUGH_MIXED[0]+GRAND_FORMS_RAW_QUALITIES_OLD[2][0],GRAND_FORMS_RAW_QUALITIES_OLD[2][1]+H2H_ROUGH_MIXED[1]])
    PROPELLER=quickCentCalcUnique([TEAMS_DRIVEN_ENGINE_X_H_SUM+DYNAMIC_WOUNDS_ARRAY[0],TEAMS_DRIVEN_ENGINE_X_A_SUM+DYNAMIC_WOUNDS_ARRAY[1]])
    CURRENT_FORM_PLUS_TRANS=quickCentCalcUnique([all_scores_cent_cut_5_home+HOME_TRANS_HUNT_QUALITIES[3],all_scores_cent_cut_5_away+AWAY_TRANS_HUNT_QUALITIES[3]])
    VARIABLE_FINAL_FORM=quickCentCalcUnique([GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES[0]+TEAMS_1st2_CONSISTENCY_CENT[0]+AwayteamPosition,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES[1]+TEAMS_1st2_CONSISTENCY_CENT[1]+HometeamPosition])
    VARIABLE_FINAL_FORM_H2H_INFLUENCED=formCent(H2H_ROUGH_MIXED,VARIABLE_FINAL_FORM)
    VARIABLE_QUALITIES=megaQualitiesCount([EXPERIMENTAL_FINAL_FORM,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES,VARIABLE_FINAL_FORM,VARIABLE_FINAL_FORM_H2H_INFLUENCED])[:3]
    VARIABLE_QUALITIES_DIFF=round((abs(VARIABLE_QUALITIES[2][0]-VARIABLE_QUALITIES[2][1])),1)
    VARIABLE_QUALITIES_PLUS_CHANGE=quickCentCalcUnique([VARIABLE_QUALITIES[2][0]+FORM_QUALITIES_CHANGE_H,VARIABLE_QUALITIES[2][1]+FORM_QUALITIES_CHANGE_A])
    GRAND_FORMS_RAW_QUALITIES_OLD_COUNT_H=GRAND_FORMS_RAW_QUALITIES_OLD[0]
    GRAND_FORMS_RAW_QUALITIES_NEW_COUNT_H=GRAND_FORMS_RAW_QUALITIES_NEW[0]
    GRAND_FORMS_RAW_QUALITIES_OLD_COUNT_A=GRAND_FORMS_RAW_QUALITIES_OLD[1]
    GRAND_FORMS_RAW_QUALITIES_NEW_COUNT_A=GRAND_FORMS_RAW_QUALITIES_NEW[1]
    QUALITIES_COUNT_MIN_ABS_DIFF=min([abs(GRAND_FORMS_RAW_QUALITIES_OLD_COUNT_H-GRAND_FORMS_RAW_QUALITIES_OLD_COUNT_A),abs(GRAND_FORMS_RAW_QUALITIES_NEW_COUNT_H-GRAND_FORMS_RAW_QUALITIES_NEW_COUNT_A)])
    GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H=formCent(H2H_ROUGH_MIXED,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES)
    GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H=formCent(H2H_ROUGH_MIXED,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES)
    GRAND_QUALITIES_MIXTURE_DIFF=[round((-1*GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H[0]+GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H[0]),1),round((-1*GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H[1]+GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H[1]),1)]
    HOME_TRANS_ARRAY=[SAME_TEAMS_TRANS_H,sum(HOME_TEAM_TRANSITION),ONLY_TEAM_TRANS_H]
    AWAY_TRANS_ARRAY=[SAME_TEAMS_TRANS_A,sum(AWAY_TEAM_TRANSITION),ONLY_TEAM_TRANS_A]
    GRAND_TRANS_SUM=[sum(HOME_TRANS_ARRAY),sum(AWAY_TRANS_ARRAY)]
    GRAND_TRANS_SUM_OTHER_QUALITIES=[GRAND_FORMS_RAW_QUALITIES_NEW2[0]+TEAMS_1st2_CONSISTENCY_CENT[0]+DYNAMIC_WOUNDS_ARRAY[0]+AwayteamPosition,GRAND_FORMS_RAW_QUALITIES_NEW2[1]+TEAMS_1st2_CONSISTENCY_CENT[1]+DYNAMIC_WOUNDS_ARRAY[1]+HometeamPosition]
    GRAND_TRANS_SUM_OTHER_QUALITIES2=[GRAND_FORMS_RAW_QUALITIES_NEW_CENT[0]+TEAMS_1st2_CONSISTENCY_CENT[0]+DYNAMIC_WOUNDS_ARRAY[0]+AwayteamPosition,GRAND_FORMS_RAW_QUALITIES_NEW_CENT[1]+TEAMS_1st2_CONSISTENCY_CENT[1]+DYNAMIC_WOUNDS_ARRAY[1]+HometeamPosition]
    GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H_GRAND_TRANS=quickCentCalcUnique([GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H[0]+GRAND_TRANS_SUM[0],GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H[1]+GRAND_TRANS_SUM[1]])
    GRAND_FORM_QUALITIES2=megaQualitiesCount([GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H,GRAND_TRANS_SUM_OTHER_QUALITIES,GRAND_TRANS_SUM_OTHER_QUALITIES2])[:3]
    GRAND_FORM_QUALITIES3=megaQualitiesCount([GRAND_FORM_QUALITIES2[2],GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H])[:3]
    GRAND_COUNTS_QUALITIES_ARRAY=[MIN_HAUL_CENT[:2],FORM_CENT_LOSSES_INDIVIDUALLY[:2],GRAND_FORMS_RAW_QUALITIES_OLD[:2],GRAND_FORMS_RAW_QUALITIES_NEW[:2],GRAND_FORM_QUALITIES2[:2],VARIABLE_QUALITIES[:2],GRAND_FORM_QUALITIES3[:2]]
    GRAND_COUNTS_QUALITIES=megaQualitiesCount(GRAND_COUNTS_QUALITIES_ARRAY)[:3]
    HOME_TOTAL_QUALITES_PLUS_WOUND=GRAND_FORM_QUALITIES3[:2][0]+GRAND_COUNTS_QUALITIES[:2][0]+TITANIC_FORM[:2][0]+DYNAMIC_WOUNDS_ARRAY[0]
    AWAY_TOTAL_QUALITES_PLUS_WOUND=GRAND_FORM_QUALITIES3[:2][1]+GRAND_COUNTS_QUALITIES[:2][1]+TITANIC_FORM[:2][1]+DYNAMIC_WOUNDS_ARRAY[1]
    HANDICAP_PREDIC=handicapFact([HOME_TOTAL_QUALITES_PLUS_WOUND,AWAY_TOTAL_QUALITES_PLUS_WOUND])
    FINAL_PROTOTYPE_FORM_ARRAY=[GRAND_FORM_QUALITIES3[2],GRAND_COUNTS_QUALITIES[2],TITANIC_FORM[2],[CUSTOM_POSITION_ARRAY[1],CUSTOM_POSITION_ARRAY[0]],GRAND_TRANS_SUM,DYNAMIC_WOUNDS_ARRAY,[TITANIC_FORM[:2][0],TITANIC_FORM[:2][1]],[GRAND_COUNTS_QUALITIES[:2][0],GRAND_COUNTS_QUALITIES[:2][1]],[GRAND_FORM_QUALITIES3[:2][0],GRAND_FORM_QUALITIES3[:2][1]]]
    FINAL_PROTOTYPE_FORM=megaQualitiesCount(FINAL_PROTOTYPE_FORM_ARRAY)[:3]
    QUALITIES_COUNT_LIM_NUM=[GRAND_FORM_QUALITIES3[:2],GRAND_COUNTS_QUALITIES[:2],TITANIC_FORM[:2],HANDICAP_PREDIC,FINAL_PROTOTYPE_FORM]
    TEAM_QUALITIES_COUNT_VERY_STRONG=qualitiesCountMagn(QUALITIES_COUNT_LIM_NUM,2)
    FINAL_PROTOTYPE_FORM_PLUS_GRAND=quickCentCalcUnique([FINAL_PROTOTYPE_FORM[2][0]+GRAND_TRANS_SUM[0],FINAL_PROTOTYPE_FORM[2][1]+GRAND_TRANS_SUM[1]])
    COMPROMISED_WOUNS_TITANIC_FORM=formCent(COMPROMISED_WOUNS,TITANIC_FORM[2])
    VARIABLES_CHANGE_LOGIC_HOME=COMPROMISED_WOUNS_TITANIC_FORM[0]>COMPROMISED_WOUNS_TITANIC_FORM[1] and GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H[0]>GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H[1] and GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H[0]>GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H[1]
    VARIABLES_CHANGE_LOGIC_AWAY=COMPROMISED_WOUNS_TITANIC_FORM[1]>COMPROMISED_WOUNS_TITANIC_FORM[0] and GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H[1]>GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H[0] and GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H[1]>GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H[0]
    HOME_TEAM_GREEN_LIGHT=[H2H_HOME_CENT,CHAINS_LOSSES_COMMENT_H_NUMBERS_INT,CUSTOM_POSITION_ARRAY[1],int(TEAMS_GRAND_MAX_D_COMMENT[0][:(len(TEAMS_GRAND_MAX_D_COMMENT[0])-1)])]
    AWAY_TEAM_GREEN_LIGHT=[H2H_AWAY_CENT,CHAINS_LOSSES_COMMENT_A_NUMBERS_INT,CUSTOM_POSITION_ARRAY[0],int(TEAMS_GRAND_MAX_D_COMMENT[1][:(len(TEAMS_GRAND_MAX_D_COMMENT[1])-1)])]
    TEAM_GREEN_LIGHT_CENT=quickCentCalcUnique([sum(HOME_TEAM_GREEN_LIGHT),sum(AWAY_TEAM_GREEN_LIGHT)])
    TRUE_TEAMS_FORM=[H2H_HOME_CENT,H2H_AWAY_CENT]
    TRUE_FORM_DEFUALT=[H2H_HOME_CENT,H2H_AWAY_CENT]
    if H2H_TUPLE[0][0]==-1:
        TRUE_TEAMS_FORM=[AwayteamPosition,HometeamPosition]
        TRUE_FORM_DEFUALT=STRIKE_DEFENCE_CENT
    TEAMS_FAILS_PATTERN_FORCE=quickCentCalcUnique([TRUE_TEAMS_FORM[0]+HOME_FAILS_PATTERN+CHAINS_LOSSES_COMMENT_H_NUMBERS_INT,TRUE_TEAMS_FORM[1]+AWAY_FAILS_PATTERN+CHAINS_LOSSES_COMMENT_A_NUMBERS_INT])
    TEAMS_FAILS_PATTERN_FORCE2=quickCentCalcUnique([HOME_FAILS_PATTERN+CHAINS_LOSSES_COMMENT_H_NUMBERS_INT+HOME_ALL_SCORES_STRIKE[1]+HOME_FAILS_PATTERN_H2H_HOME,AWAY_FAILS_PATTERN+CHAINS_LOSSES_COMMENT_A_NUMBERS_INT+AWAY_ALL_SCORES_STRIKE[1]+HOME_FAILS_PATTERN_H2H_AWAY])
    TEAMS_FAILS_PATTERN_FORCE3=quickCentCalcUnique([HOME_FAILS_PATTERN+CHAINS_LOSSES_COMMENT_H_NUMBERS_INT+CUSTOM_POSITION_ARRAY[1]+HOME_FAILS_PATTERN_H2H_HOME,AWAY_FAILS_PATTERN+CHAINS_LOSSES_COMMENT_A_NUMBERS_INT+CUSTOM_POSITION_ARRAY[0]+HOME_FAILS_PATTERN_H2H_AWAY])
    WOUND_FORCES_QUALITIES_ARRAY=[GRAND_TRANS_SUM,[CHAINS_LOSSES_COMMENT_H_NUMBERS_INT,CHAINS_LOSSES_COMMENT_A_NUMBERS_INT],[HOME_FAILS_PATTERN,AWAY_FAILS_PATTERN],[HOME_FAILS_PATTERN_H2H_HOME,HOME_FAILS_PATTERN_H2H_AWAY]]
    WOUND_FORCES_QUALITIES_ARRAY_CENT=megaQualitiesCount(WOUND_FORCES_QUALITIES_ARRAY)[:3]
    WOUND_FORCES_QUALITIES_ARRAY_CENT=megaQualitiesCount([TRUE_TEAMS_FORM,STRIKE_DEFENCE_CENT,WOUND_FORCES_QUALITIES_ARRAY_CENT[:2],WOUND_FORCES_QUALITIES_ARRAY_CENT[2]])[:3]
    TEAM_NET_STRENGHT=quickCentCalcUnique([STRIKE_DEFENCE_CENT[0]+GRAND_TRANS_SUM[0],STRIKE_DEFENCE_CENT[1]+GRAND_TRANS_SUM[1]])
    MEGA_QUALITIES_FORM_ARRAY=[FINAL_PROTOTYPE_FORM_PLUS_GRAND,TEAMS_FAILS_PATTERN_FORCE,TEAMS_FAILS_PATTERN_FORCE2,TEAMS_FAILS_PATTERN_FORCE3]
    MEGA_QUALITIES_FORM=megaQualitiesCount(MEGA_QUALITIES_FORM_ARRAY)[:3]
    COUNTER_QUALITIES_ARRAY=[GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H]
    COUNTER_QUALITIES_ARRAY_CENT=megaQualitiesCount(COUNTER_QUALITIES_ARRAY)[:3]
    WOUND_FORCES_QUALITIES_ARRAY_CENT_ABS_DIFF=abs(WOUND_FORCES_QUALITIES_ARRAY_CENT[2][0]-WOUND_FORCES_QUALITIES_ARRAY_CENT[2][1])
    MEGA_QUALITIES_SERIES_ARRAY=[EXPERIMENTAL_FINAL_FORM,WOUND_FORCES_QUALITIES_ARRAY_CENT[:2],WOUND_FORCES_QUALITIES_ARRAY_CENT[2],COUNTER_QUALITIES_ARRAY_CENT[:2],COUNTER_QUALITIES_ARRAY_CENT[2]]
    MEGA_QUALITIES_SERIES_CENT_ARRAY=aTeamQualitiesGreaterThanB(MEGA_QUALITIES_SERIES_ARRAY)
    OLD_CONSISTENT_FORMS_ARRAY=[[home_same_team_cent_local,away_same_team_cent_local],TEAMS_1st2_CONSISTENCY_CENT,[only_home_score_cent,only_away_score_cent],GRAND_H2H_CENT,[HTIM_ORGANIC_POINT_CENT,ATIM_ORGANIC_POINT_CENT]]
    OLD_CONSISTENT_FORMS_ARRAY_CENT=megaQualitiesCount(OLD_CONSISTENT_FORMS_ARRAY)[:3]
    TOTAT_WOUNDS_FRESH=[sum([CHAINS_LOSSES_COMMENT_H_NUMBERS_INT,HOME_FAILS_PATTERN_H2H_HOME,HOME_FAILS_PATTERN]),sum([CHAINS_LOSSES_COMMENT_A_NUMBERS_INT,HOME_FAILS_PATTERN_H2H_AWAY,AWAY_FAILS_PATTERN])]
    TOTAT_WOUNDS_FRESH_ABS_DIFF=abs(TOTAT_WOUNDS_FRESH[0]-TOTAT_WOUNDS_FRESH[1])
    TOTAT_WOUNDS_FRESH_LOGIC_HOME=TOTAT_WOUNDS_FRESH_ABS_DIFF<=5 or TOTAT_WOUNDS_FRESH[0]>=TOTAT_WOUNDS_FRESH[1]
    TOTAT_WOUNDS_FRESH_LOGIC_AWAY=TOTAT_WOUNDS_FRESH_ABS_DIFF<=5 or TOTAT_WOUNDS_FRESH[1]>=TOTAT_WOUNDS_FRESH[0]
    WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF=quickCentCalcUnique([TOTAT_WOUNDS_FRESH[0]+TRUE_FORM_DEFUALT[0],TOTAT_WOUNDS_FRESH[1]+TRUE_FORM_DEFUALT[1]])
    PRO_TEAM_HOME=OLD_CONSISTENT_FORMS_ARRAY_CENT[2][0]>=OLD_CONSISTENT_FORMS_ARRAY_CENT[2][1] and TOTAT_WOUNDS_FRESH_LOGIC_HOME and WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF[0]>WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF[1] and MEGA_QUALITIES_SERIES_CENT_ARRAY[2][0]>MEGA_QUALITIES_SERIES_CENT_ARRAY[2][1]
    PRO_TEAM_AWAY=OLD_CONSISTENT_FORMS_ARRAY_CENT[2][1]>=OLD_CONSISTENT_FORMS_ARRAY_CENT[2][0] and TOTAT_WOUNDS_FRESH_LOGIC_AWAY and WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF[1]>WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF[0] and MEGA_QUALITIES_SERIES_CENT_ARRAY[2][1]>MEGA_QUALITIES_SERIES_CENT_ARRAY[2][0]
    PRO_TEAM_STATUS=[PRO_TEAM_HOME,PRO_TEAM_AWAY]
    SUPER_MEGA_QUALITIES_ARRAY=[GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES,GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H,GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H,GRAND_FORM_QUALITIES3[2],GRAND_COUNTS_QUALITIES[2],TITANIC_FORM[2],FINAL_PROTOTYPE_FORM[2],TEAM_GREEN_LIGHT_CENT,TEAMS_FAILS_PATTERN_FORCE,TEAMS_FAILS_PATTERN_FORCE2,TEAMS_FAILS_PATTERN_FORCE3]
    SUPER_MEGA_QUALITIES_CENT=megaQualitiesCount(SUPER_MEGA_QUALITIES_ARRAY)[:3]
    if H2H_TUPLE_LEN>=5 and ALL_SCORES_DIRTY_LEN_MIN>=10:
        PREDICTIONS_MADE=multiMarketPredictor(HOME_TEAM,
                             AWAY_TEAM,
                             H2H_SCORES_SUM_MODE,
                             FORM_CENT_QUICK,
                             FINAL_FORM_DIFF,
                             HOME_AWAY_LOST_POINTS_CENT,
                             GRAND_LOSES_ARRAY,
                             GLDFF,
                             H2H_ROUGH_MIXED,
                             [HOME_ALL_SCORES_STRIKE_CENT,AWAY_ALL_SCORES_STRIKE_CENT],
                             [HOME_LOST_BY_ONE_USED,AWAY_LOST_BY_ONE_USED],
                             INCRE_DECRE,
                             C_DRIVEN_FORCE,
                             QUALITIES_COUNT,
                             QUICK_CENT14,
                             CDF_DIV,
                             CDF_LAST_GAMES_DIV,
                             TEAM_STRUCTURE_ARRAY,
                             [HOME_WOUNDS,AWAY_WOUNDS],
                             CENTS_ARRAY,
                             STRIKE_DEFENCE_LOSSES_CENT_COMBINED,
                             H2H_WINS_COUNT_CENT,
                             UNI_COEFFICIENT,
                             [home_dnt_wins_all_logic,away_dnt_wins_all_logic],
                             OTHER_SITES_PREDICTION,
                             LAST_H2H_SCORE_CENT,
                             [HometeamPosition,AwayteamPosition],
                             TEAMS_DRIVEN_ENGINE_X,
                             [HOME_WINS_DRAWS_CENT,AWAY_WINS_DRAWS_CENT],
                             [PURELY_HOME_H2H_CENT,PURELY_AWAY_H2H_CENT],
                             [HOME_H2H_FINAL_FORM,AWAY_H2H_FINAL_FORM],
                             H2H_DISCRET_FORM_LOCAL,
                             CDF_DIV_ABS_DFF,
                             LOST_POINTS_TOTAL_PLUS_OMTC_FORM_CENT,
                             OLD_AND_NEW_LOST_POINTS_SUM,
                             LAST_LOST_POINTS_CENT,
                             ALL_TIMES_H2H_ARG_CENT,
                             [ONLY_HOME_SCORES_LAST_SC_DIFF,ONLY_AWAY_SCORES_LAST_SC_DIFF],
                             LAST_WOUNDS_SQUAD,
                             LEAGUE_STAGE_FINALS,
                             ATT_WND_HUB,
                             FINAL_FORM_AND_ATTACKS_PLUS_SOT,
                             ATT_AND_SOT,
                             OVER_SHADOWED_CENTS,
                             FINAL_FORM_AND_OVER_SHADOWED_CENTS,
                             OVER_SHADOWED_CENTS_COUNTER,
                             TEAMS_1st2_CONSISTENCY_CENT,
                             ROUGH_FINAL_TEAMS_FORM,
                             POINTS_LEFT_HUNGER,
                             POS_COUNTER_WOUNDS_CENT,
                             ROUGH_FF_POS_CENT,
                             STRIKE_DEFENCE_CENT,
                             CONCRETE_FORM,
                             QUICK_QUALITIES,
                             QUICK_QUALITIES2,
                             TEAMS_GRAND_MAX_HUB,
                             FORM_WOUND_AND_TRANS,
                             [MIN_SUB,VERY_OLD_H2H_REC_TRIGGERED],
                             TEAMS_VETERAN_STATUS,
                             EXPERIMENTAL_FINAL_FORM,
                             [TEAM_AVERAGE_H,TEAM_AVERAGE_A],
                             [HOME_TRIO_DIFF_MIN_VAL,AWAY_TRIO_DIFF_MIN_VAL],
                             TITANIC_FORM,
                             H2H_SAME_MTCHS_CENTS_RAW,
                             [HOME_TEAM_TRANSITION_sum,AWAY_TEAM_TRANSITION_sum],
                             [HOME_DANGEROUS,AWAY_DANGEROUS],
                             STRIKERS_AND_WOUNDS_CENT,
                             VARIABLE_FINAL_FORM_H2H_INFLUENCED,
                             DYNAMIC_WOUNDS_ARRAY_ORIGINAL,
                             [HOME_CONSISTENCY,AWAY_CONSISTENCY],
                             [VARIABLE_QUALITIES_DIFF,VARIABLES_CHANGE_LOGIC_HOME,VARIABLES_CHANGE_LOGIC_AWAY],
                             [CUSTOM_POSITION_ARRAY,FINAL_PROTOTYPE_FORM],
                             TEAM_GREEN_LIGHT_CENT,
                             TEAMS_FAILS_PATTERN_FORCE,
                             MEGA_QUALITIES_SERIES_CENT_ARRAY,
                             TEAM_QUALITIES_COUNT_VERY_STRONG,
                             PRO_TEAM_STATUS)
    if PREDICTIONS_MADE:
        picked_match_count+=1
        MY_PREDICTION='PREDICTION MADE'
    print(f'TEAMS_ORE_SCORES_AVERAGE ---> {TEAMS_ORE_SCORES_AVERAGE}')
    print(f'TEAMS_LOST_BY_ONE ---> {[HOME_LOST_BY_ONE,AWAY_LOST_BY_ONE]}')
    print(f'TEAMS_WINS_DRAWS_CENT ---> {[HOME_WINS_DRAWS_CENT,AWAY_WINS_DRAWS_CENT]}')
    print(f'TEAMS_RESILIENCE_LEVEL ---> {[HOME_RESILIENCE_LEVEL,AWAY_RESILIENCE_LEVEL]}')
    print(F'TEAM_STRIKING_STRENGTH ---> {[ONLY_HOME_SCORES_OVER_2GLS_CENT,ONLY_AWAY_SCORES_OVER_2GLS_CENT]}')
    print(f'TEAM_STRUCTURAL_FORM ---> {TEAM_STRUCTURE_ARRAY}')
    print(f'GG_OVER_1_CENT ---> {GG_OVER_1_CENT}')
    MY_PREDICTION=f'{MY_PREDICTION} ---> NO.{picked_match_count}'
    mdata_add_on=f'\n{meta_addon3}\n\n{meta_add_on0}\nTOTAL TEAMS IN LEAGUE TABLE ---> {ALL_TEAMS_LEN_LOCAL}\nTOTAL LEAGUE MATCHES ---> {TOTAL_LEAGUE_MATCHES}\nTOTAL PLAYED MATCHES ---> {[TPM_HOME,TPM_AWAY]}\nTOTAL NEXT MATCHES ---> {H_A_NEXT_MATCHES_LOCAL}\nTEAMS_POINTS ---> {TEAM_POINTS_ARR} --> {PointDiff}\nTEAMS_POS ---> {[HometeamPosition,AwayteamPosition]}\nFOREBET_PREDICTION ---> {FOREBETpredictions}\nTOTAL H2H MATCHES ---> {H2H_SCR_LEN}'
    mdata=f"\n{league_title_arg2.upper()}({LeagueStatus})\n{dashes}\n{meta_data}\n{CORRECTIONS_local}\nHOME AND AWAY H2H WINS ---> {h2h_wins}\n{mdata_add_on}\nHOME{H2H_OTHER_MATCHES_CENT_HOME,ThisRelatedToUpVariableHome,DIFFS_ARR_HOME}{HOME_TEAM_TRANSITION}{home_trans_diff}\nAWAY{H2H_OTHER_MATCHES_CENT_AWAY,ThisRelatedToUpVariableAway,DIFFS_ARR_AWAY}{AWAY_TEAM_TRANSITION}{away_trans_diff}\n{dateInterOfMatches}"
    same_teams_diffs_arry=[home_same_team_cent_local-away_same_team_cent_local,ONLY_SAME_TEAMS_HOME_RECENT_CENT-ONLY_SAME_TEAMS_AWAY_RECENT_CENT]
    print(f'\t\t\t\t\t\t\t\t{MY_PREDICTION}')
    print()
    print(f'STANDINGS_OF_BOTH_TEAMS_LEN_IMPORTED ---> {STANDINGS_OF_BOTH_TEAMS_LEN_IMPORTED}')
    print(f'VERY_OLD_H2H_REC_TRIGGERED ---> {VERY_OLD_H2H_REC_TRIGGERED}')
    print(f'OBS_PTS ---> {[HOME_OBSTACLE_POINTS_IMPO,AWAY_OBSTACLE_POINTS_IMPO]}{[HOME_POINTS_LEFT_TO_QUALIFY,AWAY_POINTS_LEFT_TO_QUALIFY]}')
    print(f'PURELY_HOME_H2H_CENT ---> {PURELY_HOME_H2H_CENT}\nPURELY_AWAY_H2H_CENT ---> {PURELY_AWAY_H2H_CENT}')
    print(f'LAST_H2H_SCORE_CENT ---> {LAST_H2H_SCORE_CENT}')
    print(f'ALL_TIMES_H2H_ARG_CENT ---> {ALL_TIMES_H2H_ARG_CENT}')
    print(f'ALL_TIMES_H2H_VERY_OLD_ARG_CENT ---> {ALL_TIMES_H2H_VERY_OLD_ARG_CENT}')
    print(f'H2H_CENT_TRULY ---> {H2H_CENT_TRULY}')
    print(f'H2H_DIFF_MODAL_CENT ---> {H2H_DIFF_MODAL_CENT}')
    print(f'H2H_FINAL_FORM ---> {[HOME_H2H_FINAL_FORM,AWAY_H2H_FINAL_FORM]}')
    print(f'H2H_ROUGH_MIXED ---> {H2H_ROUGH_MIXED}')
    print(f'H2H_LDS_COUNT_CENT ---> {H2H_LDS_COUNT_CENT}')
    print(f'OTHER_M_FORM_FINAL ---> {QUICK_CENT11}')
    print(f'HOME_AWAY_FINAL_FORM ---> {[HOME_FINAL_FORM,AWAY_FINAL_FORM]}')
    print(f'OVER_SHADOWED_CENTS ---> {OVER_SHADOWED_CENTS}')
    print(f'FINAL_FORM_AND_OS_CENTS ---> {FINAL_FORM_AND_OVER_SHADOWED_CENTS}')
    print(f'QUALITIES_COUNT ---> {QUALITIES_COUNT}')
    print(f'OVER_SHADOWED_CENTS_COUNTER ---> {OVER_SHADOWED_CENTS_COUNTER}')
    print(f'ROUGH_FINAL_TEAMS_FORM ---> {ROUGH_FINAL_TEAMS_FORM}')
    print(f'ROUGH_FF_POS_CENT ---> {ROUGH_FF_POS_CENT}')
    print(f'TEAMS_MEGA_CENTS ---> {TEAMS_MEGA_CENTS}')
    print(f'MEGA_QUALITIES_AND_MEGA_WOUNDS ---> {MEGA_QUALITIES_AND_MEGA_WOUNDS} ************************** min_sub -> {MIN_SUB}')
    print(f'CONCRETE_FORM ---> {CONCRETE_FORM} ---> {c_abs(CONCRETE_FORM[0]-CONCRETE_FORM[1])}')
    print(f'FORM_WOUND_AND_TRANS ---> {FORM_WOUND_AND_TRANS} ---> {round((c_abs(FORM_WOUND_AND_TRANS[0]-FORM_WOUND_AND_TRANS[1])),1)}')
    print(f'STRIKE_DEFENCE_CENT ---> {STRIKE_DEFENCE_CENT}')
    print(f'STRIKE_DEFENCE_CENT_PURE_OLD ---> {STRIKE_DEFENCE_CENT_PURE_OLD}')
    print(f'STRIKE_DEFENCE_CENT_NEW ---> {STRIKE_DEFENCE_CENT_NEW}')
    print(f'STRIKE_DEFENCE_CENT_DYNAMIC ---> {STRIKE_DEFENCE_CENT_DYNAMIC}')
    print(f'STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT ---> {STRIKE_DEFENCE_DYNAMIC_LOSSES_CENT}')
    print(f'STRIKE_DEFENCE_LOSSES_CENT ---> {STRIKE_DEFENCE_LOSSES_CENT}')
    print(f'STRIKE_DEFENCE_LOSSES_CENT_NEW ---> {STRIKE_DEFENCE_LOSSES_CENT_NEW}')
    print(f'THE_TRIPPLETS_CENT ---> {THE_TRIPPLETS_CENT}{THE_TRIPPLETS_CENT_DIVS}')
    print(f'EXPERIMENTAL_FINAL_FORM ---> {EXPERIMENTAL_FINAL_FORM} ---> {round((EXPERIMENTAL_FINAL_FORM[0]-EXPERIMENTAL_FINAL_FORM[1]),1)}')
    print(f'EXPERIMENTAL_FINAL_FORM_NEW ---> {EXPERIMENTAL_FINAL_FORM_NEW}')
    print(f'EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED ---> {EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED}')
    print(f'EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS ---> {EXPERIMENTAL_FINAL_FORM_NEW_ENHANCED_PLUS_WOUNDS}')
    print(f'OLD_NEW_FORCES_LAST_WOUNDS_TRANS ---> {OLD_NEW_FORCES_LAST_WOUNDS_TRANS}')
    print(f'STRIKERS_AND_WOUNDS_CENT ---> {STRIKERS_AND_WOUNDS_CENT}')
    print(f'STRIKE_DEFENCE_LOSSES_CENT_COMBINED ---> {STRIKE_DEFENCE_LOSSES_CENT_COMBINED}')
    print(f'EXPERIMENTAL_FINAL_FORM_COMBINED ---> {EXPERIMENTAL_FINAL_FORM_COMBINED}')
    print(f'[TEAM_AVERAGE_H,TEAM_AVERAGE_A] ---> {[TEAM_AVERAGE_H,TEAM_AVERAGE_A]}')
    print(f'[PRO_HOME_TEAM,PRO_AWAY_TEAM] ---> {[PRO_HOME_TEAM,PRO_AWAY_TEAM]}')
    print(f'QUICK_QUALITIES ---> {QUICK_QUALITIES}')
    print(f'QUICK_QUALITIES2 ---> {QUICK_QUALITIES2}')
    print(f'QUICK_QUALITIES_SUM ---> {QUICK_QUALITIES_SUM}')
    print(f'TITANIC_FORM ---> {TITANIC_FORM}')
    print(f'TITANIC_ESTIMATED_FORM ---> {TITANIC_ESTIMATED_FORM}')
    print(f'H2H_SAME_MTCHS_CENTS_RAW ---> {H2H_SAME_MTCHS_CENTS_RAW}')
    print(f'POINTS_LEFT_PLUS_DYNAMIC_WOUNDS_ARRAY ---> {POINTS_LEFT_PLUS_DYNAMIC_WOUNDS_ARRAY}')
    print(f'H2H_SAME_MTCHS_CENTS_LOSS_ELEVATED ---> {H2H_SAME_MTCHS_CENTS_LOSS_ELEVATED}')
    print(f'H2H_DIFF_MODAL_CENT_WOUNDS ---> {H2H_DIFF_MODAL_CENT_WOUNDS}')
    print(f'TEAMS_DRIVEN_ENGINE_X ---> {TEAMS_DRIVEN_ENGINE_X}')
    print(f'MIN_HAUL_CENT ---> {MIN_HAUL_CENT}')
    print(f'ACCUMULATED_POINTS_CENT ---> {ACCUMULATED_POINTS_CENT}')
    print(f'HOME_TRANS_HUNT_QUALITIES ---> {HOME_TRANS_HUNT_QUALITIES}')
    print(f'AWAY_TRANS_HUNT_QUALITIES ---> {AWAY_TRANS_HUNT_QUALITIES}')
    print(f'CURRENT_FORM_PLUS_TRANS ---> {CURRENT_FORM_PLUS_TRANS}')
    print(f'FORM_CENT_LOSSES_INDIVIDUALLY ---> {FORM_CENT_LOSSES_INDIVIDUALLY}')
    print(f'FORM_CENT_LOSSES_INDIVIDUALLY_TRANS ---> {FORM_CENT_LOSSES_INDIVIDUALLY_TRANS}')
    print(f'GRAND_FORMS_RAW_QUALITIES_OLD ---> {GRAND_FORMS_RAW_QUALITIES_OLD}')
    print(f'GRAND_FORMS_RAW_QUALITIES_NEW ---> {GRAND_FORMS_RAW_QUALITIES_NEW}')
    print(f'GRAND_FORMS_RAW_QUALITIES_AVERAGE ---> {GRAND_FORMS_RAW_QUALITIES_AVERAGE}')
    print(f'GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H ---> {GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H}')
    print(f'GRAND_FORMS_RAW_QUALITIES_NEW2 ---> {GRAND_FORMS_RAW_QUALITIES_NEW2}')
    print(f'GRAND_TRANS_SUM_OTHER_QUALITIES ---> {GRAND_TRANS_SUM_OTHER_QUALITIES}')
    print(f'GRAND_TRANS_SUM_OTHER_QUALITIES2 ---> {GRAND_TRANS_SUM_OTHER_QUALITIES2}')
    print(f'GRAND_FORM_QUALITIES2 ---> {GRAND_FORM_QUALITIES2}')
    print(f'GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H_GRAND_TRANS ---> {GRAND_FORMS_RAW_QUALITIES_AVERAGE_H2H_GRAND_TRANS}')
    print(f'FORM_QUALITIES_CHANGE ----------------> {[FORM_QUALITIES_CHANGE_H,FORM_QUALITIES_CHANGE_A]}')
    print(f'VARIABLE_QUALITIES ---> {VARIABLE_QUALITIES} ---> {VARIABLE_QUALITIES_DIFF}')
    print(f'VARIABLE_QUALITIES_PLUS_CHANGE ---> {VARIABLE_QUALITIES_PLUS_CHANGE}')
    print(f'********************************************************************')
    print(f'GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS ---> {GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS}')
    print(f'GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT ---> {GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT}')
    print(f'GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES ---> {GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES}')
    print(f'GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES ---> {GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES}')
    print(f'GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H ---> {GRAND_FORMS_RAW_QUALITIES_OLD_PLUS_TRANS_LOSSES_H2H}')
    print(f'GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H ---> {GRAND_FORMS_RAW_QUALITIES_AVERAGE_PLUS_SAME_TEAMS_NEW_CENT_LOSSES_H2H}')
    print(f'COMPROMISED_WOUNS -------------------------------------> {COMPROMISED_WOUNS}')
    print(F'CUSTOM_POSITION -------------------------------------> {CUSTOM_POSITION_ARRAY}')
    print(f'GRAND_TRANS_SUM -------------------------------------> {GRAND_TRANS_SUM}')
    print(f'GRAND_FORM_QUALITIES3 -------------------------------------> {GRAND_FORM_QUALITIES3}')
    print(f'GRAND_COUNTS_QUALITIES -------------------------------------> {GRAND_COUNTS_QUALITIES}')
    print(f'TITANIC_FORM_CLOSER -------------------------------------> {TITANIC_FORM}')
    print(f'HANDICAP_PREDIC -------------------------------------> {HANDICAP_PREDIC}')
    print(f'FINAL_PROTOTYPE_FORM -------------------------------------> {FINAL_PROTOTYPE_FORM}')
    print(f'FINAL_PROTOTYPE_FORM_PLUS_GRAND -------------------------------------> {FINAL_PROTOTYPE_FORM_PLUS_GRAND}')
    print(f'COMPROMISED_WOUNS_TITANIC_FORM ---------------------> {COMPROMISED_WOUNS_TITANIC_FORM}')
    print(f'[CL_COMMENT_H,CL_COMMENT_A] ---> {[CHAINS_LOSSES_COMMENT_H,CHAINS_LOSSES_COMMENT_A]}')
    print(f'TEAM_GREEN_LIGHT_BRIGHTNESS -------------------------------------> {TEAM_GREEN_LIGHT_CENT}')
    print(f'TEAMS_FAILS_PATTERN_FORCE ---------------------------------------> {TEAMS_FAILS_PATTERN_FORCE}')
    print(f'TEAMS_FAILS_PATTERN_FORCE2 ---------------------------------------> {TEAMS_FAILS_PATTERN_FORCE2}')
    print(f'TEAMS_FAILS_PATTERN_FORCE3 ---------------------------------------> {TEAMS_FAILS_PATTERN_FORCE3}')
    print(f'MEGA_QUALITIES_FORM -----------------------------------------------> {MEGA_QUALITIES_FORM}')
    print(f'TEAM_NET_STRENGHT -------------------------------------------------> {TEAM_NET_STRENGHT}')
    print(f'SUPER_MEGA_QUALITIES_CENT -----------------------------------------> {SUPER_MEGA_QUALITIES_CENT}')
    print(f'WOUND_FORCES_QUALITIES_ARRAY_CENT ---------------------------------> {WOUND_FORCES_QUALITIES_ARRAY_CENT}')
    print(f'COUNTER_QUALITIES_ARRAY_CENT ---------------------------------> {COUNTER_QUALITIES_ARRAY_CENT}')
    print(f'PRO_TEAM_STATUS --------------------------------------------------> {PRO_TEAM_STATUS}')
    print(f'MEGA_QUALITIES_SERIES_CENT_ARRAY -------------------------------------> {MEGA_QUALITIES_SERIES_CENT_ARRAY}')
    print(f'OLD_CONSISTENT_FORMS_ARRAY_CENT -------------------------------------> {OLD_CONSISTENT_FORMS_ARRAY_CENT}')
    print(f'TOTAT_WOUNDS_FRESH ----------------------------------------------------> {TOTAT_WOUNDS_FRESH}')
    print(f'WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF ----------------------------------------------------> {WOUNDED_OLD_SOLDIERS_STRENGHT_H2H_INF}')
    print(f'TEAM_QUALITIES_COUNT_VERY_STRONG -------------------------------------> {TEAM_QUALITIES_COUNT_VERY_STRONG}')
    print(f'////////////////////////////////////////////////////////////////////')
    print(f'VARIABLE_FINAL_FORM ---> {VARIABLE_FINAL_FORM}')
    print(f'VARIABLE_FINAL_FORM_H2H_INFLUENCED ---> {VARIABLE_FINAL_FORM_H2H_INFLUENCED}')
    print(f'GRAND_FORMS_H2H_INFLUENCED ---> {GRAND_FORMS_H2H_INFLUENCED}')
    print(f'PROPELLER ------------> {PROPELLER}')
    print(f'[HOME_DANGEROUS,AWAY_DANGEROUS] ---> {[HOME_DANGEROUS,AWAY_DANGEROUS]}')
    print(f'TEAMS_TRIO_QUALITIES_MIN_VAL ---> [{round(HOME_TRIO_DIFF_MIN_VAL)},{round(AWAY_TRIO_DIFF_MIN_VAL)}]')
    print(f'EXPERIMENTAL_FINAL_FORM_LATEST ---> {EXPERIMENTAL_FINAL_FORM_LATEST}')
    print(f'TEAMS_GRAND_MAX_D_COMMENT ---> {TEAMS_GRAND_MAX_D_COMMENT}')
    print(f'TEAMS_VETERAN_STATUS ---> {TEAMS_VETERAN_STATUS}')
    print(f'H2H_SCORES_SUM_MODE ---> {H2H_SCORES_SUM_MODE}')
    print(f'QUALITIES_LOSSES_SLICE ---> {QUALITIES_LOSSES_SLICE}')
    print(f'POS_COUNTER_WOUNDS_CENT ---> {POS_COUNTER_WOUNDS_CENT}')
    print(f'POINTS_LEFT_HUNGER ---> {POINTS_LEFT_HUNGER}')
    print(f'ATTACKS_PLUS_SOT ---> {ATT_AND_SOT}')
    print(f'TEAMS_1st2_CONSISTENCY_CENT ---> {TEAMS_1st2_CONSISTENCY_CENT}')
    print(f'ATTACKS_STRENGTH ---> {TEAMS_ATTACK_CENT_ARG}')
    print(f'TEAMS_SHOTS_ON_TARGET_CENTS ---> {TEAMS_SHOTS_ON_TARGET_CENTS_ARG}')
    print(f'FINAL_FORM_AND_ATTACKS_PLUS_SOT ---> {FINAL_FORM_AND_ATTACKS_PLUS_SOT}')
    print(f'ATTACKS_PLUS_WOUNDS ---> {ATT_WND_HUB}')
    print(f'TEAMS_DEFENCE_LEVEL ---> {[HOME_LOST_BY_ONE,AWAY_LOST_BY_ONE]}')
    print(f'ONLY_TEAMS_STRIKER_LEVEL ---> {[HOME_ALL_SCORES_STRIKE,AWAY_ALL_SCORES_STRIKE]} ---> {scores_len_arr}')
    print(f'PURE_OLD_TEAMS_DEFENCE ---> {PURE_OLD_TEAMS_DEFENCE}')
    print(f'ONLY_TEAMS_STRIKER_LEVEL_PURE_OLD ---> {[HOME_ALL_SCORES_STRIKE_OLD,AWAY_ALL_SCORES_STRIKE_OLD]}')
    print(f'[LATEST_STRIKE_H,LATEST_DEFENCE_H] ---> {MICRO_STRIKE_DEFENCE_HOME}')
    print(f'[LATEST_STRIKE_A,LATEST_DEFENCE_A] ---> {MICRO_STRIKE_DEFENCE_AWAY}')
    print(f'TEAM_CONSISTENCY ---> {[HOME_CONSISTENCY,AWAY_CONSISTENCY]}')
    print(f'TRANSITION ---> [{HOME_TEAM_TRANSITION},{AWAY_TEAM_TRANSITION}]')
    print(f'DYNAMIC_WOUNDS_ARRAY_H2H_INFLUENCED ---> {DYNAMIC_WOUNDS_ARRAY_H2H_INFLUENCED}')
    print(f'DYNAMIC_WOUNDS_ARRAY ---> {DYNAMIC_WOUNDS_ARRAY_ORIGINAL}')
    print(f'HIDDEN_LOSSES ---> {[HIDDEN_LOSSES_HOME,HIDDEN_LOSSES_AWAY]}')
    print(f'C_DRIVEN_FORCE ---> {C_DRIVEN_FORCE}{CDF_DIV} ---> {CDF_DIV_ABS_DFF}')
    print(f'LAST_P_LOSSES ---> {[HOME_LAST_SCORES_LOSS,AWAY_LAST_SCORES_LOSS]}')
    print(f'CHAINS_LOSES ---> {[HOME_WOUND_PATTERNS,AWAY_WOUND_PATTERNS]}')
    print(f'LATEST_WOUNDS ---> {[HOME_LATEST_WOUNDS,AWAY_LATEST_WOUNDS]}')
    print(f'[HOME_KILLER,AWAY_KILLER] ---> {[HOME_KILLER,AWAY_KILLER]}')
    print(f'GRAND_FORM_PLUS_WOUNDS ---> {QUICK_CENT14}')
    print(f'TEAM_STRUCT_LOGIC ---> {TEAM_STRUCT_LOGIC}')
    print(f'LAST_3_GAMES_LOST_POINTS ---> {[LAST_3_GAMES_LOST_POINTS_HOME,LAST_3_GAMES_LOST_POINTS_AWAY]}')
    print(f'HOME_AWAY_RECENT_LOSES ---> {GRAND_LOSES_ARRAY}')
    print(f'HOME_AWAY_LOST_POINTS_CENT ---> {HOME_AWAY_LOST_POINTS_CENT}')
    print(f'POTENTIAL [HOME, AWAY, DRAW] ---> {CENTS_ARRAY}')
    print(f'TRUE_STRIKERS_INFO ---> {TRUE_STRIKERS_INFO}')
    print(f'home_same_team_cent_local(len{home_same_team_cent_local_len}) ---> {[home_same_team_cent_local,ONLY_SAME_TEAMS_HOME_RECENT_CENT]} ---> {SAME_TEAMS_TRANS_H}')
    print(f'away_same_team_cent_local(len{away_same_team_cent_local_len}) ---> {[away_same_team_cent_local,ONLY_SAME_TEAMS_AWAY_RECENT_CENT]} ---> {SAME_TEAMS_TRANS_A}')
    print(f'same_teams_diffs_arry ---> {same_teams_diffs_arry}\n')
    print(f'{both_teams_in_group2_impo}')
    print('-'*len(both_teams_in_group2_impo))
    print(f'TopGuysCentAndHomePos ---> {[HometopGuysCent,HometeamPosition]}')
    print(f'TopGuysCentAndAwayPos ---> {[AwaytopGuysCent,AwayteamPosition]}')
    print(f'BELOW_TEAMS_POS_GAME_CENTS ---> {BELOW_TEAMS_POS_GAME_CENTS}')
    #print(f'MONTHLY_SCORES_GRAND_LOCAL_HOME_DIFF ---> {MONTHLY_SCORES_GRAND_LOCAL_HOME_DIFF}')
    print(f'MONTHLY_SCORES_GRAND_LOCAL_HOME ---> {MONTHLY_SCORES_GRAND_LOCAL_HOME}')
    #print(f'MONTHLY_SCORES_GRAND_LOCAL_AWAY_DIFF ---> {MONTHLY_SCORES_GRAND_LOCAL_AWAY_DIFF}')
    print(f'MONTHLY_SCORES_GRAND_LOCAL_AWAY ---> {MONTHLY_SCORES_GRAND_LOCAL_AWAY}')
    #print(f'MONTHLY_SCORES_DIFF ---> {MONTHLY_SCORES_DIFF} DIFF_SUM ---> {MONTHLY_SCORES_DIFF_SUM}')
    print(mdata)
    print([HOME_WOUNDS,AWAY_WOUNDS])
    print(f'DRAWS: {[homeTeamDraws,awayTeamDraws]}')
    print(HomeLossForces,LossForcesDiffHome)
    print(AwayLossForces,LossForcesDiffAway)
    print()
    print(f'H2H ---> {H2H_TUPLE,[home_T_Point,away_T_Point]}')
    print()
    print(f'{home_T} ---> {ALL_SCORES_DIRTY_HOME}{HOMh_n_a_Date}')
    print()
    print(f'{away_T} ---> {ALL_SCORES_DIRTY_AWAY}{AOMh_n_a_Date}')
    print()
    totalSelectedGames+=1
    TOTAL_MISSING_GAMES=MatchCount-totalSelectedGames
    print(f'TOTAL CORRECT GAMES ---> {totalSelectedGames}/{MatchCount}: TOTAL MISSING GAMES: {TOTAL_MISSING_GAMES}')
    print('******************************** END OF UP DATA ********************************')
def nextMatchesCount(html_bytes_arg,FBT_H_A_ARG2):
    home_tm=FBT_H_A_ARG2[0]
    away_tm=FBT_H_A_ARG2[1]
    currentTornament=re.findall(r'shortagdiv tghov.+?head to head',html_bytes_arg)
    league_short_tag=re.findall(r'<span class="shorttag">.+?avg_sc',html_bytes_arg)
    LeagueTagName='A_I_K'
    for cst in currentTornament:
      shorttag_s=re.findall(r'shorttag.+?</span>',cst)
      if len(shorttag_s)>0:
          LeagueTagName=shorttag_s[0].replace('shorttag">','').replace('</span>','').strip()
          break
    NEXT_MATCHES=re.findall(r'next matches.+?</table>',html_bytes_arg)
    H_A_NEXT_MATCHES=[]
    MATCHES_NEXT_HOME=[]
    MATCHES_NEXT_AWAY=[]
    for nm in NEXT_MATCHES:
      moduletable=re.split('moduletable',nm)[1:3]
      for tnm,mt in enumerate(moduletable):
          tag_key=fr'<div class=\Sfx_tag\S>{LeagueTagName}</div>'
          tag_count=re.findall(tag_key,mt)
          tag_count_len=len(tag_count)
          if tag_count_len>0:
             match_tag=re.findall(f'{tag_key}.+?team_diff',mt)
             for to in match_tag:
                 tmm=re.findall(r'href.+?</a>',to)
                 n_m=[]
                 for t_m in tmm:
                   t_m_=re.findall(r'>.+?<',t_m)
                   cleaNam=''
                   if len(t_m_)>0:
                      cleaNam=t_m_[0].replace('<','').replace('>','').strip()
                      if tnm==0 and cleaNam!=home_tm:
                        MATCHES_NEXT_HOME+=[cleaNam]
                      if tnm==1 and cleaNam!=away_tm:
                        MATCHES_NEXT_AWAY+=[cleaNam]
          H_A_NEXT_MATCHES+=[tag_count_len]
      break
    return [H_A_NEXT_MATCHES,[MATCHES_NEXT_HOME,MATCHES_NEXT_AWAY]]
def standingsOfBothTeam(html_bytes2,hm_awy2):
    def quickPointReturn(tre_arg):
      point_t=0
      tre_num=re.findall(r'\d+',tre_arg)
      for tren,tree in enumerate(reversed(tre_num)):
          if tren==7:
              point_t=int(tree)
              break
      return point_t
    NEXT_GAMES_REC=nextMatchesCount(html_bytes2,hm_awy2)
    H_A_NEXT_MATCHES=NEXT_GAMES_REC[0]
    NEXT_GAMES_REC_HOME=NEXT_GAMES_REC[1][0]
    NEXT_GAMES_REC_AWAY=NEXT_GAMES_REC[1][1]
    HOME_OBSTACLE_POINTS=[]
    AWAY_OBSTACLE_POINTS=[]
    HOME_REC_ADDED=[]
    AWAY_REC_ADDED=[]
    Match_title_ore=re.findall(r'hdrtb prblh tb1x2.+?rcnt tr_\d+',html_bytes2)
    heading='+++++++++++++++++++'
    for mh in Match_title_ore:
        heading=re.findall(r'heading.+?</div>',mh)
        for ch in heading:
            heading=ch.replace('</div>','').replace('heading">','').strip()
    split_heading=heading.split(',')
    Possible_heading=''
    split_heading_len=len(split_heading)
    if split_heading_len>1:
        Possible_heading=split_heading[split_heading_len-1].strip()
    FB_HOM=hm_awy2[0]
    FB_AWAY=hm_awy2[1]
    HA_DIC={FB_HOM:-1,FB_AWAY:-1}
    sobts_key=fr'std_btn.+?</table>'
    #zone_count=re.findall(r'class="std_pos std_zn"',html_bytes)
    STANDINGS_OF_BOTH_TEAMS=re.findall(sobts_key,html_bytes2)
    STANDINGS_OF_BOTH_TEAMS_LEN=len(STANDINGS_OF_BOTH_TEAMS)
    ALL_TEAMS=[]
    STANDINGS_OF_BOTH_TEAMS_TABLE=[]
    ALL_TEAMS_POINTS_ARRAY=[]
    notfinaldic={'-1':[]}
    both_teams_in_group2='TEAMS IN DIFFERENT GROUPS'
    for tr in STANDINGS_OF_BOTH_TEAMS:
        group_name=re.findall(r'colspan.+?</td>',tr)
        clean_gn='********************************'
        for gn in group_name:
            clean_gn=gn.replace("colspan='2'>",'').replace('</td>','').strip()
        tr_wanted_data=re.findall(r'std_pos.+?</tr>',tr)
        for tre in tr_wanted_data:
            for hme in NEXT_GAMES_REC_HOME:
              if hme in tre and hme not in HOME_REC_ADDED:
                 fished_point_h=quickPointReturn(tre)
                 HOME_OBSTACLE_POINTS+=[fished_point_h]
                 HOME_REC_ADDED+=[hme]
            for ame in NEXT_GAMES_REC_AWAY:
              if ame in tre and ame not in AWAY_REC_ADDED:
                 fished_point_a=quickPointReturn(tre)
                 AWAY_OBSTACLE_POINTS+=[fished_point_a]
                 AWAY_REC_ADDED+=[ame]
        both_teams_in_group= FB_HOM in tr or FB_AWAY in tr and (heading==clean_gn or Possible_heading==clean_gn)
        if both_teams_in_group:
            both_teams_in_group2='TEAMS IN SAME GROUP'
            for pos,trwd in enumerate(tr_wanted_data):
               hpos=pos+1
               digits=re.findall(r'<b>\d+?</b>|<td align="center".+\d+</td>',trwd)
               digits_int=[]
               for dt in digits:
                   num=re.findall(r'\d+|-\d+',dt)
                   for nom in num:
                       digits_int+=[int(nom)]
               team=re.findall(r'<a.+?</a>',trwd)[0].split('>')[1].split('<')[0].strip()
               std_zn=trwd.find('std_zn')
               try:
                NOTFINAL=notfinaldic[f'{std_zn}']
                NOTFINAL+=[team]
                notfinaldic[f'{std_zn}']=NOTFINAL
               except KeyError:
                pass
               ALL_TEAMS+=[team]
               TEAM_POINT=digits_int[0]
               ALL_TEAMS_POINTS_ARRAY+=[TEAM_POINT]
               STANDINGS_OF_BOTH_TEAMS_TABLE+=[digits_int]
               if team in hm_awy2:
                     HA_DIC[team]=[TEAM_POINT,hpos]
    HUB2=[]
    ALL_TEAMS_LEN=len(ALL_TEAMS)
    HUB2=[HA_DIC,ALL_TEAMS_LEN,ALL_TEAMS,STANDINGS_OF_BOTH_TEAMS_TABLE,notfinaldic,ALL_TEAMS_POINTS_ARRAY,both_teams_in_group2,H_A_NEXT_MATCHES,HOME_OBSTACLE_POINTS,AWAY_OBSTACLE_POINTS,STANDINGS_OF_BOTH_TEAMS_LEN]
    return HUB2
def playersStats(fb_html_bytes):
    INJURED_AND_SUSPENDED_chunk=re.findall(r'INJURED AND SUSPENDED.+?PLAYER STATS',fb_html_bytes,re.IGNORECASE)
    PLAYER_STATS=re.findall(r'PLAYER STATS.+?</table>',fb_html_bytes,re.IGNORECASE)
    SUSPENDED_PLAYERS_DIC={'HomeTeam':{},'AwayTeam':{}}
    TOTAL_GOALS_HOME=0
    TOTAL_YCARDS_HOME=0
    TOTAL_REDCARDS_HOME=0
    ALL_HOME_GOALS=[]
    HOME_STRIKERS_GOALS_TOTAL=[]

    TOTAL_GOALS_AWAY=0
    TOTAL_YCARDS_AWAY=0
    TOTAL_REDCARDS_AWAY=0
    ALL_AWAY_GOALS=[]
    AWAY_STRIKERS_GOALS_TOTAL=[]
    def suspended_guys_compare(sus_dic,team_dic,team_max_goal):
        SUS_ARR=[]
        for skey in sus_dic:
            skey_clean=skey.split('(')[0].strip()
            try:
                sus_record=team_dic[skey_clean]
                sus_p_rec=sus_dic[skey]
                SUS_ARR+=[f'{skey_clean}--->({sus_record[0]},{team_max_goal},{sus_p_rec[2]})']
            except KeyError as suspended_players_compare_err:
                   SUS_ARR+=[sus_dic[skey]]
                   error_printer(suspended_players_compare_err)
        return SUS_ARR
    try:
        for pst in INJURED_AND_SUSPENDED_chunk:
            TEAMS_DIC_KEY='HomeTeam'
            split_at_player=pst.split('player')[1:]
            for pst in split_at_player:
                suspended_players=re.findall(r'susp_\d+.+?</tr>',pst)
                def cleaner(dirt):
                    return dirt.split('<td>')[1].replace('</td>','').strip()
                for sp in suspended_players:
                    tds=re.findall(r'<td>.+?</td>',sp)
                    plyr_name='No player'
                    games_played='0'
                    status='will not play'
                    try:
                        plyr_name=cleaner(tds[0])
                        games_played=cleaner(tds[1])
                        if len(games_played)==0:
                            games_played='0'
                        status=cleaner(tds[2])
                    except IndexError:
                        pass
                    SUSPENDED_PLAYERS_DIC[TEAMS_DIC_KEY][plyr_name]=[plyr_name,games_played,status]
                TEAMS_DIC_KEY='AwayTeam'
            #break
        GEN_DIC_ARR=[{},{}]
        for n,pt in enumerate(PLAYER_STATS):
            statof_players=re.split('standing-second-td',pt)[1:]
            for spl in statof_players:
                spl_ele=re.findall(r'>.+?<',spl)
                player_name=spl_ele[0].replace('>','').replace('<','').strip()
                def sharp(ores):
                    return ores.split('>')[2].replace('<','').strip()
                total_goals_scored=sharp(spl_ele[1])
                total_yellow_cards=sharp(spl_ele[2])
                total_red_cards=sharp(spl_ele[3])
                str_arr=[total_goals_scored,total_yellow_cards,total_red_cards]
                PLAYER_RECORDS=[]
                for ots in str_arr:
                    input_ele=ots
                    if input_ele=='-':
                       input_ele='0'
                    input_ele=int(input_ele)
                    PLAYER_RECORDS+=[input_ele]
                if n==0:
                   homeStrikerGoals=PLAYER_RECORDS[0]
                   TOTAL_GOALS_HOME+=homeStrikerGoals
                   ALL_HOME_GOALS+=[homeStrikerGoals]
                   TOTAL_YCARDS_HOME+=PLAYER_RECORDS[1]
                   TOTAL_REDCARDS_HOME+=PLAYER_RECORDS[2]
                   if homeStrikerGoals>0:
                      HOME_STRIKERS_GOALS_TOTAL+=[homeStrikerGoals]
                else:
                   awayStrikerGoals=PLAYER_RECORDS[0]
                   TOTAL_GOALS_AWAY+=awayStrikerGoals
                   ALL_AWAY_GOALS+=[awayStrikerGoals]
                   TOTAL_YCARDS_AWAY+=PLAYER_RECORDS[1]
                   TOTAL_REDCARDS_AWAY+=PLAYER_RECORDS[2]
                   if awayStrikerGoals>0:
                      AWAY_STRIKERS_GOALS_TOTAL+=[awayStrikerGoals]
                GEN_DIC_ARR[n][player_name]=PLAYER_RECORDS
        HOME_TEAM_DIC=GEN_DIC_ARR[0]
        AWAY_TEAM_DIC=GEN_DIC_ARR[1]
        if len(ALL_HOME_GOALS)==0:
            ALL_HOME_GOALS=[0,0]
        max_home_goal=max(ALL_HOME_GOALS)
        GRAND_HOME_STATS=[TOTAL_GOALS_HOME,TOTAL_YCARDS_HOME,TOTAL_REDCARDS_HOME]
        if len(ALL_AWAY_GOALS)==0:
            ALL_AWAY_GOALS=[0,0]
        max_away_goal=max(ALL_AWAY_GOALS)
        GRAND_AWAY_STATS=[TOTAL_GOALS_AWAY,TOTAL_YCARDS_AWAY,TOTAL_REDCARDS_AWAY]
        HOME_SUS_PLAYERS_RECORDS=suspended_guys_compare(SUSPENDED_PLAYERS_DIC['HomeTeam'],HOME_TEAM_DIC,max_home_goal)
        AWAY_SUS_PLAYERS_RECORDS=suspended_guys_compare(SUSPENDED_PLAYERS_DIC['AwayTeam'],AWAY_TEAM_DIC,max_away_goal)
    except IndexError as suspended__players:
           error_printer(suspended__players)
    return [GRAND_HOME_STATS,HOME_SUS_PLAYERS_RECORDS,GRAND_AWAY_STATS,AWAY_SUS_PLAYERS_RECORDS,HOME_STRIKERS_GOALS_TOTAL,AWAY_STRIKERS_GOALS_TOTAL]
def forebetScrubber(FBT_H_A,html_bytes):
    SUSPENDED_PLAYERS_RECORDS=playersStats(html_bytes)
    FOREBET_PREDICTION=[0,0]
    FBT_HOME=FBT_H_A[0]
    FBT_AWAY=FBT_H_A[1]
    fb_contest=f'{FBT_HOME} vs {FBT_AWAY}'
    HOM=[]
    AOM=[]
    home_same_team_cent=0
    away_same_team_cent=0
    HOME_SAME_TEAM_AGAINST_LEN=0
    AWAY_SAME_TEAM_AGAINST_LEN=0
    SAME_HOME_AWAY_SCORES=[]
    ALL_TEAMS_LEN_LOCAL2=0
    SBT_DIC={}
    STANDINGS_OF_BOTH_TEAMS_LEN_IMPORTED_1=0
    H_A_NEXT_MATCHES_IMPO=0
    try:
        last_n_matches=re.findall(r'last \d+ matches',html_bytes)
        last_n_matches=last_n_matches[0]
        lnm_key=f'{last_n_matches}.+?home matches'
        lastNmatchesChunk=re.findall(lnm_key,html_bytes)
        lastNmatchesChunk=lastNmatchesChunk[0]
        divided_2=lastNmatchesChunk.split('all</button>')
        divided_2_len=len(divided_2)-1
        HOME_CHUNK=divided_2[divided_2_len-1]
        AWAY_CHUNK=divided_2[divided_2_len]
        def innerGear(HA_CHUNK,hora,ALL_TEAMS_LOCAL_arg,team='H'):
            teamPosition=0
            try:
                 teamPosition=ALL_TEAMS_LOCAL_arg.index(hora)+1
            except Exception:
                pass
            ALL_SCORES_PURE=[]
            ALL_SCORES_DIRTY=[]
            ONLY_HOME_OR_AWAY_SCORES=[]
            IDEX_DIC={'0':1,'1':0}
            DateArr=[]
            HME_AWY=[]
            TOP_GUYS_SCORES=[]
            AGAINST_TEAMS=[]
            match_records_ore_arg=re.findall(r'st_row st_\d+ stlg_\d+.+?st_ltag',HA_CHUNK)
            prev_month=0
            MONTHLY_SCORES=[]
            MONTHLY_SCORES_GRAND=[]
            def date_hunter(mro_arg):
                dates=re.findall(r'\d+/\d+.+\d?</div>',mro_arg)[0]
                dates=re.findall(r'\d+',dates)[:3]
                dates_int_func=[int(di) for di in dates]
                return dates_int_func
            date_hunter_here=date_hunter(match_records_ore_arg[0])
            date_hunter_here1=date_hunter(match_records_ore_arg[1])
            d1=date_hunter_here[0]
            d2=date_hunter_here1[0]
            m1=date_hunter_here[1]
            m2=date_hunter_here1[1]
            DATE_CORRECTION=d1>d2 and m1<=m2
            month_picker=1
            if not DATE_CORRECTION:
                month_picker=0
            prev_month=date_hunter_here[month_picker]
            previous_month=CURRENT_MONTH
            _7months_in=0
            for mro in match_records_ore_arg:
                dates=re.findall(r'\d+/\d+.+\d?</div>',mro)[0]
                dates=re.findall(r'\d+',dates)[:3]
                dates_int=[int(di) for di in dates]
                date_year=dates_int[2]
                month_date=dates_int[month_picker]
                if date_year>=(CURRENT_YEAR-YEAR_RETRACER):
                    pass
                else:
                    break
                team_name_ore=re.findall(r'<a.+?</a>',mro)
                team_name_ore_len=len(team_name_ore)-1
                timA=team_name_ore[0].split('>')
                timA=timA[len(timA)-2].replace('</a','').strip()
                matchData=re.findall(r'st_res.+\d+ - \d+?</span>',mro)[0]
                timB=team_name_ore[team_name_ore_len].split('>')
                timB=timB[len(timB)-2].replace('</a','').strip()
                DYNA_H_A=[timA,timB]
                timN_dex=DYNA_H_A.index(hora)
                scores=re.findall(r'>\d+.+\d+<',matchData)[0]
                scoresInt=re.findall(r'\d+',scores)
                scoresTuple=[]
                indexFound=0
                h2h_count=0
                for tnm in DYNA_H_A:
                    if tnm in FBT_H_A:
                        h2h_count+=1
                NOT_H2H=h2h_count>=2
                if not DATE_CORRECTION:
                    dates_int=[dates_int[1],dates_int[0],dates_int[2]]
                if not NOT_H2H:
                    DateArr+=[dates_int]
                    try:
                        for tn in DYNA_H_A:
                            if tn!=hora:
                                 indexFound=ALL_TEAMS_LOCAL_arg.index(tn)+1
                    except Exception:
                             pass
                    for si in scoresInt:
                        scoresTuple+=[int(si)]
                    scores_tuple=(scoresTuple[0],scoresTuple[1])
                    if team=='H':
                        if timN_dex==0:
                           ONLY_HOME_OR_AWAY_SCORES+=[scores_tuple]
                    else:
                        if timN_dex==1:
                           ONLY_HOME_OR_AWAY_SCORES+=[scores_tuple]

                    scoresTuple=(scoresTuple[timN_dex],scoresTuple[IDEX_DIC[f'{timN_dex}']])
                    for ag in DYNA_H_A:
                          if ag!=hora:
                             AGAINST_TEAMS+=[(ag,scoresTuple)]
                    ALL_SCORES_DIRTY+=[scoresTuple]
                    df=teamPosition-indexFound
                    teamPosition_diff=(df<=2 and teamPosition!=2) or indexFound>teamPosition
                    if teamPosition_diff:
                         ALL_SCORES_PURE+=[scoresTuple]
                    else:
                         TOP_GUYS_SCORES+=[scoresTuple]
                    if month_date==prev_month:
                       MONTHLY_SCORES+=[scoresTuple]
                       # if teamPosition_diff:
                       #    MONTHLY_SCORES+=[scoresTuple]
                    else:
                          mtncent=monthlyCent(MONTHLY_SCORES,len(MONTHLY_SCORES))[0]
                          MONTHLY_SCORES_GRAND+=[mtncent]
                          MONTHLY_SCORES=[]
                          MONTHLY_SCORES+=[scoresTuple]
                    prev_month=month_date
            ALL_SCORES_PURE_CENT=monthlyCent(ALL_SCORES_PURE,len(ALL_SCORES_PURE))[0]
            topGuysPerfom=monthlyCent(TOP_GUYS_SCORES,len(TOP_GUYS_SCORES))[0]
            MONTHLY_SCORES_GRAND=list(reversed(MONTHLY_SCORES_GRAND))#from old games to current games
            return [DateArr,ALL_SCORES_DIRTY,MONTHLY_SCORES_GRAND,[topGuysPerfom,teamPosition],ALL_SCORES_DIRTY,AGAINST_TEAMS,ONLY_HOME_OR_AWAY_SCORES,ALL_SCORES_PURE_CENT]
        STANDINGS_OF_BOTH_TEAMS_RECORDS=standingsOfBothTeam(html_bytes,FBT_H_A)
        SBT_DIC=STANDINGS_OF_BOTH_TEAMS_RECORDS[0]
        ALL_TEAMS_LEN_LOCAL2=STANDINGS_OF_BOTH_TEAMS_RECORDS[1]
        ALL_TEAMS_LOCAL=STANDINGS_OF_BOTH_TEAMS_RECORDS[2]
        STANDINGS_OF_BOTH_TEAMS_TABLE_LOCAL=STANDINGS_OF_BOTH_TEAMS_RECORDS[3]
        notfinaldic_local=STANDINGS_OF_BOTH_TEAMS_RECORDS[4]
        ALL_TEAMS_POINTS_ARRAY_LOCAL=STANDINGS_OF_BOTH_TEAMS_RECORDS[5]
        both_teams_in_group2_exp=STANDINGS_OF_BOTH_TEAMS_RECORDS[6]
        H_A_NEXT_MATCHES_IMPO=STANDINGS_OF_BOTH_TEAMS_RECORDS[7]
        HOME_OBSTACLE_POINTS_EXPO=STANDINGS_OF_BOTH_TEAMS_RECORDS[8]
        AWAY_OBSTACLE_POINTS_EXPO=STANDINGS_OF_BOTH_TEAMS_RECORDS[9]
        STANDINGS_OF_BOTH_TEAMS_LEN_IMPORTED_1=STANDINGS_OF_BOTH_TEAMS_RECORDS[10]
        HOM=innerGear(HOME_CHUNK,FBT_HOME,ALL_TEAMS_LOCAL)
        AGAINST_TEAMS_HOME=HOM[5]
        AOM=innerGear(AWAY_CHUNK,FBT_AWAY,ALL_TEAMS_LOCAL,'A')
        AGAINST_TEAMS_AWAY=AOM[5]
        qarr=[AGAINST_TEAMS_HOME,AGAINST_TEAMS_AWAY]
        OPOSDIC={'0':1,'1':0}
        larr=[len(AGAINST_TEAMS_HOME),len(AGAINST_TEAMS_AWAY)]
        max_len=max(larr)
        max_len_dex=larr.index(max_len)
        max_item=qarr[max_len_dex]
        oposdex=OPOSDIC[f'{max_len_dex}']
        oposit_item=qarr[oposdex]
        HOME_SAME_TEAM_AGAINST=[]
        AWAY_SAME_TEAM_AGAINST=[]
        oposit_item=str(oposit_item)
        AGAINST_SAME_TEAMS=[]
        for mt in max_item:
              picked_team=mt[0]
              picked_scr=mt[1]
              if picked_team in oposit_item:
                 picked_team_spkit=oposit_item.split(picked_team)[1]
                 scor=''
                 for s in picked_team_spkit:
                    scor+=s
                    if s==')':
                        scores=re.findall(r'\(\d+.+\d+\)',scor)
                        scor=eval(scores[0])
                        if max_len_dex==0:
                             HOME_SAME_TEAM_AGAINST+=[picked_scr]
                             AWAY_SAME_TEAM_AGAINST+=[scor]
                        else:
                              HOME_SAME_TEAM_AGAINST+=[scor]
                              AWAY_SAME_TEAM_AGAINST+=[picked_scr]
                        scor=''
                        break
                 oposit_item=oposit_item.replace(picked_team,'',1)
        home_same_team_cent=win_loss_cent(HOME_SAME_TEAM_AGAINST,0,1)[0]
        away_same_team_cent=win_loss_cent(AWAY_SAME_TEAM_AGAINST,0,1)[0]
        HOME_SAME_TEAM_AGAINST_LEN=len(HOME_SAME_TEAM_AGAINST)
        AWAY_SAME_TEAM_AGAINST_LEN=len(AWAY_SAME_TEAM_AGAINST)
        SAME_HOME_AWAY_SCORES=[HOME_SAME_TEAM_AGAINST,AWAY_SAME_TEAM_AGAINST]
    except IndexError as last_n_matches_err:
        error_printer(last_n_matches_err)
    forbet_predictions=re.findall(r'ex_sc tabonly.+?</div>',html_bytes)
    plen=len(forbet_predictions)
    league_short_tag=re.findall(r'<span class="shorttag">.+?avg_sc',html_bytes)
    LeagueTagName='A_I_K'
    for tg in league_short_tag:
        LeagueTagName=tg.split('<span class="shorttag">')[1].split('</span>')[0].strip()
        break
    last_n_matchess=re.findall(r'last\W+\d+\W+matches',html_bytes)[0]
    H2H=re.findall(fr'head\W+to\W+head.+?match\W+intro',html_bytes)
    HOME_OR_AWAY=re.findall(r'<div>home match.+?</div>.+overall',html_bytes)[0].split('moduletable')
    #HOME_OR_AWAY=[HOME_OR_AWAY[1],HOME_OR_AWAY[2]]
    def scoreTable(scoreTableOreArr):
        HA_DIC_SCR={FBT_HOME:[],FBT_AWAY:[]}
        H2H_DATE=[]
        PURELY_HOME_AWAY_H2H_SCORES=[]
        different_year_checker_count=0
        ALL_TIMES_H2H=[]
        ALL_TIMES_H2H_VERY_OLD=[]
        h2h_old_count=0
        for hth in scoreTableOreArr:
            hth_data=re.split('st_date',hth)[1:]
            collected_date=[]
            for dn,de in enumerate(hth_data):
                m_y0=re.findall(r'\d+',de)[:3]
                m_y0_int=[int(dx) for dx in m_y0]
                collected_date+=[m_y0_int]
                if dn==1:
                    break
            collected_date_len=len(collected_date)
            month_picker0=1
            day_picker=0
            DATE_CORRECTION0=True
            if collected_date_len>1:
              date_hunter_here0=collected_date[0]
              date_hunter_here10=collected_date[1]
              d10=date_hunter_here0[0]
              d20=date_hunter_here10[0]
              m10=date_hunter_here0[1]
              m20=date_hunter_here10[1]
              DATE_CORRECTION0=d10>d20 and m10<=m20
              if not DATE_CORRECTION0:
                  day_picker=1
                  month_picker0=0
            for d in hth_data:
                H_A=[]
                tims=re.findall(r'<a href="/en/teams/.+?</a>',d)
                fscr=re.findall(r'\d+ - \d+',d)[0].split(' - ')
                FB_SCR=[int(fbs) for fbs in fscr]
                for ha in tims:
                    cleanName=ha.split('>')[1].replace('</a','').strip()
                    H_A+=[cleanName]
                fbContest=f'{H_A[0]} vs {H_A[1]}'
                FBT_HOME_DEX=H_A.index(FBT_HOME)
                dex_scr_tuple=(FB_SCR[0],FB_SCR[1])
                running_league_tag=re.findall(r'st_ltag.+?</div>',d)[0].replace('st_ltag">','')
                running_league_tag=running_league_tag.replace('</div>','')
                #if running_league_tag==LeagueTagName or fb_contest==fbContest:
                gtr_less=re.findall(r'\d+',d)
                dates=gtr_less[:3]
                dates_int=[int(dint) for dint in dates]
                match_month=dates_int[month_picker0]
                match_year=dates_int[2]
                if not DATE_CORRECTION0:
                    dates_int=[dates_int[1],dates_int[0],dates_int[2]]
                if len(ALL_TIMES_H2H)<10 and match_year>=(CURRENT_YEAR-7):
                    ALL_TIMES_H2H+=[dex_scr_tuple]
                else:
                    h2h_old_count+=1
                    if h2h_old_count<=10:
                        ALL_TIMES_H2H_VERY_OLD+=[dex_scr_tuple]
                _7months_in2=0
                if match_year>=(CURRENT_YEAR-YEAR_RETRACER):
                    H2H_DATE+=[dates_int]
                    if FBT_HOME_DEX==0:
                        PURELY_HOME_AWAY_H2H_SCORES+=[dex_scr_tuple]
                    for tmsn,tms in enumerate(H_A):
                          if tms in FBT_H_A:
                            dex_scr=FB_SCR[tmsn]
                            HA_DIC_VAL=HA_DIC_SCR[tms]
                            HA_DIC_VAL+=[dex_scr]
                            HA_DIC_SCR[tms]=HA_DIC_VAL
                else:
                    break
        for tkys in HA_DIC_SCR:
            val=HA_DIC_SCR[tkys]
            if len(val)==0:
               HA_DIC_SCR[tkys]=[-1]
        HA_DIC_SCR['H2H_DATE']=H2H_DATE
        if len(ALL_TIMES_H2H)==0:
            ALL_TIMES_H2H=[(-1,-1)]
        if len(ALL_TIMES_H2H_VERY_OLD)==0:
            ALL_TIMES_H2H_VERY_OLD=[(-1,-1)]
        return [HA_DIC_SCR,PURELY_HOME_AWAY_H2H_SCORES,ALL_TIMES_H2H,ALL_TIMES_H2H_VERY_OLD]
    H2H_DIC=scoreTable(H2H)
    HOME_OR_AWAY_DIC=[]#scoreTable(HOME_OR_AWAY,0)
    try:
        for fb in forbet_predictions:
            forbet_predictions=re.findall(r'\d+ - \d+',fb)
            if len(forbet_predictions)>0:
                fscr=forbet_predictions[0]
                fscr_split=fscr.split('-')
                FOREBET_PREDICTION=[]
                for spltf in fscr_split:
                    FOREBET_PREDICTION+=[int(spltf)]
                break
        THE_HUB=[H2H_DIC,SBT_DIC,HOME_OR_AWAY_DIC,FOREBET_PREDICTION,H_A_NEXT_MATCHES_IMPO,HOM,AOM,SUSPENDED_PLAYERS_RECORDS,ALL_TEAMS_LEN_LOCAL2,[home_same_team_cent,away_same_team_cent],[HOME_SAME_TEAM_AGAINST_LEN,AWAY_SAME_TEAM_AGAINST_LEN],STANDINGS_OF_BOTH_TEAMS_TABLE_LOCAL,notfinaldic_local,SAME_HOME_AWAY_SCORES,ALL_TEAMS_POINTS_ARRAY_LOCAL,both_teams_in_group2_exp,HOME_OBSTACLE_POINTS_EXPO,AWAY_OBSTACLE_POINTS_EXPO,STANDINGS_OF_BOTH_TEAMS_LEN_IMPORTED_1]
        return THE_HUB
    except IndexError as last_n_matches_err:
        error_printer(last_n_matches_err)
def predictor(f_url,info_meta,m_dates,league_title_arg,match_odds_arg1,clean_match_title_sportybet):
  global CONTEST_URL,totalSelectedGames
  CONTEST_URL=f_url
  CORRECTIONS=['no corrections']
  try:
    #match_scount=int(re.findall(r'\d+',info_meta)[0])-1
    picked_date=1#m_dates[match_scount]+yea_r
    content_str=scraperApi(f_url)
    Total_attacks=re.findall(r'os_attacks_total_number.+?</span>',content_str)
    Total_attacks=Total_attacks[:(len(Total_attacks)-1)]
    HOME_TOTAL_ATTACKS=[0,0]
    AWAY_TOTAL_ATTACKS=[0,0]
    for atnum,attacks in enumerate(Total_attacks):
       atnum_h=atnum+1
       attacks_split=attacks.split('>')
       attack_num='-1'
       try:
           attacks_split=attacks_split[1]
           attack_num=re.findall(r'\d+',attacks_split)[0]
       except IndexError as attack_num_error:
           error_printer(f'attack_num_error ---> {attack_num_error}')
       attack_num=int(attack_num)
       if atnum_h>1 and atnum_h%2==0:
           AWAY_TOTAL_ATTACKS+=[attack_num]
       else:
           HOME_TOTAL_ATTACKS+=[attack_num]
    TEAMS_ATTACK_CENT=quickCentCalc([sum(HOME_TOTAL_ATTACKS),sum(AWAY_TOTAL_ATTACKS)])
    os_shots_percent_value=re.findall(r'os_shots_gk_door os_flex_ce.+?on\W+target',content_str)
    TEAMS_SHOTS_ON_TARGET_CENTS=[]
    for sot in os_shots_percent_value:
       shots_on_target=re.findall(r'shots_on_target.+%',sot)
       shots_on_target_cent='-1'
       try:
           shots_on_target_cent=shots_on_target[0].split('>')[1].replace('%','').strip()
       except Exception as shots_on_target_error:
           error_printer(f'shots_on_target_error ---> {shots_on_target_error}')
       try:
        shots_on_target_cent=int(shots_on_target_cent)
       except Exception as shots_on_target_error_valueErro:
          shots_on_target_cent=0
          error_printer(f'shots_on_target_error_valueErro ---> {shots_on_target_error_valueErro}')
       TEAMS_SHOTS_ON_TARGET_CENTS+=[shots_on_target_cent]
    if len(TEAMS_SHOTS_ON_TARGET_CENTS)==0:
        TEAMS_SHOTS_ON_TARGET_CENTS=[0,0]
    LeagueStage='TRACKING_ERROR'
    leagueTitleForebet='TRACKING_ERROR'
    RIGHT_LEAGUE=True
    try:
        leagueTitleForebet=re.findall(r'leagpred_btn.+?</a>',content_str)[0].split('>')[1].split('<')[0].strip()
    except IndexError as LeagueTitleForebet_err:
        error_printer(f'LeagueTitleForebet_err ---> {LeagueTitleForebet_err}')
    for lgdf in ['youth','amateur','under']:
        if lgdf in leagueTitleForebet:
            RIGHT_LEAGUE=False
    try:
        LeagueStage=re.findall(r'<div class="heading">.+?</div>',content_str)[0].replace('<div class="heading">','')
        LeagueStage=LeagueStage.replace('</div>','')
    except IndexError as LeagueStage_err:
        error_printer(f'LeagueStage_err ---> {LeagueStage_err}')
    Corrections=re.findall(r'corrections.+-\d+ points|corrections.+\+\d+ points',content_str)
    if len(Corrections)>0:
        CORRECTIONS=[]
    for c in Corrections:
        team_nme=re.findall(r'">.+?</span>',c)
        team_point=re.findall(r'</span>.+?points',c)
        for cnn,cn in enumerate(team_nme):
            point_ore=team_point[cnn]
            clean_name=cn.replace('</span>','').replace('">','').strip()
            clean_point=point_ore.replace('</span>: ','').strip()
            formed=f'{clean_name}: {clean_point}'
            CORRECTIONS+=[formed]
    league_title_arg_local=f'{leagueTitleForebet}({LeagueStage})'
    #correct_match=re.findall(r'predblocktd.+?</time>',content_str)[0]
    #match_date=re.findall(r'\d+/\d+/\d+',correct_match)[0].split('/')
    weather_main_pr=re.findall(r'weather_main_pr.+?startdate',content_str)
    weather_unit='missing record'
    try:
        for wtr in weather_main_pr:
            weather_unit=re.findall(r'\d+\&deg',wtr)[0].replace('&','')
    except IndexError:
           pass
    _2s=[]
    match_date=[]
    for md in match_date:
      mdfrm=md
      md_len=len(md)
      if md_len==1:
         mdfrm=f'0{md}'
      _2s+=[mdfrm]
    match_date=''.join(_2s[:3])
    DATES_MATCHED=1#picked_date==match_date
    if DATES_MATCHED:
      FMA=re.findall(r'predteamnames.+?weather_main_pr',content_str)[0]#Forebet Match Arrangement
      h_vs_a_ore=re.findall("itemprop='name'.+?<",FMA)#[0].split('"')[1].split(' vs ')
      h_vs_a=[]
      for hvsa in h_vs_a_ore:
         cleanNm=hvsa.replace("itemprop='name'>",'').replace('<','').strip()
         h_vs_a+=[cleanNm]
      HOME=h_vs_a[0]
      AWAY=h_vs_a[1]
      try:
         contest=f"{HOME} vs {AWAY}"
         MATCH_FOREBET=f"MATCH(forebet): {contest} --->weather ---> {weather_unit}"
         breaks=info_meta.split("MATCH URL:")
         reformed_meta=f"{breaks[0]}{MATCH_FOREBET}\nMATCH URL:{breaks[1]}"
         OTHER_MATCHES=forebetScrubber([HOME,AWAY],content_str)
         if RIGHT_LEAGUE:
            sub_predictor([HOME,AWAY],reformed_meta,league_title_arg_local,OTHER_MATCHES,CORRECTIONS,match_odds_arg1,TEAMS_ATTACK_CENT,TEAMS_SHOTS_ON_TARGET_CENTS)
      except IndexError as er2:
        error_printer(f"er2 ----> {er2}")
    else:
      #print(f'Match missing online ---> {f_url}')
      pass
  except Exception as error:
    error_printer(f"ERROR---------------> {error}")
with open('C:\\Users\\MASCOM\\AppData\\Local\\Programs\\Python\\Python313\\custom-files\\ResultHtml.html', encoding="utf8") as fo:
  LEAGUE_CATE_DIC={}
  rbty=fo.read().replace('\n','').lower()
  MATCH_SITE_ODDS=[]
  keyword='title=".+?"'
  matches=re.findall(keyword,rbty)
  sportyDate=re.findall(r'm-table-cell date.+?<',rbty)
  match_league=re.split('m-table-cell date',rbty)
  match_league=match_league[1:]
  match_div=re.split('m-table-cell market-size',rbty)
  Months_DIC={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sept','10':'Oct','11':'Nov','12':'Dec'}
  matches_dates=[]
  for mln,ml in enumerate(match_league):
    odds_chunk=re.split('m-market market',ml)[1:]
    mdate=sportyDate[mln]
    adts=re.findall(r'\d+',mdate)
    _2s_second=[]
    for md2 in adts:
      md2_frm=md2
      md2_len=len(md2)
      if md2_len==1:
         md2_frm=f'0{md2}'
      _2s_second+=[md2_frm]
    actual_date=''.join(_2s_second)
    home_team=re.findall(r'class="home-team">.+?<',ml)
    home_team_len=len(home_team)
    for ad in range(home_team_len):
      matches_dates+=[actual_date]
  match_div_len=len(match_div)-1
  match_div=match_div[:match_div_len]
  match_odds_presentCount=0
  for mt in match_div:
    try:
      odds=re.findall(r'm-market market.+?m-market market',mt)
      match_odds_dyna=['0.00','0.00','0.00']
      for ads in odds:
        match_odds_dyna=re.findall(r'\d+\.\d+',ads)
      if len(MATCH_SITE_ODDS)>0:
        match_odds_presentCount+=1
      else:
        match_odds_dyna=['0.00','0.00','0.00']
      MATCH_SITE_ODDS+=[match_odds_dyna]
    except Exception as err3:
           error_printer(f"market size error: {err3}")
  totalmatches=len(matches)
  count=0
  match_league_wrap=re.split('match-league-wrap',rbty)[1:]
  match_odds_dex=0
  for mlw in match_league_wrap:
    league_title=re.findall(r'<span class="text">.+?</span>',mlw)[0].replace('<span class="text">','')
    league_title=league_title.replace('</span>','')
    youth_uN=re.findall(r'youth|u\d+',league_title)
    YUN=''
    for yun in youth_uN:
        YUN+=f'{yun} '
    YUN=YUN.strip()
    match_title=re.findall(keyword,mlw)
    clock_time=re.findall(r'clock-time.+?</div>',mlw)
    clock_dex=0
    for mt in match_title:
      match_odds=MATCH_SITE_ODDS[match_odds_dex]
      match_odds_dex+=1
      clean_match_title=mt.replace('title="','').replace('"','')
      clean_match_title_split=clean_match_title.split(' vs ')
      clean_match_title_written=f'{clean_match_title} ---> {match_odds}'
      time_ore=clock_time[clock_dex]
      clean_time=re.findall(r'\d+:\d+',time_ore)[0]
      GMT='PM'
      colon_split=int(clean_time.split(':')[0])
      int_len=len(str(colon_split))
      if int_len==1:
         GMT='AM'
      clean_time_len=len(clean_time)
      time_deco='~'*clean_time_len+f'{clean_time}{GMT}'+'~'*clean_time_len
      clock_dex+=1
      try:
        count+=1
        day_month=[]
        date_single=matches_dates[count-1]
        nums=re.findall(r'\d',date_single)
        day_=nums[0]+nums[1]
        month_=Months_DIC[nums[2]+nums[3]]
        date_formed=f'-{day_}+{month_}+{yea_r}'
        google_recursion_count=0
        clean_match_title_url=f'{clean_match_title} {YUN}'
        href='https://www.google.com/search?q='+clean_match_title_url.replace(' ','+')+f"+forebet+predictions+and+stats{date_formed}"
        URL=''#googleHrefFetcher(href,[clean_match_title_split[0].split(' '),clean_match_title_split[1].split(' ')])
        REVERSED_URL_FLAG=0
        FOREBET_URL_ARRAY=forebetMatchesUrls()
        if REVERSED_URL_FLAG==1:
            FOREBET_URL_ARRAY=list(reversed(FOREBET_URL_ARRAY))
        FOREBET_URL_ARRAY_LEN=len(FOREBET_URL_ARRAY)
        print(f'total matches {FOREBET_URL_ARRAY_LEN}\n')
        count=0
        for fbt_url in FOREBET_URL_ARRAY:
            count+=1
            URL=fbt_url[0]
            clean_time=fbt_url[1]
            MATCH_DATE='/'.join(clean_time[:3])
            MATCH_TIME=':'.join(clean_time[3:])
            hour=clean_time[3:][0]
            hour_int=int(hour)
            time_def='AM'
            if hour_int>=12:
                time_def='PM'
            time_deco=f'{MATCH_DATE} @ {MATCH_TIME}{time_def}'
            meta=f"MATCH NUMBER: {count}\n{time_deco}\nMATCH(sportybet): {clean_match_title_written.lower()}\nMATCH URL: {URL}"
            quick_meta=f'MATCH:{clean_match_title}\nLEAGUE:{league_title}\nTIME:{clean_time}\nODDS:{match_odds}\n'
            predictor(URL,meta,matches_dates,league_title,match_odds,quick_meta)
      except IndexError as modds_err:
             error_printer(f"modds_err ---> {modds_err}")
      break
    break
  fo.close()