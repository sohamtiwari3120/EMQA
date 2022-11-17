import pandas as pd
import statistics

def mono():
    monolingual=pd.read_csv('monolingual.csv')
    monolingual_dic={}
    monolingual_seen_language=[]
    monolingual_unseen_language=[]
    overall=[]
    dic_df={}
    #print(monolingual.head(5))
    #print(trilingual.head(5))
    for index,row in monolingual.iterrows():
        test_language=row['Name'].split("_")[-1]
        finetune_language=row['Name'].split("_")[1]
        f1=float(row['eval.Results.f1'])
        if finetune_language!='english' and test_language!='korean':
            if finetune_language not in dic_df:
                dic_df[finetune_language]={}
            dic_df[finetune_language][test_language]=f1
            if test_language not in monolingual_dic:
                monolingual_dic[test_language]=[f1]
            else:
                monolingual_dic[test_language].append(f1)
            if(test_language==finetune_language):
                monolingual_seen_language.append(f1)
            else:
                monolingual_unseen_language.append(f1)
            if(test_language!='english'):
                overall.append(f1)
    '''print('seen languages mean ',statistics.mean(monolingual_seen_language))
    print('unseen languages mean ',statistics.mean(monolingual_unseen_language))
    print('overall mean ', statistics.mean(overall))
    print('overall std-dev ', statistics.stdev(overall))
    monolingual_mean=[]
    for language in monolingual_dic:
        mean=statistics.mean(monolingual_dic[language])
        varience=statistics.stdev(monolingual_dic[language])
        monolingual_mean.append(mean)
        print('language: ',language)
        print('mean: ',mean)
        print('std-dev: ',varience)
        print()
    print('delta is ', max(monolingual_mean)-min(monolingual_mean))'''
    
    dic_df=pd.DataFrame(data=dic_df).T
    print(dic_df)
    dic_df.to_csv('monolingual_results.csv')
    
        
def tri():
    trilingual=pd.read_csv('trilingual.csv')
    trilingual_dic={}
    trilingual_seen_language=[]
    trilingual_unseen_language=[]
    overall=[]
    rs_dic={}
    rs_dic[1]=7
    rs_dic[2]=3
    rs_dic[3]=6
    rs_dic[4]=2
    rs_dic[5]=4
    rs_dic[6]=1
    rs_dic[7]=5
    rs=''
    dic_dic={}
    for index,row in trilingual.iterrows():
        test_language=row['Name'].split("_")[-1]
        split= row['Name'].split("_")[1]
        f1=float(row['eval.Results.f1'])
        '''if(rs!=split):
            rs=split
            #print('RS ', rs_dic[int(split)])'''
        val='RS '+str(rs_dic[int(split)])
            
        if test_language!='korean':
            if val not in dic_dic:
                dic_dic[val]={}
            dic_dic[val][test_language]=f1
            
            #print(test_language,f1)
            if(test_language!='english'):
                overall.append(f1)
            if test_language not in trilingual_dic:
                trilingual_dic[test_language]=[f1]
            else:
                trilingual_dic[test_language].append(f1)
            if split=='1':
                if test_language =='arabic' or test_language =='indonesian' or test_language =='swahili':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
            if split=='2':
                if test_language =='finnish' or test_language =='russian' or test_language =='swahili':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
            if split=='3':
                if test_language =='finnish' or test_language =='indonesian' or test_language =='swahili':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
            if split=='4':
                if test_language =='telugu' or test_language =='indonesian' or test_language =='swahili':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
            if split=='5':
                if test_language =='arabic' or test_language =='russian' or test_language =='telugu':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
            if split=='6':
                if test_language =='bengali' or test_language =='russian' or test_language =='telugu':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
            if split=='7':
                if test_language =='arabic' or test_language =='russian' or test_language =='finnish':
                    trilingual_seen_language.append(f1)
                else:
                    trilingual_unseen_language.append(f1)
    '''print('seen languages mean ',statistics.mean(trilingual_seen_language))
    print('unseen languages mean ',statistics.mean(trilingual_unseen_language))
    print('overall mean ', statistics.mean(overall))
    print('overall std-dev ', statistics.stdev(overall))
    trilingual_mean=[]
    for language in trilingual_dic:
        mean=statistics.mean(trilingual_dic[language])
        varience=statistics.stdev(trilingual_dic[language])
        trilingual_mean.append(mean)
        print('language: ',language)
        print('mean: ',mean)
        print('std-dev: ',varience)
        print()
    print('delta is ', max(trilingual_mean)-min(trilingual_mean))'''
    df=pd.DataFrame(data=dic_dic)
    df=(df.T).sort_index(ascending=True)
    df.to_csv('trilingual_results.csv')

def uniform(file):
    uniform=pd.read_csv(file)
    eng_val=''
    overall=[]
    
    for index,row in uniform.iterrows():
        test_language=row['Name'].split("_")[-1]
        f1=float(row['eval.Results.f1'])
        if test_language!='korean':
            if(test_language=='english'):
                eng_val=f1
            overall.append(f1)
        print(test_language, " : ",f1)
     
    
    print('overall mean ',statistics.mean(overall))
    print('overall std-dev ',statistics.stdev(overall))
    overall.remove(eng_val)
    print('overall mean w/o eng ',statistics.mean(overall))
    print('overall std-dev w/o eng ',statistics.stdev(overall))
    print('delta ',max(overall)-min(overall))
            
        
        
    
            
    
    
    
        
        



if __name__=="__main__":
    mono()
    #tri()
    #uniform('uniform.csv')
    #uniform('baseline.csv')