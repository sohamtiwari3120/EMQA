import os
import json
import random

random.seed(123)

def main():
    file_path="./TyDiQA_training_data"
    tydiqa_files = os.listdir(file_path)
    tydiqa_files = [l for l in tydiqa_files if '.json' in l]
    out_path = "./TyDiQA_500_training_data"
   
    for tydiqa_file in tydiqa_files:
        language=(tydiqa_file.split("_")[1]).split(".")[0]
        #print(language)
        dataset=json.load(open(os.path.join(file_path,tydiqa_file)))
        number_of_instances = 500
        dataset['data']=random.sample(dataset['data'],number_of_instances)
        
        out_file_name = os.path.join(out_path,'tydiqa_{}_500.json'.format(language))
        with open(out_file_name, 'w', encoding='utf-8') as outfile:
            json.dump(dataset, outfile)
    
    

if __name__ == "__main__":
    main()